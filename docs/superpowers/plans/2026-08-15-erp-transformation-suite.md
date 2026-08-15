# ERP Process Transformation Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete, local, Codex-native ERP transformation suite that converts user-supplied evidence into traceable diagnostic, prioritization, governance, and proof-of-value artifacts.

**Architecture:** Add a transformation orchestrator plus twelve bounded skills, supported by shared Markdown templates and a standard-library Python structural validator. Skills exchange named registers and tables in the Codex task; they do not access ERP systems, store customer data, run unattended, or claim facts that are not source-backed.

**Tech Stack:** Codex plugin manifest, Markdown `SKILL.md` files, Markdown reference templates, Python 3 standard library validation, PowerShell test commands.

## Global Constraints

- The product runs only in Codex; do not add a web app, user accounts, ERP credentials, external APIs, direct system connections, or background monitoring.
- Inputs are task context and user-supplied files only; unsupported formats must produce a conversion request rather than a false extraction claim.
- Tag every material statement as fact, stakeholder observation, calculation assumption, or hypothesis and link it to an evidence ID.
- Do not present external benchmarks without a user-supplied source; use only explicitly declared internal comparison populations.
- FTE and financial value are scenarios: show formula, assumptions, coverage, confidence, and double-counting risks.
- No legal, tax, audit, security, or compliance assurance; high-impact recommendations require a named human validation owner.
- Keep source in `C:\Users\reinerw\plugins\erp-process-transformation-agent`; it is not a Git repository, so do not create a fake commit. Update the Codex cachebuster only after validation passes.

---

## File Structure

| Path | Responsibility |
|---|---|
| `skills/erp-transformation-orchestrator/SKILL.md` | Routes an engagement through the suite and composes decision-grade outputs. |
| `skills/erp-evidence-intake/SKILL.md` | Builds evidence, evidence-gap, and data-map registers. |
| `skills/erp-process-playbooks/SKILL.md` | Runs O2C, P2P, R2R, M2M, Warehouse/Inventory, Pricing, and Master Data diagnostics. |
| `skills/erp-scoring-benchmarking/SKILL.md` | Calculates transparent scores and internal-only comparisons. |
| `skills/erp-executive-transformation/SKILL.md` | Produces executive packs, initiative portfolio, packaging, and proof of value. |
| `skills/erp-governance-traceability/SKILL.md` | Enforces trust boundaries, decision log, and traceability. |
| `skills/erp-industry-variants/SKILL.md` | Applies bounded industry question sets and assumptions. |
| `references/templates/*.md` | Reusable schemas for evidence, findings, scores, initiatives, decision, and value registers. |
| `scripts/validate_suite.py` | Checks required files, headings, template columns, prohibited claims, and manifest version. |
| `tests/test_validate_suite.py` | Standard-library unit tests for validator behavior. |
| `README.md` | Explains module sequence, inputs, limits, and starter prompts. |

## Shared interfaces

All skills use these exact Markdown table names and columns:

```text
Evidence Register: Evidence ID | Source | Source Type | Period | Entity | Process | Statement Type | Confidence | Sensitivity | Use Limit
Evidence Gap Register: Gap ID | Needed Evidence | Decision Blocked | Owner | Priority | Requested By
Finding Register: Finding ID | Process Step | Observation | Evidence IDs | Classification | Impact | Recommendation | Priority | Confidence | Validation Owner
Scorecard: Metric | Formula | Result | Coverage | Evidence IDs | Assumptions | Confidence
Initiative Portfolio: Initiative ID | Outcome | Source Findings | Owner Function | Dependencies | Horizon | KPI | Baseline | Risk | Rollback or Mitigation | Decision Status
Value Register: Value ID | Initiative ID | Metric | Baseline | Target | Formula | Assumptions | Evidence IDs | Owner | Review Cadence | Confidence | Variance
Decision Log: Decision ID | Decision | Rationale | Evidence IDs | Owner | Approver | Status | Date | Reversal Condition
```

