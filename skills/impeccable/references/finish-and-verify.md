# Finish and verify

Modified adaptation of Impeccable 4.9.1 polish and optimization principles. Verification uses the existing project tooling; this package includes no detector.

## Fix the right layer

Read the relevant design system and adjacent patterns. Classify each defect as a missing reusable value, an isolated implementation, a conceptual inconsistency or a local bug. Correct the cause at the narrowest appropriate level.

Prioritize blocked tasks, misleading state, data loss and inaccessible paths. Then complete recovery and state coverage, responsive structure, system consistency and finishing detail. Avoid perfecting one region while leaving another part of the same task unfinished.

## Polish the complete path

Check entry, navigation, action, feedback and return. Keep terminology, placement, hierarchy and save behavior consistent with comparable product areas. Verify alignment, spacing, text wrapping, icon families, control sizes and image proportions in context.

Preserve functionality, factual copy and identity during polish. Remove accidental churn and changes outside the requested scope. Do not use a cleanup pass to introduce unrelated abstractions.

## Optimize measured problems

Identify the observed bottleneck before changing an implementation. Distinguish network delay, asset loading, rendering work, interaction handling and unnecessary layout changes. Follow the project's existing performance budget and measurement tools.

Prefer a scoped improvement with a clear before-and-after observation. Keep loading feedback useful. Ensure an optimization does not remove accessibility, create stale state or change a functional contract. Do not equate a smaller source file with a faster experience.

## Verify proportionately

For code changes, run the repository's required validation and relevant regression and progression checks. Choose cases tied to the risk introduced or corrected by the change:

- A corrected defect no longer occurs under the original conditions.
- The intended new behavior works across the supported path.
- Existing neighboring behavior remains intact.
- Realistic content, relevant states and representative screen sizes remain usable.
- Keyboard and focus behavior, contrast and semantics remain appropriate.
- Required security and dependency checks remain satisfied according to the repository's policies.

Inspect the rendered result when possible and batch related visual checks. Use current screenshots or source analysis when live execution is unavailable, identifying the resulting limits. Do not invent test output or treat an unexecuted scenario as passed.

## Report completion

Explain the outcome, why it matters and the evidence supporting it. Name any remaining issue with its practical impact and next step. A concise completion report should let the user distinguish implemented changes, verified behavior and observations still awaiting a real environment.
