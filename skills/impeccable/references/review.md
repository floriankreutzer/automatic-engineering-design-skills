# Review and evidence

Modified adaptation of Impeccable 4.9.1 design-review principles. This guide contains no runtime dependency.

## Establish the target

Identify the page, route, component or user journey under review. Record the user's goal, relevant role, platform, viewport and content state. Inspect the current implementation and available visual evidence. Check the age and target of existing screenshots before treating them as current.

Distinguish a design critique from a technical UI audit. A critique assesses whether the experience supports its purpose. An audit checks concrete behavior and implementation quality. Both can inform the same result, but a stylistic preference is not a demonstrated defect.

## Critique the experience

Evaluate these dimensions against the selected surface mode:

- **Purpose and hierarchy:** Can the visitor recognize the main task, the current state and the next action? Does emphasis match product priority?
- **Information architecture:** Are labels, groups, navigation and disclosure understandable? Does the sequence follow the visitor's mental model?
- **Task flow:** Are arrival, action, feedback and recovery connected? Can users finish without guessing or losing context?
- **Visual system:** Do type, spacing, color, icons and components form a recognizable system across neighboring screens?
- **Content:** Is the wording specific, accurate and useful? Do labels describe actions and errors describe recovery?
- **Appropriate character:** Does the expression fit the use scene? Are decorative choices helping or competing with the task?

Explain each judgment with an observed element or interaction. Avoid reducing the review to personal taste or vague praise. If the user requests scores, define the dimensions and scale first, describe the evidence and avoid false precision.

## Audit concrete quality

Inspect the relevant paths with the tools available in the environment:

- Semantic headings, landmarks, labels and accessible control names.
- Keyboard reachability, focus visibility, focus order and recovery after dialogs or navigation.
- Text and non-text contrast against the project's applicable accessibility requirements; information communicated without color alone.
- Layout at supported sizes, content expansion, zoom, overlays and sticky elements.
- Loading, empty, error, disabled, success and restricted-access states.
- Actual action behavior, duplicate submissions, stale feedback and consistency between UI state and backend outcomes.
- Image sizing, font loading, visible layout shifts and observed interaction delays.
- Localization, dates, time zones, numeric formats and text direction where supported.

An automated check is one form of evidence. Passing it does not establish complete usability, accessibility or design quality. Do not label a check as passed if the target could not be exercised.

## Prioritize by user impact

| Priority | Meaning | Examples |
|---|---|---|
| P0 | Primary task blocked or severe integrity risk | Booking cannot complete, destructive action misrepresented, critical path inaccessible |
| P1 | Major obstacle with significant impact | Submission failure loses input, mobile action unreachable, ambiguous confirmation causes mistakes |
| P2 | Friction or inconsistency with a workable path | Unclear label, poor grouping, awkward long-content handling |
| P3 | Local refinement | Minor alignment, inconsistent decorative treatment, avoidable visual noise |

Calibrate severity to actual reach and consequence. Use the project's existing severity definitions if it has them.

## Report useful findings

Use a compact table with target, finding, impact, priority, evidence and recommended fix. Separate confirmed defects from hypotheses that need a live check. Consolidate repeated instances into their shared cause, while naming representative locations.

Recommend fixes in order: blocked or misleading tasks; missing states and recovery; hierarchy and responsive structure; visual consistency; finishing detail. Preserve known intentional decisions. End with the concrete next action that fits the user's scope.
