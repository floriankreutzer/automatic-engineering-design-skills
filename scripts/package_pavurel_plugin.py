#!/usr/bin/env python3
"""Build the reviewed skills-only account package without network access."""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile


REPOSITORY = "https://github.com/floriankreutzer/automatic-engineering-design-skills"
MANIFEST = "packaging/pavurel-design/plugin.json"
SKILL_CATALOG = "packaging/pavurel-design/skill-catalog.json"
SKILL_POLICY = "references/skill-policy.md"
REQUIRED_SKILLS_LOCK = "packaging/pavurel-design/required-design-skills.json"
REQUIRED_SKILLS = {
    "impeccable": {
        "upstream_url": "https://github.com/pbakaus/impeccable",
        "edition": "reference-only",
        "license": "Apache-2.0",
    },
    "design-taste-frontend": {
        "upstream_url": "https://github.com/Leonxlnx/taste-skill",
        "edition": "chatgpt-compatible",
        "license": "MIT",
    },
}


def relative_path(value):
    """Accept one portable, contained file path without normalizing away mistakes."""
    if (not isinstance(value, str) or not value or "\\" in value or ":" in value
            or any(ord(char) < 32 or ord(char) == 127 for char in value)):
        raise ValueError(f"Invalid relative source path: {value!r}")
    path = PurePosixPath(value)
    if (not path.parts or path.is_absolute() or path.as_posix() != value
            or any(part in (".", "..") or part.startswith(".") for part in path.parts)):
        raise ValueError(f"Invalid relative source path: {value!r}")
    return value


def read_regular_file(root, relative):
    path = root
    for part in PurePosixPath(relative_path(relative)).parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Refusing symbolic link: {relative}")
    if not path.is_file():
        raise ValueError(f"Missing source file: {relative}")
    return path.read_bytes()


def parse_json(content):
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    return json.loads(content, object_pairs_hook=unique_keys)


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def validate_mandatory_routing(payload, skill_names):
    """Guard the collection's deliberately simple, reviewed metadata format."""
    policy = payload["SKILL_POLICY.md"].decode("utf-8")
    rows = re.findall(r"^\| `([a-z0-9]+(?:-[a-z0-9]+)*)` \|", policy, re.MULTILINE)
    if len(rows) != len(set(rows)) or set(rows) != set(skill_names):
        raise ValueError("Mandatory policy table must cover the exact skill catalog once")
    for name in skill_names:
        entrypoint = payload[f"skills/{name}/SKILL.md"].decode("utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", entrypoint, re.DOTALL)
        if frontmatter is None or re.findall(
            r"^name: ([a-z0-9]+(?:-[a-z0-9]+)*)[ \t]*$", frontmatter[1], re.MULTILINE
        ) != [name]:
            raise ValueError(f"Skill frontmatter name must match its catalog entry: {name}")
        if "[the mandatory skill policy](references/skill-policy.md)" not in entrypoint:
            raise ValueError(f"Missing mandatory routing link: {name}")
        metadata = payload[f"skills/{name}/agents/openai.yaml"].decode("utf-8")
        policy_keys = re.findall(r"^[ \t]*policy:", metadata, re.MULTILINE)
        invocation_keys = re.findall(
            r"^[ \t]*allow_implicit_invocation:[^\n]*", metadata, re.MULTILINE
        )
        if (len(policy_keys) != 1
                or invocation_keys != ["  allow_implicit_invocation: true"]
                or re.search(r"^policy:\n  allow_implicit_invocation: true(?:\n|$)",
                             metadata, re.MULTILINE) is None):
            raise ValueError(f"Skill must enable one unambiguous implicit invocation policy: {name}")


