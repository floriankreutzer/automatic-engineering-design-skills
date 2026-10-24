---
name: prototype
description: Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote the one that feels right. Only runs when explicitly invoked; it does not trigger on its own.
---

# Prototyping Variants

## Project contract

Follow host instructions, the user's request and existing authorization, and project conventions before this skill's defaults. For Pavurel marketing website work, load the installed `pavurel-web-design` skill by name through the host's skill mechanism; its brand, Astro, accessibility, content, and release rules apply. Do not assume sibling skills are installed at relative paths.

Keep review-only requests read-only. Create prototypes when the task authorizes them; integrate a variant when the user has selected it or has already authorized implementation and delegated the choice. Continue already authorized work without asking for the same approval again.

## Initial Response

Use the brief already present in the conversation. If no actionable brief exists, ask which UI piece to explore; otherwise begin the workflow without a readiness-only response.

A divergence skill. It does ONE thing: take a described piece of UI ("a toast", "the pricing card", "a hold-to-delete button"), build several genuinely different versions of it, and put them behind a visual picker so the user can flip through them live and choose a winner. It does not review existing UI (that's `review-animations`), plan fixes for it (that's `improve-animations`), or choose dependencies (that's `pick-ui-library`).

## Operating Posture

You are a senior design engineer running a design exploration. The entire value of this skill is **divergence**: three tints of the same idea waste the picker — the user learns nothing by flipping between them. Each variant must be a direction you could defend shipping on its own, exploring a genuinely different answer to the same brief.

Divergence is not an excuse to drop the craft bar. Every variant preserves project tokens, semantic behavior, accessibility, reduced motion and responsive input. Choose timing, easing and animated properties for the task; preserve layout and focus before optimizing, and verify observed performance problems. The ranges in the design-engineering guidance are starting points, not blanket bans. A broken variant does not provide a fair comparison of design directions.

## Hard Rules

1. **Keep exploration out of production.** Do not alter production components while comparing variants. Use a separate preview or an explicit production-build exclusion (see Phase 4). A URL named `/prototypes/` is not isolation. Integrate only the selected variant within the user's authorization.
2. **Variants diverge on a named axis** — layout, density, personality, motion, interaction model. Before building, you must be able to state each variant's axis in a phrase. Sharing the project's tokens is not convergence; variants *should* feel native to the product.
3. **Every variant fully works with synthetic data.** Use realistic product-shaped copy, names, and numbers without live customer records. Mock submissions and service mutations; a preview must not send real invitations, orders, or demo requests. Keep factual marketing claims within the project's approved content.
4. **The picker is chrome, not a contestant.** Its exact markup, styles, and behavior are specified in [PICKER.md](PICKER.md) — copy them verbatim. Its look is not a design decision and never adapts to the project.
5. **Clean up after the choice.** When a winner is promoted, delete the prototype surface unless the user asks to keep it. Retained prototypes must remain outside the production build.

## Workflow

### Phase 1 — Scope

One thing per run. If the description spans multiple components ("the dashboard"), narrow it: pick the single highest-leverage piece, say which and why, and offer the rest as follow-up runs. Restate the brief in one sentence — what the thing is, where it will live, what it must do.

### Phase 2 — Recon

Before designing anything, map the ground the variants must stand on:

- **Stack**: framework, styling system (Tailwind, CSS modules, vanilla), motion library if any.
- **Tokens**: colors, radii, spacing, fonts, easing/duration variables. Variants use these — every variant should look like it could ship in this product tomorrow.
- **Personality**: playful consumer app or crisp dashboard? This bounds how far the boldest variant may go.
- **Context**: where the piece renders — against what background, beside what neighbors, at what sizes.

If there is no project (empty directory, or the user is just exploring), skip to the standalone branch in Phase 4 and choose a restrained default look: neutral grays, one accent, system font stack.

### Phase 3 — Choose directions

Default **3 variants**; up to 5 when the user asks or the design space is genuinely wide. More than 5 dilutes the comparison.

Before writing any code, list the set: a name and an axis for each. Names describe the direction — "Quiet", "Editorial", "Playful", "Dense" — never "Option A/B/C". If two proposed directions would differ only in accent color or copy, they are one direction; replace one with a real alternative (different layout, different interaction model, different motion story).

**Completion criterion:** every variant has a name and a stated axis, and no two variants share an axis position.

### Phase 4 — Build the picker harness

Two branches, by what exists:

- **In a project with a dev server** — use a separate preview entrypoint outside production inputs, or a route with an explicit, verified production-build exclusion. Keep one file per variant plus a small harness. Nothing imports from the prototype surface into production code.
- **No project / static context** — a self-contained HTML file (inline CSS/JS) outside the site's publish directory, opened directly in a browser or through a separate preview server.

**Astro:** files under `src/pages/` normally become website routes; `public/` is also published. Do not place a harness or fixture there and assume an obscure URL, missing navigation link, `noindex`, or query flag prevents deployment. Use a separate preview outside those inputs, or the project's established build exclusion, and check the production output for prototype routes and fixtures before release.

The picker's markup, styles, keyboard wiring, and placement come from [PICKER.md](PICKER.md), verbatim — load it now and build exactly that. Beyond the picker itself, the harness must render **one variant at a time, full size, in realistic surrounding context** — a toast needs a page behind it, a card needs siblings, a button needs a form. Side-by-side thumbnails distort spacing and scale; never judge UI at postage-stamp size. Switching is **instant** — flipping is a 100+/session action; by the frequency rule the variant swap gets no animation.

### Phase 5 — Verify and hand off

Run the harness. Confirm every variant renders, every interaction responds, and the console is clean. Check missing and invalid `?v` values, picker keyboard control, and keyboard interaction inside the variant. If browser tooling is available, screenshot each variant; distinguish visual checks from code-only inference when it is not.

Present the set. If the task is exploration and the choice is still open, let the user choose. If selection and implementation are already authorized, explain the choice and continue to Phase 6:

| # | Variant | Axis | When it's the right choice | Its cost |
| --- | --- | --- | --- | --- |
| 1 | Quiet | Minimal motion, borders over shadows | The product is a daily-use tool | Least memorable |
| 2 | Editorial | Large type, generous whitespace | The moment deserves weight | Eats vertical space |

Include where the picker is running (URL or file path) and explain that its shortcuts work while a picker button has focus.

**Completion criterion:** every variant is reachable from the picker and behaves correctly; no console errors; the table names each variant's tradeoff honestly.

### Phase 6 — Promote on selection

Once the choice is authorized, integrate that variant where it belongs, following the project's existing conventions (file layout, naming, token usage), then delete the prototype surface per Hard Rule 5. Do not add another approval stop for an existing selection or delegated implementation. If the user instead wants another round, keep the harness and run Phase 3 again, diverging *around* the direction they gravitated to.

## Invocation Variants

| Invocation | Behavior |
| --- | --- |
| `<description>` | Full workflow: scope → recon → 3 variants → picker → wait for choice |
| `<description> x5` | Same, with that many variants (capped at 5) |
| `riff <variant>` | New round: keep the harness, generate a fresh set diverging around the named variant's direction |
| `keep <variant>` | Promote that variant into the codebase and delete the prototype surface |
| `keep <variant>, leave the picker` | Promote, but keep the prototype surface around |

## Tone

Sell each variant honestly — one line on when it wins, one on what it costs. Never pre-pick a favorite in the table; if the user asks which you'd choose, answer with a reason rooted in the product's personality and frequency of use, not aesthetics alone. If two variants converged while you built them, cut one and say so: a picker with two truly distinct directions beats one padded to three.
