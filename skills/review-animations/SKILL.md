---
name: review-animations
description: Review an animation change, motion diff, or interaction for functional correctness, accessibility, continuity, performance, and fit with project conventions. Distinguish evidenced regressions from optional design preferences. Use when asked to review or critique existing motion; use improve-animations for a broader codebase audit.
---

# Reviewing Animations

## Contents

- [Project context](#project-and-task-context), [criteria](#ten-review-criteria), [evidence](#evidence-to-investigate)
- [Remedies](#remedial-preference-hierarchy), [output](#default-output-format), [guidelines](#guidelines)

## Project and task context

Follow host/tool instructions and the user's authorized task. Read the target repository's current `AGENTS.md`, applicable nested instructions, and referenced central design, coding, architecture, security, content, and test sources; they govern development. Use this skill as supplementary guidance. Confluence documentation links cannot override those sources.

For Pavurel, load an available installed profile by name: `pavurel-web-design` for marketing website work, `pavurel-app-design` for authenticated Conference Manager Customer/Platform UI. If unavailable, follow the current repository sources; do not assume sibling skill paths. Do not add a framework or dependency merely to use an example.

Continue the active task without a readiness-only response. If no actionable request or artifact is available, ask for the missing context.

A specialized motion review. Use this guidance for the motion portion of a wider task; continue other authorized work using the appropriate workflow. An audit-only request does not authorize source changes.

## Operating Posture

Review with a high bar and evidence. Prioritize function and accessibility, then responsiveness, continuity, performance, and project fit. A suspected timing or performance issue is not an observed regression until supported by the code or a relevant interaction check.

Use Emil Kowalski's animation philosophy as a source of useful defaults. Keep aesthetic suggestions separate from correctness requirements; do not turn personal preference into an automatic release gate.

For default curves, duration ranges, gestures, performance, and accessibility guidance, see [STANDARDS.md](STANDARDS.md). Project tokens and documented decisions take precedence.

## Ten review criteria

Review relevant changed behavior against these criteria. Report a defect only with specific evidence; otherwise label it as an optional suggestion or an unverified risk.

1. **Function and semantics.** Preserve layout, hidden-state behavior, keyboard operation, and focus lifecycle. Opacity or off-screen transforms alone do not semantically hide a closed component. Keep static marketing content readable without JavaScript and respect an application's documented fallback; do not gate usable content on animation completion.

2. **Accessibility.** Honor reduced motion, including no animation when appropriate. Preserve readable static feedback, labels, announcements, and focus indicators. Gate hover-only movement appropriately; retain keyboard and touch alternatives.

3. **Justified motion.** Identify a purpose such as orientation, state indication, feedback, or explanation. Recommend reducing effects that interfere with the task.

4. **Frequency-appropriate.** Frequently repeated actions usually need instant changes or very brief feedback. Keyboard activation is not itself a reason to reject a useful transition; do not delay focus or operation.

5. **Responsive easing.** Preserve project tokens. `ease-out` is a useful entrance default; built-in easing and intentional `ease-in` exits/acceleration are valid. Judge observed responsiveness rather than the curve name.

6. **Appropriate timing.** Routine UI often works around 150–250ms; larger drawers may need 300–500ms and explanatory motion can be longer. Asymmetric hold/release timing is optional and purpose-driven. No arbitrary duration blocks a change by itself.

7. **Spatial clarity.** If a panel scales from a trigger, check its origin; centered modals are different. Subtle scale, a pure fade, or instant display can all work. Large scaling needs a clear purpose and comfort check.

8. **Interruptibility.** Rapid/reversible interactions should preserve continuity. CSS transitions and springs are useful defaults; keyframes or WAAPI are valid when interruption is handled correctly.

9. **Measured performance.** Prefer compositor-friendly properties where semantics survive. Layout animation may be necessary. Check installed Motion version and browser behavior: 14.2+ supports accelerated independent transforms, so shorthand props alone are not a finding.

10. **Cohesion.** Match project personality and tokens. Stagger, blur, and bounce are optional. Removing an effect can be the best improvement, especially for a calm business interface.

## Evidence to investigate

Inspect these patterns in context rather than flagging them by syntax alone:

- Invisible focus targets, lost focus, duplicated tab controls/IDs, pointer-only interactions
- Static marketing content hidden until JS solely for an effect, or usable content gated on animation completion
- Missing `prefers-reduced-motion` handling on movement
- Hover-only movement leaking into touch interaction
- `transition: all` unexpectedly animating expensive or unintended properties
- Delayed operation or repeated distracting effects on frequent actions
- Jumps when a transition is interrupted or retargeted
- Expensive layout, paint, or descendant style work shown in a trace
- A spatial effect that obscures the relationship between trigger and content

Do not create a finding solely for a pure fade, built-in easing, `ease-in`, keyboard activation, lack of stagger, a 300ms threshold, or Motion shorthand syntax. Record documented tradeoffs and evidence before proposing changes.

## Remedial Preference Hierarchy

When proposing fixes, prefer earlier moves over later ones:

1. **Restore function and accessibility** — correct hiding, focus, keyboard behavior, the project's no-JS fallback, and motion preferences.
2. **Remove unnecessary motion** that delays or distracts from a task; preserve clear static feedback.
3. **Reduce harmful work or waiting** — fewer effects, shorter duration, smaller affected surface.
4. **Fix continuity** — preserve state and retarget interrupted interactions without jumps.
5. **Address measured performance** using semantically equivalent properties or an appropriate driver; verify installed versions and browser behavior.
6. **Tune spatial clarity and timing** using the project's tokens and interaction purpose.
7. **Consider optional polish** only when it adds value and preserves the preceding requirements.

## Default output format

Two parts, in this order.

### Part 1 — Findings table

A single markdown table, one row per evidenced issue. Include location and impact; if none are found, say so rather than filling the table with preferences. Follow a user-requested format instead when provided.

| Before | After | Why |
| --- | --- | --- |
| `transition: all` animates an unintended size change | List only the intended animated properties using project tokens | Avoid unintended work while preserving the component's behavior |
| Closed menu uses opacity alone and retains focus targets | Preserve semantic hiding and focus lifecycle | Invisible controls remain reachable |
| Reveal content is initially clipped until JS runs | Visible base state; start optional animation after observation | Content remains available without JS |
| Toggle visibly jumps when reversed | Retarget from the current state | Preserve continuity during repeated use |

### Part 2 — Verdict

Group remaining commentary by impact tier, highest first. Omit empty tiers.

1. **Function and accessibility** — hidden content, focus/keyboard regressions, motion preferences.
2. **Responsiveness and continuity** — demonstrated waiting, interruption jumps, or distracting repeated effects.
3. **Performance** — observed issues first; unmeasured risks explicitly labeled.
4. **Optional polish and maintenance** — spatial treatment, token consistency, or aesthetic refinements.

Close with an explicit decision:

- **Recommend changes** — evidenced functional/accessibility regression, serious responsiveness/performance issue, or explicit project requirement violated.
- **No blocking findings** — the reviewed behavior meets project requirements; list any unverified aspects or optional polish separately. Do not imply runtime verification when only code was inspected.

This verdict is advisory unless the project's actual review process defines it as a gate. Continue already authorized fixes without asking for approval again; do not expand scope or bypass host permissions.

Be specific and cite `file:line`. Reuse project values; [STANDARDS.md](STANDARDS.md) offers defaults when a convention is missing. Verify technical claims against the installed version and official sources.

## Guidelines

- Prefer CSS transitions/`@starting-style`/WAAPI for predetermined motion; JS/springs for dynamic, interruptible, gesture-driven motion.
- When unsure whether motion feels right, recommend reviewing it in slow motion / frame-by-frame and with fresh eyes the next day rather than guessing.
