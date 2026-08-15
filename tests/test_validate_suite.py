import sys
import tempfile
import unittest
import json
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from validate_suite import (
    REQUIRED_SKILLS,
    has_executive_statement_heading,
    validate_plugin_root,
)


EXPECTED_INNOVATION_LENSES = (
    "Transformation Evidence Graph",
    "No-Regret Transformation Engine",
    "Cross-ERP Process Semantic Layer",
    "Process Variant Genome",
    "Decision Decay Monitor",
    "Transformation Memory",
    "Change-Fatigue Forecast",
    "Policy-to-Control Compiler",
    "Value Leakage Escrow",
    "Counterfactual Transformation Twin",
    "Autonomy Ladder",
    "Executive Attention Allocation",
)
EXPECTED_INNOVATION_REQUIRED_FIELDS = (
    "Metric",
    "Kill Condition",
    "Owner",
    "Guardrails",
    "Next Validation",
)
EXPECTED_INNOVATION_REGISTER_HEADER = (
    "Opportunity ID | Innovation Lens | Target Audience | Workflow Replaced | "
    "Differentiator | Evidence IDs | Assumptions | Metric | Kill Condition | "
    "Owner | Guardrails | Confidence | Next Validation | Decision Status"
)


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
    write_skill(
        plugin_root,
        "erp-transformation-innovation",
        "\n".join(
            (*EXPECTED_INNOVATION_LENSES, *EXPECTED_INNOVATION_REQUIRED_FIELDS)
        ),
    )
    write_template(plugin_root, "import-profile.md", "grain | business key\n")
    write_template(
        plugin_root,
        "executive-pack.md",
        "## Facts\n## Stakeholder observations\n## Hypotheses\n## Recommendations\n",
    )
    write_template(
        plugin_root,
        "initiative-portfolio.md",
        "Initiative ID | Outcome | Source Findings | Owner Function | Dependencies | "
        "Horizon | KPI | Baseline | Risk | Rollback or Mitigation | Decision Status\n",
    )
    write_template(
        plugin_root,
        "value-register.md",
        "Formula: annual transactions × minutes per transaction × automatable share "
        "/ 60 / productive annual hours per FTE\nAssumptions\nDouble-counting review\n",
    )
    write_template(
        plugin_root,
        "offer-packages.md",
        "Rapid Diagnostic: limited evidence; one process; 0–90 days\n"
        "Process Deep Dive: sufficient evidence; root cause; controls; "
        "quantified opportunities\n"
        "Transformation Portfolio: multiple processes or entities; initiative; "
        "roadmap decisions\n"
        "Continuous Process Intelligence: recurring evidence refresh; approved "
        "recurring KPI review; no unattended monitoring claim\n",
    )
    write_template(
        plugin_root,
        "innovation-opportunity-register.md",
        EXPECTED_INNOVATION_REGISTER_HEADER,
    )
    write_manifest(plugin_root)


def write_manifest(plugin_root: Path, manifest: dict | None = None) -> None:
    content = {
        "name": "erp-process-transformation-agent",
        "skills": "./skills/",
        "interface": {"defaultPrompt": ["Run an evidence-backed ERP process review."]},
    }
    if manifest is not None:
        content = manifest
    manifest_path = plugin_root / ".codex-plugin" / "plugin.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(content), encoding="utf-8")


def write_skill(plugin_root: Path, name: str, content: str) -> None:
    skill_path = plugin_root / "skills" / name / "SKILL.md"
    skill_path.parent.mkdir(parents=True, exist_ok=True)
    skill_path.write_text(content, encoding="utf-8")


def write_template(plugin_root: Path, name: str, content: str) -> None:
    template_path = plugin_root / "references" / "templates" / name
    template_path.parent.mkdir(parents=True, exist_ok=True)
    template_path.write_text(content, encoding="utf-8")


