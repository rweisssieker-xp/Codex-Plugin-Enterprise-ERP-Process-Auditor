---
name: erp-evidence-intake
description: Create evidence and evidence-gap registers from user-supplied ERP transformation context and files without unsupported extraction or conclusions.
---

# ERP Evidence Intake

Use this skill before diagnostic, scoring, benchmarking, or executive-output work. It accepts only the user task context, stakeholder statements, and files explicitly supplied in Codex. It does not connect to ERP systems, external services, or data stores.

## Intake boundary

1. Inventory each supplied source: name, source type, accessible content, period, entity, process, sensitivity, and intended use.
2. Inspect only content that is accessible in the task. Never infer inaccessible content or fabricate a missing field.
3. Classify each statement as one of: fact, stakeholder observation, calculation assumption, or hypothesis.
4. Assign a stable Evidence ID and record every source-backed item in the shared **Evidence Register**.
5. Record uncertainty, partial coverage, conflicting accounts, and intended-use limits explicitly. Confidence describes evidence strength, not business importance.

## Statement-type rules

- **fact** — directly supported by accessible, user-supplied evidence; cite its Evidence ID.
- **stakeholder observation** — an attributed statement from a person; do not elevate it to fact until independently supported.
- **calculation assumption** — an input chosen for a transparent calculation; state its source or why it is provisional.
- **hypothesis** — a candidate explanation or outcome that requires validation; do not phrase it as a conclusion. When it has no source evidence, assign a Hypothesis ID and record it in the Hypothesis / Gap Register with at least one Gap ID; it is explicitly not an Evidence ID.

Every material statement must have one statement type. A fact, stakeholder observation, or source-backed calculation assumption must cite an Evidence ID. An evidence-free hypothesis must cite a Hypothesis ID and Gap ID in the Hypothesis / Gap Register, explicitly not an Evidence ID. Do not enter an unsupported hypothesis in the Evidence Register or assign it a source-backed status.

## File and data handling

Supported evidence can include accessible spreadsheet/CSV exports, documents, presentation material, ticket exports, process-event logs, screenshots, interface inventories, and ERP extract descriptions. Describe only what is actually available and readable.

For unsupported formats, create an **Evidence Gap Register** entry with a requested conversion format. For example: request a CSV/XLSX export with a data dictionary, or a searchable PDF/text transcription. State the decision blocked, proposed owner, priority, and requester. Do not claim successful extraction, parsing, or completeness for an unsupported or inaccessible file.

Minimize sensitive content: record source metadata and only the smallest necessary excerpt or field description. Use the **Sensitivity** and **Use Limit** columns to constrain further circulation or analysis. Do not copy customer, employee, financial, or other confidential values unless they are necessary and already supplied for the stated task.

## Required outputs

Produce these tables using the shared columns exactly.

### Evidence Register

| Evidence ID | Source | Source Type | Period | Entity | Process | Statement Type | Confidence | Sensitivity | Use Limit |
|---|---|---|---|---|---|---|---|---|---|
| E-001 | [user-supplied source name] | [type] | [period or unknown] | [entity or unknown] | [process] | [one permitted type] | [high/medium/low] | [handling note] | [permitted analysis or limitation] |

### Evidence Gap Register

| Gap ID | Needed Evidence | Decision Blocked | Owner | Priority | Requested By |
|---|---|---|---|---|---|
| G-001 | [specific evidence or conversion request] | [decision or conclusion limited] | [named role/person if known] | [high/medium/low] | [requesting role] |

### Hypothesis / Gap Register

Use this record only for an evidence-free hypothesis. Each hypothesis requires at least one Gap ID that identifies the missing evidence needed to validate or reject it. A Hypothesis ID is explicitly not an Evidence ID and does not support a fact, calculation, recommendation, or decision until validation creates a source-backed Evidence Register entry.

| Hypothesis ID | Hypothesis Statement | Gap IDs | Validation Needed | Owner | Status |
|---|---|---|---|---|---|
| H-001 | [unconfirmed candidate explanation] | G-001 | [specific evidence/test required] | [validation owner] | open / validated / rejected |

## Recommendation gate

Do not make a high-impact recommendation from evidence intake alone. For each high-impact recommendation carried forward, require a named Validation Owner and a Decision Log entry. State the validation needed, supporting Evidence IDs, any conflicts, and what cannot yet be concluded.

## Limits

Do not invent external benchmarks, FTE savings, financial value, legal, tax, audit, security, or compliance conclusions. Any FTE or value discussion must remain a transparent scenario with stated evidence and assumptions; otherwise record an evidence gap.
