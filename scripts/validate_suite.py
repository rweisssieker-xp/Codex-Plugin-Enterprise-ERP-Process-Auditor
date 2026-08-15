"""Structural validation for the ERP Process Transformation Suite."""

from __future__ import annotations

import argparse
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
FENCE_OPENING_PATTERN = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})[^\r\n]*$")


def has_executive_statement_heading(content: str, heading: str) -> bool:
    """Return whether an executive statement label is a level 2 or 3 heading."""
    content = without_fenced_code_blocks(content)
    pattern = rf"^#{{2,3}}[ \t]+{re.escape(heading)}[ \t]*(?:#+[ \t]*)?$"
    return re.search(pattern, content, flags=re.MULTILINE) is not None


def without_fenced_code_blocks(content: str) -> str:
    """Remove Markdown fenced blocks, respecting marker type and opening length."""
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
