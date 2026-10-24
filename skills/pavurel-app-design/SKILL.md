---
name: pavurel-app-design
description: Review and improve Conference Manager Customer and Platform interfaces under the target repository's current central development requirements. Use for request workflows, operational lists, settings, operator views, forms, status feedback, responsive behavior and accessibility. Find and apply existing GitHub design, architecture, security, i18n and test standards; do not create a parallel design system or use the marketing website profile for authenticated application work.
---

# Pavurel App Design

Make operational work understandable and efficient within the existing application. Use this profile as a workflow and source locator, not as a replacement specification.

## Establish the governing sources

1. Follow host instructions and the user's scope. Read the target repository's current root `AGENTS.md`, applicable nested instructions and every central standard they require. Start with [repository-sources.md](references/repository-sources.md) to locate the relevant design, coding, architecture, security, role and test sources.
2. Resolve the accepted `main` baseline and exact work ref. Inspect the actual code, tokens, components, translations and tests involved. Treat an unmerged PR, a dated source map and a Confluence description as distinct from current implementation.
3. Let the target GitHub requirements govern development. Keep token values, role matrices, API semantics, test gates and publication rules in their owning repositories. Reference them rather than reproducing a competing normative copy here.
4. Use Confluence for documentation, rationale, navigation and evidence. Follow its governance when updating it, preserve historical evidence and link the relevant GitHub sources. Do not make access to private documentation a substitute for the public repository's development contract or copy private material into a public change.
5. If a skill or external example conflicts with the repository, follow the repository and identify the discrepancy. Correct it within the authorized scope; ask only about a genuinely unresolved decision. Do not silently change a central rule to accommodate an example.
6. Establish the application surface, role, workflow and task mode. For reviews, inspect and report without editing files or data. For implementation, complete the already authorized scoped changes and required checks.

If mandatory repository guidance cannot be read, follow the repository's blocking rule. Otherwise continue the work available within scope; unavailable optional skills or tools are not a reason to invent access or create an unnecessary approval stop.

## Choose the surface and the useful specialist

- Read [customer.md](references/customer.md) for Employee, Conference Manager and Tenant Admin workflows.
- Read [platform.md](references/platform.md) for the separately served Platform Operator interface.
- Use `pavurel-web-design` by installed name for the public marketing website instead of applying this app profile there.
- Use `emil-design-eng`, `break-ui` and `mobile-native` for the concrete interaction, data and mobile questions in scope.
- Use `prototype` for an actual unresolved design choice and motion specialists for justified motion work. Look up installed skills by name; do not assume sibling folders exist.
- Use `21st-design-research` when the user requests external component research and it is available. Otherwise use available public references and the project's own components. Search availability does not authorize code installation, hosted generation or a new runtime.

## Work from the existing implementation

Read the current architecture before choosing a component or dependency. The verified application baseline uses native ES modules and native DOM/CSS components. Reuse the current Core UI, capability-owned presentation, central translations and semantic tokens. Recheck this baseline if the repository changes; do not introduce React, a bundler, Tailwind, Sonner or another component system solely because a skill example uses it.

Keep the official product identity, approved assets and visual rules from the central design system. Improve hierarchy, spacing, labels and action placement using its tokens. Use images when they support a real task; preserve asset provenance. Do not copy marketing layouts or another product's typography into operational screens by default.

Respect the existing module ownership and public contracts. In the verified source, `src/platform/` contains cross-cutting Customer infrastructure; `src/platform-admin/` owns the separate Operator interface. Shared appearance does not merge their APIs, sessions, data or permissions.

## Make state and actions understandable

Trace the actual read/mutation contract before changing feedback. Make loading, empty, unavailable, stale, conflicting, failed and completed states distinguishable where the workflow supports them. Do not invent a business transition, approval rule, integration or provider confirmation to make a prototype look complete.

Show success only when the applicable contract confirms it. A saved request, reserved room, requested catering order and supplier confirmation are different concepts; use the implemented status model and translations. Keep persistent work status visible after temporary feedback disappears.

Preserve validated role scope, tenant context, draft lifecycle, concurrency handling, pending-action protection and the repository's session/lock behavior. Check how late responses behave after navigation or authority loss. A visual transition must not restore old content, re-enable a protected action or move focus back to a departed view.

Use semantic controls, labels, errors and status announcements through existing helpers. Preserve keyboard operation, focus restoration, zoom/reflow and equivalent content across responsive representations. Use the current locale helpers and translation catalogs for all user-facing and accessibility text.

## Keep optional effects and previews bounded

Apply motion only when it improves orientation or feedback. Keep frequent actions immediate and respect reduced motion, including static behavior. Optional animation must not be the sole mechanism that reveals already available content.

Respect the application's documented secure bootstrap and fallback. A requirement for static marketing content to work without JavaScript does not require prerendering authenticated business data, bypassing session checks or replacing the application's architecture.

Use synthetic test/preview data and mocked external mutations. Preserve canonical Demo scenarios and reset contracts. Check the real published artifact, not just whether a preview is linked. At the verified baseline, Customer packaging includes non-Markdown files under `assets/`, while Platform uses an explicit inventory: a fixture placed in assets may ship even when no application module imports it. Reinspect the current artifact rules before adding a preview.

## Validate and document the result

Select validation from the target repository's current instructions and risk-based test strategy; this profile cannot waive a required gate. Reuse existing tests and add only coverage required by the change. Check the affected workflow, relevant locales, narrow/wide layouts, keyboard/focus and motion preferences. Use actual device evidence where available and state when only emulation or source inspection was possible.

Report the user-facing outcome, governing source paths, actual checks and remaining limitations. Distinguish skill maintenance, target-project installation, application changes, merged source and deployed behavior. Update Confluence as documentation of the verified result and its GitHub references; never mark a proposed profile as installed or a source review as runtime acceptance.
