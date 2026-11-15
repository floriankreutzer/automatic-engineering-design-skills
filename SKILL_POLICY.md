# Mandatory design skill policy

All skills in this collection are mandatory within their defined scope. None is
an opt-in specialist. At the start of a task, assess the complete catalog below,
load every applicable skill, and apply its relevant guidance. The user does not
need to name each skill. A skill being required does not make every example,
visual effect, helper script or external operation appropriate.

## Authority and resolution

Read the target repository's current root and nested `AGENTS.md` files and their
required standards first. Host instructions, the user's actual scope and current
project requirements govern brand, architecture, content, security, accessibility
and tests. Keep those requirements in their owning repository. Preserve read-only
requests; mandatory skill use does not authorize edits, new dependencies, paid
generation, account setup, publication or a different technology stack.

Resolve skills by installed name, preferably from the same reviewed Pavurel
Design release. If discovery is unavailable, inspect their actual files in the
same reviewed source checkout or package. Verify the files rather than assuming
sibling paths in an unrelated installation. Read each applicable `SKILL.md` and
its relevant references; a name mention is not evidence that a skill was used.
Reuse matching sources already read in this task. Never recursively reload a
profile or another skill that has already supplied its guidance.

The explicit source inventory is `packaging/pavurel-design/skill-catalog.json`
in the repository and `skill-catalog.json` at the plugin root. Imported editions
and hashes are in the adjacent `required-design-skills.json`. Do not silently
replace reviewed sources with a different upstream version. This policy is
copied into each skill's `references/skill-policy.md` so individual entrypoints
retain the full routing contract; package validation checks that copies agree.

## Required applicability catalog

For every Pavurel website or Customer/Platform design-planning, implementation
or review task, the baseline is the matching Pavurel profile plus `impeccable`,
`design-taste-frontend`, `emil-design-eng`, `break-ui`, `mobile-native` and
`21st-design-research`. Apply them at a depth proportional to the actual task.
Assess the remaining skills against the triggers below as well. Non-design
backend or repository-maintenance work does not acquire an unrelated UI task.

| Skill | Required when | Application boundary |
| --- | --- | --- |
| `pavurel-web-design` | Pavurel marketing website design, content/layout, implementation or review | Use current website standards and Astro architecture. |
| `pavurel-app-design` | Conference Manager Customer or Platform interface design, implementation or review | Keep operational state, role, API and native-component contracts. |
| `impeccable` | Visual or interaction design, planning, critique or refinement; always in the Pavurel baseline | Use the included reference-only edition, with no engine or hooks. |
| `design-taste-frontend` | Visual/content design, planning, critique or refinement; always in the Pavurel baseline | Adapt hierarchy, typography, spacing and copy to the surface; preserve approved brand and truthful content. |
| `emil-design-eng` | UI interaction craft, hierarchy, feedback, implementation or review; always in the Pavurel baseline | Apply principles within existing components and accessibility rules. |
| `break-ui` | UI layout/content/state planning, implementation or review; always in the Pavurel baseline | Assess relevant edge cases; only create synthetic fixtures when edits are authorized. |
| `mobile-native` | Responsive web, touch, forms, navigation, viewport or mobile behavior; always in the Pavurel baseline | Assess mobile implications; distinguish source/emulation checks from real-device evidence. |
| `21st-design-research` | UI design or component/layout decisions; always in the Pavurel baseline | Perform focused read-only catalog research through an available authorized connection; record a blocker if unavailable. |
| `apple-design` | Interaction, typography, gesture, continuity or platform-affordance design/review | Apply relevant principles without importing Apple's visual identity or requiring effects. |
| `pick-ui-library` | Choosing or reviewing an implementation approach for frontend behavior or dependencies | Evaluate native/existing options first; a decision to add no library satisfies the method. |
| `prototype` | A consequential design choice has unresolved alternatives, or comparing variants is in scope | Compare alternatives; build isolated previews only within authorized implementation/exploration. |
| `find-animation-opportunities` | UI exploration or polish includes orientation, feedback or motion opportunities | Read-only discovery can conclude that no new motion is useful. |
| `animate` | Designing or implementing a web transition, animation or motion feedback | Decide first whether static/immediate behavior is better; no animation quota. |
| `review-animations` | Existing or changed web motion/interaction is being reviewed | Check correctness, access, interruption and project fit; retain read-only scope. |
| `animation-performance` | Web motion is implemented/reviewed, a property/tool is selected, or jank needs diagnosis | Inspect the actual execution path; label unmeasured concerns and use available evidence. |
| `improve-animations` | Motion is reviewed or improved across multiple components or a broader codebase | Organize evidenced findings and the scoped plan; no gratuitous whole-repo audit. |
| `animation-vocabulary` | A motion effect needs to be named, specified or communicated precisely | Use terminology without treating an effect's name as a reason to add it. |
| `ask-sonner` | An existing or approved Sonner integration is implemented or reviewed | Verify the actual installed version; do not introduce React/Sonner merely to activate this skill. |
| `animate-expo` | An actual React Native/Expo project needs motion, gesture or related performance work | Keep native tooling confined to that native project. |
| `write-swift` | Actual Swift code is written, reviewed, migrated or diagnosed | Check the real compiler/SDK; do not introduce Swift into a web project. |

