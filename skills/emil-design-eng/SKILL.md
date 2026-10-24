---
name: emil-design-eng
description: Apply Emil Kowalski's interaction craft to UI reviews, component polish and motion decisions within the current project's brand, accessibility and architecture. Use for a specific interface or design-engineering task; treat timing and style preferences as contextual defaults, preserve semantic behavior, and diagnose performance against installed versions.
---

# Design Engineering

## Task and project context

Follow host/tool instructions, the user's task and authorization, and applicable project instructions before these defaults. Inspect existing design tokens, components, accessibility requirements and architecture. For Pavurel website work, load the installed `pavurel-web-design` skill by name when available; otherwise use the project's current design and content documents. Do not assume sibling skill packages exist after selective installation.

Treat a review request as read-only. Complete authorized implementation work without a readiness-only response or a redundant approval stop. Clarify only a material unresolved decision. Examples do not authorize a dependency installation, publication or unrelated redesign.

Preserve content, semantics and keyboard/focus behavior before visual polish. Keep content visible without JavaScript and allow fully static reduced-motion behavior. Use existing native HTML/CSS capabilities before adding a runtime.

## Core Philosophy

### Taste is trained, not innate

Good taste is not personal preference. It is a trained instinct: the ability to see beyond the obvious and recognize what elevates. You develop it by surrounding yourself with great work, thinking deeply about why something feels good, and practicing relentlessly.

When building UI, don't just make it work. Study why the best interfaces feel the way they do. Reverse engineer animations. Inspect interactions. Be curious.

### Unseen details compound

Most details users never consciously notice. That is the point. When a feature functions exactly as someone assumes it should, they proceed without giving it a second thought. That is the goal.

> "All those unseen details combine to produce something that's just stunning, like a thousand barely audible voices all singing in tune." - Paul Graham

Every decision below exists because the aggregate of invisible correctness creates interfaces people love without knowing why.

### Beauty is leverage

People select tools based on the overall experience, not just functionality. Good defaults and good animations are real differentiators. Beauty is underutilized in software. Use it as leverage to stand out.

## Review format

Lead with functional and accessibility findings, then measured performance issues and contextual design suggestions. Include a source location, user impact, proposed change and how it was checked. Distinguish observation from inference; respect the user's requested format.

Use a Before / After / Why table when it makes concrete comparisons clearer:

| Before | After | Why |
| --- | --- | --- |
| `transition: all` | Explicit transition properties | Avoid animating unrelated changes. |
| Hidden controls still focusable | Correct hidden state and focus handling | Visibility and operability must agree. |
| An effect delays frequent input | Immediate feedback, shorter or no motion | Preserve the user's pace. |

## The Animation Decision Framework

Before writing any animation code, answer these questions in order:

### 1. Should this animate at all?

**Ask:** How often will users see this animation?

| Frequency                                                   | Decision                     |
| ----------------------------------------------------------- | ---------------------------- |
| Very frequent (keyboard shortcuts, command palette toggle) | Prefer immediate updates; justify any transition |
| Frequent (hover effects, list navigation)                  | Keep feedback immediate and brief |
| Occasional (modals, drawers, toasts)                        | Animate only a useful state or spatial change |
| Rare/first-time (onboarding, feedback forms, celebrations)  | Can add delight              |

**Do not delay keyboard-initiated actions.** Evaluate motion by purpose and frequency, not input device alone. Keep focus, selection and action feedback immediate; a short orientation transition may still help when it does not hold up the action.

### 2. What is the purpose?

Every animation must have a clear answer to "why does this animate?"

Valid purposes:

- **Spatial consistency**: toast enters and exits from the same direction, making swipe-to-dismiss feel intuitive
- **State indication**: a morphing feedback button shows the state change
- **Explanation**: a marketing animation that shows how a feature works
- **Feedback**: a button scales down on press, confirming the interface heard the user
- **Orientation**: a transition can explain a change when an immediate update would be difficult to follow

If the purpose is just "it looks cool" and the user will see it often, don't animate.

### 3. What easing should it use?

Is the element entering or exiting?
  Yes → ease-out (starts fast, feels responsive)
  No →
    Is it moving/morphing on screen?
      Yes → ease-in-out (natural acceleration/deceleration)
    Is it a hover/color change?
      Yes → ease
    Is it constant motion (marquee, progress bar)?
      Yes → linear
    Default → ease-out

**Reuse the project's easing tokens first.** Built-in CSS curves are valid. Introduce a custom curve only when it improves this interaction; these are examples, not mandatory replacements.

```css
/* Strong ease-out for UI interactions */
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);

/* Strong ease-in-out for on-screen movement */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);

/* iOS-like drawer curve (from Ionic Framework) */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);
```

