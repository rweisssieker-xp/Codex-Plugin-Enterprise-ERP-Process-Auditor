# Innovation Layer Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add ten evidence-bounded innovation lenses and GitHub documentation to the Transformation Innovation Layer.

**Architecture:** Extend the existing innovation skill and register; keep all additions within the current evidence/owner/metric/kill-condition contract. Extend structural validation and README/manifest documentation.

**Tech Stack:** Markdown skills/templates, Python `unittest`, standard-library validator.

## Global Constraints

- Codex-only, user-supplied evidence only, no autonomous ERP execution.
- No unsupported external benchmark, vendor, saving, ROI, or compliance claim.
- Each lens is a hypothesis until evidence, metric, owner, guardrails, kill condition, confidence, and next validation are recorded.

---

### Task 1: Expand lenses, contract, tests, README, and release metadata

**Files:**
- Modify: `skills/erp-transformation-innovation/SKILL.md`
- Modify: `references/templates/innovation-opportunity-register.md`
- Modify: `scripts/validate_suite.py`
- Modify: `tests/test_validate_suite.py`
- Modify: `README.md`
- Modify: `.codex-plugin/plugin.json`

**Interfaces:**
- Produces a twenty-two-lens Innovation Layer and a register with `Blast Radius | Knowledge Concentration | Decision Latency | Reuse Potential | Exit Criterion` as optional, evidence-backed fields.

- [ ] **Step 1: Write failing regression tests**

```python
def test_innovation_layer_requires_each_expansion_lens(tmp_path):
    for lens in EXPANSION_LENSES:
        root = create_complete_suite(tmp_path)
        remove_literal(root / "skills/erp-transformation-innovation/SKILL.md", lens)
        assert f"erp-transformation-innovation: missing lens {lens}" in validate_plugin_root(root)
```

- [ ] **Step 2: Run tests and verify failure**

Run: `python -m unittest tests/test_validate_suite.py -v`

Expected: FAIL before validator and skill expansion.

- [ ] **Step 3: Implement the ten exact lenses and five register fields**

Add: Transformation Decision Compiler; Process Friction-to-Policy Mapper; ERP Change Blast-Radius Map; Standard Capability Proof Pack; Operational Resilience Score; Exception Half-Life Tracker; ERP Knowledge Concentration Risk; Transformation Reuse Index; Decision Latency Cost Model; Process Exit Strategy.

- [ ] **Step 4: Update validator, README, and manifest**

Independently hard-code all ten lens names in tests. Require all five added fields in the register. Document all twenty-two lenses and add one new manifest starter prompt for change blast radius and exit strategy.

- [ ] **Step 5: Run release validation, cachebuster, and commit**

Run:

```powershell
python -m unittest tests/test_validate_suite.py -v
python scripts/validate_suite.py .
python C:\Users\reinerw\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\reinerw\plugins\erp-process-transformation-agent
```

Expected: PASS.

Commit: `git add skills references scripts tests README.md .codex-plugin/plugin.json && git commit -m "feat: expand transformation innovation lenses"`

## Self-review

The single task covers all ten lenses, five fields, independent tests, README, manifest, release validation, and evidence boundaries. No placeholders remain.
