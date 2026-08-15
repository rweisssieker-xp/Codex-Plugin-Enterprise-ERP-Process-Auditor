# ERP Process Transformation Suite

An evidence-backed, vendor-neutral suite for assessing ERP process transformation. It helps CIO and COO teams turn supplied operating evidence into traceable findings, internal comparisons, initiative options, and proof-of-value reviews. It supports SAP, Microsoft Dynamics 365, Oracle, NetSuite, Infor, AX, and Business Central as context; no product is treated as the target operating model.

## What the suite does

- Takes in and classifies process evidence, assumptions, stakeholder observations, and hypotheses.
- Maps O2C, P2P, R2R, M2M, warehouse and inventory, pricing, and master-data workflows.
- Identifies standardization, configuration, control, data, integration, and shadow-process opportunities.
- Produces transparent scorecards, comparable **internal** benchmarks, an initiative portfolio, executive materials, and proof-of-value scenarios.

## What it does not do

The suite does not invent client facts, promise savings, make legal/tax/audit/compliance assurances, provide an external market benchmark, or perform unattended monitoring. It distinguishes evidence-backed facts from stakeholder observations, hypotheses, and calculations. A named human owner must validate material recommendations and decisions.

## Module sequence

1. `erp-evidence-intake` establishes scope, provenance, evidence quality, and gaps.
2. `erp-governance-traceability` records decisions, validation ownership, and reversal conditions.
3. `erp-process-playbooks` reconstructs the selected process domain.
4. `erp-scoring-benchmarking` creates evidence-backed scorecards and comparable internal cohorts.
5. `erp-industry-variants` applies bounded industry-pattern guidance.
6. `erp-executive-transformation` assembles decision-ready outputs and value scenarios.
7. `erp-transformation-orchestrator` runs the complete engagement; `erp-process-audit` is the bounded rapid-diagnostic entry point.

## Accepted evidence

Use supplied SOPs, process maps, screenshots, ERP reports and exports, spreadsheets, ticket data, interface inventories, role designs, sample transactions, interview notes, and approved KPI extracts. Capture the source, date, owner, scope, grain, business key, and limitations for every material item. Treat interview claims as stakeholder observations until corroborated.

## Artifact catalogue

The templates in `references/templates/` provide an evidence register, finding register, process map, scorecard, benchmark comparison, complexity balance sheet, initiative portfolio, value register, executive pack, offer packages, import profile, and decision log.

## Data and privacy limits

Share only the minimum necessary business evidence. Remove or mask personal data, credentials, payment information, secrets, and unnecessary customer or employee identifiers before use. Keep outputs within the approved workspace and follow the organisation's retention, access-control, and data-residency requirements. Escalate security, privacy, legal, tax, and compliance questions to the appropriate human specialists.

## Validation and release

Run from the plugin root:

```powershell
python -m unittest tests/test_validate_suite.py -v
python scripts/validate_suite.py .
python C:\Users\reinerw\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\reinerw\plugins\erp-process-transformation-agent
python C:\Users\reinerw\.codex\skills\.system\plugin-creator\scripts\update_plugin_cachebuster.py C:\Users\reinerw\plugins\erp-process-transformation-agent
```

Before release, smoke-test the starter prompts below in a new task and record any failures in `references/templates/decision-log.md`.

## Starter prompts

1. “Run a rapid O2C diagnostic using these SOPs and invoice-rework examples; separate facts from hypotheses and list the minimum missing evidence.”
2. “Set up a P2P evidence intake for these interviews, purchase-order reports, and supplier-master extracts, including provenance and data-quality gaps.”
3. “Assess this R2R material for insufficient evidence. Do not score it; explain the evidence gaps, validation owners, and reversal conditions.”
4. “Create a comparable internal benchmark for O2C across these entities using only the supplied evidence, cohort rules, coverage, and confidence.”
5. “Build an O2C initiative and value scenario from these findings, stating assumptions, dependencies, double-counting checks, risks, and decisions required.”