### Task 1: Establish suite contracts, templates, and validator

**Files:**
- Create: `references/templates/evidence-register.md`
- Create: `references/templates/finding-register.md`
- Create: `references/templates/scorecard.md`
- Create: `references/templates/initiative-portfolio.md`
- Create: `references/templates/value-register.md`
- Create: `references/templates/decision-log.md`
- Create: `scripts/validate_suite.py`
- Create: `tests/test_validate_suite.py`

**Interfaces:**
- Consumes: the shared interface names and columns in this plan.
- Produces: `validate_plugin_root(plugin_root: Path) -> list[str]`; an empty list means success and every later task relies on this check.

- [ ] **Step 1: Write failing validator tests**

```python
def test_reports_missing_required_skill(tmp_path):
    errors = validate_plugin_root(tmp_path)
    assert any("erp-transformation-orchestrator" in error for error in errors)

def test_accepts_complete_minimum_suite(tmp_path):
    create_minimum_suite(tmp_path)
    assert validate_plugin_root(tmp_path) == []
```

- [ ] **Step 2: Run the tests to verify failure**

Run: `python -m unittest tests/test_validate_suite.py -v`

Expected: FAIL because `validate_plugin_root` does not exist.

- [ ] **Step 3: Create the six exact templates and minimal validator**

```python
REQUIRED_SKILLS = {
    "erp-transformation-orchestrator", "erp-evidence-intake", "erp-process-playbooks",
    "erp-scoring-benchmarking", "erp-executive-transformation",
    "erp-governance-traceability", "erp-industry-variants",
}

def validate_plugin_root(plugin_root: Path) -> list[str]:
    errors = []
    for name in REQUIRED_SKILLS:
        if not (plugin_root / "skills" / name / "SKILL.md").is_file():
            errors.append(f"missing skill: {name}")
    return errors
```

Each template starts with its exact header row from **Shared interfaces** and includes one illustrative empty row; do not include client data.

- [ ] **Step 4: Run the unit tests**

Run: `python -m unittest tests/test_validate_suite.py -v`

Expected: PASS.

- [ ] **Step 5: Run structural validation against the plugin root**

Run: `python scripts/validate_suite.py .`

Expected: non-zero until Tasks 2–6 create the required skills.

### Task 2: Implement evidence intake, governance, and traceability

**Files:**
- Create: `skills/erp-evidence-intake/SKILL.md`
- Create: `skills/erp-governance-traceability/SKILL.md`
- Modify: `references/templates/evidence-register.md`
- Modify: `references/templates/decision-log.md`

**Interfaces:**
- Consumes: user task context and supplied files.
- Produces: `Evidence Register`, `Evidence Gap Register`, and `Decision Log` matching the shared columns.

- [ ] **Step 1: Add failing content assertions to the validator tests**

```python
def test_evidence_skill_requires_statement_types(tmp_path):
    create_minimum_suite(tmp_path)
    write_skill(tmp_path, "erp-evidence-intake", "# Evidence Intake")
    errors = validate_plugin_root(tmp_path)
    assert "erp-evidence-intake: missing statement-type rule" in errors
```

- [ ] **Step 2: Run the targeted test**

Run: `python -m unittest tests/test_validate_suite.py -v`

Expected: FAIL until the validator and skill contain the required rule.

- [ ] **Step 3: Write both skills with these mandatory rules**

```markdown
Classify each statement as one of: fact, stakeholder observation, calculation assumption, or hypothesis.
Never infer inaccessible content or fabricate a missing field.
For unsupported formats, create an Evidence Gap Register entry with a requested conversion format.
For high-impact recommendations, require a named Validation Owner and a Decision Log entry.
```

Governance must add: confidential-data minimization, human approval requirement, no assurance disclaimer, conflicting-evidence handling, and reversal condition for material decisions.

- [ ] **Step 4: Extend `validate_suite.py` to require the literal statement-type rule and Validation Owner**

