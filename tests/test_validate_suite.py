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
    write_skill(
        plugin_root,
        "erp-evidence-intake",
        "stakeholder observation; calculation assumption; hypothesis; "
        "Hypothesis / Gap Register; not an Evidence ID\n",
    )
    write_skill(
        plugin_root,
        "erp-governance-traceability",
        "Validation Owner; reversal condition\n",
    )
    write_skill(
        plugin_root,
        "erp-process-playbooks",
        "## O2C\n## P2P\n## R2R\n## M2M\n## Warehouse and Inventory\n## Pricing\n## Master Data\n",
    )
    write_skill(
        plugin_root,
        "erp-scoring-benchmarking",
        "Formula; Coverage; Evidence IDs; Assumptions; Confidence\n",
    )
    write_skill(
        plugin_root,
        "erp-industry-variants",
        "Industry pattern guidance, not client fact\n"
        "## Manufacturing\n## Distribution\n## Retail\n"
        "## Project Business\n## Regulated Operations\n",
    )
    write_skill(
        plugin_root,
        "erp-executive-transformation",
        "Facts; Stakeholder observations; Hypotheses; Recommendations\n",
    )
    write_template(plugin_root, "import-profile.md", "grain | business key\n")
    write_template(
        plugin_root,
        "executive-pack.md",
        "## Facts\n## Stakeholder observations\n## Hypotheses\n## Recommendations\n",
    )


def write_skill(plugin_root: Path, name: str, content: str) -> None:
    skill_path = plugin_root / "skills" / name / "SKILL.md"
    skill_path.parent.mkdir(parents=True, exist_ok=True)
    skill_path.write_text(content, encoding="utf-8")


def write_template(plugin_root: Path, name: str, content: str) -> None:
    template_path = plugin_root / "references" / "templates" / name
    template_path.parent.mkdir(parents=True, exist_ok=True)
    template_path.write_text(content, encoding="utf-8")


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

    def test_evidence_skill_requires_statement_types(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_skill(plugin_root, "erp-evidence-intake", "# Evidence Intake\n")
            errors = validate_plugin_root(plugin_root)
        self.assertIn("erp-evidence-intake: missing statement-type rule", errors)

    def test_evidence_skill_requires_gap_traceability_for_unsupported_hypotheses(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_skill(
                plugin_root,
                "erp-evidence-intake",
                "stakeholder observation; calculation assumption; hypothesis\n",
            )
            errors = validate_plugin_root(plugin_root)
        self.assertIn(
            "erp-evidence-intake: missing unsupported-hypothesis traceability rule",
            errors,
        )

    def test_playbook_lists_all_domains(self):
        domains = (
            "O2C",
            "P2P",
            "R2R",
            "M2M",
            "Warehouse and Inventory",
            "Pricing",
            "Master Data",
        )
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            for missing_domain in domains:
                with self.subTest(missing_domain=missing_domain):
                    create_minimum_suite(plugin_root)
                    remaining_domains = (
                        domain for domain in domains if domain != missing_domain
                    )
                    write_skill(
                        plugin_root,
                        "erp-process-playbooks",
                        "\n".join(f"## {domain}" for domain in remaining_domains),
                    )
                    errors = validate_plugin_root(plugin_root)
                    self.assertIn(
                        f"erp-process-playbooks: missing domain {missing_domain}",
                        errors,
                    )

    def test_rapid_audit_delegates_executive_outputs(self):
        audit_skill = (
            Path(__file__).resolve().parents[1]
            / "skills"
            / "erp-process-audit"
            / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertIn("Delegate the executive summary", audit_skill)
        self.assertNotIn("shaping the executive narrative", audit_skill)
        self.assertNotIn("Start with an executive summary", audit_skill)

    def test_scorecard_requires_formula_coverage_and_confidence(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_skill(
                plugin_root,
                "erp-scoring-benchmarking",
                "## Scorecard\nMetric | Result\n",
            )
            errors = validate_plugin_root(plugin_root)
        self.assertIn("erp-scoring-benchmarking: missing formula rule", errors)
        self.assertIn("erp-scoring-benchmarking: missing coverage rule", errors)
        self.assertIn("erp-scoring-benchmarking: missing evidence-ID rule", errors)
        self.assertIn("erp-scoring-benchmarking: missing assumptions rule", errors)
        self.assertIn("erp-scoring-benchmarking: missing confidence rule", errors)

    def test_industry_skill_requires_all_bounded_patterns(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_skill(
                plugin_root,
                "erp-industry-variants",
                "Industry pattern guidance, not client fact\n## Manufacturing\n",
            )
            errors = validate_plugin_root(plugin_root)
        self.assertIn("erp-industry-variants: missing industry pattern Distribution", errors)

    def test_executive_skill_requires_fact_hypothesis_separation(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_skill(plugin_root, "erp-executive-transformation", "# Executive Outputs")
            errors = validate_plugin_root(plugin_root)
        self.assertIn(
            "erp-executive-transformation: missing fact/hypothesis separation", errors
        )

    def test_import_profile_requires_grain_and_business_key(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(plugin_root, "import-profile.md", "# Import Profile\n")
            errors = validate_plugin_root(plugin_root)
        self.assertIn("import-profile.md: missing grain rule", errors)
        self.assertIn("import-profile.md: missing business key rule", errors)

    def test_executive_pack_requires_statement_type_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(plugin_root, "executive-pack.md", "## Facts\n")
            errors = validate_plugin_root(plugin_root)
        self.assertIn(
            "executive-pack.md: missing heading Stakeholder observations", errors
        )

    def test_executive_pack_rejects_prose_and_inline_code_as_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(
                plugin_root,
                "executive-pack.md",
                "Required sections include `## Facts`, `## Stakeholder observations`, "
                "`## Hypotheses`, and `## Recommendations`.\n",
            )
            errors = validate_plugin_root(plugin_root)
        self.assertIn("executive-pack.md: missing heading Facts", errors)
        self.assertIn(
            "executive-pack.md: missing heading Stakeholder observations", errors
        )
        self.assertIn("executive-pack.md: missing heading Hypotheses", errors)
        self.assertIn("executive-pack.md: missing heading Recommendations", errors)

    def test_executive_pack_accepts_level_three_statement_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(
                plugin_root,
                "executive-pack.md",
                "### Facts\n### Stakeholder observations\n"
                "### Hypotheses\n### Recommendations\n",
            )
            self.assertEqual(validate_plugin_root(plugin_root), [])


if __name__ == "__main__":
    unittest.main()
