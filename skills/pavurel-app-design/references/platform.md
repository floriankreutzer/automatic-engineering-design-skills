# Platform Operator review

Use the current operator contracts, security sources and artifact rules identified in [repository-sources.md](repository-sources.md). This reference is a workflow aid, not a parallel authorization or operations policy.

## Establish the operator context

Identify the actual environment, operator capabilities and target tenant of the task. Read the relevant `src/platform-admin/` composition and API adapters. Do not confuse them with cross-cutting Customer infrastructure under `src/platform/`.

Customer and Platform may reuse approved visual primitives while retaining their independently governed origins, sessions, APIs, audit and deployment boundaries. Derive the applicable controls from current source; do not add or remove an operational confirmation because a design example is simpler.

## Review useful work units

| Unit | Inspect | Questions |
| --- | --- | --- |
| Customer directory | Current filtering, representation, empty results and pagination | Are customer identity and state easy to compare? What happens with long names, missing optional status and additional pages? |
| Customer detail and operations | Target context, available actions, confirmation, pending/error/completion | Is the effect clear before activation? Is an unknown result distinguished from failure? Does retry follow the actual operation contract? |
| Insights and provider status | Source identity, observation time, freshness, completeness and fallback | Can the operator distinguish missing, stale and last-known information? Are unavailable values kept distinct from zero? |
| Navigation and access | Session gate, keyboard navigation, step-up/passkey presentation and expiry | Does focus remain meaningful? Does visual polish preserve the existing authentication and authority boundary? |

At the verified baseline, the directory in `src/platform-admin/application.js` is a filterable card list with cursor pagination. Do not describe it as a table or redesign it implicitly. The current insight tabs and source-status modules already provide semantics and source context; preserve these while improving presentation.

## Preserve state during updates

Inspect the real asynchronous lifecycle. Keep the selected section/tab and a meaningful focus destination across authorized refreshes. Do not let late replies reopen a departed screen, expose old protected content or announce success before the governing contract confirms it.

Keep persistent operational status separate from temporary notices. Preserve existing target/effect/reason fields and additional confirmations for sensitive operations. Tooling or prototype data cannot grant operator authority.

## Validate the relevant boundary

Use synthetic tenants and mocked operations in isolated previews. Never send real invitations, reset an environment or invoke production provider operations as a side effect of design research.

Test the affected interaction using the repository's current requirements, including keyboard, relevant locales, narrow layouts and data-state cases. State whether evidence comes from source inspection, executed tests, browser/device behavior or a named deployment. A well-rendered dashboard does not establish system health or release acceptance.
