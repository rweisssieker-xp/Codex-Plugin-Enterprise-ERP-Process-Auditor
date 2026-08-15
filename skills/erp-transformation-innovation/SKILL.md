---
name: erp-transformation-innovation
description: Turn user-supplied ERP transformation evidence into bounded innovation hypotheses, validation experiments, and an executive innovation brief.
---

# ERP transformation innovation layer

Use this skill after evidence intake, findings, and scoring are available. It consumes the Evidence Register, Finding Register, Scorecard, Initiative Portfolio, Decision Log, and Value Register. It produces an Innovation Opportunity Register and an executive innovation brief; it does not replace the contracts of those inputs.

## Evidence and safety boundary

Use only user-supplied evidence. Classify every statement as an observed fact, stakeholder observation, assumption, hypothesis, or approved decision. An innovation lens is a hypothesis unless user-supplied evidence supports it. Do not infer or claim external benchmarks, market facts, vendor capabilities, financial outcomes, ROI, or other results absent supplied evidence.

Rank opportunities evidence-first: prefer direct Evidence IDs, clear scope and period, stated denominator or population, and fewer material assumptions. Lower confidence or unresolved conflict lowers priority; it does not justify a claim.

This layer may frame reversible validation experiments and decision inputs only. It does not authorize, configure, deploy, or execute changes in ERP systems, connected systems, or business operations. Every high-impact proposal requires a named validation owner, stated evidence, Metric, Kill Condition, Guardrails, Confidence, and a reversible Next Validation before any approved decision.

## Innovation lenses

Treat each lens below as a hypothesis-generation prompt, never as a factual capability or outcome.

1. **Transformation Evidence Graph** — test whether supplied Evidence IDs and their relationships make a decision path more traceable.
2. **No-Regret Transformation Engine** — test whether the supplied evidence identifies a reversible action with bounded downside.
3. **Cross-ERP Process Semantic Layer** — test whether user-supplied process terms can be consistently mapped across stated ERP contexts.
4. **Process Variant Genome** — test whether supplied process maps and findings describe meaningful variants that warrant validation.
5. **Decision Decay Monitor** — test whether a recorded decision has an evidenced expiry, changed assumption, or review trigger.
6. **Transformation Memory** — test whether decision-log and evidence history can reduce repeated unanswered questions within the supplied scope.
7. **Change-Fatigue Forecast** — test whether user-supplied change signals indicate a need to stage or defer an experiment.
8. **Policy-to-Control Compiler** — test whether a supplied policy can be translated into a proposed, reviewable control statement.
9. **Value Leakage Escrow** — test whether the Value Register and findings identify an unvalidated loss mechanism requiring measurement.
10. **Counterfactual Transformation Twin** — test a stated comparison between the current evidence-backed workflow and a bounded alternative scenario.
11. **Autonomy Ladder** — test which decision or activity remains human-approved at each proposed level of assistance.
12. **Executive Attention Allocation** — test whether evidence strength, impact, uncertainty, and decision timing warrant executive attention now.

## Opportunity register

Use `references/templates/innovation-opportunity-register.md`. Create an entry only when its evidence basis, assumptions, and uncertainty can be recorded. Use `not supplied` for unavailable information and request the smallest missing input; do not manufacture a value.

For each opportunity, record the target audience and the workflow replaced as a proposed scope, the differentiator as a hypothesis, direct Evidence IDs, Assumptions, Metric, Kill Condition, Owner, Guardrails, Confidence, reversible Next Validation, and Decision Status. A Kill Condition must state what result, threshold, or evidence gap stops the experiment. Guardrails must state the protected boundary, including that execution remains outside this skill.

Do not elevate a hypothesis to an approved decision. Only the supplied Decision Log may establish an approved decision; otherwise set Decision Status to `hypothesis`, `validation proposed`, or `not supplied`, as applicable.

## Executive innovation brief

Prepare a concise executive innovation brief that contains:

- The three highest-priority opportunities, with Innovation Lens, intended decision, owner, and decision status.
- Evidence and uncertainty for each: Evidence IDs, material assumptions, confidence, and conflicts or gaps.
- The decision required and the named approval or validation owner.
- The recommended reversible experiment, its Metric, Kill Condition, Guardrails, and Next Validation.
- The explicit reason lower-priority opportunities are not pursued now, such as missing evidence, weak confidence, unresolved risk, unavailable owner, or a higher-priority decision dependency.

State that the brief is evidence-bounded and non-executing. Withhold rankings that would imply a financial outcome, implementation feasibility, vendor capability, or external comparison without user-supplied evidence.