```python
required_phrases = {
    "erp-evidence-intake": ["stakeholder observation", "calculation assumption", "hypothesis"],
    "erp-governance-traceability": ["Validation Owner", "reversal condition"],
}
```

- [ ] **Step 5: Run tests and manual scenario**

Run: `python -m unittest tests/test_validate_suite.py -v; python scripts/validate_suite.py .`

Manual prompt: `Create an evidence register for an O2C assessment using an Excel order export, a billing SOP, and two stakeholder statements; list what cannot yet be concluded.`

Expected: source-tagged evidence and explicit evidence gaps; no unsupported conclusion.

### Task 3: Implement the transformation orchestrator and process playbooks

**Files:**
- Create: `skills/erp-transformation-orchestrator/SKILL.md`
- Create: `skills/erp-process-playbooks/SKILL.md`
- Modify: `skills/erp-process-audit/SKILL.md`
- Create: `references/templates/process-map.md`

**Interfaces:**
- Consumes: Evidence Register, Evidence Gap Register, and scoped process/domain.
- Produces: current-state process map and Finding Register.

- [ ] **Step 1: Add failing validator tests for every supported domain**

```python
def test_playbook_lists_all_domains(tmp_path):
    create_minimum_suite(tmp_path)
    write_skill(tmp_path, "erp-process-playbooks", "## O2C\n## P2P")
    errors = validate_plugin_root(tmp_path)
    assert "erp-process-playbooks: missing domain R2R" in errors
```

- [ ] **Step 2: Run the test**

Run: `python -m unittest tests/test_validate_suite.py -v`

Expected: FAIL because the complete domain set is absent.

- [ ] **Step 3: Implement orchestration sequence and playbooks**

The orchestrator must execute this exact order: scope -> evidence intake -> governance -> playbook -> evidence-gap check -> scoring -> benchmarking when comparable -> initiatives -> executive output -> proof of value.

The playbook skill must include sections for O2C, P2P, R2R, M2M, Warehouse and Inventory, Pricing, and Master Data. Each section asks for trigger, roles, data objects, standard/custom behavior, system handoffs, exceptions, controls, and outcome.

- [ ] **Step 4: Update the existing audit skill to delegate rather than duplicate**

Replace broad duplicated instructions with a clear entry-point note: use the orchestrator for complete engagements and this skill for a rapid process diagnostic. Preserve the existing 40 USPs.

- [ ] **Step 5: Run tests and two manual scenarios**

Run: `python -m unittest tests/test_validate_suite.py -v; python scripts/validate_suite.py .`

Manual prompts:

```text
Run a rapid O2C diagnostic from an order export and billing SOP.
Run an R2R diagnostic with no close calendar or reconciliation evidence.
```

Expected: O2C produces findings; R2R produces a structured evidence request rather than invented findings.

### Task 4: Implement scoring, internal benchmarking, and industry variants

**Files:**
- Create: `skills/erp-scoring-benchmarking/SKILL.md`
- Create: `skills/erp-industry-variants/SKILL.md`
- Create: `references/templates/benchmark-comparison.md`

**Interfaces:**
- Consumes: validated Finding Register plus comparable entity data.
- Produces: Scorecard, benchmark comparison, and industry assumption list.

- [ ] **Step 1: Write failing scoring tests**

```python
def test_scorecard_requires_formula_coverage_and_confidence(tmp_path):
    create_minimum_suite(tmp_path)
    write_skill(tmp_path, "erp-scoring-benchmarking", "## Scorecard\nMetric | Result")
    assert "erp-scoring-benchmarking: missing formula rule" in validate_plugin_root(tmp_path)
```

- [ ] **Step 2: Run the test**

Run: `python -m unittest tests/test_validate_suite.py -v`

Expected: FAIL until formula, coverage, evidence IDs, assumptions, and confidence rules exist.

- [ ] **Step 3: Implement six score definitions and benchmark refusals**

