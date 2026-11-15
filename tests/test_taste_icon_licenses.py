"""Exercise icon credits offline and retain the reviewed asset notices."""

import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/design-taste-frontend"
ICON_ASSETS = SKILL / "assets/icons"
SCRIPT = SKILL / "scripts/icons.mjs"
VSCODE_TERMS = (
    "https://github.com/vscode-icons/vscode-icons/blob/"
    "e8980080a2c491d60073df937c0aece669ba1486/README.md#license"
)
LUCIDE_TERMS = (
    "https://github.com/lucide-icons/lucide/blob/"
    "55782beff3a0133df79c417eb68f96e8f19e2404/LICENSE"
)
# Exact UTF-8 bytes of the full ISC/Feather MIT license at the pinned author ref.
LUCIDE_LICENSE_SHA256 = "b495047bd93a9b06913511076f504daba17d5bbeb3e0650f3bb53a4220329c57"
FILE_SOURCE = "https://cdn.jsdelivr.net/npm/@iconify-json/vscode-icons@1.2.30/icons.json"
UI_SOURCE = "https://cdn.jsdelivr.net/npm/@iconify-json/lucide@1.2.100/icons.json"


class TasteIconLicenseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.node = shutil.which("node")
        if cls.node is None:
            raise RuntimeError("Node.js is required for the offline Taste icon behavior tests")

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.site = self.directory / "site"
        self.cache = self.directory / "cache"
        self.site.mkdir()
        self.cache.mkdir()
        self.preload = self.directory / "offline.mjs"
        self.preload.write_text(
            "globalThis.fetch = async () => { throw new Error('Network disabled in icon tests'); };\n",
            encoding="utf-8",
        )
        self.env = {**os.environ, "TASTE_SKILL_ICON_CACHE": str(self.cache)}
        self.cache_json(FILE_SOURCE, {
            "prefix": "vscode-icons", "width": 32, "height": 32,
            "icons": {
                "default-file": {"body": '<path fill="#b7c6d1" d="M4 2h20v28H4z"/>'},
                "file-type-ai": {"body": '<rect fill="#ff9a00" x="2" y="2" width="28" height="28"/>'},
            },
        })
        self.cache_json(UI_SOURCE, {
            "prefix": "lucide", "width": 24, "height": 24,
            "icons": {"arrow-right": {"body": '<path d="M5 12h14m-6-6 6 6-6 6"/>'}},
        })

    def cache_json(self, url, content):
        filename = re.sub(r"[^a-z0-9.@-]+", "_", url.removeprefix("https://"), flags=re.I)
        (self.cache / filename).write_text(json.dumps(content), encoding="utf-8")

    def fetch_icons(self, *icons):
        result = subprocess.run(
            [self.node, "--import", str(self.preload), str(SCRIPT), "fetch", *icons, "--out", "icons"],
            cwd=self.site, env=self.env, capture_output=True, text=True, timeout=15,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads((self.site / "icons/icons-credits.json").read_text(encoding="utf-8"))

    def assert_file_terms(self, credit):
        self.assertIn("non-branded", credit["licence"])
        self.assertIn("owner-specific", credit["licence"])
        self.assertNotIn(credit["licence"], ("MIT", "CC-BY-SA-4.0"))
        self.assertEqual(credit["licenceUrl"], VSCODE_TERMS)
        self.assertEqual(credit["source"], "@iconify-json/vscode-icons@1.2.30")
        self.assertEqual(credit["sourceUrl"], FILE_SOURCE)
        self.assertEqual(credit["upstreamVersion"], "12.14.0")
        self.assertEqual(credit["author"], "Roberto Huertas")
        self.assertIsNone(credit["trademark"])
        for wording in ("source code under MIT", "CC BY-SA 4.0", "branded icons", "own copyright licenses"):
            self.assertIn(wording, credit["terms"])

    def test_cli_preserves_scoped_terms_and_copies_complete_notices(self):
        rows = self.fetch_icons("file:default-file", "file:file-type-ai", "ui:arrow-right")
        credits = {row["icon"]: row for row in rows}
        self.assertEqual(set(credits), {"file:default-file", "file:file-type-ai", "ui:arrow-right"})
        for icon in ("file:default-file", "file:file-type-ai"):
            credit = credits[icon]
            self.assert_file_terms(credit)
            self.assertEqual(credit["noticeFile"], "VSCODE-ICONS-NOTICE.md")
            self.assertEqual(
                (self.site / "icons" / credit["noticeFile"]).read_bytes(),
                (ICON_ASSETS / "VSCODE-ICONS-NOTICE.md").read_bytes(),
            )
        self.assertIn('fill="#ff9a00"', (self.site / "icons/ai.svg").read_text())
        self.assertIn('d="M4 2h20v28H4z"', (self.site / "icons/file.svg").read_text())
        ui = credits["ui:arrow-right"]
        self.assertIn("ISC", ui["licence"])
        self.assertIn("MIT for Feather-derived", ui["licence"])
        self.assertEqual(ui["sourceUrl"], UI_SOURCE)
        self.assertEqual(ui["licenceUrl"], LUCIDE_TERMS)
        self.assertIs(ui["trademark"], False)
        self.assertEqual(ui["noticeFile"], "LUCIDE-LICENSE.txt")
        copied = (self.site / "icons" / ui["noticeFile"]).read_bytes()
        self.assertEqual(copied, (ICON_ASSETS / "LUCIDE-LICENSE.txt").read_bytes())
        self.assertEqual(hashlib.sha256(copied).hexdigest(), LUCIDE_LICENSE_SHA256)
        self.assertIn('d="M5 12h14m-6-6 6 6-6 6"', (self.site / "icons/ui-arrow-right.svg").read_text())

    def test_refetch_replaces_stale_credit_without_losing_unrelated_records(self):
        out = self.site / "icons"
        out.mkdir()
        unrelated = {"file": "unrelated.svg", "icon": "local:unrelated", "licence": "Existing terms", "custom": "keep"}
        stale = {"file": "ai.svg", "icon": "file:file-type-ai", "licence": "MIT", "trademark": False}
        (out / "icons-credits.json").write_text(json.dumps([unrelated, stale]), encoding="utf-8")
        first = self.fetch_icons("file:file-type-ai", "ui:arrow-right")
        second = self.fetch_icons("file:ai", "ui:arrow-right")
        self.assertEqual(first, second)
        self.assertIn(unrelated, second)
        self.assertEqual(len(second), 3)
        self.assertEqual([row["file"] for row in second], sorted(row["file"] for row in second))
        self.assert_file_terms(next(row for row in second if row["icon"] == "file:file-type-ai"))
        for row in second:
            if "noticeFile" in row:
                self.assertTrue((out / row["noticeFile"]).is_file())


class BundledIconNoticeTests(unittest.TestCase):
    def test_complete_author_notice_and_scoped_notice_are_locked(self):
        self.assertEqual(
            hashlib.sha256((ICON_ASSETS / "LUCIDE-LICENSE.txt").read_bytes()).hexdigest(),
            LUCIDE_LICENSE_SHA256,
        )
        notice = (ICON_ASSETS / "VSCODE-ICONS-NOTICE.md").read_text(encoding="utf-8")
        self.assertIn(VSCODE_TERMS, notice)
        self.assertIn("https://creativecommons.org/licenses/by-sa/4.0/", notice)
        self.assertIn("Branded icons retain their own copyright licenses", notice)
        lock = json.loads((ROOT / "packaging/pavurel-design/required-design-skills.json").read_text())
        vendor = next(entry for entry in lock["skills"] if entry["name"] == "design-taste-frontend")
        records = {entry["path"]: entry["sha256"] for entry in vendor["files"]}
        for name in ("LUCIDE-LICENSE.txt", "VSCODE-ICONS-NOTICE.md"):
            self.assertEqual(records["assets/icons/" + name], hashlib.sha256((ICON_ASSETS / name).read_bytes()).hexdigest())

    def test_bundled_credits_and_index_retain_correct_source_terms(self):
        index = json.loads((ICON_ASSETS / "index.json").read_text())
        counts = {"file": 0, "ui": 0}
        for file in (ICON_ASSETS / "demo/icons-credits.json", SKILL / "assets/ui/icons/icons-credits.json"):
            rows = json.loads(file.read_text())
            for row in rows:
                set_name = row["icon"].split(":", 1)[0]
                if set_name not in counts:
                    continue
                counts[set_name] += 1
                metadata = index["sets"][set_name]
                for key in ("licence", "licenceUrl", "terms"):
                    self.assertEqual(row[key], metadata[key])
                self.assertEqual(row["source"], metadata["pkg"])
                self.assertTrue((file.parent / row["noticeFile"]).is_file())
                if set_name == "file":
                    self.assertIsNone(row["trademark"])
                    self.assertEqual(row["licenceUrl"], VSCODE_TERMS)
                    self.assertIn("owner-specific", row["licence"])
                    self.assertEqual(row["sourceUrl"], FILE_SOURCE)
                else:
                    self.assertEqual(row["licenceUrl"], LUCIDE_TERMS)
                    self.assertEqual(row["sourceUrl"], UI_SOURCE)
                    self.assertEqual(
                        hashlib.sha256((file.parent / row["noticeFile"]).read_bytes()).hexdigest(),
                        LUCIDE_LICENSE_SHA256,
                    )
        self.assertEqual(counts, {"file": 35, "ui": 432})


if __name__ == "__main__":
    unittest.main()
