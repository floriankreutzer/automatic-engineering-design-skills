---
name: pavurel-web-design
description: Design, review and improve Pavurel's Conference Manager marketing website using its approved brand, customer journey, content ownership and Astro architecture. Use for Pavurel page layouts, images and icons, sales copy, demo CTA density, repeated content, responsive behavior, accessibility, or bounded product illustrations. Combine with a specialist skill only for the specific task. Do not use this website profile to redesign the authenticated application or change product capabilities.
---

# Pavurel Web Design

Make the customer's meeting process understandable and each next step useful. Apply the website's current GitHub development requirements; this profile supplies a workflow and source map, not a second brand, content or engineering specification.

## Establish context before changing anything

1. Follow host/tool instructions and the user's current task and authorization. Read the target repository's current `AGENTS.md`, applicable nested instructions and the central standards they reference. Those GitHub sources govern development and override profile or specialist defaults. Do not treat a skill as permission to install, publish, merge or change another project.
2. Read the current website's `docs/DESIGN-SYSTEM.md`, `docs/MARKETING-EXPERIENCE.md`, `docs/CONTENT-GOVERNANCE.md` and `docs/ARCHITECTURE.md`, or their current equivalents. Read relevant coding, accessibility and security standards. Inspect existing components, tokens, assets and routes.
3. Use [website-context.md](references/website-context.md) to locate current central sources. Resolve accepted `main` and the exact work ref; use dated refs only as evidence. Keep normative token values, CTA policy, offer terms and test gates in their owning repository. Confluence documents rationale, decisions and evidence with GitHub links; it does not override the development contract. Identify conflicts and clarify only unresolved material decisions. Never infer that an intended integration is implemented.
4. Establish the page, locale and customer question in scope. For a site-wide audit, inventory all localized routes and shared layouts, including footer destinations and legacy routes. Distinguish the marketing site, public demo launcher and authenticated application.
5. Use an installed specialist by name only when needed. Select `pavurel-app-design` for a separate authenticated application task. Select `21st-design-research` for requested catalog research; its results remain subordinate to this repository's standards. If an optional skill or tool is unavailable, follow the project sources and complete the available work without inventing access.

For a read-only review, inspect and report without creating fixtures or editing the website. For an implementation request, complete authorized edits and proportionate checks without a redundant approval stop. Ask only about an unresolved product, commercial, brand or publication decision that affects the result.

## Give each page one customer purpose

- Read the current audience, tone and locale requirements in `docs/CONTENT-GOVERNANCE.md` and `docs/MARKETING-EXPERIENCE.md`. Explain the meeting outcome, the information needed and the work made clearer for that audience; keep supported locales equivalent.
- Give each detailed explanation one primary page. Keep short orientation for direct arrivals; link to the owning page instead of repeating a full feature list, process, offer or FAQ.
- State the customer question, answer, evidence or illustration, and useful next step for each section. Remove a section when it adds no new information.
- Explain how Conference Manager complements existing room reservation and identity systems and brings meeting coordination together. Describe replacement of separate catering spreadsheets or forms only within confirmed scope.
- Distinguish implemented capability, setup-dependent behavior and a proposed or separately assessed integration. Do not invent availability, automation, certifications, customer logos, testimonials, savings or ROI.
- Keep product, team, workflow, integration, setup/pilot and trust pages focused on their distinct questions. Preserve established routes and bilingual pairing.

## Control demo CTA density by destination

Read the approved placement and page-ownership policy in the current `docs/MARKETING-EXPERIENCE.md` before counting or changing actions. Derive the allowed placements from that source; do not preserve an obsolete numerical limit from a skill or copied checklist.

Count links by their resolved localized destination, not their wording. A renamed button pointing to the same request form is still a demo CTA. Audit header, hero, inline sections, closing panels, footer and mobile navigation together. Inspect header and mobile variants in their actual responsive states; do not remove the only accessible navigation action merely because both variants exist in source.

Use descriptive reading links where the policy calls for them. Locate the owning page for the illustrative meeting example and link to it rather than cloning the same story. Distinguish the demo-request form from the separate public demo launcher and application sign-in.

