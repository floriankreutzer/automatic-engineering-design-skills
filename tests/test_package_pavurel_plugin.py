"""Check the real archive once and exercise failures with small source fixtures."""

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import stat
import tempfile
import unittest
import zipfile


SOURCE_ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "package_pavurel_plugin", SOURCE_ROOT / "scripts/package_pavurel_plugin.py"
)
PACKAGE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(PACKAGE)
SOURCE_REF = "a" * 40
LOCK_PATH = "packaging/pavurel-design/required-design-skills.json"
CATALOG_PATH = "packaging/pavurel-design/skill-catalog.json"
POLICY_PATH = "references/skill-policy.md"
BASELINE_RESOURCES = {
    "21st-design-research": ["references/21st-reference.md"],
    "animate": ["RECIPES.md"],
    "animate-expo": ["RECIPES.md"],
    "animation-performance": [],
    "animation-vocabulary": [],
    "apple-design": [],
    "ask-sonner": ["API.md"],
    "break-ui": ["CATALOG.md"],
    "emil-design-eng": ["references/component-patterns.md"],
    "find-animation-opportunities": [],
    "improve-animations": ["AUDIT.md", "PLAN-TEMPLATE.md"],
    "mobile-native": [],
    "pavurel-app-design": [
        "references/customer.md", "references/platform.md", "references/repository-sources.md",
        "references/required-design-review.md",
    ],
    "pavurel-web-design": ["references/website-context.md", "references/required-design-review.md"],
    "pick-ui-library": [],
    "prototype": ["PICKER.md"],
    "review-animations": ["STANDARDS.md"],
    "write-swift": [],
}
EXPECTED_SKILLS = set(BASELINE_RESOURCES) | {"impeccable", "design-taste-frontend"}


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.root = self.directory / "source"
        self.output = self.directory / "package.zip"
        self.manifest = {
            "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
            "name": "pavurel-design",
            "version": "1.1.0",
            "extensions": {"com.openai": {"interface": {
                "displayName": "Pavurel Design",
                "shortDescription": "Pavurel design workflows",
                "defaultPrompt": ["Website review", "App review", "Requested 21st research"],
            }}},
        }
        self.write("packaging/pavurel-design/plugin.json", json.dumps(self.manifest))
        self.write("LICENSE", "Original MIT notice\n")
        self.write("THIRD_PARTY_NOTICES.md", "Required skills retain their own licenses.\n")
        self.policy = ("# Skill policy\n\nEvery skill is required when its task applies.\n\n"
                       + "\n".join(f"| `{name}` | Relevant task |" for name in sorted(EXPECTED_SKILLS))
                       + "\n").encode("utf-8")
        self.write("SKILL_POLICY.md", self.policy)
        self.catalog = {"schema_version": 1, "policy": "required-when-applicable", "skills": []}
        for name, files in BASELINE_RESOURCES.items():
            self.write(f"skills/{name}/SKILL.md", f"---\nname: {name}\ndescription: Review.\n---\n"
                       "\nRead [the mandatory skill policy](references/skill-policy.md).\n")
            self.write(
                f"skills/{name}/agents/openai.yaml",
                "policy:\n  allow_implicit_invocation: true\n",
            )
            self.write(f"skills/{name}/{POLICY_PATH}", self.policy)
            for filename in files:
                self.write(f"skills/{name}/{filename}", f"# {filename}\n")
            self.catalog["skills"].append({
                "name": name, "files": sorted(["SKILL.md", "agents/openai.yaml", POLICY_PATH, *files]),
            })

        self.vendor_files = {
            "impeccable": {
                "SKILL.md": b"---\nname: impeccable\ndescription: Design guidance.\n---\n",
                "agents/openai.yaml": b"policy:\n  allow_implicit_invocation: true\n",
                "LICENSE": b"Apache 2.0 notice\n",
                "NOTICE.md": b"Original Impeccable attribution\n",
                "references/review.md": b"# Evidence-based review\n",
                POLICY_PATH: self.policy,
            },
            "design-taste-frontend": {
                "SKILL.md": b"---\nname: design-taste-frontend\ndescription: Website design.\n---\n",
                "agents/openai.yaml": b"policy:\n  allow_implicit_invocation: true\n",
                "LICENSE": b"Taste MIT notice\n",
                "references/layout.md": b"# Layout guidance\n",
                "assets/example.zip": b"\x00\xff\x01binary test resource\x00",
                "scripts/check.mjs": b"throw new Error('Packaging must not execute this helper');\n",
                POLICY_PATH: self.policy,
            },
        }
        metadata = {
            "impeccable": {
                "upstream_url": "https://github.com/pbakaus/impeccable",
                "upstream_ref": "b" * 40, "upstream_version": "4.9.1",
                "edition": "reference-only", "license": "Apache-2.0",
            },
            "design-taste-frontend": {
                "upstream_url": "https://github.com/Leonxlnx/taste-skill",
                "upstream_ref": "c" * 40, "upstream_version": "2.5.1",
                "edition": "chatgpt-compatible", "license": "MIT",
            },
        }
        self.lock = {"schema_version": 1, "skills": []}
        for name, files in self.vendor_files.items():
            files["SKILL.md"] += b"\nRead [the mandatory skill policy](references/skill-policy.md).\n"
            self.catalog["skills"].append({"name": name, "vendor_lock": True})
            entry = {"name": name, **metadata[name], "files": []}
            for relative, content in sorted(files.items()):
                self.write(f"skills/{name}/{relative}", content)
                entry["files"].append({
                    "path": relative, "sha256": hashlib.sha256(content).hexdigest(),
                })
            self.lock["skills"].append(entry)
        self.write_lock(self.lock)
        self.catalog["skills"].sort(key=lambda entry: entry["name"])
        self.write_catalog(self.catalog)

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode("utf-8") if isinstance(content, str) else content)

    def write_lock(self, lock):
        self.write(LOCK_PATH, json.dumps(lock, sort_keys=True, indent=2) + "\n")

    def write_catalog(self, catalog):
        self.write(CATALOG_PATH, json.dumps(catalog, sort_keys=True, indent=2) + "\n")

    def build(self, output=None, source_ref=SOURCE_REF):
        return PACKAGE.build(self.root, output or self.output, source_ref)

    def test_complete_package_preserves_all_twenty_skills_and_resource_bytes(self):
        result = self.build()
        self.assertEqual(set(result["skills"]), EXPECTED_SKILLS)
        self.assertEqual(result["source_ref"], SOURCE_REF)
        with zipfile.ZipFile(self.output) as archive:
            names = archive.namelist()
            actual_skills = {
                name.split("/")[2] for name in names
                if name.startswith("pavurel-design/skills/") and name.endswith("/SKILL.md")
            }
            self.assertEqual(actual_skills, EXPECTED_SKILLS)
            self.assertEqual(len(names), len(set(names)))
            self.assertEqual(names, sorted(names))
            self.assertEqual(result["files"], len(names))
            self.assertEqual(json.loads(archive.read("pavurel-design/plugin.json")), self.manifest)
            self.assertEqual(json.loads(archive.read("pavurel-design/required-design-skills.json")), self.lock)
            self.assertEqual(json.loads(archive.read("pavurel-design/skill-catalog.json")), self.catalog)
            self.assertEqual(archive.read("pavurel-design/SKILL_POLICY.md"), self.policy)
            for name in EXPECTED_SKILLS:
                metadata = f"skills/{name}/agents/openai.yaml"
                self.assertEqual(archive.read("pavurel-design/" + metadata), (self.root / metadata).read_bytes())
                self.assertEqual(archive.read(f"pavurel-design/skills/{name}/{POLICY_PATH}"), self.policy)
            for name, files in self.vendor_files.items():
                for relative, content in files.items():
                    self.assertEqual(archive.read(f"pavurel-design/skills/{name}/{relative}"), content)
            provenance = json.loads(archive.read("pavurel-design/source-provenance.json"))
            self.assertEqual(provenance["reviewed_source_ref"], SOURCE_REF)
            self.assertEqual(provenance["required_design_skills_lock"], "required-design-skills.json")
            self.assertEqual(provenance["skill_catalog"], "skill-catalog.json")
            self.assertEqual(provenance["skill_policy"], "SKILL_POLICY.md")
            self.assertEqual(
                {skill["name"] for skill in provenance["required_design_skills"]},
                {"impeccable", "design-taste-frontend"},
            )
            for name, record in provenance["files"].items():
                original = (self.root / record["source_path"]).read_bytes()
                self.assertEqual(archive.read("pavurel-design/" + name), original)
                self.assertEqual(record["sha256"], hashlib.sha256(original).hexdigest())
            for info in archive.infolist():
                self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0))
                self.assertEqual(info.external_attr >> 16, stat.S_IFREG | 0o644)

    def test_identical_inputs_are_deterministic_despite_file_mtimes(self):
        first = self.build()
        for path in self.root.rglob("*"):
            if path.is_file():
                os.utime(path, (123456789, 123456789))
        second_path = self.directory / "again.zip"
        second = self.build(output=second_path)
        self.assertEqual(self.output.read_bytes(), second_path.read_bytes())
        self.assertEqual(first["sha256"], second["sha256"])

    def test_implicit_invocation_cannot_be_missing_false_or_ambiguous(self):
        for metadata in (
            "interface:\n  display_name: Prototype\n",
            "policy:\n  allow_implicit_invocation: false\n",
            "policy:\n  allow_implicit_invocation: true\n  allow_implicit_invocation: false\n",
            "policy:\n  allow_implicit_invocation: true\npolicy:\n  allow_implicit_invocation: true\n",
            "policy:\n  allow_implicit_invocation: 'true'\n",
        ):
            with self.subTest(metadata=metadata):
                self.write("skills/prototype/agents/openai.yaml", metadata)
                with self.assertRaisesRegex(ValueError, "implicit invocation policy"):
                    self.build()
                self.assertFalse(self.output.exists())

    def test_each_skill_entrypoint_requires_matching_name_and_policy_link(self):
        for body, error in (
            ("---\nname: prototype\ndescription: Review.\n---\n", "Missing mandatory routing link"),
            ("---\nname: another-skill\ndescription: Review.\n---\n", "frontmatter name"),
            ("# Missing frontmatter\n", "frontmatter name"),
        ):
            with self.subTest(body=body):
                self.write("skills/prototype/SKILL.md", body)
                with self.assertRaisesRegex(ValueError, error):
                    self.build()
                self.assertFalse(self.output.exists())

    def test_policy_table_must_include_every_skill_exactly_once(self):
        for content in (
            self.policy.replace(b"| `prototype` | Relevant task |\n", b""),
            self.policy + b"| `prototype` | Duplicate row |\n",
            self.policy + b"| `unknown-skill` | Unreviewed row |\n",
        ):
            with self.subTest(content=content):
                self.write("SKILL_POLICY.md", content)
                for name in EXPECTED_SKILLS:
                    self.write(f"skills/{name}/{POLICY_PATH}", content)
                changed = copy.deepcopy(self.lock)
                for skill in changed["skills"]:
                    for record in skill["files"]:
                        if record["path"] == POLICY_PATH:
                            record["sha256"] = hashlib.sha256(content).hexdigest()
                self.write_lock(changed)
                with self.assertRaisesRegex(ValueError, "policy table"):
                    self.build()
                self.assertFalse(self.output.exists())

    def test_each_required_skill_must_be_present_in_the_lock(self):
        for missing in ("impeccable", "design-taste-frontend"):
            with self.subTest(missing=missing):
                changed = copy.deepcopy(self.lock)
                changed["skills"] = [entry for entry in changed["skills"] if entry["name"] != missing]
                self.write_lock(changed)
                with self.assertRaisesRegex(ValueError, "exactly both required"):
                    self.build()
                self.assertFalse(self.output.exists())

    def test_all_twenty_skills_must_exist_on_disk(self):
        for name in sorted(EXPECTED_SKILLS):
            with self.subTest(name=name):
                path = self.root / "skills" / name
                parked = self.directory / "parked"
                path.rename(parked)
                try:
                    with self.assertRaisesRegex(ValueError, "catalog does not match source entrypoints"):
                        self.build()
                finally:
                    parked.rename(path)
                self.assertFalse(self.output.exists())

    def test_missing_resource_does_not_replace_a_previous_archive(self):
        self.output.write_bytes(b"previous accepted archive")
        (self.root / "skills/design-taste-frontend/references/layout.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing source file"):
            self.build()
        self.assertEqual(self.output.read_bytes(), b"previous accepted archive")

    def test_modified_resource_requires_a_reviewed_hash_update(self):
        self.write("skills/design-taste-frontend/scripts/check.mjs", "changed helper")
        with self.assertRaisesRegex(ValueError, "Source hash mismatch"):
            self.build()
        self.assertFalse(self.output.exists())

    def test_required_entrypoint_metadata_and_licenses_cannot_be_omitted(self):
        for name, relative in (
            ("impeccable", "SKILL.md"), ("impeccable", "NOTICE.md"),
            ("design-taste-frontend", "agents/openai.yaml"), ("design-taste-frontend", "LICENSE"),
            ("impeccable", POLICY_PATH), ("design-taste-frontend", POLICY_PATH),
        ):
            with self.subTest(name=name, relative=relative):
                changed = copy.deepcopy(self.lock)
                for entry in changed["skills"]:
                    if entry["name"] == name:
                        entry["files"] = [record for record in entry["files"] if record["path"] != relative]
                self.write_lock(changed)
                with self.assertRaisesRegex(ValueError, "Missing required entrypoint"):
                    self.build()

    def test_source_file_and_ancestor_symlinks_are_refused(self):
        for relative in (
            "skills/design-taste-frontend/references/layout.md",
            "skills/design-taste-frontend/references",
            "skills/animate", "skills", "SKILL_POLICY.md", LOCK_PATH, CATALOG_PATH,
        ):
            with self.subTest(relative=relative):
                path = self.root / relative
                parked = self.directory / "parked"
                path.rename(parked)
                path.symlink_to(parked, target_is_directory=parked.is_dir())
                try:
                    with self.assertRaisesRegex(ValueError, "Refusing symbolic link"):
                        self.build()
                finally:
                    path.unlink()
                    parked.rename(path)
                self.assertFalse(self.output.exists())

    def test_unsafe_noncanonical_and_hidden_locked_paths_are_refused(self):
        for relative in (
            "../outside.md", "/outside.md", "C:/outside.md", "references\\outside.md",
            "references//guide.md", "./SKILL.md", ".", "references/../guide.md",
            "references/./guide.md", "references/name\n.md", "references/.env",
        ):
            with self.subTest(relative=relative):
                changed = copy.deepcopy(self.lock)
                changed["skills"][1]["files"].append({"path": relative, "sha256": "d" * 64})
                self.write_lock(changed)
                with self.assertRaisesRegex(ValueError, "Invalid relative source path"):
                    self.build()
                self.assertFalse(self.output.exists())

    def test_duplicate_skill_and_file_records_are_refused(self):
        changed = copy.deepcopy(self.lock)
        changed["skills"].append(copy.deepcopy(changed["skills"][0]))
        self.write_lock(changed)
        with self.assertRaisesRegex(ValueError, "Duplicate required skill"):
            self.build()
        changed = copy.deepcopy(self.lock)
        changed["skills"][0]["files"].append(copy.deepcopy(changed["skills"][0]["files"][0]))
        self.write_lock(changed)
        with self.assertRaisesRegex(ValueError, "Duplicate required skill file"):
            self.build()

    def test_unknown_skill_and_unreviewed_impeccable_runtime_are_refused(self):
        changed = copy.deepcopy(self.lock)
        changed["skills"][0]["name"] = "another-skill"
        self.write_lock(changed)
        with self.assertRaisesRegex(ValueError, "Unexpected required skill"):
            self.build()
        changed = copy.deepcopy(self.lock)
        changed["skills"][0]["files"].append({"path": "scripts/engine", "sha256": "d" * 64})
        self.write_lock(changed)
        with self.assertRaisesRegex(ValueError, "reference-only Impeccable"):
            self.build()

    def test_provenance_and_hash_shapes_are_checked(self):
        for key, value in (
            ("edition", "full-runtime"), ("license", "Unspecified"),
            ("upstream_url", "https://example.com/replacement"), ("upstream_ref", "main"),
            ("upstream_version", ""),
        ):
            with self.subTest(key=key):
                changed = copy.deepcopy(self.lock)
                changed["skills"][0][key] = value
                self.write_lock(changed)
                with self.assertRaises(ValueError):
                    self.build()
        changed = copy.deepcopy(self.lock)
        changed["skills"][0]["files"][0]["sha256"] = "not-a-hash"
        self.write_lock(changed)
        with self.assertRaisesRegex(ValueError, "Invalid sha256"):
            self.build()

    def test_duplicate_json_keys_and_unsupported_lock_schema_are_refused(self):
        self.write(LOCK_PATH, '{"schema_version":1,"schema_version":1,"skills":[]}')
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            self.build()
        for version in (2, True, "1", None):
            with self.subTest(version=version):
                changed = copy.deepcopy(self.lock)
                changed["schema_version"] = version
                self.write_lock(changed)
                with self.assertRaisesRegex(ValueError, "schema_version 1"):
                    self.build()

    def test_unlisted_files_never_enter_the_archive(self):
        for relative in (
            ".env", "skills/design-taste-frontend/private-notes.txt",
            "skills/impeccable/scripts/unrequested-helper.py", "skills/animate/local-notes.md",
            "skills/unrelated/notes.md",
        ):
            self.write(relative, "UNLISTED_TEST_CANARY")
        self.build()
        with zipfile.ZipFile(self.output) as archive:
            self.assertFalse(any("UNLISTED_TEST_CANARY".encode() in archive.read(name) for name in archive.namelist()))

    def test_new_skill_requires_an_explicit_catalog_update(self):
        self.write("skills/new-skill/SKILL.md", "# New skill\n")
        with self.assertRaisesRegex(ValueError, "unlisted=\\['new-skill'\\]"):
            self.build()
        self.assertFalse(self.output.exists())

    def test_each_skill_must_be_present_in_the_catalog(self):
        for name in sorted(EXPECTED_SKILLS):
            with self.subTest(name=name):
                changed = copy.deepcopy(self.catalog)
                changed["skills"] = [entry for entry in changed["skills"] if entry["name"] != name]
                self.write_catalog(changed)
                with self.assertRaises(ValueError):
                    self.build()
                self.assertFalse(self.output.exists())

    def test_catalog_requires_entrypoint_metadata_and_policy(self):
        for relative in ("SKILL.md", "agents/openai.yaml", POLICY_PATH):
            with self.subTest(relative=relative):
                changed = copy.deepcopy(self.catalog)
                changed["skills"][0]["files"].remove(relative)
                self.write_catalog(changed)
                with self.assertRaisesRegex(ValueError, "Missing required entrypoint, metadata or policy"):
                    self.build()

    def test_missing_catalog_resource_is_refused(self):
        (self.root / "skills/animate/RECIPES.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing source file: skills/animate/RECIPES.md"):
            self.build()
        self.assertFalse(self.output.exists())

    def test_missing_canonical_policy_is_refused(self):
        (self.root / "SKILL_POLICY.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing source file: SKILL_POLICY.md"):
            self.build()

    def test_every_policy_copy_must_equal_canonical_policy(self):
        altered = b"# Inconsistent policy\n"
        for name in sorted(EXPECTED_SKILLS):
            with self.subTest(name=name):
                self.write(f"skills/{name}/{POLICY_PATH}", altered)
                changed = copy.deepcopy(self.lock)
                for skill in changed["skills"]:
                    if skill["name"] == name:
                        for record in skill["files"]:
                            if record["path"] == POLICY_PATH:
                                record["sha256"] = hashlib.sha256(altered).hexdigest()
                self.write_lock(changed)
                with self.assertRaisesRegex(ValueError, "Skill policy differs from canonical"):
                    self.build()
                self.assertFalse(self.output.exists())
                self.write(f"skills/{name}/{POLICY_PATH}", self.policy)
        self.write_lock(self.lock)
        self.write("SKILL_POLICY.md", altered)
        with self.assertRaisesRegex(ValueError, "Skill policy differs from canonical"):
            self.build()

    def test_catalog_duplicate_entries_and_paths_are_refused(self):
        changed = copy.deepcopy(self.catalog)
        changed["skills"].append(copy.deepcopy(changed["skills"][0]))
        self.write_catalog(changed)
        with self.assertRaisesRegex(ValueError, "Duplicate catalog skill"):
            self.build()
        changed = copy.deepcopy(self.catalog)
        changed["skills"][0]["files"].append("SKILL.md")
        self.write_catalog(changed)
        with self.assertRaisesRegex(ValueError, "Duplicate catalog skill file"):
            self.build()

    def test_catalog_skill_names_paths_and_vendor_inventory_boundaries_are_checked(self):
        for name in ("../escape", "/absolute", "nested/name", "mixedCase", "bad\\name", ""):
            with self.subTest(name=name):
                changed = copy.deepcopy(self.catalog)
                changed["skills"][0]["name"] = name
                self.write_catalog(changed)
                with self.assertRaisesRegex(ValueError, "Invalid catalog skill name"):
                    self.build()
        for path in ("../outside", "/absolute", "references\\escape.md", ".env", "references//a.md"):
            with self.subTest(path=path):
                changed = copy.deepcopy(self.catalog)
                changed["skills"][0]["files"].append(path)
                self.write_catalog(changed)
                with self.assertRaisesRegex(ValueError, "Invalid relative source path"):
                    self.build()
        changed = copy.deepcopy(self.catalog)
        changed["skills"][0] = {"name": "21st-design-research", "vendor_lock": True}
        self.write_catalog(changed)
        with self.assertRaisesRegex(ValueError, "explicit files list"):
            self.build()
        changed = copy.deepcopy(self.catalog)
        for entry in changed["skills"]:
            if entry["name"] == "impeccable":
                entry["files"] = ["SKILL.md", "agents/openai.yaml", POLICY_PATH]
        self.write_catalog(changed)
        with self.assertRaisesRegex(ValueError, "must use its existing vendor lock"):
            self.build()

    def test_catalog_schema_and_required_policy_cannot_be_changed_silently(self):
        self.write(CATALOG_PATH, '{"schema_version":1,"schema_version":1}')
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            self.build()
        for key, value in (
            ("schema_version", 2), ("schema_version", True), ("skills", None),
            ("policy", "optional"), ("policy", None),
        ):
            with self.subTest(key=key, value=value):
                changed = copy.deepcopy(self.catalog)
                changed[key] = value
                self.write_catalog(changed)
                with self.assertRaises(ValueError):
                    self.build()

    def test_source_ref_must_be_a_full_lowercase_commit_sha(self):
        for source_ref in ("main", "A" * 40, "a" * 39, "a" * 41, None, SOURCE_REF + "\n"):
            with self.subTest(source_ref=source_ref):
                with self.assertRaisesRegex(ValueError, "full reviewed Git commit SHA"):
                    self.build(source_ref=source_ref)
                self.assertFalse(self.output.exists())

    def test_output_cannot_overwrite_a_locked_resource_or_its_hard_link(self):
        source = self.root / "skills/design-taste-frontend/assets/example.zip"
        original = source.read_bytes()
        with self.assertRaisesRegex(ValueError, "must not overwrite"):
            self.build(output=source)
        os.link(source, self.output)
        with self.assertRaisesRegex(ValueError, "hard link"):
            self.build()
        self.assertEqual(source.read_bytes(), original)

    def test_output_symlink_and_symlink_parent_are_refused(self):
        target = self.directory / "target.zip"
        target.write_bytes(b"untouched")
        self.output.symlink_to(target)
        with self.assertRaisesRegex(ValueError, "symbolic-link output"):
            self.build()
        self.assertEqual(target.read_bytes(), b"untouched")
        self.output.unlink()
        parent = self.directory / "linked-output"
        parent.symlink_to(self.directory, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symbolic-link output"):
            self.build(output=parent / "new.zip")


class RepositoryPackageTests(unittest.TestCase):
    def test_real_repository_build_includes_all_twenty_skills_and_their_resources(self):
        lock = json.loads((SOURCE_ROOT / LOCK_PATH).read_bytes())
        expected_paths = {
            "plugin.json", "LICENSE", "THIRD_PARTY_NOTICES.md", "NOTICE.md",
            "required-design-skills.json", "source-provenance.json", "skill-catalog.json",
            "SKILL_POLICY.md",
        }
        for name, references in BASELINE_RESOURCES.items():
            expected_paths.update({
                f"skills/{name}/SKILL.md", f"skills/{name}/agents/openai.yaml", f"skills/{name}/{POLICY_PATH}",
            })
            expected_paths.update(f"skills/{name}/{reference}" for reference in references)
        for skill in lock["skills"]:
            expected_paths.update(f"skills/{skill['name']}/{record['path']}" for record in skill["files"])

        # Test provenance is synthetic; this temporary archive is never published.
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "test-only.zip"
            result = PACKAGE.build(SOURCE_ROOT, output, SOURCE_REF)
            self.assertEqual(set(result["skills"]), EXPECTED_SKILLS)
            with zipfile.ZipFile(output) as archive:
                self.assertEqual(set(archive.namelist()), {"pavurel-design/" + path for path in expected_paths})
                actual_skills = {
                    path.split("/")[2] for path in archive.namelist()
                    if path.startswith("pavurel-design/skills/") and path.endswith("/SKILL.md")
                }
                self.assertEqual(actual_skills, EXPECTED_SKILLS)
                policy = (SOURCE_ROOT / "SKILL_POLICY.md").read_bytes()
                self.assertEqual(archive.read("pavurel-design/SKILL_POLICY.md"), policy)
                for name in EXPECTED_SKILLS:
                    self.assertEqual(archive.read(f"pavurel-design/skills/{name}/{POLICY_PATH}"), policy)
                    metadata = f"skills/{name}/agents/openai.yaml"
                    self.assertEqual(archive.read("pavurel-design/" + metadata), (SOURCE_ROOT / metadata).read_bytes())
                for skill in lock["skills"]:
                    for record in skill["files"]:
                        path = f"skills/{skill['name']}/{record['path']}"
                        content = archive.read("pavurel-design/" + path)
                        self.assertEqual(hashlib.sha256(content).hexdigest(), record["sha256"], path)
                        self.assertEqual(content, (SOURCE_ROOT / path).read_bytes(), path)
                self.assertEqual(
                    archive.read("pavurel-design/plugin.json"),
                    (SOURCE_ROOT / "packaging/pavurel-design/plugin.json").read_bytes(),
                )
                self.assertEqual(
                    archive.read("pavurel-design/required-design-skills.json"),
                    (SOURCE_ROOT / LOCK_PATH).read_bytes(),
                )
                self.assertEqual(
                    archive.read("pavurel-design/skill-catalog.json"),
                    (SOURCE_ROOT / CATALOG_PATH).read_bytes(),
                )


if __name__ == "__main__":
    unittest.main()
