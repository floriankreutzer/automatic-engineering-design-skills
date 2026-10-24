# Animation Recipes

Visual starting points for common cases. Adapt them to the user's task, project architecture, design tokens, and existing accessible components. For Pavurel marketing website work, follow the installed `pavurel-web-design` skill when available and the project's documented rules.

Curves use `--ease-out`, `--ease-in-out`, and `--ease-drawer` as illustrative tokens; retain the project's values. These fragments do not implement roles, focus trapping/restoration, keyboard controls, dismissal, or hiding. Preserve those behaviors in the component. Neither opacity nor an off-screen transform alone makes a closed component noninteractive or inaccessible to assistive technology.

For every recipe, provide reduced motion, including no animation when appropriate. Disable nonessential transitions/animations without discarding open/closed state. Keep static marketing content readable without JavaScript and preserve an application's documented fallback; do not gate usable content on animation completion. Do not introduce a library just to reproduce a recipe.

## Contents

- [One-shot entrance lifecycle](#one-shot-entrance-lifecycle)
- [Button press](#button-press), [popover](#dropdown-popover-menu-select), [tooltip](#tooltip), [modal](#modal)
- [Drawer](#drawer--sheet), [toast](#toast), [accordion](#accordion--collapse), [stagger](#stagger-a-group-entrance)
- [Hold to confirm](#hold-to-confirm), [tab indicator](#tab-indicator-with-a-color-transition), [scroll reveal](#scroll-reveal)
- [Drag to dismiss](#drag-to-dismiss), [crossfade](#masking-a-crossfade-that-wont-settle), [WAAPI](#programmatic-without-a-library)

## One-shot entrance lifecycle

Use this helper for the stagger and scroll-reveal examples below. The base CSS is visible; never put `data-entering` in the initial HTML. Consume each element once and permanently remove the trigger on completion, cancellation, focus, or a motion-preference change. A CSS-only `:focus-within { animation: none }` override is insufficient: focusout can restart the entrance.

```js
const playedEntrances = new WeakSet();
const entranceMotionPreference = window.matchMedia('(prefers-reduced-motion: reduce)');

function playEntranceOnce(element, animationName) {
  if (playedEntrances.has(element)) return () => {};
  playedEntrances.add(element);
  element.removeAttribute('data-entering');

  if (entranceMotionPreference.matches || element.matches(':focus-within')) {
    return () => {};
  }

  function finish() {
    element.removeAttribute('data-entering');
    element.removeEventListener('animationend', onAnimationFinished);
    element.removeEventListener('animationcancel', onAnimationFinished);
    element.removeEventListener('focusin', finish);
    entranceMotionPreference.removeEventListener('change', finish);
  }

  function onAnimationFinished(event) {
    if (event.target === element && event.animationName === animationName) finish();
  }

  element.addEventListener('animationend', onAnimationFinished);
  element.addEventListener('animationcancel', onAnimationFinished);
  element.addEventListener('focusin', finish);
  entranceMotionPreference.addEventListener('change', finish);
  element.setAttribute('data-entering', '');

  // If CSS animation is disabled/unavailable, do not leave a deferred trigger.
  const names = window.getComputedStyle(element).animationName.split(',').map((name) => name.trim());
  if (!names.includes(animationName)) finish();

  return finish; // Call on component teardown if the view can be disposed mid-animation.
}
```

Skipping an effect for reduced motion or existing focus also consumes that entrance. Later focusout, preference toggles, repeated observation, or duplicate calls cannot replay it. Use a component's existing lifecycle to invoke the returned cleanup when it unmounts.

---

## Button press

An option for pressable elements that need additional feedback. Keep the existing active/focus treatment when it already communicates the state clearly.

```css
.button {
  transition: transform 160ms var(--ease-out);
}

.button:active {
  transform: scale(0.97);
}
```

`scale()` scales children too — the label and icons come along, which is what makes it read as a physical press.

No hover gating is needed for `:active`; it can respond to touch. Gate hover-only motion separately, preserve a clear `:focus-visible` treatment, and omit the scale effect for reduced motion if appropriate.

---

## Dropdown, popover, menu, select

Scales out of its trigger, not out of thin air.

```css
.popover {
  transform-origin: var(--transform-origin); /* Base UI supplies this */
  transition:
    opacity 200ms var(--ease-out),
    transform 200ms var(--ease-out);
}

.popover[data-starting-style],
.popover[data-ending-style] {
  opacity: 0;
  transform: scale(0.95);
}
```

The `transform-origin` is the whole point — the panel should look like it came out of the thing you clicked.

---

## Tooltip

Same shape as a popover, faster, plus the detail most implementations miss.

```css
.tooltip {
  transform-origin: var(--transform-origin);
  transition:
    transform 125ms var(--ease-out),
    opacity 125ms var(--ease-out);
}

.tooltip[data-starting-style],
.tooltip[data-ending-style] {
  opacity: 0;
  transform: scale(0.97);
}

/* Once one tooltip is open, neighbours open instantly */
.tooltip[data-instant] {
  transition-duration: 0ms;
}
```

The initial delay prevents accidental activation. After that, skipping both the delay and the animation makes the whole toolbar feel faster.

---

## Modal

The one popover that stays centered.

```css
.modal {
  transform-origin: center; /* exempt — not anchored to a trigger */
  transition:
    opacity 250ms var(--ease-out),
    transform 250ms var(--ease-out);
}

.modal[data-starting-style],
.modal[data-ending-style] {
  opacity: 0;
  transform: scale(0.96);
}

.backdrop {
  transition: opacity 250ms var(--ease-out);
}
```

Animate the backdrop's opacity alongside it so they read as one surface.

---

## Drawer / sheet

```css
.drawer {
  transform: translateY(0);
  transition: transform 500ms var(--ease-drawer);
}

.drawer[data-closed] {
  transform: translateY(100%);
}
```

This translates the visual surface; it does not implement semantic hiding. The component must also handle focus, modal behavior where applicable, and whether the closed drawer is present or inert. The 500ms duration is an option for a larger sheet, not a default for all UI.

Add drag and it becomes a gesture problem — see **Drag to dismiss** below.

---

## Toast

```css
.toast {
  opacity: 1;
  transform: translateY(0);
  transition:
    opacity 400ms ease,
    transform 400ms ease;

  @starting-style {
    opacity: 0;
    transform: translateY(100%);
  }
}
```

- `ease` rather than `ease-out`, slightly slower than typical UI: Sonner reads as elegant partly because its motion is tuned to the component's personality rather than to the generic UI budget.
- Without `@starting-style`, a visible toast with no entrance animation is a useful fallback. In an existing React component, a mount flag is another option if it cannot leave content hidden before hydration:

```jsx
useEffect(() => { setMounted(true); }, []);
// <div data-mounted={mounted}>
```

When toasts stack and the list reflows, the opacity change has to work against the height change. There's no formula for that pair — adjust until it feels right, then check it again the next day.

---

## Accordion / collapse

```css
.content {
  overflow: hidden;
  transition:
    height 200ms var(--ease-out),
    opacity 200ms var(--ease-out);
}
```

Keep it short and profile the layout cost. Expansion must move surrounding content, so replacing height with `scaleY()` would change behavior. Prefer an existing accessible disclosure/accordion or native `details`; use its measured dimensions if animation needs them. Preserve hidden-state and keyboard semantics, and avoid adding JavaScript solely to animate an otherwise functional disclosure.

---

## Stagger a group entrance

An optional treatment for a list or grid the user sees occasionally. Simultaneous or instant display is also valid. Avoid delaying forms, navigation, or data the user needs immediately.

```css
.item {
  opacity: 1;
  transform: none;
}

@media (prefers-reduced-motion: no-preference) {
  .item[data-entering] { animation: fadeIn 240ms var(--ease-out) backwards; }
  .item:nth-child(2) { animation-delay: 50ms; }
  .item:nth-child(3) { animation-delay: 100ms; }
  .item:nth-child(4) { animation-delay: 150ms; }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
}
```

Start only the chosen group's items once using the lifecycle helper:

```js
document.querySelectorAll('.stagger-group > .item').forEach((element) => {
  playEntranceOnce(element, 'fadeIn');
});
```

The base state stays visible if JavaScript or animation is disabled. Focus permanently ends the effect on its containing item; focusout cannot replay it. Stagger is decorative; do not block interaction while it plays.

---

## Hold to confirm

For destructive actions where a plain click is too easy to fire by accident.

Use this only when the product calls for a hold interaction. Keep a keyboard-operable confirmation or undo alternative. This CSS visualizes progress; it does not implement the action, its timing, cancellation, or accessible instructions.

```css
.overlay {
  clip-path: inset(0 100% 0 0);
  transition: clip-path 200ms var(--ease-out); /* release: snappy */
}

.button:active .overlay {
  clip-path: inset(0 0 0 0);
  transition: clip-path 2s linear;             /* press: slow and deliberate */
}

.button:active {
  transform: scale(0.97);
}
```

`linear` is correct here — the fill is a progress indicator, and progress shouldn't ease.

---

## Tab indicator with a color transition

When separate color transitions look out of sync, a clipped decorative layer is an option. A single indicator with ordinary color transitions is often sufficient.

Keep one semantic, keyboard-operable tab list. If a visual copy is needed, render noninteractive text/spans in a separate `aria-hidden="true" inert` layer; do not duplicate buttons, tab roles, IDs, handlers, or focus targets. Style that copy as the active state and clip it to the active tab:

```html
<div class="tabs-active-copy" aria-hidden="true" inert>
  <!-- Decorative spans matching the real tab labels; no controls or IDs. -->
</div>
```

```css
.tabs-active-copy {
  pointer-events: none;
  clip-path: inset(0 60% 0 20%); /* driven by the active tab's position */
  transition: clip-path 250ms var(--ease-in-out);
}
```

Text and background then move together. Keep selection state, focus indicators, accessible names, and relationships on the real controls. Disable the clip transition for reduced motion; the active state must still be clear if the decorative layer is absent.

---

## Scroll reveal

Use sparingly on marketing surfaces when it helps explanation. Keep hero copy, calls to action, forms, and frequently used functional UI immediately readable. The base state below is visible; JavaScript only starts an optional animation after an element enters view.

```css
.reveal {
  clip-path: none;
}

@media (prefers-reduced-motion: no-preference) {
  .reveal[data-entering] {
    animation: reveal-in 400ms var(--ease-in-out);
  }
}

@keyframes reveal-in {
  from { clip-path: inset(0 0 100% 0); }
  to { clip-path: inset(0 0 0 0); }
}
```

Run this optional enhancement after the relevant markup and the lifecycle helper above exist:

```js
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      playEntranceOnce(entry.target, 'reveal-in');
      observer.unobserve(entry.target);
    }
  }, { threshold: 0.1 });

  document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));
}
```

With missing/failed JavaScript, unsupported observation, or reduced motion, content stays visible. The helper removes the trigger permanently on focus, completion, cancellation, or a preference change. No animation-end handler is required for basic visibility. Disconnect observers and run active entrance cleanups when an app view is disposed.

---

## Drag to dismiss

The gesture recipe. Springs, not durations, because the user can reverse mid-motion.

```js
// Dismiss on a flick, not just on distance
const timeTaken = Math.max(1, Date.now() - dragStartTime.current);
const velocity = Math.abs(swipeAmount) / timeTaken;

if (Math.abs(swipeAmount) >= SWIPE_THRESHOLD || velocity > 0.11) {
  dismiss();
}
```

```js
// Set transform on the dragged element directly.
// A frequently updated inherited variable can increase descendant style work.
element.style.transform = `translateY(${distance}px)`;
```

Four details that separate a good drag from a bad one:

Keep a visible keyboard-operable dismiss control. The sample velocity is average pixels per millisecond and `0.11` is illustrative; tune distance, velocity, cancellation, and reduced-motion behavior on real devices.

- **Pointer capture** once the drag starts, so it continues when the pointer leaves the element's bounds.
- **Multi-touch protection** — `if (isDragging) return` on new touch points, or switching fingers mid-drag makes the element jump.
- **Damping past boundaries** — dragging beyond a natural edge moves the element less the further it goes. Real things slow before they stop.
- **Friction, not a wall** — allow the over-drag with rising resistance rather than refusing it.

Settle with a spring so an interrupted drag keeps its velocity:

```js
{ type: "spring", duration: 0.5, bounce: 0.2 }
```

---

## Masking a crossfade that won't settle

When two states overlap visibly during a transition and no amount of easing or duration tuning fixes it, blur the seam:

```css
.content {
  transition:
    filter 200ms ease,
    opacity 200ms ease;
}

.content.transitioning {
  filter: blur(2px);
  opacity: 0.7;
}
```

Blur may help a decorative crossfade, but keep essential text legible. Start with a small radius and profile the actual surface; 20px is not a universal safe threshold. Prefer a simpler fade or instant change when blur is costly or distracting.

---

## Programmatic, without a library

When motion needs JavaScript control, WAAPI can avoid a library dependency. Keep the final visible state in CSS and skip nonessential animation for reduced motion:

```js
if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && element.animate) {
  element.animate(
    [{ clipPath: 'inset(0 0 100% 0)' }, { clipPath: 'inset(0 0 0 0)' }],
    { duration: 400, easing: 'cubic-bezier(0.77, 0, 0.175, 1)' }
  );
}
```

Acceleration depends on the property and browser. WAAPI exposes playback controls; implement and verify cancellation/retargeting when needed rather than assuming every new animation is continuous. Honor preference changes during longer effects, and never make visibility or focus depend on completion.
