---
name: erp-process-playbooks
description: Build evidence-backed current-state ERP process maps and candidate findings for seven core process domains.
---

# ERP Process Playbooks

Use this skill after evidence intake for one or more scoped domains. Consume the scope, Evidence Register, Evidence Gap Register, and any permitted user-supplied source. Produce a current-state process map using `references/templates/process-map.md`, candidate Finding Register records using `references/templates/finding-register.md`, and unanswered questions.

## Common playbook rules

- Map only what the supplied evidence supports. Cite Evidence IDs in the process map and Finding Register.
- A stakeholder observation remains an observation; an evidence-free explanation is a hypothesis with a Gap ID, not a finding.
- Ask the eight diagnostic questions in every selected domain: **trigger, roles, data objects, standard/custom behavior, system handoffs, exceptions, controls, and outcome**.
- Mark standard/custom behavior `unknown` when configuration or product-release evidence is unavailable. Do not assert vendor features or an external benchmark.
- Describe controls as observed process design only; do not offer legal, tax, compliance, audit, or assurance conclusions.
- If a required source is absent, add a specific Evidence Gap Register request and return questions instead of invented findings.

## O2C

Map the flow from customer demand to cash, including order capture, credit review, availability, fulfilment, billing, cash application, disputes, credit notes, collections, and any revenue-recognition handoff supported by evidence.

| Ask | Domain question |
|---|---|
| Trigger | What customer order, contract, shipment, or billing event starts the flow? |
| Roles | Which sales, customer service, credit, logistics, billing, and finance roles act? |
| Data objects | Which customer, order, contract, price, delivery, invoice, payment, and dispute objects are used? |
| Standard/custom behavior | Which behavior is evidenced as standard, custom, workaround, or unknown? |
| System handoffs | Where do data or accountability pass across ERP, CRM, WMS, bank, spreadsheet, email, or portal? |
| Exceptions | Which blocked orders, price overrides, billing rework, disputes, or cash-application exceptions are evidenced? |
| Controls | Which observed approvals, credit checks, reconciliations, and evidence trails govern the flow? |
| Outcome | What evidence establishes fulfilment, invoice issuance, payment application, and closure? |

## P2P

Map demand to approved payment, including requisition, sourcing, purchase order, receipt, invoice capture, matching, exception resolution, payment, and supplier query handling.

| Ask | Domain question |
|---|---|
| Trigger | What demand, replenishment signal, contract call-off, or invoice event starts the flow? |
| Roles | Which requester, buyer, approver, receiver, AP, treasury, and supplier roles act? |
| Data objects | Which supplier, material/service, requisition, PO, receipt, invoice, tax-code, and payment objects are used? |
| Standard/custom behavior | Which behavior is evidenced as standard, custom, workaround, or unknown? |
| System handoffs | Where do data or accountability pass across procurement, ERP, receiving, invoice capture, bank, spreadsheet, email, or portal? |
| Exceptions | Which non-PO invoices, match exceptions, blocked invoices, urgent payments, or supplier disputes are evidenced? |
| Controls | Which observed approvals, segregation checks, matching rules, and payment controls govern the flow? |
| Outcome | What evidence establishes authorized receipt, liability, payment, and query closure? |

## R2R

Map transaction recording to an evidenced close, including journal preparation/approval, subledger handoffs, reconciliations, close calendar activities, consolidation, reporting, and correction handling.

| Ask | Domain question |
|---|---|
| Trigger | What period-end, transaction, allocation, or reporting event starts the activity? |
| Roles | Which accounting, controller, shared-service, consolidation, and reviewer roles act? |
| Data objects | Which ledger, journal, account, cost centre, entity, reconciliation, and close-calendar objects are used? |
| Standard/custom behavior | Which behavior is evidenced as standard, custom, workaround, or unknown? |
| System handoffs | Where do data or accountability pass across subledgers, consolidation, reporting, spreadsheet, email, or close tools? |
| Exceptions | Which late journals, unreconciled balances, manual consolidations, or post-close corrections are evidenced? |
| Controls | Which observed approvals, reconciliations, close tasks, and review evidence govern the flow? |
| Outcome | What evidence establishes an approved, reconciled, and reported period outcome? |

## M2M