## Keep the offer accurate

Read the current commercial wording and required disclosures in `docs/CONTENT-GOVERNANCE.md` and the owning offer content. Check setup cost, free-use conditions, start event and scope together. Keep qualifications next to the relevant claim as required by that source. Do not invent amounts, periods, tiers, renewal, refund, billing or setup-duration promises, or treat a template pricing component as an approved offer.

## Preserve the Pavurel visual language

- Read `docs/DESIGN-SYSTEM.md` and its actual token/asset sources. Reuse their current palette, typography, spacing, geometry and approved asset families. Do not maintain a second set of brand constants in this profile.
- Combine operational clarity with warm workplace hospitality. Use spacing, hierarchy and relevant imagery to make the page easy to read. Apply brand accents selectively.
- Inspect existing photos, illustrations, icons and asset manifests before extending them. Keep icon stroke, scale, shape and meaning consistent. Use the project's SVG/icon system for simple icons; use an available image-generation capability for requested new raster imagery, matching approved references.
- Preserve the signet. Label illustrative product examples honestly; do not present generated imagery as a real customer, real deployment or actual product screenshot.
- Adapt benchmark principles to the customer task. Do not introduce another product's palette, typography, glass surfaces, decorative effects or layout merely to imitate its appearance.
- Preserve intrinsic image dimensions, responsive sources, loading priorities and asset provenance required by the project.

## Build within the existing architecture

Prefer existing Astro components, semantic HTML and CSS. Use TypeScript and bounded progressive enhancement for justified interactions. Keep readable content, navigation and ordinary links usable without JavaScript. Add a framework, UI library, third-party embed or runtime only for a demonstrated requirement and within the project's authorization and dependency process.

Preserve form endpoints, validation, consent, anti-spam controls, localization, restrictive CSP and application handoffs. Do not claim that a form succeeded if its processing endpoint is unavailable. Do not turn the marketing site into an application authentication boundary.

Keep prototype routes, synthetic test fixtures and diagnostic switches outside production output. A route named `/prototypes/`, a hidden link or `noindex` is not a build exclusion. Inspect the resulting output when introducing a preview mechanism.

## Make interaction serve comprehension

- Use motion to explain a meaningful state change, preserve orientation or acknowledge an action. Leave reading and frequent work immediate.
- Respect reduced-motion preferences, including fully static behavior. Retain text, status and focus cues without movement.
- Preserve semantics and focus when hiding content; opacity or clipping alone is not an accessible hidden state. Keep visual duplicates noninteractive and out of the accessibility tree.
- Prefer visible base content and optional entrance effects. Never depend on an observer or animation callback to reveal essential content or make an action available.
- Preserve keyboard behavior, visible focus, browser zoom, selectable content and native scrolling. A visual press response may begin on pointer-down; activation must retain native click/keyboard behavior and cancellation.
- Diagnose performance against installed versions and real behavior. Treat timing, easing, blur and hardware acceleration as context-dependent choices, not universal pass/fail rules.

## Verify the changed behavior

Choose checks that address the change and the project's required gates. Use the current repository's required gates and test strategy; do not waive them based on this profile. Avoid a new dependency or additional broad test suite for a copy-only change when the repository does not require it.

For page or interaction changes, inspect relevant narrow and wide layouts, long German text, keyboard/focus behavior, 200% zoom and reduced motion. Check a 320 CSS-pixel layout where required by project standards. Check no-JavaScript behavior when enhancement or initial visibility changes. Test touch behavior on real hardware when possible and state when only emulation or source inspection was available.

For a site-wide content pass, verify all affected routes in both languages, CTA destinations and placement, shared-layout duplication, page ownership, internal links and qualified feature/offer statements. Use synthetic data for stress cases. Review the production build for accidental preview routes when relevant.

Report the result in this order:

1. Customer-facing changes and their purpose.
2. Concrete checks and observed results; separate source inspection from browser or device verification.
3. Remaining limitations and the precise review or publication step, if one still requires the user's decision.

Do not claim formal accessibility conformance, measured conversion improvement, successful delivery or deployment from a source review alone.
