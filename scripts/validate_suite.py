"""Structural validation for the ERP Process Transformation Suite."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_SKILLS = {
    "erp-transformation-orchestrator",
    "erp-evidence-intake",
    "erp-process-playbooks",
    "erp-scoring-benchmarking",
    "erp-executive-transformation",
    "erp-governance-traceability",
    "erp-industry-variants",
    "erp-transformation-innovation",
}

REQUIRED_PHRASES = {
    "erp-evidence-intake": [
        "stakeholder observation",
        "calculation assumption",
        "hypothesis",
        "Hypothesis / Gap Register",
        "not an Evidence ID",
    ],
    "erp-governance-traceability": ["Validation Owner", "reversal condition"],
}

PLAYBOOK_DOMAINS = (
    "O2C",
    "P2P",
    "R2R",
    "M2M",
    "Warehouse and Inventory",
    "Pricing",
    "Master Data",
)

SCORECARD_RULES = {
    "formula": "Formula",
    "coverage": "Coverage",
    "evidence-ID": "Evidence IDs",
    "assumptions": "Assumptions",
    "confidence": "Confidence",
}

INDUSTRY_PATTERNS = (
    "Manufacturing",
    "Distribution",
    "Retail",
    "Project Business",
    "Regulated Operations",
)

EXECUTIVE_STATEMENT_HEADINGS = (
    "Facts",
    "Stakeholder observations",
    "Hypotheses",
    "Recommendations",
)

EXECUTIVE_TEMPLATE = "executive-pack.md"
IMPORT_TEMPLATE = "import-profile.md"
INITIATIVE_TEMPLATE = "initiative-portfolio.md"
VALUE_TEMPLATE = "value-register.md"
OFFER_PACKAGES_TEMPLATE = "offer-packages.md"
INNOVATION_TEMPLATE = "innovation-opportunity-register.md"
INNOVATION_LENSES = (
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
    "Transformation Decision Compiler",
    "Process Friction-to-Policy Mapper",
    "ERP Change Blast-Radius Map",
    "Standard Capability Proof Pack",
    "Operational Resilience Score",
    "Exception Half-Life Tracker",
    "ERP Knowledge Concentration Risk",
    "Transformation Reuse Index",
    "Decision Latency Cost Model",
    "Process Exit Strategy",
)
INNOVATION_REQUIRED_FIELDS = (
    "Metric",
    "Kill Condition",
    "Owner",
    "Guardrails",
    "Next Validation",
)
INNOVATION_OPTIONAL_EVIDENCE_FIELDS = (
    "Blast Radius",
    "Knowledge Concentration",
    "Decision Latency",
    "Reuse Potential",
    "Exit Criterion",
)
INNOVATION_REGISTER_HEADER = (
    "Opportunity ID | Innovation Lens | Target Audience | Workflow Replaced | "
    "Differentiator | Evidence IDs | Assumptions | Metric | Kill Condition | "
    "Owner | Guardrails | Confidence | Blast Radius | Knowledge Concentration | "
    "Decision Latency | Reuse Potential | Exit Criterion | Next Validation | "
    "Decision Status"
)
MANIFEST_PATH = ".codex-plugin/plugin.json"
README_PATH = "README.md"
INNOVATION_README_HEADING = "Innovation Layer"
INNOVATION_STARTER_PROMPT_PHRASE = "innovation opportunit"
README_EXPANSION_LENSES = (
    "Transformation Decision Compiler",
    "Process Friction-to-Policy Mapper",
    "ERP Change Blast-Radius Map",
    "Standard Capability Proof Pack",
    "Operational Resilience Score",
    "Exception Half-Life Tracker",
    "ERP Knowledge Concentration Risk",
    "Transformation Reuse Index",
    "Decision Latency Cost Model",
    "Process Exit Strategy",
)
INITIATIVE_REQUIRED_COLUMNS = {
    "owner function": "owner function",
    "dependencies": "dependencies",
    "horizon": "horizon",
    "KPI": "kpi",
    "baseline": "baseline",
    "risk": "risk",
    "rollback or mitigation": "rollback or mitigation",
    "decision status": "decision status",
}
VALUE_FTE_FORMULA = (
    "annual transactions × minutes per transaction × automatable share / 60 / "
    "productive annual hours per FTE"
)
OFFER_SELECTION_RULES = {
    "Rapid Diagnostic": ("limited evidence", "one process", "0–90 days"),
    "Process Deep Dive": (
        "sufficient evidence",
        "root cause",
        "controls",
        "quantified opportunities",
    ),
    "Transformation Portfolio": (
        "multiple processes or entities",
        "initiative",
        "roadmap decisions",
    ),
    "Continuous Process Intelligence": (
        "recurring evidence refresh",
        "approved recurring KPI review",
        "no unattended monitoring claim",
    ),
}
FENCE_OPENING_PATTERN = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})[^\r\n]*$")


def has_executive_statement_heading(content: str, heading: str) -> bool:
    """Return whether an executive statement label is a level 2 or 3 heading."""
    content = without_fenced_code_blocks(content)
    pattern = rf"^#{{2,3}}[ \t]+{re.escape(heading)}[ \t]*(?:#+[ \t]*)?$"
    return re.search(pattern, content, flags=re.MULTILINE) is not None


def without_fenced_code_blocks(content: str) -> str:
    """Remove Markdown fenced blocks, respecting marker type and opening length."""
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    retained_lines = []
    marker_character = None
    marker_length = 0

    for line in content.splitlines(keepends=True):
        if marker_character is None:
            opening_match = FENCE_OPENING_PATTERN.match(line)
            if opening_match:
                marker = opening_match.group(1)
                marker_character = marker[0]
                marker_length = len(marker)
            else:
                retained_lines.append(line)
            continue

        closing_pattern = (
            rf"^[ \t]{{0,3}}{re.escape(marker_character)}{{{marker_length},}}[ \t]*"
            rf"(?:\r?\n)?$"
        )
        if re.match(closing_pattern, line):
            marker_character = None
            marker_length = 0

    return "".join(retained_lines)


def validate_plugin_root(plugin_root: Path) -> list[str]:
    """Return structural errors for a plugin root; an empty list is valid."""
    errors = []
    manifest_path = plugin_root / MANIFEST_PATH
    if not manifest_path.is_file():
        errors.append("manifest: missing plugin.json")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            errors.append("manifest: invalid JSON")
        else:
            if manifest.get("skills") != "./skills/":
                errors.append("manifest: missing skills path")
            prompts = manifest.get("interface", {}).get("defaultPrompt")
            if not isinstance(prompts, list) or not any(
                isinstance(prompt, str) and prompt.strip() for prompt in prompts
            ):
                errors.append("manifest: missing nonempty starter prompts")
            elif not any(
                INNOVATION_STARTER_PROMPT_PHRASE in prompt.lower()
                for prompt in prompts
                if isinstance(prompt, str)
            ):
                errors.append("manifest: missing innovation starter prompt")
            elif not any(
                "blast radius" in prompt.lower() and "exit strategy" in prompt.lower()
                for prompt in prompts
                if isinstance(prompt, str)
            ):
                errors.append(
                    "manifest: missing blast-radius and exit-strategy starter prompt"
                )

    readme_path = plugin_root / README_PATH
    if not readme_path.is_file():
        errors.append("README: missing Innovation Layer")
    else:
        readme = readme_path.read_text(encoding="utf-8")
        if INNOVATION_README_HEADING not in readme:
            errors.append("README: missing Innovation Layer")
        for lens in README_EXPANSION_LENSES:
            if lens not in readme:
                errors.append(f"README: missing innovation lens {lens}")
    for name in sorted(REQUIRED_SKILLS):
        skill_path = plugin_root / "skills" / name / "SKILL.md"
        if not skill_path.is_file():
            errors.append(f"missing skill: {name}")
            continue

        required_phrases = REQUIRED_PHRASES.get(name, [])
        if name == "erp-process-playbooks":
            content = skill_path.read_text(encoding="utf-8")
            for domain in PLAYBOOK_DOMAINS:
                if f"## {domain}" not in content:
                    errors.append(f"{name}: missing domain {domain}")
        if name == "erp-scoring-benchmarking":
            content = skill_path.read_text(encoding="utf-8")
            for rule, phrase in SCORECARD_RULES.items():
                if phrase not in content:
                    errors.append(f"{name}: missing {rule} rule")
        if name == "erp-industry-variants":
            content = skill_path.read_text(encoding="utf-8")
            if "Industry pattern guidance, not client fact" not in content:
                errors.append(f"{name}: missing industry guidance boundary")
            for pattern in INDUSTRY_PATTERNS:
                if f"## {pattern}" not in content:
                    errors.append(f"{name}: missing industry pattern {pattern}")
        if name == "erp-executive-transformation":
            content = skill_path.read_text(encoding="utf-8")
            if not all(heading in content for heading in EXECUTIVE_STATEMENT_HEADINGS):
                errors.append(f"{name}: missing fact/hypothesis separation")
        if name == "erp-transformation-innovation":
            content = skill_path.read_text(encoding="utf-8")
            for lens in INNOVATION_LENSES:
                if lens not in content:
                    errors.append(f"{name}: missing lens {lens}")
            for field in INNOVATION_REQUIRED_FIELDS:
                if field not in content:
                    errors.append(f"{name}: missing {field}")
        if required_phrases:
            content = skill_path.read_text(encoding="utf-8")
            if name == "erp-evidence-intake":
                statement_type_phrases = [
                    "stakeholder observation",
                    "calculation assumption",
                    "hypothesis",
                ]
                traceability_phrases = ["Hypothesis / Gap Register", "not an Evidence ID"]
                if not all(phrase in content for phrase in statement_type_phrases):
                    errors.append(f"{name}: missing statement-type rule")
                if not all(phrase in content for phrase in traceability_phrases):
                    errors.append(
                        f"{name}: missing unsupported-hypothesis traceability rule"
                    )
            elif not all(phrase in content for phrase in required_phrases):
                errors.append(f"{name}: missing governance traceability rule")

    import_profile_path = plugin_root / "references" / "templates" / IMPORT_TEMPLATE
    if not import_profile_path.is_file():
        errors.append(f"missing template: {IMPORT_TEMPLATE}")
    else:
        import_profile = import_profile_path.read_text(encoding="utf-8").lower()
        if "grain" not in import_profile:
            errors.append(f"{IMPORT_TEMPLATE}: missing grain rule")
        if "business key" not in import_profile:
            errors.append(f"{IMPORT_TEMPLATE}: missing business key rule")

    executive_pack_path = plugin_root / "references" / "templates" / EXECUTIVE_TEMPLATE
    if not executive_pack_path.is_file():
        errors.append(f"missing template: {EXECUTIVE_TEMPLATE}")
    else:
        executive_pack = executive_pack_path.read_text(encoding="utf-8")
        for heading in EXECUTIVE_STATEMENT_HEADINGS:
            if not has_executive_statement_heading(executive_pack, heading):
                errors.append(f"{EXECUTIVE_TEMPLATE}: missing heading {heading}")

    initiative_path = plugin_root / "references" / "templates" / INITIATIVE_TEMPLATE
    if not initiative_path.is_file():
        errors.append(f"missing template: {INITIATIVE_TEMPLATE}")
    else:
        initiative = initiative_path.read_text(encoding="utf-8").lower()
        for error_label, required_column in INITIATIVE_REQUIRED_COLUMNS.items():
            if required_column not in initiative:
                errors.append(f"initiative template: missing {error_label}")

    value_path = plugin_root / "references" / "templates" / VALUE_TEMPLATE
    if not value_path.is_file():
        errors.append(f"missing template: {VALUE_TEMPLATE}")
    else:
        value_register = value_path.read_text(encoding="utf-8").lower()
        if VALUE_FTE_FORMULA.lower() not in value_register:
            errors.append("value register: missing FTE capacity formula")
        if "assumption" not in value_register:
            errors.append("value register: missing assumptions rule")
        if "double-counting" not in value_register:
            errors.append("value register: missing double-counting review rule")

    offer_packages_path = plugin_root / "references" / "templates" / OFFER_PACKAGES_TEMPLATE
    if not offer_packages_path.is_file():
        errors.append(f"missing template: {OFFER_PACKAGES_TEMPLATE}")
    else:
        offer_packages = offer_packages_path.read_text(encoding="utf-8").lower()
        for package, phrases in OFFER_SELECTION_RULES.items():
            if package.lower() not in offer_packages or not all(
                phrase.lower() in offer_packages for phrase in phrases
            ):
                errors.append(f"offer packages: missing {package} selection rule")

    innovation_path = plugin_root / "references" / "templates" / INNOVATION_TEMPLATE
    if not innovation_path.is_file():
        errors.append(f"missing template: {INNOVATION_TEMPLATE}")
    else:
        innovation_register = innovation_path.read_text(encoding="utf-8")
        for field in INNOVATION_OPTIONAL_EVIDENCE_FIELDS:
            if field not in innovation_register:
                errors.append(f"innovation register: missing field {field}")
        if INNOVATION_REGISTER_HEADER not in innovation_register:
            errors.append("innovation register: missing exact header")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an ERP transformation plugin root.")
    parser.add_argument("plugin_root", type=Path)
    args = parser.parse_args()

    errors = validate_plugin_root(args.plugin_root)
    if errors:
        print("ERP transformation suite validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("ERP transformation suite validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
