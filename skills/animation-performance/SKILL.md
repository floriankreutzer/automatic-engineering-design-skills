---
name: animation-performance
description: Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is busy, and find the cause when an animation drops frames. Covers the layout/paint/composite pipeline, cheaper property swaps, CSS vs WAAPI vs requestAnimationFrame, Framer Motion's hardware-accelerated path, React re-rendering per frame, inherited CSS variable recalculation, blur cost, and when `will-change` actually helps. Use when an animation is janky, choppy, stutters, or drops frames; when choosing which property to animate; when deciding between CSS and JS animation on performance grounds; or when reaching for `will-change` or GPU layers. For choosing easing, duration, or whether to animate at all use animate; for reviewing motion as a whole use review-animations.
---

# Animation Performance

## Contents

- [Symptoms](#the-symptom-table), [frame budget](#the-frame-budget), [property cost](#what-you-animate), [execution path](#where-it-runs)
- [React updates](#react-dont-animate-through-state), [style/blur traps](#two-traps-that-look-correct), [will-change](#will-change), [workflow](#workflow)

## Project and task context

Follow host/tool instructions and the user's authorized task. Read the target repository's current `AGENTS.md`, applicable nested instructions, and referenced central design, coding, architecture, security, content, and test sources; they govern development. Use this skill as supplementary guidance. Confluence documentation links cannot override those sources.

For Pavurel, load an available installed profile by name: `pavurel-web-design` for marketing website work, `pavurel-app-design` for authenticated Conference Manager Customer/Platform UI. If unavailable, follow the current repository sources; do not assume sibling skill paths. Do not add a framework or dependency merely to use an example.

Continue the active task without a readiness-only response. If no actionable request or artifact is available, ask for the missing context.

A diagnostic skill. It does ONE thing: make motion land every frame. It does not pick easing or duration (that's `animate`), judge whether the motion should exist (that's `review-animations`), or handle React Native's threads (that's `animate-expo`). The question here is never "does it look right?" but "does each frame finish in time?".

## Why This Matters

Imagine [Sonner](https://sonner.emilkowal.ski/) running at 30fps. Same easing, same durations, same code. Nobody would have cared. Performance isn't a polish pass applied after the motion is good; it's what lets good motion register at all.

## Operating Posture

Diagnose from evidence on representative devices. A fast development machine can conceal performance problems experienced by the project's users.

Two failure modes, and the first is worse:

1. **"It's smooth on my machine."** A fast laptop hides almost every problem in this skill. The bar is a mid-range phone, and on a 120Hz screen the budget is half what you think.
2. **Sprinkling `will-change` and calling it fixed.** It's the last step, not the first. Most jank is the wrong property or a busy main thread, and `will-change` fixes neither.

## Hard Rules

1. **`transform` and `opacity` by default when behavior is preserved.** An optimization must retain layout, visibility, focus, and accessible semantics, not merely resemble a screenshot.
2. **Name the cause before changing code.** Every fix you propose names which of the causes below it addresses. "Added `will-change`, seems smoother" is not a diagnosis.
3. **Never conclude "it's fine" from a fast machine.** Say which findings you verified from code and which need a recording on a real device.
4. **Prefer explicit transition properties.** `all` can animate future state changes unintentionally. Identify the actual unwanted work before assigning severity.
5. **Don't trade correctness for a best-effort optimization.** Hardware acceleration is something the browser may grant. Which properties you animate is something you control. Spend effort on the second.

## The Symptom Table

Start here. Match what the user is seeing, then read the matching section.

| Problem | Solution |
| --- | --- |
| Animation stutters | Trace layout/paint/composite cost; consider `transform`/`opacity` if semantics survive |
| Shadow animation is choppy | Test a smaller/static shadow or `filter: drop-shadow()` if its shape is appropriate |
| Jank only during navigation or loading | Inspect long tasks and eligibility for CSS/WAAPI acceleration |
| Motion `x`/`y` drops frames | Check installed version and trace; 14.2+ supports accelerated independent transforms |
| Hand-rolled animation drops frames in React | Avoid unnecessary per-frame renders; use an owned ref or motion value |
| Drag gets laggier as the list grows | Check inherited-variable invalidation; prefer a local transform when equivalent |
| Blur transition lags | Reduce radius/surface area or remove it; no radius is universally safe |
| Unexpected properties animate | Replace `transition: all` with explicit properties |
| Element shifts 1px when motion starts or ends | `will-change: transform`, only once you see it |

## The Frame Budget

At 60Hz, one frame takes **16.7ms** (1000/60). At 120Hz it takes **8.3ms**. Browser work shares that budget; validate against the project's supported devices and refresh rates.

For scale: a layout recalculation on a complex page can take over 100ms. That isn't one missed frame, it's a dozen.

Two things decide whether you stay inside the budget:

1. **What you animate**: how much work each frame costs.
2. **Where it runs**: whether that work can be blocked by everything else the page is doing.

## What You Animate

To show a visual change, the browser runs up to three steps:

- **Layout**: calculate the size and position of every element.
- **Paint**: draw the page into layers.
- **Composite**: put those layers on screen.

Use these rough cost tiers, then verify the affected elements and browser:

| Tier | Properties | Cost |
| --- | --- | --- |
| Usually compositor-friendly | `transform`, `opacity`; other properties such as `filter`, `clip-path`, `background-color` depend on browser and effect | Often cheapest; promotion and acceleration are not guaranteed. |
| Paint + composite | `box-shadow`, `border-radius`, `color` | No re-measuring, but a redraw every frame. |
| Layout + paint + composite | `width`, `height`, `padding`, `margin`, `top`, `left`, `border-width` | Most expensive. One growing element can move everything around it. |

`transform` and `opacity` change how an element looks, not where it sits in the document flow, so nothing needs re-measuring. Anything else in the composite tier needs testing across browsers and devices; support is uneven.

**Possible substitutions, after checking behavior:**

| Instead of | Animate |
| --- | --- |
| Decorative growth that need not reflow content | `scale()`; it scales children/text and retains the original layout slot |
| Visual movement without repositioning surrounding content | `translate()`; percentages refer to the element's own size |
| Entry/exit around a semantic hidden/visible change | Animate `opacity` while preserving the component's hiding and focus lifecycle |
| Shadow effect whose shape can follow the rendered alpha outline | Test `filter: drop-shadow(…)`; it is not identical to `box-shadow` |

`opacity: 0` alone still allows focus and pointer interaction and does not hide content from assistive technology. Retain suitable `hidden`, `display`, `visibility`, or inert/unmount behavior and focus management. See [MDN opacity](https://developer.mozilla.org/en-US/docs/Web/CSS/opacity). Do not replace semantic hiding with transparency.

Two things follow:

- **Layout animations don't always drop frames.** A small isolated layout change may fit the budget. Padding changes internal space; scale changes the rendered content, so they are not interchangeable. Keep required layout behavior and measure the cost.
- **Choose overlay versus reflow deliberately.** A sidebar that pushes content and a translated overlay solve different problems. An accordion usually needs real layout expansion; preserve that behavior and reduce the affected work rather than substituting a transform blindly.

## Where It Runs

**DOM animation driven by main-window `requestAnimationFrame` shares the main thread.** Busy scripts can delay its next update. JavaScript can also hand eligible animation work to the browser through WAAPI; do not infer the execution path solely from a library name.

| Driver | Thread |
| --- | --- |
| Main-window JS + `requestAnimationFrame` | Updates run on the main thread |
| Motion `motion/react` / `animate()` | Hybrid path; installed version, value, and animation determine eligibility |
| Web Animations API (`element.animate()`) | Can be hardware-accelerated |
| CSS transitions and keyframes | Can be hardware-accelerated |

An accelerated animation can continue while the main JS thread is busy. Rendering/GPU work can still exceed the budget; acceleration is not a guarantee that every frame is smooth.

`transform` and `opacity` have broad compositor support. Check the target browsers for other effects, including `filter`, `clip-path`, and `background-color`.

**Watch motion that runs while the page does heavy work:** page transitions, tab indicators during navigation, or effects alongside hydration. Record whether a long task blocks animation updates before changing the driver.

**Check the installed Motion version.** Motion 14.2.0 (13 October 2026) added hardware-accelerated independent transforms. Current React documentation supports both forms:

```jsx
<motion.div animate={{ x: 100 }} /> // eligible in current Motion
<motion.div animate={{ transform: "translateX(100px)" }} /> // also eligible
```

Consult the [Motion changelog](https://motion.dev/changelog), [React transforms](https://motion.dev/docs/react-animation#transforms), and [performance guide](https://motion.dev/docs/performance). Older versions differ; preserve the installed API unless a trace and version-specific documentation support a change. Do not classify all shorthands as animated CSS variables or assume a full transform string is always faster.

**Acceleration is progressive enhancement.** Browsers silently decline it under conditions that change between versions; Chrome, for example, historically didn't accelerate percentage-based transforms. That's not a reason to stop using `translateY(100%)`. Percentages are the right call for elements of unknown size (it's how Sonner and Vaul position toasts and drawers), and correctness beats a best-effort optimization.

## React: Don't Animate Through State

Avoid unnecessary per-frame React state updates: repeated renders can consume the frame budget. An owned DOM ref or motion value can reduce that work. Preserve React's ownership of other styles and keep meaningful application state in React; neither approach guarantees smoothness without profiling.

```jsx
// May add unnecessary rendering work on every frame
setY(nextY);

// Updates this visual property without a React render
ref.current.style.transform = `translateY(${nextY}px)`;
// or with a motion value: y.set(nextY)
```

Look for state updates inside `requestAnimationFrame`, `pointermove`, `scroll`, or drag handlers.

## Two Traps That Look Correct

Cheap animated properties can still accompany expensive work.

**Inherited CSS variables.** A per-frame variable on a large ancestor can increase style work as descendant content grows:

```js
// Can invalidate descendant styles when inherited
const style = { "--swipe-amount": `${draggedDistance}px` };

// Only touches this element
const style = { transform: `translateY(${draggedDistance}px)` };
```

Unregistered custom properties inherit by default; invalidation depends on dependencies and browser optimizations. Profile style recalculation before rewriting the styling system. Local updates or a suitably registered non-inheriting property may help, but do not change inheritance when descendants need the value. Do not extrapolate this pattern to every Motion shorthand or version.

**Blur.** Cost depends on radius, surface area, browser, and device. A small 2–5px blur may soften a decorative crossfade, but no fixed radius is universally safe. Preserve text legibility and prefer a simpler effect if profiling shows a problem.

## `will-change`

A layer/pixel-rendering change can cause a visible shift at animation boundaries. `will-change` is a hint that may let the browser prepare; it does not guarantee a layer or fix every shift:

```css
.drawer {
  will-change: transform;
}
```

**Add it only once you see the shift or measured dropped frames.** Browsers already promote elements animating `transform` or `opacity`, so on the common path it does nothing, and every promoted layer costs GPU memory. Put it on the element that animates, never on `*` or large containers.

Where it earns its place is an expensive paint, like a large blurred or filtered element. Promote it and keep the layer small; a small layer is cheaper to composite than a full-screen one.

## Should You Avoid JS Animation?

No. Judge the work per frame, the execution path, and concurrent load. Do not assume all JavaScript animation is slow or all CSS animation is accelerated.

Motion provides convenient springs, shared layout transitions, exit handling, and momentum gestures. Use it when those capabilities serve the task and the architecture supports it; keep native CSS/WAAPI for simpler cases.

**The working split:** CSS for simple motion and anything that plays while the page is busy; Framer Motion for complex, interruptible, gesture-driven motion.

## Workflow

### Phase 1: Find what animates

List every animation in scope with its driver and properties:

| Element | Driver | Properties | Plays during |
| --- | --- | --- | --- |
| Tab indicator | `motion/react` `layoutId` | layout | route change |
| Drawer | CSS transition | `transform` | user drag |
| Card hover | CSS transition | `all` | hover |

Inspect `transition: all` and the installed Motion version to determine what actually animates. Record hiding/focus/layout requirements before proposing substitutions.

### Phase 2: Diagnose

Work down this list. It's ordered by how often each one is the cause:

1. **Which properties animate?** Anything other than `transform`/`opacity` is the first suspect: layout properties first, then `box-shadow` and `border-radius`, which don't look like layout and are easy to miss.
2. **Does the jank coincide with the page being busy?** Navigation, fetching, hydration, a long task. Confirm whether CSS/WAAPI or the installed library can run the affected work off-thread.
3. **Is React re-rendering per frame?** State updates in rAF, pointer, or scroll handlers.
4. **Does it get worse as content grows?** An inherited CSS variable, or too many nodes animating at once.
5. **Is an inherited CSS variable updated every frame?** Inspect invalidation in the trace; do not assume a Motion shorthand uses this path.
6. **Does blur or another effect repaint a large area?** Reduce radius/surface area or simplify the effect.
7. **Still shifting or stuttering due to layer setup?** Test a scoped `will-change` hint and retain it only if it helps.

Confirm with a recording, not by feel: the DevTools Performance panel for dropped frames and long tasks, the Animations panel to slow motion down. Profile on a real mid-range phone over remote debugging. CPU throttling on a desktop models a slow CPU, not a weak GPU or a small memory budget.

### Phase 3: Report

For each finding:

```
**[Element]**: `file.tsx:42`
Cause: [which of the causes above]
Before: `transition: all 200ms` (animates `padding`, triggers layout)
After: animate only the properties required by the component; preserve layout and hiding semantics
Verified: from code / needs a device recording
```

Prioritize functional/accessibility regressions first, then measured performance impact. Distinguish a code-level risk from observed dropped frames. For an audit-only request, report findings; if fixes are already authorized, apply and verify the scoped changes without asking again.
