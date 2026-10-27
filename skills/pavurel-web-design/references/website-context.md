# Pavurel website source map

Read the current local equivalents in the target checkout, including any renamed successors. GitHub central requirements govern development; this reference locates them and supplies review questions. Confluence documents decisions, rationale and evidence through links to the owning GitHub sources.

## Current public sources

| Question | Owning source |
| --- | --- |
| Mandatory instructions and precedence | [AGENTS.md](https://github.com/floriankreutzer/conference-manager-website/blob/main/AGENTS.md) |
| Design, typography, tokens and asset families | [Design system](https://github.com/floriankreutzer/conference-manager-website/blob/main/docs/DESIGN-SYSTEM.md) |
| Shared functional icons, versioned asset sources and separate provider marks | [Canonical icon system](https://github.com/floriankreutzer/conference-manager/blob/main/docs/ICON-SYSTEM.md); verify the linked manifests and actual Astro consumers |
| Audience journey, page ownership and CTA placement | [Marketing experience](https://github.com/floriankreutzer/conference-manager-website/blob/main/docs/MARKETING-EXPERIENCE.md) |
| Approved claims, product boundaries and offer wording | [Content governance](https://github.com/floriankreutzer/conference-manager-website/blob/main/docs/CONTENT-GOVERNANCE.md) |
| Runtime, component and application boundary | [Architecture](https://github.com/floriankreutzer/conference-manager-website/blob/main/docs/ARCHITECTURE.md) |
| Implementation and validation | [Coding standards](https://github.com/floriankreutzer/conference-manager-website/blob/main/docs/CODING-STANDARDS.md), [test strategy](https://github.com/floriankreutzer/conference-manager-website/blob/main/docs/TEST-STRATEGY.md) |
| Public forms, scripts and trusted handoffs | [Security standards](https://github.com/floriankreutzer/conference-manager-website/blob/main/docs/SECURITY.md) |

Resolve accepted main and the exact work ref. Follow relevant approved repository changes rather than a dated skill snapshot; distinguish a proposed PR from accepted requirements. Do not transfer a central requirement into this package as an independent normative copy.

## Build a task-specific content map

Read the current route map and content ownership before a site-wide pass. Record each actual page's customer question, locale, detailed explanation, evidence and next step. Audit shared navigation/footer/mobile states as well as page bodies. Count repeated actions by resolved destination, even when the labels differ.

Locate the source for audience, tone, commercial terms and capability claims. Verify setup-dependent behavior and separately assessed integrations against the current evidence; a desired feature or external template is not a shipping capability.

Keep orientation for direct arrivals while linking to the owner of the detailed explanation. Preserve localized pairing and existing approved routes. Do not copy a frozen route/CTA matrix from a previous audit.

## Useful specialists

Look up optional installed skills by name, not sibling paths.

| Task | Skill |
| --- | --- |
| Interaction hierarchy | `emil-design-eng` |
| Long, missing or unusual content | `break-ui` |
| Mobile browser behavior | `mobile-native` |
| A concrete layout choice | `prototype` |
| Observed animation performance | `animation-performance` |
| Existing motion | `review-animations` |
| A justified transition | `animate` |
| Requested external catalog research | `21st-design-research` |
| Separate authenticated application work | `pavurel-app-design` |

Keep native Expo/Swift work in its own project. Use dependency specialists only for a demonstrated need under the target repository's architecture process.

## Verification provenance

The map was checked on 2026-10-24 against website `63c72fed1502bc43b4142900f87d052a8b967350`. This ref records what was inspected; it is not a permanent implementation baseline. Do not place internal documentation URLs, customer data, credentials or private operational evidence in this public package.

The cross-repository icon-system locator was reviewed separately on 2026-10-27 against the published application source [`a39664b20bef4d32a897577f0127bda74d86b28f`](https://github.com/floriankreutzer/conference-manager/commit/a39664b20bef4d32a897577f0127bda74d86b28f) in [PR #402](https://github.com/floriankreutzer/conference-manager/pull/402). This immutable reference records the inspected icon contract; its `main` link locates the current owning source. Publication of the PR source alone does not establish merge, UI integration or deployment.
