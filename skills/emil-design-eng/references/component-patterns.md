# Component and interaction patterns

Use these examples only after the task, brand, semantics and reduced-motion checks in the parent skill. Existing project decisions take priority.

## Contents

- [Spring animations](#spring-animations)
- [Component building principles](#component-building-principles)

## Spring Animations

Springs feel more natural than duration-based animations because they simulate real physics. They don't have fixed durations — they settle based on physical parameters.

### When to use springs

- Drag interactions with momentum
- Elements that should feel "alive" (like Apple's Dynamic Island)
- Gestures that can be interrupted mid-animation
- Decorative mouse-tracking interactions

### Spring-based mouse interactions

Direct tracking suits precise controls. Spring smoothing is optional for a justified decorative interaction. If the project already uses Motion, use its installed version's motion-value and spring APIs; do not install it for a decorative hover effect. Retain a static reduced-motion state.

Keep decorative tracking away from reading, selection and precise data controls. Omit it when it adds movement without helping the task.

### Spring configuration

**Apple's approach (recommended — easier to reason about):**

```js
{ type: "spring", duration: 0.5, bounce: 0.2 }
```

**Traditional physics (more control):**

```js
{ type: "spring", mass: 1, stiffness: 100, damping: 10 }
```

Keep bounce subtle (0.1-0.3) when used. Avoid bounce in most UI contexts. Use it for drag-to-dismiss and playful interactions.

### Interruptibility advantage

Springs can preserve velocity when retargeted. CSS transitions also retarget from the current visual state; restarting a keyframe animation from its initial keyframe can cause a jump. This makes springs ideal for gestures users might change mid-motion. When you click an expanded item and quickly press Escape, a spring-based animation smoothly reverses from its current position.

## Component Building Principles

### Buttons must feel responsive

Give immediate visible press feedback using the project's control states. A small scale is one option when it does not impair readability or conflict with an existing transform; color or border feedback can be sufficient.

```css
@media (prefers-reduced-motion: no-preference) {
  .button {
    transition: transform 160ms ease-out;
  }
  .button:active {
    transform: scale(0.97);
  }
}
```

Keep visible non-motion press and focus states outside this media query. Use native click/keyboard activation; pointer-down feedback must not commit the action.

If scale is appropriate, keep it subtle and component-specific. Do not apply it globally to every link or button.

### Avoid distracting scale entrances

Starting a large UI element at zero scale can be distracting. A small scale range, a pure fade or no animation may be more suitable. Preserve visible base content; apply an entrance's initial styles only within a successfully initialized enhancement.

```css
/* Bad */
.entering {
  transform: scale(0);
}

/* Good */
.entering {
  transform: scale(0.95);
  opacity: 0;
}
```

### Make popovers origin-aware

Popovers should scale in from their trigger, not from center. The default `transform-origin: center` is wrong for almost every popover. **Exception: modals.** Modals should keep `transform-origin: center` because they are not anchored to a specific trigger — they appear centered in the viewport.

```css
/* Base UI */
.popover {
  transform-origin: var(--transform-origin);
}
```

Whether the user notices the difference individually does not matter. In the aggregate, unseen details become visible. They compound.

### Tooltips: skip delay on subsequent hovers

Tooltips should delay before appearing to prevent accidental activation. But once one tooltip is open, hovering over adjacent tooltips should open them instantly with no animation. This feels faster without defeating the purpose of the initial delay.

```css
.tooltip {
  transition: transform 125ms ease-out, opacity 125ms ease-out;
  transform-origin: var(--transform-origin);
}

.tooltip[data-starting-style],
.tooltip[data-ending-style] {
  opacity: 0;
  transform: scale(0.97);
}

/* Skip animation on subsequent tooltips */
.tooltip[data-instant] {
  transition-duration: 0ms;
}
```

### Use CSS transitions over keyframes for interruptible UI

CSS transitions can be interrupted and retargeted mid-animation. Re-starting an entrance keyframe from the beginning can jump; controlled animations can also preserve current state. Prefer the simplest mechanism that correctly handles rapid reversals.

```css
/* Interruptible - good for UI */
.toast {
  transition: transform 400ms ease;
}

/* Re-starting this entrance from its first frame can jump */
@keyframes slideIn {
  from {
    transform: translateY(100%);
  }
  to {
    transform: translateY(0);
  }
}
```

### Use blur to mask imperfect transitions

First correct timing, overlap and layout when a crossfade feels unclear. A small blur is an optional effect only if the project style allows it and text remains readable. Prefer a clear fade or static change when that is enough.

**Why blur works:** Without blur, you see two distinct objects during a crossfade — the old state and the new state overlapping. This looks unnatural. Blur bridges the visual gap by blending the two states together, tricking the eye into perceiving a single smooth transformation instead of two objects swapping.

If blur is justified, apply it to a decorative icon or visual wrapper rather than essential text. Keep the base state clear and the optional effect within the motion preference:

```css
.decorative-swap {
  opacity: 1;
  filter: none;
}
@media (prefers-reduced-motion: no-preference) {
  .decorative-swap {
    transition: filter 160ms ease, opacity 160ms ease;
  }
  .decorative-swap.transitioning {
    filter: blur(2px);
    opacity: 0.7;
  }
}
```

Keep blur small and localized if used; no pixel threshold guarantees low cost across devices. Test the affected surface and browser, and remove the effect for reduced motion when appropriate.

### Animate enter states with @starting-style

The modern CSS way to animate element entry without JavaScript:

```css
.toast-motion {
  opacity: 1;
  transform: translateY(0);
}
@media (prefers-reduced-motion: no-preference) {
  .toast-motion {
    transition: opacity 200ms ease-out, transform 200ms ease-out;
    @starting-style {
      opacity: 0;
      transform: translateY(8px);
    }
  }
}
```

Use `@starting-style` as progressive enhancement when supported. Keep the final visible style as the base so unsupported browsers show the content immediately. Place optional motion in a `prefers-reduced-motion: no-preference` media query; a JavaScript mount flag must never be required to reveal essential content.