Define process maturity, friction, automation readiness, standardization potential, data-quality risk, and control risk. Each uses an explicit weighted count of finding severity, affected population, evidence confidence, and stated denominator. The skill must label scores provisional when the denominator or evidence coverage is missing.

Add this mandatory benchmark gate:

```markdown
Compare entities only when the metric definition, period, population, process scope, and data grain are the same. Otherwise provide a comparability-gap table and do not rank entities.
```

- [ ] **Step 4: Add industry pattern boundaries**

Create distinct question sets for manufacturing, distribution, retail, project business, and regulated operations. Each output begins with `Industry pattern guidance, not client fact`.

- [ ] **Step 5: Run tests and manual comparison scenarios**

Run: `python -m unittest tests/test_validate_suite.py -v; python scripts/validate_suite.py .`

Manual prompts: compare two plants with identical monthly order volumes; then compare one monthly plant with one quarterly country total.

Expected: first comparison is accepted with limits; second is rejected as incomparable.

### Task 5: Implement import/data map and executive transformation outputs

**Files:**
- Create: `skills/erp-executive-transformation/SKILL.md`
- Create: `references/templates/import-profile.md`
- Create: `references/templates/executive-pack.md`
- Create: `references/templates/complexity-balance-sheet.md`

**Interfaces:**
- Consumes: evidence, findings, scores, benchmarks, and governance records.
- Produces: import profile, executive summary, heatmap input, complexity balance sheet, target operating model, and roadmap.

- [ ] **Step 1: Write failing output tests**

```python
def test_executive_skill_requires_fact_hypothesis_separation(tmp_path):
    create_minimum_suite(tmp_path)
    write_skill(tmp_path, "erp-executive-transformation", "# Executive Outputs")
    assert "erp-executive-transformation: missing fact/hypothesis separation" in validate_plugin_root(tmp_path)
```

- [ ] **Step 2: Run the test**

Run: `python -m unittest tests/test_validate_suite.py -v`

Expected: FAIL until the skill and template include the separation.

- [ ] **Step 3: Implement import and output contract**

The import profile records source file, format, table/sheet, grain, business key, period, entity coverage, available columns, quality limitation, and conversion request. The executive pack contains exactly: executive summary, top root causes, findings table, heatmap narrative, complexity balance sheet, target operating model, roadmap, decisions required, and open evidence.

- [ ] **Step 4: Add structural validator rules**

Require `Facts`, `Stakeholder observations`, `Hypotheses`, and `Recommendations` headings in the executive pack template and `grain` plus `business key` in the import profile template.

- [ ] **Step 5: Run tests and manual output scenario**

Run: `python -m unittest tests/test_validate_suite.py -v; python scripts/validate_suite.py .`

Manual prompt: `Create a steering-committee pack from three validated O2C findings and two open evidence gaps.`

Expected: the pack separates knowns from unknowns and includes decisions required.

### Task 6: Implement initiative portfolio, packaging, and proof of value

**Files:**
- Modify: `skills/erp-executive-transformation/SKILL.md`
- Modify: `references/templates/initiative-portfolio.md`
- Modify: `references/templates/value-register.md`
- Create: `references/templates/offer-packages.md`

**Interfaces:**
- Consumes: Finding Register, Scorecard, Decision Log, and approved baselines.
- Produces: Initiative Portfolio, Value Register, and offer-package recommendation.

- [ ] **Step 1: Write failing initiative and value tests**

```python
def test_initiative_requires_owner_dependency_kpi_and_rollback(tmp_path):
    create_minimum_suite(tmp_path)
    write_template(tmp_path, "initiative-portfolio.md", "Initiative ID | Outcome")
    assert "initiative template: missing rollback or mitigation" in validate_plugin_root(tmp_path)
```

- [ ] **Step 2: Run the test**

Run: `python -m unittest tests/test_validate_suite.py -v`

Expected: FAIL until all required columns and the value formula rule exist.

- [ ] **Step 3: Implement initiative and value rules**

