"""Structural validation for the ERP Process Transformation Suite."""

from __future__ import annotations

import argparse
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
