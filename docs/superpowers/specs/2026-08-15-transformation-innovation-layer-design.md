# Transformation Innovation Layer — Design Specification

## Purpose

Add one central Codex-native Transformation Innovation Layer to the ERP Transformation Suite. It augments existing evidence, diagnostic, scoring, executive, and proof-of-value skills without replacing their contracts.

## Architecture

Create `skills/erp-transformation-innovation/SKILL.md` as the central orchestration layer. It consumes existing evidence, findings, scorecards, initiative portfolio, decision log, and value register. It emits an Innovation Opportunity Register. Every entry must contain the target audience, workflow replaced, differentiator, evidence basis, metric, kill condition, owner, next validation, guardrails, and confidence.

## Twelve innovation lenses

1. Transformation Evidence Graph
2. No-Regret Transformation Engine
3. Cross-ERP Process Semantic Layer
4. Process Variant Genome
5. Decision Decay Monitor
6. Transformation Memory
7. Change-Fatigue Forecast
8. Policy-to-Control Compiler
9. Value Leakage Escrow
10. Counterfactual Transformation Twin
11. Autonomy Ladder
12. Executive Attention Allocation

## Safety and evidence rules

- An innovation lens is a hypothesis unless backed by user-supplied evidence.
- No external benchmark, market fact, vendor capability, financial outcome, or ROI claim may be inferred.
- The layer must distinguish observed facts, stakeholder observations, assumptions, hypotheses, and approved decisions.
- High-impact proposals require a named validation owner and a reversible validation step.
- It may not authorize or execute changes in ERP systems.

## Outputs

Add `references/templates/innovation-opportunity-register.md` with columns: Opportunity ID, Innovation Lens, Target Audience, Workflow Replaced, Differentiator, Evidence IDs, Assumptions, Metric, Kill Condition, Owner, Guardrails, Confidence, Next Validation, Decision Status.

The Innovation Layer produces an executive innovation brief with: the three highest-priority opportunities, evidence and uncertainty, decision required, recommended experiment, and the explicit reason not to pursue lower-priority opportunities now.

## GitHub documentation

Update `README.md` with a dedicated Innovation Layer section, all twelve lenses, clear product boundaries, an architecture overview, five starter prompts, contribution/testing instructions, and a GitHub-friendly project structure section.

## Testing

Extend `scripts/validate_suite.py` and `tests/test_validate_suite.py` to require the Innovation Layer skill, the register header, mandatory evidence/metric/kill-condition/owner/guardrail wording, and all twelve lens names. Verify the plugin manifest and README reference the Innovation Layer.