Every high-priority initiative needs owner function, dependencies, horizon, KPI, baseline, risk, rollback/mitigation, and decision status. Every value scenario uses this calculation where applicable:

```text
annual transactions × minutes per transaction × automatable share / 60 / productive annual hours per FTE
```

Require an assumption and double-counting review before totaling FTE impact.

- [ ] **Step 4: Implement the four package-selection rules**

```markdown
Rapid Diagnostic: limited evidence, one process, decision required within 0–90 days.
Process Deep Dive: sufficient evidence for root cause, controls, and quantified opportunities.
Transformation Portfolio: multiple processes or entities with initiative and roadmap decisions.
Continuous Process Intelligence: recurring evidence refresh and approved recurring KPI review; no unattended monitoring claim.
```

- [ ] **Step 5: Run tests and proof-of-value scenario**

Run: `python -m unittest tests/test_validate_suite.py -v; python scripts/validate_suite.py .`

Manual prompt: `Turn two validated O2C findings into initiatives and calculate an FTE scenario from 120,000 annual orders, 4 minutes per order, 35% automatable share, and 1,600 productive hours.`

Expected: two owned initiatives plus a transparent 1.75-FTE theoretical capacity scenario, assumptions, and double-counting warning.

### Task 7: Document, validate, and release

**Files:**
- Create: `README.md`
- Modify: `.codex-plugin/plugin.json`
- Modify: `skills/erp-process-audit/SKILL.md`

**Interfaces:**
- Consumes: all completed skills and templates.
- Produces: discoverable plugin metadata, starter prompts, and a reproducible validation/release procedure.

- [ ] **Step 1: Write a failing release validation test**

```python
def test_manifest_declares_skills_and_nonempty_prompts(tmp_path):
    create_minimum_suite(tmp_path)
    write_manifest(tmp_path, {"name": "erp-process-transformation-agent"})
    assert "manifest: missing skills path" in validate_plugin_root(tmp_path)
```

- [ ] **Step 2: Run the test**

Run: `python -m unittest tests/test_validate_suite.py -v`

Expected: FAIL until manifest metadata is complete.

- [ ] **Step 3: Update documentation and manifest**

README sections: what the suite does, what it does not do, module sequence, accepted evidence types, artifact catalogue, data/privacy limits, validation steps, and five starter prompts.

Update `plugin.json` description and starter prompts to mention evidence-backed transformation suite, O2C deep dive, internal benchmarking, initiative portfolio, and proof-of-value review. Keep `skills: "./skills/"`; do not add unsupported app, MCP, or hooks fields.

- [ ] **Step 4: Run all structural and plugin validation**

Run:

```powershell
python -m unittest tests/test_validate_suite.py -v
python scripts/validate_suite.py .
python C:\Users\reinerw\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\reinerw\plugins\erp-process-transformation-agent
```

Expected: all commands exit with code 0.

- [ ] **Step 5: Update the plugin cachebuster and perform smoke tests**

Run:

```powershell
python C:\Users\reinerw\.codex\skills\.system\plugin-creator\scripts\update_plugin_cachebuster.py C:\Users\reinerw\plugins\erp-process-transformation-agent
```

Smoke-test these five prompts in a new Codex task: rapid O2C diagnostic, P2P evidence intake, R2R insufficient-evidence case, comparable internal benchmark, and O2C initiative/value scenario. Record failures in the Decision Log template before release.

## Plan self-review

| Specification requirement | Implementing task |
|---|---|
| Evidence intake and data map | Tasks 2 and 5 |
| Process playbooks | Task 3 |
| Scores and internal benchmarks | Task 4 |
| Executive deliverables | Task 5 |
| Audit trail and governance | Task 2 |
| Initiative execution loop | Task 6 |
| Industry variants | Task 4 |
| Product packaging | Task 6 |
| Proof of value | Task 6 |
| Testing, documentation, and release | Tasks 1 and 7 |

Placeholder scan completed: this plan contains no implementation placeholders. Interface names, template columns, score fields, and validation function names are used consistently across all tasks.