class ValidateSuiteTests(unittest.TestCase):
    def test_manifest_declares_skills_and_nonempty_prompts(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_manifest(plugin_root, {"name": "erp-process-transformation-agent"})
            self.assertIn("manifest: missing skills path", validate_plugin_root(plugin_root))

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

    def test_executive_pack_rejects_prose_and_code_as_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(
                plugin_root,
                "executive-pack.md",
                "Required sections include `## Facts`, `## Stakeholder observations`, "
                "`## Hypotheses`, and `## Recommendations`.\n\n"
                "```markdown\n## Facts\n## Stakeholder observations\n"
                "## Hypotheses\n## Recommendations\n```\n",
            )
            errors = validate_plugin_root(plugin_root)
        self.assertIn("executive-pack.md: missing heading Facts", errors)
        self.assertIn(
            "executive-pack.md: missing heading Stakeholder observations", errors
        )
        self.assertIn("executive-pack.md: missing heading Hypotheses", errors)
        self.assertIn("executive-pack.md: missing heading Recommendations", errors)

    def test_executive_pack_rejects_tilde_fence_as_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(
                plugin_root,
                "executive-pack.md",
                "~~~~markdown\n## Facts\n## Stakeholder observations\n"
                "## Hypotheses\n## Recommendations\n~~~~\n",
            )
            errors = validate_plugin_root(plugin_root)
        self.assertIn("executive-pack.md: missing heading Facts", errors)

    def test_executive_pack_rejects_four_backtick_fence_as_headings(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(
                plugin_root,
                "executive-pack.md",
                "````markdown\n## Facts\n## Stakeholder observations\n"
                "## Hypotheses\n## Recommendations\n````\n",
            )
            errors = validate_plugin_root(plugin_root)
        self.assertIn("executive-pack.md: missing heading Facts", errors)

    def test_executive_pack_rejects_crlf_tilde_fence_as_headings(self):
        content = (
            "~~~~markdown\r\n## Facts\n## Stakeholder observations\n"
            "## Hypotheses\n## Recommendations\n~~~~\n"
        )
        self.assertFalse(has_executive_statement_heading(content, "Facts"))
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(
                plugin_root,
                "executive-pack.md",
                content,
            )
            errors = validate_plugin_root(plugin_root)
        self.assertIn("executive-pack.md: missing heading Facts", errors)

    def test_executive_pack_rejects_crlf_four_backtick_fence_as_headings(self):
        content = (
            "````markdown\r\n## Facts\n## Stakeholder observations\n"
            "## Hypotheses\n## Recommendations\n````\n"
        )
        self.assertFalse(has_executive_statement_heading(content, "Facts"))
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(
                plugin_root,
                "executive-pack.md",
                content,
            )
            errors = validate_plugin_root(plugin_root)
        self.assertIn("executive-pack.md: missing heading Facts", errors)

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

    def test_initiative_requires_owner_dependency_kpi_and_rollback(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(plugin_root, "initiative-portfolio.md", "Initiative ID | Outcome")
            errors = validate_plugin_root(plugin_root)
        self.assertIn("initiative template: missing owner function", errors)
        self.assertIn("initiative template: missing dependencies", errors)
        self.assertIn("initiative template: missing KPI", errors)
        self.assertIn("initiative template: missing rollback or mitigation", errors)

    def test_value_register_requires_formula_assumption_and_double_counting_review(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(plugin_root, "value-register.md", "Value ID | Initiative ID")
            errors = validate_plugin_root(plugin_root)
        self.assertIn("value register: missing FTE capacity formula", errors)
        self.assertIn("value register: missing assumptions rule", errors)
        self.assertIn("value register: missing double-counting review rule", errors)

    def test_offer_packages_require_selection_rules_and_monitoring_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            write_template(plugin_root, "offer-packages.md", "# Offer packages\n")
            errors = validate_plugin_root(plugin_root)
        self.assertIn("offer packages: missing Rapid Diagnostic selection rule", errors)
        self.assertIn(
            "offer packages: missing Continuous Process Intelligence selection rule",
            errors,
        )

    def test_innovation_layer_requires_each_lens(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            for missing_lens in EXPECTED_INNOVATION_LENSES:
                with self.subTest(missing_lens=missing_lens):
                    create_minimum_suite(plugin_root)
                    write_skill(
                        plugin_root,
                        "erp-transformation-innovation",
                        "\n".join(
                            lens
                            for lens in EXPECTED_INNOVATION_LENSES
                            if lens != missing_lens
                        ),
                    )
                    errors = validate_plugin_root(plugin_root)
                    self.assertIn(
                        f"erp-transformation-innovation: missing lens {missing_lens}",
                        errors,
                    )

    def test_innovation_layer_requires_each_safety_field(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            for missing_field in EXPECTED_INNOVATION_REQUIRED_FIELDS:
                with self.subTest(missing_field=missing_field):
                    create_minimum_suite(plugin_root)
                    write_skill(
                        plugin_root,
                        "erp-transformation-innovation",
                        "\n".join(
                            (*EXPECTED_INNOVATION_LENSES,)
                            + tuple(
                                field
                                for field in EXPECTED_INNOVATION_REQUIRED_FIELDS
                                if field != missing_field
                            )
                        ),
                    )
                    errors = validate_plugin_root(plugin_root)
                    self.assertIn(
                        f"erp-transformation-innovation: missing {missing_field}",
                        errors,
                    )

    def test_innovation_register_rejects_exact_header_mutation(self):
        with tempfile.TemporaryDirectory() as directory:
            plugin_root = Path(directory)
            create_minimum_suite(plugin_root)
            mutated_header = EXPECTED_INNOVATION_REGISTER_HEADER.replace(
                "Workflow Replaced", "Workflow Replacement"
            )
            write_template(plugin_root, "innovation-opportunity-register.md", mutated_header)
            errors = validate_plugin_root(plugin_root)
        self.assertIn("innovation register: missing exact header", errors)


if __name__ == "__main__":
    unittest.main()
