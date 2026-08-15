---
name: erp-executive-transformation
description: Produce evidence-bounded ERP import profiles and steering-committee transformation packs from user-supplied artifacts.
---

# ERP executive transformation outputs

Use this skill after evidence intake, finding validation, scoring, and governance review. It turns only user-supplied evidence, findings, scores, benchmark comparisons, value scenarios, initiatives, and governance records into an import profile and an executive transformation pack. It does not access ERP systems, parse unavailable files, obtain external benchmarks, or treat a requested outcome as evidence.

## Import and data map

For every supplied file or export description, create a row using `references/templates/import-profile.md`. Record the source file, format, table or sheet, grain, business key, period, entity coverage, available columns, quality limitation, process question supported, and conversion request. Describe columns only where they are supplied or explicitly described. If a file cannot be accessed or its format is unsupported, record the limitation and a structured conversion request; do not claim extraction, parsing, or completeness.

Treat each import profile as metadata, not proof of the values in the source. Link a usable source to its Evidence ID. Record omitted fields as `not supplied`, not as assumptions or negative findings.

## Executive pack

Use `references/templates/executive-pack.md`. Complete only these executive-pack sections: executive summary, top root causes, findings table, heatmap narrative, complexity balance sheet, target operating model, roadmap, decisions required, and open evidence. Use `references/templates/complexity-balance-sheet.md` for the complexity assessment.

Within the executive summary and every material recommendation, preserve these separate headings:

## Facts

State only source-backed statements and their Evidence IDs, scope, period, and confidence. If a fact is materially incomplete or conflicted, say so and label the affected conclusion provisional.

## Stakeholder observations

Attribute stakeholder statements, identify their source, and do not promote them to facts without validating evidence.

## Hypotheses

Give each unsupported proposition a Hypothesis ID and its linked Gap ID. A hypothesis cannot support a decision-grade priority, score, value statement, or recommendation until validated.

## Recommendations

Link every material recommendation to finding IDs and Evidence IDs. If it depends on an unvalidated hypothesis, state that dependency, mark it provisional, and name the validation needed. Recommendations are options for accountable human decision; they are not implementation instructions, approvals, or assurances.

## Presentation rules

- The heatmap is a narrative of supplied evidence and stated score coverage; it is not a claim of broad process performance. Do not fill unobserved process/entity cells with inferred risk.
- The complexity balance sheet separates observed complexity burden, constraints, candidate simplifications, dependencies, and open evidence. Do not label customizations, controls, interfaces, or local variation unnecessary without evidence and accountable validation.
- The target operating model is a proposed state. Record scope, owner, dependencies, assumptions, and validation gates; do not imply that it is approved or feasible.
- The roadmap groups proposed initiatives by stated horizon and dependency. Every item must cite its source findings or be identified as a hypothesis, name an accountable owner or `owner not supplied`, and include a decision or validation gate.
- In decisions required, name the decision, accountable human owner, evidence/finding IDs, status, and reversal condition. Do not imply human approval where none is recorded.
- In open evidence, state the gap, impact on the pack, requested evidence, and validation owner. Withhold decision-grade conclusions where a material gap or conflict remains.

Do not claim savings, FTE release, compliance, control effectiveness, implementation success, or external benchmark standing. A supplied value scenario may be reported only with its formula, Evidence IDs, assumptions, coverage, confidence, realization conditions, and double-counting risk.
