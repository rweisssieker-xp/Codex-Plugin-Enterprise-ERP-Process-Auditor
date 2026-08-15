---
name: erp-governance-traceability
description: Apply evidence, approval, privacy, conflict-resolution, and reversal controls to ERP transformation decisions.
---

# ERP Governance and Traceability

Use this skill after evidence intake and before presenting decision-grade findings, scores, recommendations, or value scenarios. It creates a reviewable chain from a material statement to its evidence, accountable reviewer, decision, and potential reversal.

## Governance boundary

- Use only user-supplied task context and accessible files. Do not access ERP systems, external APIs, external benchmarks, or other data sources.
- Apply confidential-data minimization: retain source identifiers, necessary metadata, and the minimum relevant content. Avoid reproducing personal, customer, financial, or other confidential data in outputs unless necessary for the approved task purpose.
- Respect every source's Sensitivity and Use Limit. If intended use exceeds the limit, stop and request human direction.
- This skill provides no legal, tax, audit, security, or compliance assurance. Recommend validation by the appropriate accountable internal function where such questions arise.

## Traceability rules

1. For every material finding, calculation, recommendation, or decision, capture Evidence IDs, statement type, confidence, scope/period, owner, validation status, and change rationale.
2. Keep facts, stakeholder observations, calculation assumptions, and hypotheses distinct. A stakeholder observation or hypothesis does not become a fact merely because it supports a preferred outcome.
3. When sources conflict, retain all conflicting Evidence IDs, describe the precise conflict without choosing a winner, lower confidence as appropriate, and create an Evidence Gap Register request for accountable resolution.
4. Do not issue a decision-grade conclusion when evidence gaps or conflicts materially affect it; mark it provisional and state what validation is required.

## Human approval gate

High-impact recommendations require a named Validation Owner, evidence review, and explicit human approval before they are treated as approved actions. Record the proposed action, evidence, approver, status, and Validation Owner in the Decision Log. Do not imply automated approval, implementation authority, or assurance.

## Material decision controls

For each material decision, use the shared **Decision Log** columns. The decision must include a testable reversal condition: the event, threshold, evidence, or failed validation that triggers reconsideration, rollback, or escalation. A reversal condition is not optional for a material decision.

| Decision ID | Decision | Rationale | Evidence IDs | Owner | Approver | Status | Date | Reversal Condition |
|---|---|---|---|---|---|---|---|---|
| D-001 | [decision] | [traceable rationale] | [E-IDs] | [accountable owner] | [human approver] | proposed / approved / rejected / reversed | [date] | [testable condition] |

## Review output

Return the Decision Log, unresolved conflicts, Evidence Gap Register items, and an approval-status summary. For a high-impact recommendation, state the named Validation Owner, whether human approval has occurred, and the reversal condition. If any of those are absent, state that the recommendation is not approved.

## Value and assurance limits

Do not claim legal, tax, compliance, audit, security, savings, or FTE assurance. FTE or financial value can be presented only as a transparent scenario with formula, evidence IDs, assumptions, coverage, confidence, and double-counting risks; otherwise defer it pending evidence and human validation.
