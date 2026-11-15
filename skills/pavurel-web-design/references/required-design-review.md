# Required design review

## Scope and authority

Follow [the mandatory full-catalog policy](skill-policy.md) for every task.
This reference details the Impeccable and Taste passes within that larger gate;
it does not replace the other required skills. For every design-planning,
implementation or review task using a Pavurel profile, load and apply both
`impeccable` and `design-taste-frontend` without a separate user invocation. Pure backend, infrastructure or other non-design
work does not acquire an unrelated design task through this rule.

First read the target repository's current instructions and required standards.
Host instructions, the user's scope and current target requirements retain
precedence over both supporting skills. Keep brand constants, architecture,
content contracts and test gates in their owning project.

## Resolve and read the required sources

1. Find `impeccable` and `design-taste-frontend` by installed name. Prefer the
   copies in the same reviewed Pavurel Design release. Read each `SKILL.md` and
   the references applicable to the requested surface; merely mentioning a name
   does not satisfy this requirement.
2. If installed discovery is unavailable, inspect the actual named skill files
   in the same reviewed source checkout or package. This repository provides
   `skills/impeccable/SKILL.md` and `skills/design-taste-frontend/SKILL.md`.
   Verify that those files exist and match the reviewed source; do not assume a
   sibling folder in another installation or silently fetch a newer upstream.
3. Use the source editions recorded in
   `packaging/pavurel-design/required-design-skills.json` in the repository,
   or `required-design-skills.json` at the packaged plugin root. A compatible
   already-loaded copy is reusable when its identity and reviewed provenance
   match. Avoid repeated reads within the same task and source scope.
4. Follow references relative to their actual skill directory. Do not re-enter
   the calling Pavurel profile when a supporting skill refers back to it;
   the target requirements and profile have already been established.
5. If either required source cannot be read, state which one is missing. Continue
   independent authorized investigation or other work, but do not finalize new
   design decisions or claim the required design review is complete. Do not
   replace the missing source with 21st research or invent its contents; 21st has
   its own mandatory research requirement in the full-catalog policy.
   A missing source is not a request for a redundant approval or unrelated setup.

## Apply both passes to the actual surface

| Surface | Impeccable contribution | Taste contribution | Constraints to retain |
| --- | --- | --- | --- |
| Customer or Platform UI | Operational clarity, action hierarchy, states, usability, responsive layout and finishing | Typography, grouping, spacing, copy precision, visual coherence and avoidance of generic UI | Existing native components, roles, tenant context, status/API contracts, translations and functional icons |
| Marketing website | Page critique, usability, hierarchy, accessibility, responsive behavior and finishing | Composition, type, meaningful imagery, copy and consistent visual direction | Approved brand, truthful claims, offer qualifications, legal/contact content, CTA ownership and Astro architecture |
| Planning or read-only review | Explain evidence, choices, priorities and limitations | Evaluate applicable visual and content choices within the brief | Preserve read-only scope; do not create fixtures, run mutations or invent observed findings |

Every scoped task receives both passes, including a small refinement. Scale the
depth to the task. A supporting recommendation may be overridden by a specific
project requirement; identify that requirement and the resulting decision.
Do not mark an entire supporting skill optional merely because one aesthetic
default does not fit.

In operational UI, do not require marketing heroes, stock photographs, randomized
palettes, full-screen sections or decorative motion. On the website, do not
remove required captions, contact/legal details or approved colours to satisfy
a generic house rule. Use the target's accessibility, security and content
requirements to resolve conflicts.

## Keep guidance and runtime checks distinct

The included Impeccable edition is reference-only: it provides no external
engine, automatic detector, hooks or live browser editing. Do not claim those
features ran or install them to satisfy this review.

Taste includes its reviewed helper scripts and assets. Reading and applying its
guidance is mandatory; running every helper or copying its asset kit is not.
Read a helper before task-specific use, follow the active tool and permission
rules, and use authorized local fixtures/previews with fresh disposable browser
profiles. A helper may remove its supplied profile directory. Never supply an
existing user profile or treat kit-maintenance commands as page-design steps.

Missing Node, a compatible browser or network access does not prevent reading
the available design guidance. Use permitted source/manual checks and report
which automation could not run. Preserve repository-required checks and do not
claim runtime acceptance from source inspection alone.

## Record the gate honestly

In the task's existing review or implementation result, record a compact entry
for each required skill:

| Required skill | Source and edition read | Applicable guidance and decisions | Actual checks and limitations |
| --- | --- | --- | --- |
| `impeccable` | Reviewed reference-only source | Relevant findings, refinements or justified unchanged choices | Evidence actually examined; no invented engine result |
| `design-taste-frontend` | Reviewed Taste source | Relevant visual/content findings and project-specific overrides | Checks actually performed; distinguish guidance from executed helpers |

These two passes are complete only when both sources were read and their
applicable guidance was assessed. The full design gate additionally requires
every other applicable catalog entry and an explicit complete coverage record,
with no unresolved applicable source or research blocker. For implementation, the target repository's
required tests and unresolved findings also govern completion. For planning,
completion means a supported plan, not an implemented or browser-tested result.
This workflow is an instruction contract; a repository cannot force a host to
load an unavailable skill or grant additional tools and permissions.
