# Transformation Innovation Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an evidence-bounded Innovation Layer and GitHub-ready documentation to the ERP Transformation Suite.

**Architecture:** One `erp-transformation-innovation` skill consumes existing registers and emits an Innovation Opportunity Register plus an executive innovation brief. The structural validator proves the skill, its twelve lenses, safety language, register schema, README, and manifest integration are present.

**Tech Stack:** Codex plugin skills, Markdown templates/README, Python standard-library validator, `unittest`.

## Global Constraints

- Run only in Codex; do not add web services, system credentials, APIs, or unattended execution.
- Use user-supplied evidence only; label every unvalidated lens output as a hypothesis.
- No external benchmark, market, vendor, ROI, or financial claim without supplied evidence.
- Every high-impact proposal needs evidence, metric, kill condition, owner, guardrails, confidence, and reversible next validation.

---

### Task 1: Innovation Layer skill, register, and validation

**Files:**
- Create: `skills/erp-transformation-innovation/SKILL.md`
- Create: `references/templates/innovation-opportunity-register.md`
- Modify: `scripts/validate_suite.py`
- Modify: `tests/test_validate_suite.py`

**Interfaces:**
- Consumes: Evidence Register, Finding Register, Scorecard, Initiative Portfolio, Decision Log, Value Register.
- Produces: `Innovation Opportunity Register` with `Opportunity ID | Innovation Lens | Target Audience | Workflow Replaced | Differentiator | Evidence IDs | Assumptions | Metric | Kill Condition | Owner | Guardrails | Confidence | Next Validation | Decision Status`.

- [ ] **Step 1: Write failing tests**

```python
def test_innovation_layer_requires_all_lenses_and_safety_fields(tmp_path):
    create_minimum_suite(tmp_path)
    write_skill(tmp_path, "erp-transformation-innovation", "# Innovation Layer")
    assert "erp-transformation-innovation: missing lens Transformation Evidence Graph" in validate_plugin_root(tmp_path)
```

- [ ] **Step 2: Run test**

Run: `python -m unittest tests/test_validate_suite.py -v`

Expected: FAIL because the skill and required language do not exist.

- [ ] **Step 3: Implement the skill and register**

Include all twelve exact lens names, evidence-first ranking, the mandatory opportunity columns, executive innovation brief, all global constraints, and explicit non-execution boundary.

- [ ] **Step 4: Extend validator and tests**

Require the skill, all twelve lens strings, `Metric`, `Kill Condition`, `Guardrails`, `Next Validation`, and the exact register header. Add a complete-skill positive fixture.

- [ ] **Step 5: Validate and commit**

Run: `python -m unittest tests/test_validate_suite.py -v; python scripts/validate_suite.py .`

Expected: PASS.

Commit: `git add skills references scripts tests && git commit -m "feat: add transformation innovation layer"`

### Task 2: GitHub documentation, manifest, and release validation

**Files:**
- Modify: `README.md`
- Modify: `.codex-plugin/plugin.json`
- Modify: `tests/test_validate_suite.py`

**Interfaces:**
- Consumes: Innovation Layer skill and register.
- Produces: GitHub-ready product documentation and discoverable plugin prompts.

- [ ] **Step 1: Write failing documentation tests**

```python
def test_readme_and_manifest_reference_innovation_layer(tmp_path):
    create_minimum_suite(tmp_path)
    assert "README: missing Innovation Layer" in validate_plugin_root(tmp_path)
```

- [ ] **Step 2: Run test**

Run: `python -m unittest tests/test_validate_suite.py -v`

Expected: FAIL before README and manifest integration.

- [ ] **Step 3: Update README**

Add product positioning, architecture/module overview, Innovation Layer with all twelve lenses, five starter prompts, input/evidence boundaries, testing, installation, GitHub project structure, and contribution guidance.

- [ ] **Step 4: Update manifest and validator**

Revise description and prompts to mention evidence-backed innovation opportunities. Require `Innovation Layer` in README and one innovation starter prompt in manifest tests.

- [ ] **Step 5: Release checks and commit**

Run:

```powershell
python -m unittest tests/test_validate_suite.py -v
python scripts/validate_suite.py .
python C:\Users\reinerw\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\reinerw\plugins\erp-process-transformation-agent
```

Expected: all PASS.

Commit: `git add README.md .codex-plugin/plugin.json tests && git commit -m "docs: publish innovation layer for GitHub"`

## Self-review

Task 1 covers the central skill, all twelve lenses, safety, schema, and tests. Task 2 covers README, GitHub presentation, manifest discovery, and release validation. No placeholders or undefined interfaces remain.
