# Repository source map

Use this map to find the current development contract. Read the local equivalent at the exact work ref, and resolve current accepted main before making implemented-state claims. Links to main locate living sources; the dated verification refs below are evidence only.

## Application: Customer and Platform

Owner: [conference-manager](https://github.com/floriankreutzer/conference-manager).

| Question | Central source |
| --- | --- |
| Mandatory entry and source precedence | [AGENTS.md](https://github.com/floriankreutzer/conference-manager/blob/main/AGENTS.md) |
| Engineering and validation requirements | [Coding standards](https://github.com/floriankreutzer/conference-manager/blob/main/docs/CODING-STANDARDS.md) |
| Architecture and capability ownership | [Architecture](https://github.com/floriankreutzer/conference-manager/blob/main/docs/ARCHITECTURE.md) |
| Brand, typography, density and CSS ownership | [Design system](https://github.com/floriankreutzer/conference-manager/blob/main/docs/DESIGN-SYSTEM.md), [tokens](https://github.com/floriankreutzer/conference-manager/blob/main/assets/tokens.css) |
| Existing UI and localization contracts | [Core UI](https://github.com/floriankreutzer/conference-manager/blob/main/src/core/ui.js), [i18n](https://github.com/floriankreutzer/conference-manager/blob/main/src/core/i18n.js) |
| Customer roles and technical/business ownership | [Role model](https://github.com/floriankreutzer/conference-manager/blob/main/docs/ROLE-MODEL.md) |
| Security and session behavior | [Production security](https://github.com/floriankreutzer/conference-manager/blob/main/docs/PRODUCTION-SECURITY.md), [Production session](https://github.com/floriankreutzer/conference-manager/blob/main/docs/PRODUCTION-SESSION.md), [Demo security](https://github.com/floriankreutzer/conference-manager/blob/main/docs/DEMO-SECURITY.md) |
| Customer branding and locale projection | [Tenant presentation](https://github.com/floriankreutzer/conference-manager/blob/main/docs/SAAS2-TENANT-PRESENTATION.md) |
| Operator interface and separate artifacts | [Platform frontend](https://github.com/floriankreutzer/conference-manager/blob/main/docs/PLATFORM-ADMIN-FRONTEND.md), [repository topology](https://github.com/floriankreutzer/conference-manager/blob/main/docs/ADR-009-PLATFORM-OPERATIONS-REPOSITORY-TOPOLOGY.md) |
| Actual protected output boundary | [Artifact assembly](https://github.com/floriankreutzer/conference-manager/blob/main/scripts/protected-frontend-artifacts.mjs), [Platform inventory](https://github.com/floriankreutzer/conference-manager/blob/main/deployment/platform-admin-production.json) |
| Validation commands and required automation | [package.json](https://github.com/floriankreutzer/conference-manager/blob/main/package.json), [CI](https://github.com/floriankreutzer/conference-manager/blob/main/.github/workflows/ci.yml), [browser projects](https://github.com/floriankreutzer/conference-manager/blob/main/playwright.config.js) |
| Permanent Demo workflows and reset acceptance | [Scenario acceptance](https://github.com/floriankreutzer/conference-manager/blob/main/docs/SAAS-3.7-SCENARIO-ACCEPTANCE.md) |

Read capability-specific contracts and tests for the actual change. A source-map entry is not proof of live enablement; check the owning code, feature configuration and deployment evidence when relevant.

## Other repositories

- [conference-manager-api/AGENTS.md](https://github.com/floriankreutzer/conference-manager-api/blob/main/AGENTS.md) owns backend work. The [shared test strategy](https://github.com/floriankreutzer/conference-manager-website/blob/main/docs/TEST-STRATEGY.md) is maintained in the public Website repository; the [API strategy path](https://github.com/floriankreutzer/conference-manager-api/blob/main/docs/TEST-STRATEGY.md) is a compatibility reference. Neither replaces each target repository's mandatory gates. Do not replace backend authorization or provider contracts with UI assumptions.
- [conference-manager-website/AGENTS.md](https://github.com/floriankreutzer/conference-manager-website/blob/main/AGENTS.md) owns public website development. Select `pavurel-web-design` there and follow its local source map.
- [conference-manager-developer/AGENTS.md](https://github.com/floriankreutzer/conference-manager-developer/blob/main/AGENTS.md) owns the public developer documentation. UI profiles do not authorize new API promises or publication of internal material.

Read each affected repository's own instructions for cross-repository work. Do not impose one repository's framework, release state or test commands on another.

## Verification provenance

This map was checked on 2026-10-24 against application `03cc888b434deaada756447359703a166cd85c23` and website `63c72fed1502bc43b4142900f87d052a8b967350`. Resolve current main on later use. Keep Confluence records, private URLs and operational evidence outside this public skill package.
