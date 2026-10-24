# Plan Template

Use this structure when a plan is requested or useful for a larger authorized change. Make the handoff self-contained; do not refer to "the audit above" without the needed evidence. Host/user scope and project design/architecture take precedence. For Pavurel marketing website work, use the installed `pavurel-web-design` skill when available, without assuming a cross-skill filesystem path.

````markdown
# NNN — <Short imperative title>

- **Status**: TODO
- **Commit**: <output of `git rev-parse --short HEAD` when this plan was written>
- **Severity**: HIGH | MEDIUM | LOW
- **Category**: <audit category>
- **Estimated scope**: <n files, rough size>

## Problem

What is wrong, where, and its functional, accessibility, performance, or
usability impact. Distinguish an observed failure from an unmeasured risk.
Cite locations as `path/to/file.tsx:123` and include relevant current code:

```css
/* src/components/dropdown.css:14 — current */
.dropdown { transition: all 400ms ease-in; }
```

## Target

The exact end state, preserving layout, hiding, keyboard, and focus behavior.
Spell out project tokens, durations, state changes, and reduced-motion behavior.
Explain any intentional deviation from existing conventions:

```css
/* target */
.dropdown {
  transition: transform 200ms var(--ease-out), opacity 200ms var(--ease-out);
  transform-origin: var(--transform-origin);
}
```

## Repo conventions to follow

How this codebase already does it, with one exemplar the executor should
imitate (token names, file placement, prop patterns):

- Reuse the actual easing/duration tokens in <project token file>; include their current values and an exemplar. Do not introduce parallel tokens for a stylistic preference.
- Record installed framework/Motion versions if API behavior or acceleration is relevant, with version-specific official documentation.
- <exemplar file:line that already does this correctly>

## Steps

1. <One concrete edit per step: file, what changes, resulting code.>
2. …

## Boundaries

- Do NOT touch <files/components out of scope>.
- Do NOT change markup/structure — motion properties only (unless a step says otherwise).
- Do NOT add new dependencies.
- If code has drifted, re-read the affected files and adapt routine details within the authorized scope. Pause only for a material conflict, unresolved product decision, or real approval boundary; identify it specifically.

## Verification

- **Mechanical**: <focused existing checks required by the change/project, with expected outcome; do not add tests that merely restate the edit>.
- **Function and access**: verify keyboard operation, focus entry/return, hidden-state behavior, accessible names/announcements, and relevant no-JS fallback. Confirm that no essential content depends on an animation-end callback.
- **Feel check**: run the UI, trigger <interaction>, and confirm:
  - <observable check, e.g. "the dropdown scales from its trigger, not from center">
  - <e.g. "spamming the toggle never restarts the animation from zero">
  - In DevTools, set playback to 10% (Animations panel) and confirm <detail>.
  - Toggle `prefers-reduced-motion` and confirm a gentler or instant result with understandable static feedback. Verify preference changes do not break visibility or operation.
- **Performance, when relevant**: <representative interaction/device recording and expected improvement; do not claim measured gains from static review alone>.
- **Done when**: <machine- or eye-checkable completion criteria>.
````

## Notes for the plan author

- One plan per finding. If two findings share every file and the same fix pattern (e.g. the same easing token swap across components), they may merge into one plan.
- Prefer the project's established values; [AUDIT.md](AUDIT.md) supplies fallback defaults, not mandatory curves or durations.
- Include concrete visual/interaction checks. Perform available checks; if a device or runtime is unavailable, name the unverified aspect without inventing a result or blocking unrelated authorized work.
- For several plans, maintain the project's plan index with status, order, and dependencies. A single small direct fix does not need extra administrative files.
