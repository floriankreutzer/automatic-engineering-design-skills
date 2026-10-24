# Animation Standards Reference

Default values and review guidance informed by Emil Kowalski's design engineering philosophy. Follow host/user scope and project design, accessibility, and architecture requirements. For Pavurel marketing website work, use the installed `pavurel-web-design` skill when available. Prefer existing tokens and documented decisions over these examples. Check function and accessibility before polish; these aesthetic defaults are not release criteria by themselves.

The snippets show visual effects, not complete accessible components. Preserve state, focus, hiding, and reduced-motion behavior. Keep static marketing content readable without JavaScript and respect an application's documented fallback; do not gate usable content on animation completion.

## Contents

- [Frequency](#should-it-animate-frequency-table), [easing](#easing), [duration](#duration), [physicality](#physicality)
- [Springs](#springs), [interruptibility](#interruptibility), [asymmetric timing](#asymmetric-timing)
- [Performance](#performance), [transforms](#transforms--clip-path), [gestures](#gestures--drag)
- [Crossfades](#masking-imperfect-crossfades), [stagger](#stagger), [accessibility](#accessibility)
- [Debugging](#debugging-recommend-in-reviews-when-feel-is-uncertain), [cohesion](#cohesion)

## Should it animate? (frequency table)

| Frequency | Decision |
| --- | --- |
| Very frequent (e.g. 100+ times/day; command palette toggle) | Prefer instant changes; keep brief feedback only when useful |
| Tens of times/day (hover effects, list navigation) | Remove or drastically reduce |
| Occasional (modals, drawers, toasts) | Standard animation |
| Rare / first-time (onboarding, feedback, celebrations) | Can add delight |

**Judge purpose and frequency, not input method.** Keyboard initiation is not a defect. Preserve immediate focus and state feedback, and do not delay operation for an effect.

Valid purposes for motion: spatial consistency, state indication, explanation, feedback, preventing jarring change. "It looks cool" on a frequently-seen element is not valid.

## Easing

Decision order:
- Entering or exiting → **`ease-out`** (starts fast, feels responsive)
- Moving / morphing on screen → **`ease-in-out`**
- Hover / color change → **`ease`**
- Constant motion (marquee, progress) → **`linear`**
- Default → **`ease-out`**

**Default to responsive feedback.** `ease-out` often suits an entrance. `ease-in` can suit intentional acceleration or an exit; assess the observed result rather than the curve name.

Built-in easing and project tokens are valid. If no convention exists, these stronger curves are options:

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);        /* strong ease-out for UI */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1);    /* strong ease-in-out for on-screen movement */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);     /* iOS-like drawer curve (Ionic) */
```

Find other curves at [easing.dev](https://easing.dev/) or [easings.co](https://easings.co/); choose deliberately and verify the interaction.

## Duration

| Element | Duration |
| --- | --- |
| Button press feedback | 100–160ms |
| Tooltips, small popovers | 125–200ms |
| Dropdowns, selects | 150–250ms |
| Modals, drawers | 200–500ms |
| Marketing / explanatory | Can be longer |

**Use the table as starting ranges.** Routine UI often works around 150–250ms; a larger drawer may need 300–500ms. Explanatory motion can take longer. Keep controls usable throughout and avoid repeated tooltip delay during rapid toolbar exploration. A duration alone is not a defect.

## Physicality

- **Prefer subtle entrances.** A small scale (`0.9–0.97`) with opacity, a pure fade, or instant display can all work. Larger scaling needs a clear purpose and comfort check.
- **Origin-aware popovers.** Scale from the trigger, not center:
  ```css
  .popover { transform-origin: var(--transform-origin); } /* Base UI */
  ```
  **Modals are exempt** — they appear centered in the viewport, keep `transform-origin: center`.
- **Button press feedback.** Clear active/focus styling may be sufficient. A subtle `scale(0.97)` with a short transition is an option; it is not mandatory for every control.

## Springs

Springs can convey momentum and preserve continuity during gestures. Physics-based springs settle according to their parameters; some APIs also expose duration/bounce controls. Use them when the interaction needs this behavior, within the existing stack.

```js
// Apple-style (easier to reason about) — recommended
{ type: "spring", duration: 0.5, bounce: 0.2 }

// Traditional physics (more control)
{ type: "spring", mass: 1, stiffness: 100, damping: 10 }
```

Keep bounce restrained; 0.1–0.3 is a starting range where the API supports it. Many business interactions need no bounce. A suitable spring implementation can carry velocity through interruption; verify the behavior rather than assuming every animation does.

For decorative tracking in an existing Motion app, `useSpring` may soften pointer updates. Direct tracking may be correct for functional controls; avoid lagging the user's input. Do not add decorative tracking to essential content.

## Interruptibility

CSS transitions are a useful default for retargetable states. Restarted entrance keyframes may jump; keyframes and WAAPI are also valid when cancellation and continuity are implemented. Verify rapid and reversed interactions.

```css
/* A retargetable transition; keep the project's timing */
.toast { transition: transform 400ms ease; }

/* Restarting this entrance without preserving current progress can jump */
@keyframes slideIn { from { transform: translateY(100%); } to { transform: translateY(0); } }
```

Use `@starting-style` for entry without JS:

```css
.toast {
  opacity: 1; transform: translateY(0);
  transition: opacity 400ms ease, transform 400ms ease;
  @starting-style { opacity: 0; transform: translateY(100%); }
}
```

Fallback: render the final visible state without an entrance effect. An existing React component can use a mount flag if needed, but content must not remain hidden before hydration or when JavaScript fails. The illustrative 400ms toast is a larger expressive transition, not a required duration.

## Asymmetric timing

An intentional hold can have a slow progress phase and a fast reset. Do not delay ordinary activation or require asymmetry everywhere. Retain a keyboard-operable confirmation/undo alternative; CSS progress alone does not implement the action.

```css
.overlay { transition: clip-path 200ms ease-out; }            /* release: fast */
.button:active .overlay { transition: clip-path 2s linear; }  /* press: slow, deliberate */
```

## Performance

- **Prefer `transform` and `opacity` when semantics survive.** Layout properties can cost more but may be required for reflow. Do not replace an expanding accordion with a scale effect that leaves surrounding content unmoved.
- **Profile inherited-variable updates.** Per-frame updates on a large ancestor can increase descendant style work. Prefer a local transform when behavior is equivalent, not a blanket rewrite of shared styles.
  ```js
  element.style.setProperty('--swipe-amount', `${d}px`); // inspect inherited invalidation
  element.style.transform = `translateY(${d}px)`; // local visual update
  ```
- **Check installed Motion version and browser.** Motion 14.2.0 added hardware-accelerated independent transforms. Current React supports both forms below; older versions and animation conditions differ:
  ```jsx
  <motion.div animate={{ x: 100 }} /> // eligible in current Motion
  <motion.div animate={{ transform: "translateX(100px)" }} /> // also eligible
  ```
- Verify [Motion's changelog](https://motion.dev/changelog), [React transforms](https://motion.dev/docs/react-animation#transforms), and [performance guidance](https://motion.dev/docs/performance) against the installed package. Shorthand syntax alone is not a performance finding.
- **Eligible CSS/WAAPI animations can run off-thread.** Main-window rAF shares the main thread; all approaches still have rendering costs. Confirm acceleration and jank in a trace.
- **WAAPI** offers programmatic control without a library. Keep the final visible state in CSS and skip nonessential effects for reduced motion:
  ```js
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches && element.animate) {
    element.animate([{ clipPath: 'inset(0 0 100% 0)' }, { clipPath: 'inset(0 0 0 0)' }],
      { duration: 400, easing: 'cubic-bezier(0.77, 0, 0.175, 1)' });
  }
  ```

  Check cancellation/retargeting and preference changes for longer effects. Do not use an animation completion callback as the only way to expose content.

## Transforms & clip-path

- **`translate` percentages** are relative to the element's own size — `translateY(100%)` moves by the element's height regardless of dimensions (how Sonner/Vaul position toasts/drawers). Prefer over hardcoded px.
- **`scale()` scales children too** (font, icons, content) and retains the original layout slot. It is not equivalent to changing padding or size.
- **3D**: `rotateX/Y` + `transform-style: preserve-3d` for depth/orbit/flip without JS.
- **`clip-path: inset(t r b l)`** can support decorative reveals, progress overlays, or comparison visuals. For scroll reveals, keep base content visible and add the animation only after observation; reduced motion and missing JS must remain readable.
- **Tab color copies are decorative only.** Keep one semantic tab list. Any visual copy uses noninteractive spans, no duplicate IDs/handlers/roles, `aria-hidden="true"`, `inert`, and `pointer-events: none`. Preserve the real controls' selected state, focus, and keyboard behavior.
- **Opacity is not semantic hiding.** `opacity: 0` still permits focus/pointer interaction and accessibility exposure ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/opacity)). Preserve the component's appropriate hidden/inert/unmount lifecycle and focus management.

## Gestures & drag

- **Momentum dismissal**: combine distance and velocity when it fits the interaction. `Math.abs(distance)/Math.max(1, elapsedMs)` gives average pixels per millisecond; thresholds such as `0.11` are illustrative and need real-device tuning.
- **Damping at boundaries**: dragging past a natural edge moves less the further you go (real things slow before stopping).
- **Pointer capture** once dragging starts, so it continues when the pointer leaves bounds.
- **Multi-touch protection**: ignore extra touch points after the drag begins (`if (isDragging) return`) — prevents jumps.
- **Friction over hard stops** — allow over-drag with rising resistance rather than an invisible wall.

Keep a visible keyboard-operable dismiss/control alternative, and test cancellation as well as successful gestures.

## Masking imperfect crossfades

A small blur can blend a decorative crossfade, but a simpler fade or instant change may be clearer. Preserve text legibility and profile the radius and affected area; there is no universally safe 20px threshold.

## Stagger

Optionally stagger an occasional group entrance by 30–80ms if it clarifies hierarchy. Simultaneous or instant display is valid. Stagger is decorative; avoid delaying controls or essential reading.

```css
.item { opacity: 1; transform: none; }
@media (prefers-reduced-motion: no-preference) {
  .item[data-entering] { animation: fadeIn 240ms ease-out backwards; }
  .item:nth-child(2) { animation-delay: 50ms; }
  .item:nth-child(3) { animation-delay: 100ms; }
}
@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } }
```

`data-entering` must be set by a one-shot lifecycle, never initial markup: consume the element once, skip if reduced motion or focus is already active, and permanently clear the trigger on animation end/cancel, focus entry, preference change, or teardown. Clear it immediately if the expected animation is unavailable. Retain a consumed flag/WeakSet so focusout and later preference changes cannot replay it. Do not rely only on `:focus-within { animation: none }`, which restarts when focus leaves. With no JavaScript, this CSS leaves the base content visible.

## Accessibility

```css
@media (prefers-reduced-motion: reduce) {
  .element { animation: none; transition: none; } /* preserve the component's state styles */
}
@media (hover: hover) and (pointer: fine) and (prefers-reduced-motion: no-preference) {
  .element:hover { transform: scale(1.05); } /* gate hover motion — touch fires false hovers on tap */
}
```

```jsx
const reduce = useReducedMotion();
const transition = reduce ? { duration: 0 } : { duration: 0.2 };
```

Reduced motion may mean a gentler effect or **no animation**. Preserve clear text, color, focus, and stable state feedback. Do not zero a transform that encodes closed/open state without preserving that behavior elsewhere. Verify keyboard operation, semantic hiding, and the project's no-JS fallback before judging polish.

## Debugging (recommend in reviews when feel is uncertain)

- **Slow motion**: bump duration 2–5× or use DevTools animation inspector. Check colors crossfade cleanly, easing doesn't stop abruptly, `transform-origin` is right, coordinated properties stay in sync.
- **Frame-by-frame**: Chrome DevTools Animations panel reveals timing drift between coordinated properties.
- **Real devices** for gestures (drawers, swipe) — connect a phone, hit the dev server by IP, use Safari remote devtools.
- **Fresh eyes next day** — imperfections invisible during development surface later.

## Cohesion

Match motion to the component's personality: playful can be bouncier; a professional dashboard should be crisp and fast. Sonner feels right partly because easing, duration, design, and even the name are in harmony — slightly slower, `ease` rather than `ease-out`, to feel elegant. Opacity + height in entering/exiting lists is trial and error; there's no formula — adjust until it feels right.