Map demand or plan to manufactured and moved product, including planning, BOM/routing use, production order release, material issue, execution confirmation, quality events where supplied, receipt, and transfer.

| Ask | Domain question |
|---|---|
| Trigger | What forecast, sales demand, replenishment, or production plan starts the flow? |
| Roles | Which planner, production supervisor, operator, quality, warehouse, and finance roles act? |
| Data objects | Which material, BOM, routing, work centre, production order, batch, inventory, and costing objects are used? |
| Standard/custom behavior | Which behavior is evidenced as standard, custom, workaround, or unknown? |
| System handoffs | Where do data or accountability pass across planning, MES, ERP, quality, warehouse, spreadsheet, or email? |
| Exceptions | Which shortages, schedule changes, rework, yield variances, or confirmation corrections are evidenced? |
| Controls | Which observed release, material, quality, and inventory controls govern the flow? |
| Outcome | What evidence establishes completed product, inventory movement, and production closure? |

## Warehouse and Inventory

Map inventory receipt, storage, movement, counting, adjustment, fulfilment, and disposition across physical and system records.

| Ask | Domain question |
|---|---|
| Trigger | What receipt, pick, transfer, count, adjustment, or shipment event starts the activity? |
| Roles | Which receiver, warehouse operator, supervisor, inventory controller, planner, and finance roles act? |
| Data objects | Which material, location, bin, batch/serial, stock, transfer, count, and adjustment objects are used? |
| Standard/custom behavior | Which behavior is evidenced as standard, custom, workaround, or unknown? |
| System handoffs | Where do data or accountability pass across WMS, ERP, scanner, transport, spreadsheet, or email? |
| Exceptions | Which stock discrepancies, blocked stock, manual movements, count variances, or failed scans are evidenced? |
| Controls | Which observed count, approval, segregation, and movement-evidence controls govern the flow? |
| Outcome | What evidence establishes accurate available inventory and completed physical movement? |

## Pricing

Map price creation and maintenance to applied commercial terms, including price lists, agreements, discounts, rebates where supplied, approvals, effective dates, and billing handoffs.

| Ask | Domain question |
|---|---|
| Trigger | What contract, market event, customer request, product change, or review starts price activity? |
| Roles | Which commercial, sales, pricing, master-data, finance, and approver roles act? |
| Data objects | Which customer, product, price list, condition, agreement, discount, effective-date, and invoice objects are used? |
| Standard/custom behavior | Which behavior is evidenced as standard, custom, workaround, or unknown? |
| System handoffs | Where do data or accountability pass across CPQ/CRM, ERP, spreadsheet, email, portal, or billing? |
| Exceptions | Which overrides, expired terms, manual price changes, disputed invoices, or retroactive corrections are evidenced? |
| Controls | Which observed approval, effective-date, segregation, and audit-trail controls govern the flow? |
| Outcome | What evidence establishes an approved price applied to the relevant transaction? |

## Master Data

Map create/change/retire requests for business-critical data, including request intake, validation, approval, enrichment, distribution, correction, and ownership.

| Ask | Domain question |
|---|---|
| Trigger | What onboarding, change, product, supplier, customer, or correction request starts the flow? |
| Roles | Which requester, data steward, approver, process owner, IT, and downstream consumer roles act? |
| Data objects | Which customer, supplier, material, chart-of-accounts, location, price, and reference-data objects are used? |
| Standard/custom behavior | Which behavior is evidenced as standard, custom, workaround, or unknown? |
| System handoffs | Where do data or accountability pass across MDM, ERP, CRM, PLM, WMS, spreadsheet, email, or portal? |
| Exceptions | Which duplicates, incomplete records, failed interfaces, emergency changes, or recurring corrections are evidenced? |
| Controls | Which observed validation, approval, ownership, duplicate-prevention, and change-evidence controls govern the flow? |
| Outcome | What evidence establishes correct, timely, single-maintained data available to intended consumers? |

## Candidate finding and gap protocol

For each observed issue, use the Finding Register fields exactly: process step, observation, Evidence IDs, classification, impact, recommendation, priority, confidence, and Validation Owner. Do not write a finding when the observation has no supporting evidence. Instead, add a Hypothesis / Gap Register entry and ask for the smallest source needed to validate or reject it.