def catalog_skill_files(root):
    """Check all skill entrypoints while packaging only explicitly reviewed files."""
    catalog = parse_json(read_regular_file(root, SKILL_CATALOG))
    if (not isinstance(catalog, dict) or type(catalog.get("schema_version")) is not int
            or catalog["schema_version"] != 1 or not isinstance(catalog.get("skills"), list)):
        raise ValueError("Skill catalog must use schema_version 1 and a skills list")
    if catalog.get("policy") != "required-when-applicable":
        raise ValueError("Skill catalog policy must be required-when-applicable")

    names = set()
    vendor_names = set()
    source_paths = []
    for skill in catalog["skills"]:
        if not isinstance(skill, dict):
            raise ValueError("Invalid catalog skill entry")
        name = skill.get("name")
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            raise ValueError(f"Invalid catalog skill name: {name!r}")
        if name in names:
            raise ValueError(f"Duplicate catalog skill: {name}")
        names.add(name)
        if name in REQUIRED_SKILLS:
            if set(skill) != {"name", "vendor_lock"} or skill["vendor_lock"] is not True:
                raise ValueError(f"Required vendor skill must use its existing vendor lock: {name}")
            vendor_names.add(name)
            continue
        if set(skill) != {"name", "files"} or not isinstance(skill.get("files"), list):
            raise ValueError(f"Catalog skill must declare an explicit files list: {name}")
        seen = set()
        for value in skill["files"]:
            path = relative_path(value)
            if path in seen:
                raise ValueError(f"Duplicate catalog skill file: {name}/{path}")
            seen.add(path)
            source_paths.append(f"skills/{name}/{path}")
        if not {"SKILL.md", "agents/openai.yaml", SKILL_POLICY} <= seen:
            raise ValueError(f"Missing required entrypoint, metadata or policy for catalog skill: {name}")

    if vendor_names != set(REQUIRED_SKILLS):
        raise ValueError("The catalog must include both locked vendor skills")
    skills_root = root / "skills"
    if skills_root.is_symlink():
        raise ValueError("Refusing symbolic link: skills")
    actual_names = {path.parent.name for path in skills_root.glob("*/SKILL.md")}
    if actual_names != names:
        missing = sorted(names - actual_names)
        unlisted = sorted(actual_names - names)
        raise ValueError(f"Skill catalog does not match source entrypoints: missing={missing}, unlisted={unlisted}")
    return sorted(source_paths), sorted(names)


def locked_skill_files(root):
    """Read the reviewed allowlist; never discover vendor files by directory walk."""
    lock = parse_json(read_regular_file(root, REQUIRED_SKILLS_LOCK))
    if (not isinstance(lock, dict) or type(lock.get("schema_version")) is not int
            or lock["schema_version"] != 1 or not isinstance(lock.get("skills"), list)):
        raise ValueError("Required design skills lock must use schema_version 1 and a skills list")

    expected_hashes = {}
    found = set()
    provenance = []
    for skill in lock["skills"]:
        if not isinstance(skill, dict):
            raise ValueError("Invalid required skill entry")
        name = skill.get("name")
        if not isinstance(name, str) or name not in REQUIRED_SKILLS:
            raise ValueError(f"Unexpected required skill: {name!r}")
        if name in found:
            raise ValueError(f"Duplicate required skill: {name}")
        found.add(name)
        for key, value in REQUIRED_SKILLS[name].items():
            if skill.get(key) != value:
                raise ValueError(f"Unexpected {key} for required skill: {name}")
        if (not isinstance(skill.get("upstream_ref"), str)
                or not re.fullmatch(r"[0-9a-f]{40}", skill["upstream_ref"])):
            raise ValueError(f"Invalid upstream_ref for required skill: {name}")
        if not isinstance(skill.get("upstream_version"), str) or not skill["upstream_version"].strip():
            raise ValueError(f"Missing upstream_version for required skill: {name}")
        files = skill.get("files")
        if not isinstance(files, list) or not files:
            raise ValueError(f"Missing file allowlist for required skill: {name}")
        seen = set()
        for record in files:
            if not isinstance(record, dict):
                raise ValueError(f"Invalid file record for required skill: {name}")
            path = relative_path(record.get("path"))
            if path in seen:
                raise ValueError(f"Duplicate required skill file: {name}/{path}")
            seen.add(path)
            digest = record.get("sha256")
            if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
                raise ValueError(f"Invalid sha256 for required skill file: {name}/{path}")
            if name == "impeccable" and not (
                path in {"SKILL.md", "LICENSE", "NOTICE.md", "agents/openai.yaml"}
                or (path.startswith("references/") and path.endswith(".md"))
            ):
                raise ValueError(f"Unexpected file in reference-only Impeccable: {path}")
            expected_hashes[f"skills/{name}/{path}"] = digest
        required = {"SKILL.md", "agents/openai.yaml", "LICENSE", SKILL_POLICY}
        if name == "impeccable":
            required.add("NOTICE.md")
        if not required <= seen:
            raise ValueError(f"Missing required entrypoint, metadata, license or policy for skill: {name}")
        provenance.append({key: value for key, value in skill.items() if key != "files"})

    if found != set(REQUIRED_SKILLS):
        raise ValueError("The lock must contain exactly both required design skills")
    return expected_hashes, sorted(provenance, key=lambda skill: skill["name"])


