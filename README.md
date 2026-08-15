# ERP Process Transformation Suite

An evidence-backed, vendor-neutral ERP transformation suite for CIO and COO teams. It turns supplied operating evidence into traceable process findings, bounded innovation opportunities, comparable internal benchmarks, and decision-ready portfolios. SAP, Microsoft Dynamics 365, Oracle, NetSuite, Infor, AX, and Business Central are supported as context; none is prescribed as the target operating model.

## Product positioning

Use the suite to assess O2C, P2P, R2R, M2M, warehouse and inventory, pricing, and master-data workflows. It distinguishes facts, stakeholder observations, hypotheses, and calculation assumptions, then carries evidence, ownership, and reversal conditions through to a decision. It does not invent client facts, promise savings, make legal, tax, audit, or compliance assurances, provide external market benchmarks, or perform unattended monitoring.

## Architecture and module overview

1. `erp-evidence-intake` establishes evidence scope, provenance, quality, and gaps.
2. `erp-governance-traceability` records decisions, validation owners, and reversal conditions.
3. `erp-process-playbooks` reconstructs the selected process domain.
4. `erp-scoring-benchmarking` produces evidence-backed scorecards and internal cohorts.
5. `erp-industry-variants` applies bounded industry-pattern guidance.
6. `erp-executive-transformation` assembles decision-ready outputs and value scenarios.
7. `erp-transformation-innovation` identifies and governs evidence-backed innovation opportunities.
8. `erp-transformation-orchestrator` runs the engagement; `erp-process-audit` is the bounded rapid-diagnostic entry point.

## Innovation Layer

The Innovation Layer uses twenty-two lenses to turn validated process friction into testable opportunities. Every opportunity must record evidence IDs, assumptions, metric, owner, guardrails, kill condition, confidence, and next validation in the innovation opportunity register. Blast Radius, Knowledge Concentration, Decision Latency, Reuse Potential, and Exit Criterion are optional fields: record them only when user-supplied evidence supports them, otherwise use `not supplied`.

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
13. Transformation Decision Compiler
14. Process Friction-to-Policy Mapper
15. ERP Change Blast-Radius Map
16. Standard Capability Proof Pack
17. Operational Resilience Score
18. Exception Half-Life Tracker
19. ERP Knowledge Concentration Risk
20. Transformation Reuse Index
21. Decision Latency Cost Model
22. Process Exit Strategy

These are evaluation lenses, not claims about a client’s current state or promises of autonomous execution. Human owners approve material actions; guardrails and kill conditions define when to stop, reverse, or escalate.

## Inputs and evidence boundaries

Use supplied SOPs, process maps, screenshots, ERP reports and exports, spreadsheets, ticket data, interface inventories, role designs, sample transactions, interview notes, and approved KPI extracts. For every material item, capture source, date, owner, scope, grain, business key, and limitations. Treat interview claims as stakeholder observations until corroborated.

Share only the minimum necessary business evidence. Remove or mask personal data, credentials, payment information, secrets, and unnecessary customer or employee identifiers. Keep outputs in the approved workspace and follow the organisation’s retention, access-control, and data-residency requirements. Escalate security, privacy, legal, tax, and compliance questions to human specialists.

## Starter prompts

1. “Identify evidence-backed innovation opportunities from these O2C SOPs and invoice-rework examples; state the lens, metric, guardrails, owner, kill condition, and next validation.”
2. “Run a rapid O2C diagnostic using these SOPs and invoice-rework examples; separate facts from hypotheses and list the minimum missing evidence.”
3. “Set up a P2P evidence intake for these interviews, purchase-order reports, and supplier-master extracts, including provenance and data-quality gaps.”
4. “Create a comparable internal benchmark for O2C across these entities using only the supplied evidence, cohort rules, coverage, and confidence.”
5. “Turn these validated findings and innovation opportunities into an initiative portfolio with owners, dependencies, risks, KPIs, guardrails, and decision status.”
6. “Map the evidence-backed blast radius of this proposed ERP process change and define an exit strategy, including supplied dependencies, guardrails, owner, validation, and exit criterion.”

## Install and test

Install the plugin from this repository into a Codex plugin directory, then start a new task and use a starter prompt with approved, minimised evidence. From the plugin root, run:

```powershell
python -m unittest tests/test_validate_suite.py -v
python scripts/validate_suite.py .
python C:\Users\reinerw\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\reinerw\plugins\erp-process-transformation-agent
```

Before release, smoke-test the five prompts in a new task and record failures in `references/templates/decision-log.md`.

## GitHub project structure

```text
.codex-plugin/plugin.json     Plugin metadata and discoverable prompts
skills/                       Operating instructions for each module
references/templates/         Evidence, decision, portfolio, and innovation artifacts
scripts/validate_suite.py     Structural release validator
tests/                        Validator regression tests
docs/                         Product and delivery documentation
```

## Contributing

Keep contributions evidence-bound and vendor-neutral. Add or update tests for every validator rule, preserve fact/hypothesis separation, and document any new artifact field, owner, guardrail, and reversal condition. Do not add claims that imply guaranteed savings, compliance, unattended monitoring, or autonomous production changes. Open a focused pull request with the validation commands above passing.
