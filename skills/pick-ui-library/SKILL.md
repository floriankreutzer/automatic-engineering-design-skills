---
name: pick-ui-library
description: Decide whether a frontend task needs a dependency, then use a curated library shortlist when it fits the existing architecture. Prefer native HTML/CSS and installed components for simple work. Covers numbers, OTP inputs, charts, menus, virtualization, drag and drop, toasts, state, and styling. Only runs when explicitly invoked.
---

# Picking The Right Library

## Project contract

Follow host instructions, the user's request and existing authorization, and project conventions before this skill's defaults. For Pavurel marketing website work, load the installed `pavurel-web-design` skill by name through the host's skill mechanism; its brand, Astro, accessibility, content, and release rules apply. Do not assume sibling skills are installed at relative paths.

Treat the list as candidates, not a requirement to install packages. Keep review-only requests read-only. Perform installation or integration only within authorized scope and project architecture rules; do not request the same approval again when it already exists.

## Initial Response

Use the frontend task already present in the conversation. If none exists, ask what behavior is needed; otherwise begin without a readiness-only response.

A lookup skill. First decide whether the behavior needs a library. If it does, consider the curated list below alongside the existing stack and the user's explicit choice. The correct recommendation can be native HTML/CSS, an installed component, or a better-fitting alternative outside this list.

## How to use this

1. **Identify the actual behavior and constraints.** Respect a library the user explicitly selected; discuss a mismatch rather than silently replacing it. A simple dropdown may be a native `<select>`, while a command menu has different needs.
2. **Inspect the architecture and existing dependencies.** Read project instructions, `package.json`, and the lockfile. Account for Astro versus React/Next, SSR/SSG, hydration, browser support, accessibility, and the client-JavaScript budget. Reuse compatible installed components; do not replace an existing dependency merely because it is absent from this list.
3. **Try native HTML/CSS first for simple tasks.** Do not introduce React, another runtime, a theme provider, or an animation library just for marketing-page hover/fade effects. On Pavurel's Astro website, preserve its established architecture unless the user has authorized a justified change.
4. **If a dependency is needed, verify its fit.** Use the installed version or current primary documentation for compatibility, maintenance, license, and API details. Explain the concrete benefit and added cost. Many candidates below are React/Next-specific and are not drop-in Astro components.
5. **Recommend the simplest suitable approach.** Install and wire it only when that work is authorized; record package changes in the existing lockfile and verify the affected build. If no listed library fits, say so and choose an appropriate alternative rather than forcing the shortlist.

## The list

### UI components & primitives

| Task | Library |
| --- | --- |
| Unstyled, accessible UI components (dialogs, popovers, menus, selects…) | [base-ui](https://base-ui.com) |
| Command menus (⌘K palettes) | [cmdk](https://cmdk.paco.me) |
| Toasts / notifications | [Sonner](https://sonner.emilkowal.ski) |
| One-time password / verification code inputs | [input-otp](https://input-otp.rodz.dev) |
| Customizable GUIs / control panels | [Leva](https://github.com/pmndrs/leva) — [dialkit](https://joshpuckett.me/dialkit) is an alternative |

### Motion & visuals

| Task | Library |
| --- | --- |
| General-purpose animation (springs, layout animations, enter/exit) | [motion](https://motion.dev) (Framer Motion) |
| Animating numbers (counters, prices, stats) | [NumberFlow](https://number-flow.barvian.me) |
| Animated text components | [torph](https://torph.lochie.me/) |
| 3D globes | [Cobe](https://cobe.vercel.app) |
| Dynamic OG images (HTML/CSS → SVG/PNG) | [Satori](https://github.com/vercel/satori) |
| Syntax highlighting | [shiki](https://shiki.style) |

Consider motion for springs, layout transitions, exit animations, or gestures only when the existing stack and interaction justify it. A simple hover or fade uses CSS; respect reduced motion and the project's performance budget.

### Charts

| Task | Library |
| --- | --- |
| Real-time / streaming charts | [Liveline](https://github.com/benjitaylor/liveline) |
| General charts (static or interactive dashboards) | [recharts](https://recharts.org) |

For a compatible interactive app, consider Liveline for streaming data and Recharts for general charts. A static marketing comparison may be clearer as a table or native SVG and does not justify a React chart runtime on its own.

### Interaction & performance

| Task | Library |
| --- | --- |
| Drag and drop | [dnd kit](https://dndkit.com) |
| Virtualization (long lists, large tables) | [Virtuoso](https://virtuoso.dev) |

### State & styling

| Task | Library |
| --- | --- |
| State management | [zustand](https://zustand.docs.pmnd.rs) |
| Constructing `className` strings conditionally | [clsx](https://github.com/lukeed/clsx) |
| Type-safe, variant-driven styling for Tailwind | [cva](https://cva.style) |
| Theme switching / dark mode (no flash on load) | [next-themes](https://github.com/pacocoursey/next-themes) |

The styling split: clsx for ad-hoc conditional classes; cva when a component has real variants (size, intent, state) that deserve a typed API. They compose — cva uses clsx-style inputs internally.

## Common mismatches to catch

- **Complex custom toast behavior in a React app** → consider Sonner; a simple persistent form result may only need accessible inline feedback.
- **A `<div>`-based dropdown/dialog with manual focus handling** → consider a suitable native element, existing accessible component, or base-ui in a compatible React app.
- **An interaction that genuinely needs animated digits** → consider NumberFlow if its runtime fits; do not animate numbers by default.
- **A large list that is slow in measurement** → choose pagination or virtualization from the user's task and accessibility needs; consider Virtuoso in a compatible stack.
- **Shared React state with a clear coordination problem** → consider the existing state solution or Zustand; avoid adding global state for local UI.
- **Repeated conditional classes or component variants** → reuse existing helpers; consider clsx/cva when the complexity warrants a dependency.
