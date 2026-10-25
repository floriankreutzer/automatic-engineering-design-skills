#!/usr/bin/env python3
"""Build the reviewed skills-only account package without network access."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import zipfile


REPOSITORY = "https://github.com/floriankreutzer/automatic-engineering-design-skills"
MANIFEST = "packaging/pavurel-design/plugin.json"
SKILL_FILES = {
    "pavurel-web-design": (
        "SKILL.md", "agents/openai.yaml", "references/website-context.md",
    ),
    "pavurel-app-design": (
        "SKILL.md", "agents/openai.yaml", "references/customer.md",
        "references/platform.md", "references/repository-sources.md",
    ),
    "21st-design-research": (
        "SKILL.md", "agents/openai.yaml", "references/21st-reference.md",
    ),
}


def read_regular_file(root, relative):
    path = root
    for part in Path(relative).parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Refusing symbolic link: {relative}")
    if not path.is_file():
        raise ValueError(f"Missing source file: {relative}")
    return path.read_bytes()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def build(root, output, source_ref):
    if not re.fullmatch(r"[0-9a-f]{40}", source_ref):
        raise ValueError("source-ref must be the full reviewed Git commit SHA")
    root = root.resolve()
    output = output.absolute()
    if output.suffix != ".zip":
        raise ValueError("Output must be a .zip archive")
    if output.is_symlink():
        raise ValueError("Refusing a symbolic-link output")

    manifest_bytes = read_regular_file(root, MANIFEST)
    manifest = json.loads(manifest_bytes)
    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        raise ValueError("The manifest must use Agent Plugins 1.0")
    if manifest.get("name") != "pavurel-design":
        raise ValueError("Unexpected plugin name")
    interface = manifest["extensions"]["com.openai"]["interface"]
    if not 1 <= len(interface["shortDescription"]) <= 30:
        raise ValueError("The listing subtitle must contain 1 to 30 characters")

    source_paths = ["LICENSE", MANIFEST]
    source_paths.extend(
        f"skills/{name}/{relative}"
        for name, relatives in SKILL_FILES.items()
        for relative in relatives
    )
    if output.resolve() in {(root / path).resolve() for path in source_paths}:
        raise ValueError("Output must not overwrite a source file")
    payload = {"plugin.json": manifest_bytes}
    source_records = {}
    for relative in source_paths:
        content = read_regular_file(root, relative)
        target = "plugin.json" if relative == MANIFEST else relative
        payload[target] = content
        source_records[target] = {
            "source_path": relative,
            "sha256": hashlib.sha256(content).hexdigest(),
        }

    payload["source-provenance.json"] = json_bytes({
        "repository": REPOSITORY,
        "reviewed_source_ref": source_ref,
        "source_ref_note": "The caller must verify that these inputs match this reviewed commit.",
        "files": source_records,
    })
    payload["NOTICE.md"] = (
        "# Attribution\n\n"
        "Original design engineering guidance by Emil Kowalski.\n"
        "Curated and adapted for Pavurel in the source repository:\n"
        + REPOSITORY + "\n\n"
        "The original MIT copyright and permission notice is included in LICENSE.\n"
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
            "files": len(payload), "skills": sorted(SKILL_FILES), "source_ref": source_ref}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-ref", required=True, help="Full reviewed Git commit SHA for the verified inputs")
    parser.add_argument("--source-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=Path("dist/pavurel-design-1.0.0.zip"))
    args = parser.parse_args()
    try:
        result = build(args.source_root, args.output, args.source_ref)
    except (ValueError, KeyError, OSError, zipfile.BadZipFile) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