**Prefer an immediate response for entrances.** Ease-out often suits a dropdown; ease-in can suit an exit or another intentionally accelerating movement. Judge the actual interaction and existing tokens rather than blocking a curve by name.

**Easing references:** Compare curves in [easing.dev](https://easing.dev/) or [easings.co](https://easings.co/) when an existing token does not serve the task.

### 4. How fast should it be?

| Element                  | Duration      |
| ------------------------ | ------------- |
| Button press feedback    | 100-160ms     |
| Tooltips, small popovers | 125-200ms     |
| Dropdowns, selects       | 150-250ms     |
| Modals, drawers          | 200-300ms by default; longer only when justified |
| Marketing/explanatory    | Can be longer |

**Use these ranges as starting points, not release gates.** Keep frequent controls brief. Justify longer travel or explanatory sequences against user benefit, reduced motion and measured behavior.

### Perceived performance

Speed in animation is not just about feeling snappy — it directly affects how users perceive your app's performance:

- Give immediate, honest **pending and completion feedback**; do not imply progress that has not occurred
- A **180ms select** animation feels more responsive than a **400ms** one
- **Instant tooltips** after the first one is open (skip delay + skip animation) make the whole toolbar feel faster

The perception of speed matters as much as actual speed. Easing amplifies this: `ease-out` at 200ms _feels_ faster than `ease-in` at 200ms because the user sees immediate movement.

## Component patterns

For springs, press feedback, popovers, tooltips, interruptible transitions and CSS entry examples, read [component-patterns.md](references/component-patterns.md) when the task needs them. Preserve native semantics and visible no-JavaScript content before applying an effect.

## CSS Transform Mastery

### translateY with percentages

Percentage values in `translate()` are relative to the element's own size. Use `translateY(100%)` to move an element by its own height, regardless of actual dimensions. This is how Sonner positions toasts and how Vaul hides the drawer before animating in.

```css
/* Works regardless of drawer height */
.drawer-hidden {
  transform: translateY(100%);
}

/* Works regardless of toast height */
.toast-enter {
  transform: translateY(-100%);
}
```

Prefer percentages over hardcoded pixel values. They are less error-prone and adapt to content.

### scale() scales children too

Unlike `width`/`height`, `scale()` scales children and leaves the original layout space unchanged. Use it only when those differences are intended. Do not replace layout changes mechanically; protect readable text, hit targets and surrounding flow.

### 3D transforms for depth

`rotateX()`, `rotateY()` with `transform-style: preserve-3d` create real 3D effects in CSS. Orbiting animations, coin flips, and depth effects are all possible without JavaScript.

```css
.wrapper {
  transform-style: preserve-3d;
}

@keyframes orbit {
  from {
    transform: translate(-50%, -50%) rotateY(0deg) translateZ(72px) rotateY(360deg);
  }
  to {
    transform: translate(-50%, -50%) rotateY(360deg) translateZ(72px) rotateY(0deg);
  }
}
```

### transform-origin

Every element has an anchor point from which transforms execute. The default is center. Set it to match where the trigger lives for origin-aware interactions.

## clip-path for Animation

`clip-path` is not just for shapes. It is one of the most powerful animation tools in CSS.

### The inset shape

`clip-path: inset(top right bottom left)` defines a rectangular clipping region. Each value "eats" into the element from that side.

```css
/* Fully hidden from right */
.hidden {
  clip-path: inset(0 100% 0 0);
}

/* Fully visible */
.visible {
  clip-path: inset(0 0 0 0);
}

/* Reveal from left to right */
.overlay {
  clip-path: inset(0 100% 0 0);
  transition: clip-path 200ms ease-out;
}
.button:active .overlay {
  clip-path: inset(0 0 0 0);
  transition: clip-path 2s linear;
}
```

### Tabs with perfect color transitions

Keep one semantic, keyboard-operable tab list. If a clipped overlay is justified, build its visual copy from noninteractive text, mark it `aria-hidden="true"` and `inert`, disable its pointer events and avoid duplicated IDs. The real controls alone own focus, selection and events. A plain color change is a valid simpler solution.

### Hold-to-delete pattern

A clip-path overlay may show hold progress, but it is not an action controller. Preserve cancellation on release, pointer cancellation and focus loss, and provide an accessible click/keyboard confirmation alternative. Do not require a timing-dependent gesture as the only way to perform a destructive action.

### Image reveals on scroll

Keep images and text visible in base HTML/CSS. An observer may add a one-shot entrance animation after initialization; it must not be the only code that reveals content. Skip optional motion when reduced motion is requested or observation is unavailable.

### Comparison sliders

Overlay two images and clip the top one. Drive the comparison with an accessible labeled control that supports keyboard input as well as dragging. Test `clip-path` performance on target browsers; hardware acceleration is not universal.

## Gesture and Drag Interactions

### Momentum-based dismissal

Don't require dragging past a threshold. Calculate velocity: `Math.abs(dragDistance) / elapsedTime`. If velocity exceeds ~0.11, dismiss regardless of distance. A quick flick should be enough.

```js
const timeTaken = Math.max(1, new Date().getTime() - dragStartTime.current.getTime());
const velocity = Math.abs(swipeAmount) / timeTaken;

if (Math.abs(swipeAmount) >= SWIPE_THRESHOLD || velocity > 0.11) {
  dismiss();
}
```

### Damping at boundaries

When a user drags past the natural boundary (e.g., dragging a drawer up when already at top), apply damping. The more they drag, the less the element moves. Things in real life don't suddenly stop; they slow down first.

### Pointer capture for drag

Once dragging starts, set the element to capture all pointer events. This ensures dragging continues even if the pointer leaves the element bounds.

### Multi-touch protection

Ignore additional touch points after the initial drag begins. Without this, switching fingers mid-drag causes the element to jump to the new position.

```js
function onPress() {
  if (isDragging) return;
  // Start drag...
}
```

### Friction instead of hard stops

Instead of preventing upward drag entirely, allow it with increasing friction. It feels more natural than hitting an invisible wall.

## Performance rules

### Preserve behavior before optimizing

Prefer `transform` and `opacity` for visual effects when they preserve layout and meaning. Their compositing path is often efficient, but not an unconditional guarantee. Layout properties can be justified when content must reflow; measure the affected area.

Do not substitute `opacity: 0` for a real hidden state. Preserve focus management, accessibility-tree visibility and interaction state through appropriate HTML/CSS. Likewise, `scale()` changes child rendering and leaves layout space intact; it is not equivalent to changing height or padding.

### Check inherited updates

Per-frame updates to inherited CSS custom properties can invalidate descendant styles. Profile the actual subtree; localize the update or use an appropriate non-inherited property when supported. Preserve any existing transforms instead of overwriting them blindly.

### Check the installed Motion version

Older advice that Motion `x`, `y` or `scale` always run on the main thread is not a current universal rule. Motion 14.2.0 (2026-10-13) added hardware-accelerated independent transforms. Check the installed package version, animation and browser before changing an API.

The current [React animation guide](https://motion.dev/docs/react-animation), [changelog](https://motion.dev/changelog) and [performance guide](https://motion.dev/docs/performance) describe the supported paths and caveats. Treat acceleration as progressive enhancement, not a guarantee.

### Choose CSS, WAAPI or a library by the task

CSS transitions and WAAPI can run eligible animations off the main thread; a JavaScript library can also hand animation to WAAPI. A `requestAnimationFrame` loop itself runs on the main thread. Choose native HTML/CSS first for simple website interactions; use an existing library for behavior that justifies it.

Keep base content visible and optional animations out of the reduced-motion path. Do not infer that CSS, WAAPI, `clip-path` or a library name alone guarantees smoothness. Measure a demonstrated problem before adding layers, `will-change` or dependencies.

## Accessibility

### prefers-reduced-motion

Remove or reduce nonessential motion, including a fully static state. A short opacity or color transition can remain when useful, but it is not mandatory. Preserve text, selection, focus and status cues independently of movement.

Prefer opt-in motion:

```css
/* Content and controls are visible and functional in the base styles. */
@media (prefers-reduced-motion: no-preference) {
  .state-indicator {
    transition: opacity 160ms ease-out;
  }
}
```

For existing components, override only their motion effects. Do not reset transforms globally: some transforms position content or convey functional state. Ensure enter/exit cleanup and hidden states still complete when a duration is zero.

### Touch device hover states

```css
@media (hover: hover) and (pointer: fine) {
  .element:hover {
    transform: scale(1.05);
  }
}
```

Touch devices trigger hover on tap, causing false positives. Gate hover animations behind this media query.

## The Sonner Principles (Building Loved Components)

These principles from Sonner's component design can inform other components:

1. **Developer experience is key.** No hooks, no context, no complex setup. Insert `<Toaster />` once, call `toast()` from anywhere. The less friction to adopt, the more people will use it.

2. **Good defaults matter more than options.** Ship beautiful out of the box. Most users never customize. The default easing, timing, and visual design should be excellent.

3. **Naming creates identity.** "Sonner" (French for "to ring") feels more elegant than "react-toast". Sacrifice discoverability for memorability when appropriate.

4. **Handle edge cases invisibly.** Pause toast timers when the tab is hidden. Fill gaps between stacked toasts with pseudo-elements to maintain hover state. Capture pointer events during drag. Users never notice these, and that is exactly right.

5. **Preserve state during interruption.** Toasts may be added rapidly. Transitions can retarget smoothly; any other mechanism must also handle a mid-animation update without restarting visibly.

6. **Build a great documentation site.** Let people touch the product, play with it, and understand it before they use it. Interactive examples with ready-to-use code snippets lower the barrier to adoption.

### Cohesion matters

Sonner's animation feels satisfying partly because the whole experience is cohesive. The easing and duration fit the vibe of the library. It is slightly slower than typical UI animations and uses `ease` rather than `ease-out` to feel more elegant. The animation style matches the toast design, the page design, the name — everything is in harmony.

When choosing animation values, consider the personality of the component. A playful component can be bouncier. A professional dashboard should be crisp and fast. Match the motion to the mood.

### The opacity + height combination

When items enter and exit a list (like Family's drawer), the opacity change must work well with the height animation. This is often trial and error. There is no formula — you adjust until it feels right.

### Review your work the next day

Review animations with fresh eyes. You notice imperfections the next day that you missed during development. Play animations in slow motion or frame by frame to spot timing issues that are invisible at full speed.

### Asymmetric enter/exit timing

Pressing should be slow when it needs to be deliberate (hold-to-delete: 2s linear), but release should always be snappy (200ms ease-out). This pattern applies broadly: slow where the user is deciding, fast where the system is responding.

```css
/* Release: fast */
.overlay {
  transition: clip-path 200ms ease-out;
}

/* Press: slow and deliberate */
.button:active .overlay {
  transition: clip-path 2s linear;
}
```

## Stagger animations

Use a short stagger only when it improves reading order or explains a small set of related items. Showing all items immediately is often preferable, especially for frequent tasks and long lists. Never delay access to essential information or controls.

Implement an optional entrance as a one-shot lifecycle:

1. Keep the base content visible and operable. Skip the effect for reduced motion, an already focused item or an unavailable enhancement API.
2. Start only a justified entrance, with a short bounded total delay; preserve existing layout transforms.
3. When focus enters, the animation completes or is canceled, permanently clear its entrance trigger and expose the final visible state. Later focus-out or motion-preference changes must not replay the entrance.
4. Clean up listeners when the view is disposed. Essential content must not depend on animation completion or cleanup to become available.

Do not merely toggle `animation: none` with `:focus-within` while leaving the entrance trigger set: focus leaving can restart the animation and make the item disappear again. Leave long reading content and frequently used controls immediate.

## Debugging Animations

### Slow motion testing

Play animations at reduced speed to spot issues invisible at full speed. Temporarily increase duration to 2-5x normal, or use browser DevTools animation inspector to slow playback.

Things to look for in slow motion:

- Do colors transition smoothly, or do you see two distinct states overlapping?
- Does the easing feel right, or does it start/stop abruptly?
- Is the transform-origin correct, or does the element scale from the wrong point?
- Are multiple animated properties (opacity, transform, color) in sync?

### Frame-by-frame inspection

Step through animations frame by frame in Chrome DevTools (Animations panel). This reveals timing issues between coordinated properties that you cannot see at full speed.

### Test on real devices

For touch interactions, use a physical target device when an authorized setup is available. Emulation and source inspection provide partial evidence; state which device behaviors remain unverified. Do not assume the user has a separate computer or expose a development server just to satisfy this check. Complete the checks available in the current environment.

## Review checklist

| Check | Response |
| --- | --- |
| Hidden or clipped content remains focusable | Correct semantics and focus before animating. |
| Essential content depends on JavaScript to become visible | Keep visible base HTML/CSS; enhance after initialization. |
| Reduced-motion preference or rapid keyboard input is obstructed | Remove or reduce the effect; keep state and focus feedback. |
| `transition: all` changes unrelated properties | Specify only the intended properties. |
| An entrance, easing, duration or stagger distracts | Use project tokens, simplify or remove it; explain the observed impact. |
| An anchored popover moves from the wrong place | Align the origin with its trigger; centered dialogs have different needs. |
| Repeated actions restart or block an animation | Retarget from current state without delaying the action. |
| Hover assumptions fail on touch | Gate hover effects by capability and preserve touch/keyboard alternatives. |
| Motion or a paint-heavy effect drops frames | Check versions, profile the affected case, then make a targeted change. |

Do not treat taste preferences as automatic merge blockers. Report exactly what was inspected, run or observed and any remaining device/browser limitations.
