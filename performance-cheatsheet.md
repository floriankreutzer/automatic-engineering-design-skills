# Performance Cheatsheet

Follow the host/user task and existing project architecture, design tokens, and accessibility rules. For Pavurel marketing website work, use the installed `pavurel-web-design` skill when available. Diagnose before changing behavior; these are starting points, not automatic rewrites.

| Problem | Check / possible improvement |
| --- | --- |
| Animation stutters | Record layout, paint, and long tasks; prefer `transform`/`opacity` only when layout and interaction semantics survive |
| Long list scrolls slowly | Measure DOM/render cost; consider pagination or virtualization while preserving keyboard access, focus, and required content access |
| Blur causes performance issues | Reduce radius and affected area, or remove the effect; no fixed radius guarantees good performance |
| Motion's `x`/`y` drops frames | Check installed version, browser, and trace; Motion 14.2+ supports accelerated independent transforms |
| Unexpected properties animate | Replace `transition: all` with the intended properties |
| React re-renders every frame | Avoid unnecessary per-frame state updates; use an owned DOM ref or motion value for purely visual updates |
| Element shifts 1px as motion starts | Investigate layer/pixel rendering; test a scoped `will-change` hint only after observing the problem |
| Hidden UI remains focusable | Preserve semantic hiding and focus management; `opacity: 0` alone is insufficient |
| Static content needs JS solely to reveal it | Default static marketing content to visible; preserve the app's documented fallback and reduced-motion behavior, including no animation |

Check [Motion's version history](https://motion.dev/changelog), [current React transform support](https://motion.dev/docs/react-animation#transforms), and [performance documentation](https://motion.dev/docs/performance). Motion 14.2.0 added accelerated independent transforms on 13 October 2026; earlier versions and browser conditions differ. Acceleration is an optimization, not a guarantee. See [MDN opacity](https://developer.mozilla.org/en-US/docs/Web/CSS/opacity) for focus and visibility behavior.