def build(root, output, source_ref):
    if not isinstance(source_ref, str) or not re.fullmatch(r"[0-9a-f]{40}", source_ref):
        raise ValueError("source-ref must be the full reviewed Git commit SHA")
    root = root.resolve()
    output = output.absolute()
    if output.suffix != ".zip":
        raise ValueError("Output must be a .zip archive")
    if output.is_symlink() or any(parent.is_symlink() for parent in output.parents):
        raise ValueError("Refusing a symbolic-link output")

    manifest_bytes = read_regular_file(root, MANIFEST)
    manifest = parse_json(manifest_bytes)
    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        raise ValueError("The manifest must use Agent Plugins 1.0")
    if manifest.get("name") != "pavurel-design":
        raise ValueError("Unexpected plugin name")
    interface = manifest["extensions"]["com.openai"]["interface"]
    if not 1 <= len(interface["shortDescription"]) <= 30:
        raise ValueError("The listing subtitle must contain 1 to 30 characters")

    catalog_paths, skill_names = catalog_skill_files(root)
    expected_hashes, required_provenance = locked_skill_files(root)
    source_paths = [
        "LICENSE", "THIRD_PARTY_NOTICES.md", "SKILL_POLICY.md", MANIFEST,
        SKILL_CATALOG, REQUIRED_SKILLS_LOCK,
    ]
    source_paths.extend(catalog_paths)
    source_paths.extend(sorted(expected_hashes))
    if output.resolve() in {(root / path).resolve() for path in source_paths}:
        raise ValueError("Output must not overwrite a source file")
    if output.exists() and any(
        (root / path).exists() and output.samefile(root / path) for path in source_paths
    ):
        raise ValueError("Output must not overwrite a source file through a hard link")
    payload = {"plugin.json": manifest_bytes}
    source_records = {}
    for relative in source_paths:
        content = read_regular_file(root, relative)
        target = {
            MANIFEST: "plugin.json", SKILL_CATALOG: "skill-catalog.json",
            REQUIRED_SKILLS_LOCK: "required-design-skills.json",
        }.get(relative, relative)
        digest = hashlib.sha256(content).hexdigest()
        if relative in expected_hashes and digest != expected_hashes[relative]:
            raise ValueError(f"Source hash mismatch: {relative}")
        payload[target] = content
        source_records[target] = {
            "source_path": relative,
            "sha256": digest,
        }

    for name in skill_names:
        if payload[f"skills/{name}/{SKILL_POLICY}"] != payload["SKILL_POLICY.md"]:
            raise ValueError(f"Skill policy differs from canonical SKILL_POLICY.md: {name}")
    validate_mandatory_routing(payload, skill_names)

    payload["source-provenance.json"] = json_bytes({
        "repository": REPOSITORY,
        "reviewed_source_ref": source_ref,
        "source_ref_note": "The caller must verify that these inputs match this reviewed commit.",
        "skill_catalog": "skill-catalog.json",
        "skill_policy": "SKILL_POLICY.md",
        "required_design_skills_lock": "required-design-skills.json",
        "required_design_skills": required_provenance,
        "files": source_records,
    })
    payload["NOTICE.md"] = (
        "# Attribution\n\n"
        "Original design engineering guidance by Emil Kowalski.\n"
        "Curated and adapted for Pavurel in the source repository:\n"
        + REPOSITORY + "\n\n"
        "The original MIT copyright and permission notice is included in LICENSE.\n"
        "Required Impeccable and Taste Skill snapshots retain their own licenses and notices.\n"
        "See THIRD_PARTY_NOTICES.md and the license files in their skill directories.\n"
    ).encode("utf-8")

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative, content in sorted(payload.items()):
            entry = zipfile.ZipInfo("pavurel-design/" + relative, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = (stat.S_IFREG | 0o644) << 16
            entry.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(entry, content, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return {"archive": str(output), "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
            "files": len(payload), "skills": skill_names,
            "source_ref": source_ref}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-ref", required=True, help="Full reviewed Git commit SHA for the verified inputs")
    parser.add_argument("--source-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("dist/pavurel-design-1.1.0.zip"))
    args = parser.parse_args()
    try:
        result = build(args.source_root, args.output, args.source_ref)
    except (ValueError, KeyError, OSError, zipfile.BadZipFile) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
