---
name: erp-transformation-orchestrator
description: Coordinate evidence-backed ERP process transformation engagements from scope through decision outputs, without external connections or unsupported conclusions.
---

# ERP Transformation Orchestrator

Use this skill for a complete ERP transformation engagement spanning diagnosis, prioritization, and executive decisions. It consumes the scoped process/domain plus the Evidence Register and Evidence Gap Register. It produces a current-state process map, Finding Register, governed decision outputs, and a proof-of-value plan. For a focused, rapid diagnostic, use `erp-process-audit` instead.

## Operating boundary

- Work only from user-supplied task context and accessible files in Codex. Do not connect to ERP systems, external APIs, services, or data stores.
- Do not invent external benchmarks. Benchmark only comparable internal populations with user-supplied definitions and evidence.
- Keep facts, stakeholder observations, calculation assumptions, and hypotheses distinct. An unsupported hypothesis belongs in the Hypothesis / Gap Register, not the Evidence Register.
- Do not provide legal, tax, compliance, audit, security, or savings assurance. Route such decisions to an accountable human owner.
- Present FTE, financial, cash, or value results only as transparent scenarios with formula, input evidence IDs, assumptions, coverage, confidence, and double-counting risks. Withhold a decision-grade value figure when those inputs are not available.

## Mandatory engagement sequence

Execute these stages in exactly this order. Do not skip the evidence-gap gate or move benchmarking before comparability has been established.

1. **Scope** — confirm process/domain, entities, period, objective, decision audience, operating constraints, and supplied sources. Record unresolved scope as an Evidence Gap.
2. **Evidence intake** — run `erp-evidence-intake` to create or update the Evidence Register, Evidence Gap Register, and (where needed) Hypothesis / Gap Register.
3. **Governance** — run `erp-governance-traceability` to apply sensitivity/use limits, conflict handling, named Validation Owners, human approval gates, and reversal conditions.
4. **Playbook** — run `erp-process-playbooks` for each scoped domain. Produce the current-state process map, candidate finding records, and unanswered diagnostic questions.
5. **Evidence-gap check** — test every candidate finding against its Evidence IDs, scope, and confidence. Convert unsupported candidates to hypotheses and request the minimum missing evidence. If material gaps remain, return a diagnostic plan and evidence requests rather than false precision.
6. **Scoring** — send validated findings and declared assumptions to `erp-scoring-benchmarking`. Mark scores provisional when evidence coverage is insufficient.
7. **Benchmarking when comparable** — use `erp-scoring-benchmarking` only when user-supplied populations have matching definitions, period, scope, and measurement basis. Otherwise record the comparability limit and do not rank entities or imply an external benchmark.
8. **Initiatives** — convert validated findings and value hypotheses into `erp-initiative-portfolio` cards, with accountable owner, dependencies, KPI/baseline, risk/mitigation, and required decision.
9. **Executive output** — use `erp-executive-transformation` to compose an evidence-linked executive summary, Finding Register, target operating model, roadmap, decisions required, and open evidence requests.
10. **Proof of value** — use `erp-proof-of-value` to define baseline, target, formula, evidence, review owner, cadence, confidence, and variance explanation. These are realization measures, not promised savings.

## Gates and outputs

At the end of each stage, retain the named artifact and record its limitations. A material recommendation may move to an executive output only when its evidence and Validation Owner are visible; otherwise label it provisional.

| Gate | Required artifact | Continue only when | If not met |
|---|---|---|---|
| Scope | scoped engagement statement | domain, entity, period, and decision are sufficiently clear | request scope clarification |
| Evidence | Evidence Register and Evidence Gap Register | evidence is classified and permitted for use | limit conclusions and request evidence |
| Diagnosis | current-state process map and Finding Register | candidate findings cite evidence or are hypotheses | create Gap IDs / Hypothesis IDs |
| Quantification | scorecard and, where relevant, value scenario | formula, inputs, coverage, and confidence are shown | mark provisional or withhold result |
| Decision | initiative cards and Decision Log | owner, approval status, and reversal condition are explicit | do not call the action approved |

## Insufficient-evidence response

When evidence cannot substantiate a process map or finding, deliver: (1) the scoped diagnostic plan, (2) an Evidence Gap Register with the minimum source request, (3) unanswered playbook questions, and (4) hypotheses clearly labelled as unvalidated. Never convert missing close calendars, reconciliations, system extracts, or stakeholder accounts into implied process failures.
