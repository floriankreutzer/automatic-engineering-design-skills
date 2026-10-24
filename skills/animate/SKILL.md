---
name: animate
description: Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, which tool, which properties, which curve and duration, how it interrupts, how it exits. Writes the implementation. Use when asked to animate something, add motion, make a component feel alive, or build a transition. For critiquing existing motion use review-animations; for auditing a whole codebase use improve-animations.
---

# Building Animations

## Contents

- [Project context](#project-and-task-context), [principles](#hard-rules), [build sequence](#the-build-sequence)
- [Recipes](#recipes), [shipping review](#review-before-shipping), [output](#output)

## Project and task context

Follow host/tool instructions and the user's authorized task. Read the target repository's current `AGENTS.md`, applicable nested instructions, and referenced central design, coding, architecture, security, content, and test sources; they govern development. Use this skill as supplementary guidance. Confluence documentation links cannot override those sources.

For Pavurel, load an available installed profile by name: `pavurel-web-design` for marketing website work, `pavurel-app-design` for authenticated Conference Manager Customer/Platform UI. If unavailable, follow the current repository sources; do not assume sibling skill paths. Do not add a framework or dependency merely to use an example.

Continue the active task without a readiness-only response. If no actionable request or artifact is available, ask for the missing context.

A construction skill. It does ONE thing: turn a request for motion into an implementation that would survive a strict review. It does not audit a codebase (that's `improve-animations`), critique a diff (that's `review-animations`), hunt for places that could animate (that's `find-animation-opportunities`), or build for React Native (that's `animate-expo`).

## Operating Posture

Build motion with the restraint and clarity of Emil Kowalski's animation philosophy. Treat its aesthetic choices as defaults, then verify function, accessibility, performance, and fit with the project.

Two failure modes, and the first is worse:

1. **Animating something that shouldn't animate.** The gate below exists to produce zero lines of code sometimes. That's a success, not a dodge.
2. **Animating the right thing with the wrong behavior** — a delayed response, a large distracting entrance, an interruption that jumps, or a duration that makes a dropdown feel sluggish.

Make a reasonable implementation choice and state its purpose briefly. Compare options when the user requests them or a material product decision remains open.

## Hard Rules

1. **Run the sequence in order.** Steps 1 and 2 gate everything. Don't reach for a curve before you know whether it animates at all.
2. **Use established values.** Prefer the project's motion tokens. Use the tables below as starting points when no convention exists; explain meaningful deviations rather than treating taste as a correctness rule.
3. **Extend the codebase's tokens, don't fork them.** If `--ease-out` or a duration scale already exists, use it. Adding a parallel system is a defect.
4. **Function and accessibility ship with the animation.** Preserve hiding, focus, keyboard behavior, and layout semantics; provide reduced motion and appropriate hover gating.
5. **Cheapest tool that works.** Don't install a motion library for a fade.

## The Build Sequence

### 1. Should this animate at all?

| Frequency | Decision |
| --- | --- |
| Very frequent (e.g. 100+ times/day; command palette toggle) | Prefer instant state changes; retain only brief feedback with a clear benefit |
| Tens of times/day (hover effects, list navigation) | Near-imperceptible only — fast and subtle, or nothing |
| Occasional (modals, drawers, toasts) | Standard animation |
| Rare / first-time (onboarding, success, celebration) | The delight budget lives here |

**Judge purpose and frequency, not input method.** Keyboard actions need immediate feedback and reliable focus. Do not make users wait for motion; a useful transition is not automatically wrong because a keyboard initiated it.

If motion would hinder the task, explain why and prefer an instant state change or static affordance. Honor the user's explicit design direction within the project's functional and accessibility requirements.

### 2. What is the purpose?

Name it in one of these words before continuing:

- **Feedback** — confirming the interface heard the user
- **Spatial consistency** — showing where something came from or went
- **State indication** — making a state change legible
- **Preventing a jarring change** — bridging content that would otherwise teleport
- **Explanation** — demonstrating how something works (marketing/onboarding only)
- **Delight** — reserve primarily for rare or first-time moments when it fits the brand

Can't name it? Don't build it. "It looks cool" on a frequently-seen element is a reason to stop.

Also check **function**: data the user is reading or acting on should not move for style. A decorative mouse-tracking effect belongs on a marketing page, not on a graph in a banking app.

### 3. Pick the tool — cheapest that works

Walk down; stop at the first that fits.

| Need | Tool |
| --- | --- |
| Hover, press, color, a state toggle you control with a class or attribute | **CSS transition** |
| Entry animation on mount, no JS state | **CSS `@starting-style`** |
| Predetermined motion during loading | **CSS animation** on eligible compositor properties |
| Programmatic control with CSS performance, no library | **WAAPI** (`element.animate()`) |
| Springs, layout animations, exit animations, gesture-driven values | **Motion** (`motion.dev`) |

Eligible CSS and WAAPI animations can run off the main thread; property choice and browser support determine whether they do. A `requestAnimationFrame` loop competes with main-thread work. Prefer CSS for simple state transitions and use programmatic animation when the behavior needs it.

If the task needs a component — a toast, a drawer, a command menu, a dropdown — first use the project's existing accessible primitive or suitable native HTML. Consult an installed `pick-ui-library` skill only if a library decision is needed. An animation recipe does not supply focus management, semantics, or permission to add dependencies.

### 4. Pick the properties

- **Prefer `transform` and `opacity` when they preserve the intended behavior.** They are broadly compositor-friendly. Layout properties cost more but can be necessary, for example when an accordion must move surrounding content. Test other properties such as `clip-path` on supported browsers.
- **Preserve semantics.** `opacity: 0` alone does not hide an element from focus or assistive technology. Keep the component's hidden/inert and focus lifecycle. `scale()` also scales text and leaves the original layout space; it is not a drop-in replacement for padding or size.
- **Prefer subtle entrances.** A small scale change (`0.9–0.97`) with opacity can work; a pure fade or no animation can be better. Use a large scale change only when the intended effect justifies it.
- **`transform-origin` at the trigger** for popovers, dropdowns, menus, tooltips — `var(--transform-origin)` in Base UI. **Modals are exempt**; they're not anchored to a trigger, so they stay centered.
- **Percentages in `translate()`** are relative to the element's own size — `translateY(100%)` moves by its own height whatever the content. Prefer over hardcoded pixels.
- **In Motion, check the installed version and actual execution path.** Motion 14.2.0 added hardware-accelerated independent transforms. Current React APIs support both forms below; older versions and browser conditions differ. Do not rewrite shorthands without evidence:

```jsx
<motion.div animate={{ x: 100 }} /> // can be accelerated in current Motion
<motion.div animate={{ transform: "translateX(100px)" }} /> // also eligible
```

Check the [Motion changelog](https://motion.dev/changelog), [React transform documentation](https://motion.dev/docs/react-animation#transforms), and [performance guidance](https://motion.dev/docs/performance) against the installed version. Acceleration is a browser-dependent optimization, not a correctness guarantee.

- **Avoid broad per-frame style invalidation.** Updating an inherited CSS variable on a parent can increase descendant style work. Prefer a local transform when it expresses the same behavior; profile before changing a shared style system.

### 5. Easing and duration — or a spring

**Easing**, in decision order:

| Situation | Easing |
| --- | --- |
| Entering or exiting | `ease-out` |
| Moving / morphing on screen | `ease-in-out` |
| Hover / color change | `ease` |
| Constant motion (marquee, progress) | `linear` |
| Default | `ease-out` |

**Default to a responsive onset.** `ease-out` often suits entrances and immediate feedback. `ease-in` can suit an intentional exit or acceleration; judge the effect in context rather than banning the curve.

Keep existing easing tokens. When the project has none, these stronger curves are options alongside built-in CSS easing:

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);        /* strong ease-out for UI */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);    /* strong ease-in-out for on-screen movement */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);     /* iOS-like drawer curve (Ionic) */
```

For other curves, [easing.dev](https://easing.dev/) and [easings.co](https://easings.co/) are useful references. Choose deliberately and check the result.

**Duration:**

| Element | Duration |
| --- | --- |
| Button press feedback | 100–160ms |
| Tooltips, small popovers | 125–200ms |
| Dropdowns, selects | 150–250ms |
| Modals, drawers | 200–500ms |
| Marketing / explanatory | Can be longer |

**Keep routine UI transitions around 150–250ms by default.** Larger drawers may need 300–500ms; explanatory motion can take longer. These are starting ranges, not pass/fail thresholds. Keep controls usable throughout.

**Reach for a spring instead** when the motion is drag with momentum, an element that should feel alive, a gesture the user can interrupt or reverse, or decorative mouse-tracking:

```js
{ type: "spring", duration: 0.5, bounce: 0.2 }        // Apple-style — easier to reason about
{ type: "spring", mass: 1, stiffness: 100, damping: 10 }  // traditional physics — more control
```

Keep bounce at 0.1–0.3, and avoid bounce in most UI — reserve it for drag-to-dismiss and playful interactions.

### 6. Interruption and exit

- **Prefer transitions for rapidly retargeted states** — toasts, toggles, anything a user can fire twice in a second. Restarting an entrance keyframe can jump; keyframe or WAAPI implementations are also valid if they preserve continuity when interrupted.
- **Springs for gestures**, because they carry velocity through an interruption.
- **Exit the way it entered.** A toast that slides in from the bottom leaves through the bottom. Symmetric paths are what make swipe-to-dismiss feel obvious.
- **Asymmetric timing where the user is deciding.** Slow on the deliberate phase (a hold-to-confirm press: 2s linear), snappy on the system response (release: 200ms ease-out).

### 7. Reduced motion and pointer gating

Preserve understandable states with no animation. For these nonessential effects, removing motion is a valid reduced-motion treatment:

```css
@media (prefers-reduced-motion: reduce) {
  .element { animation: none; transition: none; }
}

