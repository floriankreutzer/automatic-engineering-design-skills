# Animation Audit Playbook

The eight audit categories and useful starting values, informed by Emil Kowalski's design engineering philosophy ([emilkowal.ski](https://emilkowal.ski/)). Follow host/user scope and project requirements; retain existing tokens over these defaults. For Pavurel marketing website work, use the installed `pavurel-web-design` skill when available. Check function and accessibility before performance and polish. A stylistic difference alone is not a defect.

## Contents

1. [Purpose and frequency](#1-purpose--frequency)
2. [Easing and duration](#2-easing--duration)
3. [Physicality and origin](#3-physicality--origin)
4. [Interruptibility](#4-interruptibility)
5. [Performance](#5-performance)
6. [Accessibility](#6-accessibility) — check this first
7. [Cohesion and tokens](#7-cohesion--tokens)
8. [Missed opportunities](#8-missed-opportunities)

## 1. Purpose & frequency

Every animation must answer "why does this animate?" — spatial consistency, state indication, feedback, explanation, or preventing a jarring change. "It looks cool" on a frequently-seen element is not a purpose.

| Frequency | Decision |
| --- | --- |
| Very frequent (e.g. 100+ times/day; command palette toggle) | Prefer instant changes; retain brief feedback only when it helps |
| Tens of times/day (hover effects, list navigation) | Remove or drastically reduce |
| Occasional (modals, drawers, toasts) | Standard animation |
| Rare / first-time (onboarding, feedback, celebrations) | Can add delight |

Hunt for unnecessary waiting and repeated distraction. Keyboard initiation is not itself a defect; preserve immediate focus/state feedback for every input method. Removing unnecessary motion is often the strongest improvement.

## 2. Easing & duration

Decision order for easing:

- Entering or exiting → **`ease-out`** (starts fast, feels responsive)
- Moving / morphing on screen → **`ease-in-out`**
- Hover / color change → **`ease`**
- Constant motion (marquee, progress) → **`linear`**
- Default → **`ease-out`**

Default to responsive feedback. A slow onset may feel delayed, but `ease-in` can fit intentional acceleration or an exit. Built-in easing is valid. Preserve project tokens; these stronger curves are optional starting points when no convention exists:

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);        /* strong ease-out for UI */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);    /* strong ease-in-out for on-screen movement */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);     /* iOS-like drawer curve */
```

Starting duration ranges — routine UI often works around 150–250ms; larger drawers can justify 300–500ms. Keep controls usable during the transition:

| Element | Duration |
| --- | --- |
| Button press feedback | 100–160ms |
| Tooltips, small popovers | 125–200ms |
| Dropdowns, selects | 150–250ms |
| Modals, drawers | 200–500ms |
| Marketing / explanatory | Can be longer |

Hunt for an observed delayed response, unnecessarily repeated tooltip delay, or motion that blocks progress. A duration above 300ms or a particular easing name is a review prompt, not a finding by itself.

## 3. Physicality & origin

- **Prefer subtle entrances when useful.** A small scale (`0.9–0.97`) plus opacity, a pure fade, or an instant state can all work. Evaluate large scaling against purpose and comfort.
- **Popovers/dropdowns/tooltips scale from their trigger**, not center:
  ```css
  .popover { transform-origin: var(--transform-origin); } /* Base UI */
  ```
  **Modals are exempt** — they appear centered; `transform-origin: center` is correct there. Do not report it.
- **Press feedback**: preserve clear active/focus styling. A subtle `scale(0.97)` with a short transition is one option, not a requirement for every control.

Hunt for confusing spatial changes, distracting scale, or missing feedback. Pure fades and nonanimated controls are valid when state and operation are clear.

## 4. Interruptibility

CSS transitions are a useful default for retargeting states. Restarted entrance keyframes can jump; keyframes or WAAPI are also valid when the implementation handles interruption continuously. Check behavior rather than banning an API.

- Entry without JS: consider `@starting-style`; an instant visible base state is the fallback. Do not leave content hidden awaiting hydration.
- Springs can preserve velocity for gestures; use them when this behavior is needed.
- Spring configs, Apple-style (recommended): `{ type: "spring", duration: 0.5, bounce: 0.2 }`. Keep bounce subtle (0.1–0.3); reserve visible bounce for drag-to-dismiss and playful moments.
- **Asymmetric timing** can express a deliberate hold followed by a fast response. Symmetry is also valid when it suits the interaction; do not add delay to ordinary button activation.

Hunt for jumps on rapid toggles, lost gesture continuity, or unintended dismissal. Tune velocity/distance thresholds on real devices; no single threshold suits every surface. Preserve a keyboard-operable dismissal/control alternative.

## 5. Performance

- **Prefer `transform` and `opacity` when behavior is preserved.** Layout properties can cost more but may be required for reflow, such as an expanding accordion. `scale()` changes children and retains the original layout slot; it is not equivalent to padding/size changes.
- **Prefer explicit transition properties.** Investigate unintended work caused by `transition: all`.
- **Check the installed Motion version.** Version 14.2.0 added accelerated independent transforms; current `x`/`y`/`scale` and full-transform APIs can be accelerated. Browser and animation conditions still apply. Consult the [changelog](https://motion.dev/changelog), [React transforms](https://motion.dev/docs/react-animation#transforms), and [performance guide](https://motion.dev/docs/performance) before proposing an API change.
- **Profile inherited-variable updates.** They can increase descendant style work; use local transforms where equivalent, not a blanket rewrite of shared styles.
- Eligible CSS/WAAPI work can run off-thread; other work still costs rendering time. Record a trace before claiming dropped frames or guaranteed acceleration.
- Profile blur radius and affected area. There is no universally safe pixel threshold; preserve text legibility.

Hunt for expensive work shown in recordings, unnecessary per-frame renders, repeated layout reads/writes, broad style invalidation, and motion competing with long tasks. Label code-only suspicions as risks needing measurement.

## 6. Accessibility

```css
@media (prefers-reduced-motion: reduce) {
  .element { animation: none; transition: none; } /* retain the visible/state styles */
}
@media (hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference) {
  .element:hover { transform: scale(1.05); } /* touch fires false hovers on tap */
}
```

Reduced motion can mean a gentler effect or **no animation**. Preserve understandable feedback using text, color, focus, and stable state changes. Disable nonessential motion without breaking open/closed state or depending on completion callbacks.

Preserve semantic hiding and focus management: `opacity: 0` alone does not remove focus or accessibility exposure ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/opacity)). Default static marketing content to visible without JavaScript; enhance scroll reveals only after initialization. Respect an authenticated app's documented runtime/fallback requirements. A decorative tab copy must contain no controls/duplicate IDs and be inert/hidden from assistive technology while the real tab list remains fully operable.

Hunt for hidden focus targets, missing announcements/labels, lost focus, motion-preference violations, pointer-only controls, and static content that needs JS solely to reveal it. Do not gate usable content on animation completion. Removing an animation is not removing feedback when the resulting state is still clear.

## 7. Cohesion & tokens

- Motion should match the product's personality — playful can be bouncier, a dashboard stays crisp. Mismatched personality across components is a finding.
- Curves and durations should live as shared tokens. Five hand-typed cubic-beziers that almost match is a consolidation finding.
- A **30–80ms stagger** is an optional group treatment. Simultaneous or instant display is valid; never block interaction or reading for decoration.
- A decorative crossfade may benefit from a small blur, but a simpler fade or instant change can be clearer. Keep essential text legible.

Hunt for unnecessary token duplication, inconsistent personality, and crossfades that obscure content. Do not report absent stagger as a defect.

## 8. Missed opportunities

The additive category — places where motion might help an observed usability issue:

- State changes that teleport (content swaps, layout jumps) where a brief transition would prevent a jarring change.
- Spatially-connected UI (a panel that appears from a trigger) with no motion explaining where it came from.
- Rare moments (first-run, success, celebration) where a restrained effect fits the brand and improves comprehension or feedback.
- `translate` percentages (`translateY(100%)` = element's own height) and `clip-path: inset()` reveals as tools for these — no hardcoded pixel offsets.

Report at most a handful, grounded in actual behavior. An empty list is valid. Preserve the project's no-JS fallback and reduced-motion behavior in every proposal.
