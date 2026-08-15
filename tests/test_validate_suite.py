import sys
import tempfile
import unittest
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from validate_suite import REQUIRED_SKILLS, validate_plugin_root


def create_minimum_suite(plugin_root: Path) -> None:
    for name in REQUIRED_SKILLS:
        skill_path = plugin_root / "skills" / name / "SKILL.md"
        skill_path.parent.mkdir(parents=True, exist_ok=True)
        skill_path.write_text("# Placeholder\n", encoding="utf-8")


class ValidateSuiteTests(unittest.TestCase):
    def test_reports_missing_required_skill(self):
        with tempfile.TemporaryDirectory() as directory:
            errors = validate_plugin_root(Path(directory))
        self.assertTrue(any("erp-transformation-orchestrator" in error for error in errors))

    def test_accepts_complete_minimum_suite(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            self.assertEqual(validate_plugin_root(plugin_root), [])


if __name__ == "__main__":
    unittest.main()