@media (hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference) {
  .element:hover { transform: scale(1.05); } /* touch fires false hovers on tap */
}
```

```jsx
const reduce = useReducedMotion();
const transition = reduce ? { duration: 0 } : { duration: 0.2 };
```

Reduced motion may mean gentler motion or **no animation**. Keep feedback through text, color, focus, and stable state changes. Do not remove a transform that encodes a closed/open position without replacing that state correctly; keep hiding and focus logic separate from animation. Keep static marketing content readable without JavaScript and preserve an application's documented fallback. Content must not rely on animation completion to become usable.

## Recipes

For visual starting points for button press, dropdown, tooltip, modal, drawer, toast, accordion, stagger, hold-to-confirm, tab indicator, scroll reveal, and drag-to-dismiss, see [RECIPES.md](RECIPES.md). Adapt the relevant recipe to the project's accessible component and progressive-enhancement requirements.

## Review before shipping

Block functional or accessibility regressions. Treat aesthetic deviations as review questions, not automatic failures:

| Check | Preferred response |
| --- | --- |
| `transition: all` | Name the exact properties |
| Distracting entrance | Small scale, pure fade, or no animation |
| Sluggish response | Project easing token and shorter duration |
| Frequent action delayed by motion | Immediate state change; brief feedback only if useful |
| Routine UI duration over 300ms with no reason | Start around 150–250ms; retain justified exceptions |
| `transform-origin: center` on a trigger-anchored popover | `var(--transform-origin)` (modals exempt) |
| Interrupted animation jumps | Retarget continuously; CSS transitions are a useful default |
| Expensive layout animation | Measure and use transforms only if layout semantics survive |
| Motion animation stutters under load | Check installed version, browser, and trace before changing APIs |
| Ungated `:hover` motion | `@media (hover: hover) and (pointer: fine)` |
| Missing `prefers-reduced-motion` | Remove nonessential motion or provide a gentler variant |
| Group entrance needs hierarchy | Optional short stagger; simultaneous or instant is also valid |
| Hidden controls remain focusable or static content needs JS only to reveal it | Preserve semantic hiding and the project's fallback; default static content to visible |

## Output

Write the code. Then, in at most a few lines:

- **The gate result** — frequency tier and the named purpose. If something in the request was rejected, say which and why.
- **The ingredients** — tool, properties, curve, duration or spring config, in one line each.
- **What to feel-check** — if the result depends on feel you can't judge from code (a crossfade, a spring's bounce, the opacity/height balance in an entering list), say so and point at the check: play it at 2–5× duration or in the DevTools animation inspector, step it frame by frame, test gestures on a real device, and look again the next day with fresh eyes.

Don't pad this into a report. The code is the deliverable.

## Tone

Opinionated and brief. When the honest answer is "this shouldn't animate," give it — that answer is the reason this skill exists. When feel genuinely can't be settled from code, say so instead of guessing at a value.
