# Customer workflow review

Use the current repository role model, design system, capability contracts and tests identified in [repository-sources.md](repository-sources.md). This reference supplies review questions, not an alternative feature or permission specification.

## Establish the actor and the workflow

Identify the server-derived Employee, Conference Manager or Tenant Admin capabilities involved. Check the current role/field ownership instead of inferring permissions from a menu, title or proposed design. Include the actual combined-role case when relevant.

| Surface | Inspect in the existing implementation | Useful review questions |
| --- | --- | --- |
| Employee request | Request editor, room/availability presentation, services, catering, cost allocation, review and draft lifecycle | Are missing inputs understandable? Is the next action clear? Does the review reflect current selections? What survives navigation, retry or interruption? |
| Conference Manager | Worklist, filters, decisions, change review, room planning, reports and business settings | Can the operator identify the work item, current status and available action? Are changes and conflicts understandable without relying only on color? |
| Tenant Admin | Settings shell, section registry, organization, users/roles, integrations and audit | Are configuration scope and consequences clear? Do validation and recovery preserve entered data where the contract permits? Is another role's responsibility kept separate? |

At the verified baseline, representative entry files include `src/employee/production-application.js`, `src/manager/production-application.js` and `src/tenant-admin/settings-shell.js`. Follow public capability APIs and recheck their current ownership before editing.

## Inspect transitions as well as screens

Trace a complete bounded task: create or resume an input, review it, submit, observe the response and return to ongoing work. Include server rejection, a changed revision, unavailable data and navigation while a response is pending when relevant. Preserve the actual draft and lifecycle contracts; a visual cleanup must not add storage or silently abandon a workflow.

Use existing labels and status definitions. Confirmed business state, requested work and provider response must retain their actual meaning. If the user requests a new approval rule or provider behavior, treat it as a separately scoped product/API change, not a design improvement.

## Exercise representative boundaries

Use existing test fixtures and canonical Demo scenarios before creating new synthetic cases. Select cases tied to the change: longer translated labels, empty/large lists, missing optional values, boundary quantities, failed reads, stale data or revoked authority. Do not manufacture invalid business values merely to produce a visual failure.

Preserve semantic responsive representations. Review table/card equivalence, bounded calendar scrolling, reachable form actions, keyboard focus and mobile keyboard behavior against the current design system. Read existing focus, role, responsive and asynchronous regression tests; add coverage only for a concrete new risk.

Keep optional imagery purposeful, such as a governed room preview. Route any external component research through the repository's existing dependency, privacy and asset rules.
