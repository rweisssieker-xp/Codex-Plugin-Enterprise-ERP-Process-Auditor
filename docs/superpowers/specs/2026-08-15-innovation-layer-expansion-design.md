# Innovation Layer Expansion — Design Specification

## Scope

Extend the central Transformation Innovation Layer from twelve to twenty-two evidence-bounded lenses. The ten additions are Transformation Decision Compiler, Process Friction-to-Policy Mapper, ERP Change Blast-Radius Map, Standard Capability Proof Pack, Operational Resilience Score, Exception Half-Life Tracker, ERP Knowledge Concentration Risk, Transformation Reuse Index, Decision Latency Cost Model, and Process Exit Strategy.

## Integration

Add the lenses to `erp-transformation-innovation`, the Innovation Opportunity Register, structural validator, regression tests, README, and plugin discovery prompts. Every added lens remains a hypothesis until it references user-supplied evidence and has an owner, metric, kill condition, guardrails, confidence, and next validation.

## Register fields

Add optional assessment fields: Blast Radius, Knowledge Concentration, Decision Latency, Reuse Potential, and Exit Criterion. They must be evidence-backed or marked as assumptions.

## Constraints

No ERP execution, external benchmark, vendor feature, guaranteed saving, or compliance assertion may be inferred. The README must make these constraints explicit and describe the full twenty-two-lens catalog.

## Validation

Regression tests must independently hard-code all ten lens names and test that each is required. They must check the five added register fields and README/manifest references. The complete suite, structural validator, and plugin validator must pass before the cachebuster is updated.
