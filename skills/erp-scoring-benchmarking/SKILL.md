---
name: erp-scoring-benchmarking
description: Create transparent ERP process scorecards and comparable internal benchmark comparisons using only user-supplied evidence.
---

# ERP scoring and internal benchmarking

Use this skill after a validated Finding Register and before prioritizing initiatives. Consume only user-supplied findings, their Evidence IDs, and user-supplied comparable-entity data. Do not access ERP systems, external APIs, external benchmarks, or other data sources. Do not infer a denominator, evidence coverage, population, period, or process scope that the supplied material does not establish.

## Scorecard

Create one row per metric using `references/templates/scorecard.md`. Each score is a 0–100 diagnostic indicator, not a performance assurance or an external benchmark. Record the Formula, stated denominator, contributing finding IDs, Evidence IDs, Coverage, Assumptions, and Confidence for every result.

For each included finding *i*, set: severity weight `S_i` (1 low, 2 medium, 3 high, 4 critical); affected-population weight `P_i` (affected units / stated denominator, capped at 1); and evidence-confidence weight `E_i` (1 high, 0.6 medium, 0.3 low). The weighted count is `W = sum(S_i × P_i × E_i)`. State the finding inclusion rule and denominator beside the calculation. Never substitute a guessed population or a count of records for a process population.

Use `min(100, 25 × W)` for risk/opportunity scores. For process maturity, use `max(0, 100 − 25 × W)` after defining which maturity-gap findings were included. These common weights are calculation assumptions, not validated industry norms; a requester may replace them only when the revised weights and rationale are recorded.

| Metric | Finding inclusion rule | Formula | Interpretation |
|---|---|---|---|
| Process maturity | Findings that evidence an absent, inconsistently performed, or unowned process practice | `max(0, 100 − 25 × W)` | Higher is more mature within the stated scope. |
| Friction | Findings that evidence delay, rework, handoff failure, or manual touch | `min(100, 25 × W)` | Higher indicates more evidenced process friction. |
| Automation readiness | Findings that evidence stable, repeatable, rule-based work with a defined input and outcome | `min(100, 25 × W)` | Higher indicates more evidenced candidate readiness, not implementation feasibility. |
| Standardization potential | Findings that evidence unexplained variation across included entities or teams | `min(100, 25 × W)` | Higher indicates more evidenced potential to test harmonization. |
| Data-quality risk | Findings that evidence incomplete, duplicate, inaccurate, untimely, or uncontrolled data | `min(100, 25 × W)` | Higher indicates more evidenced data-quality risk. |
| Control risk | Findings that evidence a missing, bypassed, ineffective, or unverified control | `min(100, 25 × W)` | Higher indicates more evidenced control risk; it is not a compliance assurance. |

### Coverage and confidence rules

Coverage is `included population / stated denominator`, shown as a fraction and percentage. Evidence coverage is `findings with direct Evidence IDs / findings included in the score`. Confidence is high only when the denominator, process scope, period, affected population, and direct Evidence IDs are present with no material unresolved conflict; otherwise use medium or low and explain why.

Label a score **Provisional** when either the denominator or evidence coverage is missing, partial, or cannot be calculated. Also label it provisional when material evidence conflicts or key findings are only stakeholder observations. Do not produce a decision-grade ranking from a provisional score; list the smallest requested evidence needed to recalculate it. Hypothesis IDs and Gap IDs are not Evidence IDs and cannot contribute to `W`.

### FTE and value boundaries

Scores do not establish savings, FTE release, cash benefit, or financial value. If a requester asks for such a scenario, state a Formula, input Evidence IDs, Assumptions, Coverage, Confidence, realization conditions, and double-counting risk separately. For example, a theoretical capacity scenario may be `avoided touches × evidenced minutes per touch / 60 / stated annual productive hours`; it is not an FTE commitment or assurance. Withhold a total when overlapping initiatives could count the same work or when inputs are absent.

## Internal benchmark gate

Use `references/templates/benchmark-comparison.md`. Compare entities only when the metric definition, period, population, process scope, and data grain are the same. Otherwise provide a comparability-gap table and do not rank entities.

The only permitted comparison population is the user-supplied internal population. Before accepting a comparison, record each entity's metric definition, time period, population and denominator, process scope, data grain, source Evidence IDs, and exclusions. A same-month comparison of two plants with the same metric definition, population, process scope, and grain may be accepted with stated coverage and limitations. A monthly plant result and a quarterly country total are incomparable: complete the gap table, request alignment, and do not rank either entity.

When comparison is accepted, report the measured values, denominator, coverage, confidence, and limitations. Describe differences as observed within the supplied population; do not call any entity best practice, below benchmark, compliant, or deficient. If the accepted data is partial, label the comparison provisional.
