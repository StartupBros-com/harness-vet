"""Exercise the actual CI shell step with synthetic gh responses, offline."""

import base64
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
PIN = "a" * 40
CURRENT = "carries the current announce workflow"
SKIPPED = "::notice::could not read the announce workflow"
DRIFT = "::error::release-train pins"


def encoded(content):
    return base64.b64encode(content).decode("ascii")


def announce_step():
    lines = (ROOT / ".github/workflows/ci.yml").read_text().splitlines()
    start = lines.index("      - name: Announce workflow pin is current")
    start = lines.index("        run: |", start) + 1
    end = start
    while end < len(lines) and (not lines[end] or lines[end].startswith("          ")):
        end += 1
    return textwrap.dedent("\n".join(lines[start:end])) + "\n"


class AnnouncePinTests(unittest.TestCase):
    def run_check(self, pinned, main, *, pin=PIN):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = root / ".github/workflows/release-train.yml"
            workflow.parent.mkdir(parents=True)
            workflow.write_text(f"uses: example/hov-tool-drop-announce.yml@{pin}\n")
            binary = root / "bin"
            binary.mkdir()
            gh = binary / "gh"
            gh.write_text(
                f"#!{sys.executable}\n"
                "import os, sys\n"
                "assert len(sys.argv) == 5 and sys.argv[1] == 'api'\n"
                "assert sys.argv[3] == '--jq'\n"
                "prefix = 'repos/StartupBros-com/hov-marketplace/contents/'\n"
                "prefix += '.github/workflows/hov-tool-drop-announce.yml?ref='\n"
                "assert sys.argv[2].startswith(prefix)\n"
                f"assert sys.argv[2][len(prefix):] in ('main', '{PIN}')\n"
                "key = 'MAIN' if sys.argv[2].endswith('ref=main') else 'PINNED'\n"
                "sys.stdout.write(os.environ[key + '_CONTENT'])\n"
                "sys.exit(int(os.environ[key + '_STATUS']))\n"
            )
            gh.chmod(0o755)
            env = dict(os.environ, PATH=f"{binary}:{os.environ['PATH']}")
            for key, (content, status) in (("PINNED", pinned), ("MAIN", main)):
                env[f"{key}_CONTENT"] = content
                env[f"{key}_STATUS"] = str(status)
            return subprocess.run(
                ["bash", "--noprofile", "--norc", "-e", "-o", "pipefail", "-c", announce_step()],
                cwd=root, env=env, text=True, capture_output=True, timeout=10,
            )

    def test_matching_workflows_report_current(self):
        content = encoded(b"name: announce\n\non: workflow_call\n")
        # GitHub wraps base64 content; different wrapping must not mean drift.
        wrapped = "\n".join(content[i:i + 12] for i in range(0, len(content), 12)) + "\n"
        result = self.run_check((content, 0), (wrapped, 0))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(CURRENT, result.stdout)
        self.assertNotIn(SKIPPED, result.stdout)
        self.assertNotIn(DRIFT, result.stdout)

    def test_different_bytes_report_drift(self):
        for main in (b"name: changed\n", b"name: announce\n\n"):
            with self.subTest(main=main):
                result = self.run_check((encoded(b"name: announce\n"), 0), (encoded(main), 0))
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertIn(DRIFT, result.stdout)
                self.assertNotIn(CURRENT, result.stdout)
                self.assertNotIn(SKIPPED, result.stdout)

    def test_unreadable_workflows_skip_without_claiming_current(self):
        good = (encoded(b"name: announce\n"), 0)
        unreadable = {
            "fetch_failure": ("", 1),
            "fetch_failure_with_output": (good[0], 1),
            "empty_response": ("", 0),
            "blank_response": ("\n\n", 0),
            "invalid_base64": ("%%%", 0),
            "partial_decode": (good[0] + "%", 0),
        }
        for failure, bad in unreadable.items():
            for side, pinned, main in (("pinned", bad, good), ("main", good, bad), ("both", bad, bad)):
                with self.subTest(failure=failure, side=side):
                    result = self.run_check(pinned, main)
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                    self.assertNotIn(CURRENT, result.stdout)
                    self.assertIn(SKIPPED, result.stdout)
                    self.assertNotIn(DRIFT, result.stdout)

    def test_missing_pin_still_fails(self):
        good = (encoded(b"name: announce\n"), 0)
        result = self.run_check(good, good, pin="not-a-sha")
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn(CURRENT, result.stdout)
        self.assertNotIn(SKIPPED, result.stdout)


if __name__ == "__main__":
    unittest.main()
