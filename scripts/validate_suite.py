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
    "erp-evidence-intake": ["stakeholder observation", "calculation assumption", "hypothesis"],
    "erp-governance-traceability": ["Validation Owner", "reversal condition"],
}


def validate_plugin_root(plugin_root: Path) -> list[str]:
    """Return structural errors for a plugin root; an empty list is valid."""
    errors = []
    for name in sorted(REQUIRED_SKILLS):
        skill_path = plugin_root / "skills" / name / "SKILL.md"
        if not skill_path.is_file():
            errors.append(f"missing skill: {name}")
            continue

        required_phrases = REQUIRED_PHRASES.get(name, [])
        if required_phrases:
            content = skill_path.read_text(encoding="utf-8")
            if not all(phrase in content for phrase in required_phrases):
                if name == "erp-evidence-intake":
                    errors.append(f"{name}: missing statement-type rule")
                else:
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
