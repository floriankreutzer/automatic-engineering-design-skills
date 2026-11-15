# States, content and resilience

Modified adaptation of Impeccable 4.9.1 hardening, clarification and onboarding guidance. This is a conceptual checklist to apply through the existing project workflow.

## Build a state inventory

For each relevant flow, identify default, loading, partial, empty, error, success, disabled and restricted-access states. Include entry and exit paths. Decide what the user can understand and do in each state, and which state changes need immediate feedback.

Distinguish an empty dataset from a failed request, a search with no matches, unavailable permissions and a filter that excludes everything. These conditions need different explanations and actions.

## Exercise realistic extremes

Review short, long, missing and unusual input; large and zero values; few and many records; slow responses; interrupted requests; and consecutive or overlapping actions. Use representative localized content and actual supported date, number and currency formats.

Let content containers grow or reflow when possible. If truncation is necessary, keep essential information discoverable through an accessible path. Do not hide the information needed to choose or confirm an action.

Retain valid input when validation or submission fails. Prevent duplicate submissions in the interface and verify that backend protections remain appropriate for the operation. Handle conflicts and stale data explicitly rather than silently overwriting another change.

For custom gestures, check cancellation, interrupted capture, release outside the control and loss of focus. The next interaction must still work. Preserve keyboard or alternative access to the task.

## Write useful messages

Controls should name the action and, when useful, its object. Use the product's existing terminology. Explain irreversible or consequential outcomes at the decision point without adding unrelated warnings.

An error message should state what failed, what remains safe or preserved, and what the user can do next. Translate technical failures into useful language; avoid exposing internal diagnostics or sensitive data. Keep detailed diagnostics in the project's appropriate support or logging channel.

Validation belongs near the affected input and must remain perceivable with assistive technology. Do not rely on placeholder text as the only label. Explain requirements before input when that prevents predictable errors.

Keep factual claims tied to supplied product truth. Treat examples as examples and avoid inventing commitments, metrics or customer statements.

## Design onboarding and empty states

Identify the smallest meaningful first success. Introduce requirements when they become relevant and preserve a clear path back to the primary task. Show real progress and explain why requested information is needed.

An empty state should explain the state, set an appropriate expectation and offer a useful next action. If users cannot act because of their role, give the correct explanation instead of an unusable button. Use examples only when they help users understand the product's structure.

Allow experienced users to proceed efficiently. Avoid mandatory tours that obscure a usable interface. Keep help contextual and available later.

## Verify resilience

Exercise the main task with at least one meaningful failure and recovery path, plus content and layout boundaries relevant to the change. Check that feedback matches the actual outcome and that a retry does not create unintended duplication. Follow the repository's testing and security standards for any implementation change.
