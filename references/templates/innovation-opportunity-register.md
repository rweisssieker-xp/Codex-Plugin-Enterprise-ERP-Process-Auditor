# Innovation Opportunity Register

Use one row for each evidence-bounded innovation hypothesis. Evidence IDs must refer to the supplied Evidence Register. Record unsupported inputs as `not supplied`; do not replace them with an inferred claim. A high-impact row requires a named Owner, a reversible Next Validation, and explicit Guardrails before any decision can be approved.

| Opportunity ID | Innovation Lens | Target Audience | Workflow Replaced | Differentiator | Evidence IDs | Assumptions | Metric | Kill Condition | Owner | Guardrails | Confidence | Blast Radius | Knowledge Concentration | Decision Latency | Reuse Potential | Exit Criterion | Next Validation | Decision Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | not supplied | not supplied | not supplied | not supplied | not supplied | | |

## Completion rules

- Treat every lens and differentiator as a hypothesis until user-supplied evidence supports it.
- State Metric units, measurement scope, period, and Evidence IDs when supplied; otherwise use `not supplied` and request the smallest needed evidence.
- Make Kill Condition observable and decision-relevant; it must say when the proposed validation stops or does not progress.
- Set Guardrails for protected controls, data, people, decision rights, and the non-execution boundary. This register does not authorize or execute ERP changes.
- Set Confidence from the supplied evidence coverage and assumptions; it is not an assurance of outcome.
- Record Blast Radius only from supplied process, interface, role, control, or data dependencies; do not infer a change impact.
- Record Knowledge Concentration, Decision Latency, and Reuse Potential only with supplied scope, period, measurement basis, and Evidence IDs; otherwise use `not supplied`.
- Record Exit Criterion as the evidence-backed condition that ends, pauses, reverses, or hands off a proposed validation; it does not authorize ERP or operational execution.
- Next Validation must be reversible and name the validation owner for high-impact proposals.
- Use only the Decision Log to label a row approved; otherwise use `hypothesis`, `validation proposed`, or `not supplied`.