An incompatible technology is a concrete non-applicability reason. Lack of an
installed skill, a connector, time or explicit invocation is not. No separate
opt-in is required for an applicable skill. A single review may apply several
skills together; it need not repeat the same finding in separate audits.

## Missing sources, tools and constrained operations

If an applicable source cannot be read, mark it **blocked**, identify the missing
source and continue independent authorized work. Do not mark it optional,
substitute a different skill, or claim the required design gate is complete.
Do not invent an unavailable tool or ask for permission already supplied.

For 21st, frame a concrete component/layout question and discover the connection
actually exposed by the host. Respect a search-only request. If search is
unavailable or disallowed, record the research as blocked and use the target's
existing components for independent work; this fallback does not count as a
successful 21st pass. An empty but real, relevant search is valid evidence.
Code retrieval, hosted generation, installers and account changes still need
their own applicable scope, license, entitlement and cost conditions.

Impeccable has no executable runtime in this collection. Taste's reviewed helpers
and assets are available for suitable tasks; loading its guidance does not
require running every helper. Read a helper before use, respect active tool
rules and use authorized previews with fresh disposable browser profiles only.
Some helpers remove their supplied profile directory. Never use a personal or
existing browser profile or run kit-maintenance commands as ordinary UI work.
Missing helper dependencies do not prevent a guidance pass, but required target
tests or a requested runtime check must remain explicitly unverified/blocked.

For reviews, inspect and report without creating fixtures or changing code/data.
For implementation, complete already authorized work and the target's required
tests. Do not force stock photographs, decorative motion, randomized palettes,
marketing layouts, extra libraries or native frameworks into an incompatible
surface. A documented project override applies to a recommendation; it does not
make the applicable skill optional or waive an unrelated project gate.

## Completion record

Maintain one compact coverage record for the complete catalog, using only:

- **Applied:** identify the reviewed source, relevant guidance, decision and
  evidence actually examined. An unchanged design can be a supported outcome.
- **Not applicable:** give a concrete task/surface/technology reason. Related
  exclusions may be grouped as long as every skill is named. Baseline skills
  cannot be excluded from a Pavurel UI design task for convenience.
- **Blocked:** name the unavailable required source, connection, permission or
  check, its impact and the remaining work. This is not a passing result.

The skill gate is complete only when all applicable skills are applied and the
catalog has no unexplained omission or unresolved applicable blocker. The target
repository's tests and acceptance rules also govern implementation completion.
Planning/review evidence does not prove implementation, browser acceptance or
deployment. This is a workflow contract and a validated package inventory; it
cannot make a host load missing sources or grant unavailable capabilities.
