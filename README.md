# Pavurel Design Engineering Skills

A curated fork of [Emil Kowalski's design engineering skills](https://github.com/emilkowalski/skills), adapted for Pavurel's Conference Manager website, Customer application and Platform interface.

Use these profiles to locate and apply the target project's existing requirements. Specialists supply focused design and engineering methods. Read [AGENTS.md](AGENTS.md) when maintaining this collection.

## Delivery authority and documentation

Jira is authoritative for internal work management and delivery status. GitHub is authoritative for engineering implementation and native technical evidence: read the target repository's current `AGENTS.md`, applicable nested instructions and the central design, coding, architecture, security, content and test documents they reference. Existing central requirements remain in their owning repositories; profiles do not replace them or duplicate token values, role models, API contracts or release gates. Host instructions and the user's explicit decisions retain precedence.

Confluence documents durable decisions, rationale, procedures, source links and evidence. It does not supply a competing implementation contract. Reconcile documentation with accepted Jira/GitHub sources, distinguish open PRs from main and deployed behavior, and keep private documentation out of public repositories.

| Target | Authoritative entry | Profile |
| --- | --- | --- |
| Marketing website | [Website AGENTS.md](https://github.com/floriankreutzer/conference-manager-website/blob/main/AGENTS.md) | `pavurel-web-design` |
| Customer and Platform UI | [Application AGENTS.md](https://github.com/floriankreutzer/conference-manager/blob/main/AGENTS.md) | `pavurel-app-design` |
| Trusted backend/API | [API AGENTS.md](https://github.com/floriankreutzer/conference-manager-api/blob/main/AGENTS.md) | Repository requirements; UI profiles only for a separately scoped companion UI task |
| Public developer documentation | [Developer AGENTS.md](https://github.com/floriankreutzer/conference-manager-developer/blob/main/AGENTS.md) | Repository requirements; no implicit transfer of marketing or app rules |

When a profile/example conflicts with a current repository rule, follow the repository and identify the discrepancy. Do not weaken a rule to adopt a component. A reference to a profile does not install it.

For Pavurel icon work, follow the [canonical icon system](https://github.com/floriankreutzer/conference-manager/blob/main/docs/ICON-SYSTEM.md) and the target repository's design system. Read the linked versioned asset manifests before reuse; distinguish the asset draft from an integrated component. Keep Microsoft sign-in and other provider marks separate from Pavurel functional icons, using their original assets and owning guidance. These profiles locate the shared policy rather than maintaining another icon catalogue.

## All skills are mandatory within scope

The complete collection contains **20 skills**. [SKILL_POLICY.md](SKILL_POLICY.md) defines their required applicability and completion gate. There are no optional specialist installations or separate invocation requirements. Assess all catalog entries at the start of a task and apply every matching skill. Record each as **applied**, **not applicable with a concrete reason**, or **blocked**. Missing sources or tools must not be silently skipped or reported as a successful review.

For every Pavurel UI design-planning, implementation or review task, the required baseline is:

| Scope | Required skills |
| --- | --- |
| Marketing website | `pavurel-web-design`, `impeccable`, `design-taste-frontend`, `emil-design-eng`, `break-ui`, `mobile-native`, `21st-design-research` |
| Customer and Platform | `pavurel-app-design`, `impeccable`, `design-taste-frontend`, `emil-design-eng`, `break-ui`, `mobile-native`, `21st-design-research` |
| Further matching work | `apple-design`, `pick-ui-library`, `prototype`, `animate`, `review-animations`, `animation-performance`, `find-animation-opportunities`, `improve-animations`, `animation-vocabulary`, `ask-sonner`, `animate-expo`, `write-swift`, according to the full policy |

Use Impeccable's reference-only critique, usability, states and finishing guidance. Apply Taste to hierarchy, typography, spacing, copy and visual coherence, adapting it to operational screens or marketing pages as appropriate. Preserve the target brand, native components, approved content and architecture. Detailed surface guidance is bundled in each profile's `references/required-design-review.md`.

Mandatory scope does not require a technology migration: `write-swift` applies to actual Swift code, `animate-expo` to a React Native/Expo project, and `ask-sonner` to an existing or approved Sonner integration. They remain installed and assessed, with a concrete non-applicability reason for an incompatible web task. A decision to retain native components can complete `pick-ui-library`; a decision against additional motion can complete motion discovery. Decorative effects and unneeded runtime helpers remain task-dependent.

Each skill links a self-contained copy of the policy. Reuse sources already read for the same task and avoid recursive profile invocation. Current project standards and the user's task still govern what may change. Review-only work stays read-only; fixtures, previews, dependency changes, publishing and paid services require applicable authorization.

## Required 21st research

[21st-design-research](skills/21st-design-research/SKILL.md) is part of the Pavurel baseline. Frame a concrete component/layout question, discover the actually available connection and run focused read-only catalog search. Record relevant source IDs, URLs, provenance, architecture fit and known limitations. No separate request naming 21st is needed.

If the connection or required search is unavailable, mark that step **blocked** and continue independent work using existing project components. That fallback does not complete the 21st requirement. An actual relevant search with no suitable result is valid evidence. Source retrieval, hosted generation, installation and account changes remain distinct operations with their own scope, rights, entitlement and cost conditions. Installing this collection does not connect an account or add service calls to the shipped product.

## Install the complete reviewed collection

Creating or editing this repository does not automatically install skills in another project or deploy an application. Install the full catalog together to satisfy its source dependencies; invocation follows the applicability policy.

1. Clone this fork into a source directory and check out the approved full commit.
2. From the target project, run the pinned installer with all 20 named skills.
3. Choose **Project** at the installer's installation-scope prompt, inspect the resulting changes and preserve the project's existing conventions and instructions.

Replace the example paths and `REVIEWED_COMMIT_SHA` with the actual reviewed values:

```bash
git clone https://github.com/floriankreutzer/automatic-engineering-design-skills.git /path/to/design-skills
git -C /path/to/design-skills checkout --detach REVIEWED_COMMIT_SHA
git -C /path/to/design-skills rev-parse HEAD
cd /path/to/target-project
npx skills@1.7.4 add /path/to/design-skills \
  --agent codex \
  --skill pavurel-web-design \
  --skill pavurel-app-design \
  --skill impeccable \
  --skill design-taste-frontend \
  --skill emil-design-eng \
  --skill break-ui \
  --skill mobile-native \
  --skill 21st-design-research \
  --skill apple-design \
  --skill pick-ui-library \
  --skill prototype \
  --skill animate \
  --skill review-animations \
  --skill animation-performance \
  --skill find-animation-opportunities \
  --skill improve-animations \
  --skill animation-vocabulary \
  --skill ask-sonner \
  --skill animate-expo \
  --skill write-swift
```

All `agents/openai.yaml` files enable implicit invocation. This permits automatic task routing where the host supports that metadata; it does not enforce loading in every host or grant tools and permissions. If another supported agent is the target, choose it explicitly and inspect its equivalent invocation behavior. A partial installation leaves matching missing skills blocked.

CLI syntax and version were checked against the official [skills 1.7.4 source](https://github.com/vercel-labs/skills/tree/a80e4c9d12d607631249d4d7d059f835d4b2f13a). The installer has its own network and telemetry behavior; see its [documentation](https://github.com/vercel-labs/skills/blob/a80e4c9d12d607631249d4d7d059f835d4b2f13a/docs/troubleshooting.md). Review a CLI update deliberately instead of silently switching to `@latest`.

## Private ChatGPT plugin package

The versioned manifest in `packaging/pavurel-design/plugin.json` and the network-free Python 3 builder package **all 20 skills**, including their complete reviewed resources, agent metadata and policy references. `skill-catalog.json` defines the explicit full inventory. `required-design-skills.json` pins Impeccable and Taste editions and resource hashes. Both inventories are included in the archive and recorded in source provenance.

The full validation suite requires Python 3 and Node 22+ for offline icon-helper regression checks. The archive builder itself requires only Python 3 and does not execute imported helpers.

From a reviewed checkout, run the validation and build with its accepted full commit SHA:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/package_pavurel_plugin.py \
  --source-ref REVIEWED_COMMIT_SHA \
  --output dist/pavurel-design-1.1.0.zip
```

Verify that source inputs match that commit before building. The builder records the supplied ref and hashes; it does not independently authenticate the commit. It rejects catalog omissions, missing resources, divergent policy copies, incomplete routing tables, missing entrypoint policy links, disabled or ambiguous implicit invocation, invalid hashes, unsafe paths and symlink/source-overwrite hazards. Unlisted local files are excluded. Update the explicit inventory deliberately when resources change. Identical inputs produce the same archive with fixed ordering, timestamps and modes. Archives stay outside version control.

The package includes Taste's helper scripts and assets. The builder does not execute them, install a runtime, configure browser profiles or register hooks. Impeccable remains reference-only. Follow the policy and inspect helpers before any task-specific execution. Preserve original attribution and each imported license; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Save the inspected archive through the supported Plugin Creator account flow and verify the returned scope, skill inventory and stored contents. Preserve the existing private audience and account presentation metadata. Account storage, installation and availability in a new conversation are separate checks. Test realistic read-only website/application tasks and required research behavior, including missing-capability cases. GitHub remains authoritative; publishing this package does not establish automatic synchronization. Keep private identifiers, account receipts and Confluence URLs out of this public repository.

## Using the workflow

Naming the matching profile is enough to trigger the complete mandatory policy:

- “Use `$pavurel-web-design` to review the German and English pages for duplicate content and demo CTA placement without editing.”
- “Use `$pavurel-app-design` to improve the approved request-summary layout within the current application standards.”
- “Use `$prototype` to compare two navigation alternatives in an isolated preview.”
- “Use `$21st-design-research` to search for relevant review-panel patterns; do not retrieve code or generate variants.”

Directly invoking a specialist still applies the same catalog gate. Report actual sources, findings, project overrides and checks. Keep a compact complete coverage record in task or PR evidence; group related non-applicability reasons when communicating results. Do not claim runtime acceptance from source inspection or completion while an applicable requirement is blocked.

## Fork adaptations and maintenance

The fork started from upstream commit `2d228630ba1446365f614a108cb8252f1feda202`. The Pavurel adaptation:

- Adds website and application profiles with current central-source locators and dated verification provenance.
- Adds required 21st research with explicit missing-capability reporting and no implied account, spending or production-runtime authorization.
- Keeps GitHub development requirements authoritative and Confluence documentation linked to them.
- Makes project brand, architecture, accessibility and user scope explicit across the skills.
- Corrects visibility/focus, progressive enhancement, gesture zoom and prototype-isolation guidance.
- Makes Motion performance advice version-aware and review heuristics contextual.
- Corrects the prototype picker, Sonner option reference and identified native example errors.
- Packages the complete collection and makes all 20 skills mandatory within their scope, including reviewed Impeccable and Taste sources.

When updating from upstream, inspect the diff against these adaptations. Verify library advice against installed versions and primary documentation. Validate changed skill frontmatter, bundled relative links and examples that contain behavior; use realistic task checks for substantial instruction changes. Keep the policy, catalog, README and UI metadata aligned with the actual skills. Do not add production dependencies or publishing workflows merely to distribute Markdown skills.

The public source maps were checked on 2026-10-24 against website `63c72fed1502bc43b4142900f87d052a8b967350` and application `03cc888b434deaada756447359703a166cd85c23`. They point to current target-project sources instead of treating those snapshots as permanent specifications. Keep internal business and customer data outside this public repository.

Icon-routing references were reviewed separately on 2026-10-27 against the published application source [`a39664b20bef4d32a897577f0127bda74d86b28f`](https://github.com/floriankreutzer/conference-manager/commit/a39664b20bef4d32a897577f0127bda74d86b28f) in [PR #402](https://github.com/floriankreutzer/conference-manager/pull/402). This immutable reference records the inspected icon contract; the `main` links above locate its current owning source. Publication of the PR source alone does not establish merge, UI integration or deployment.

## Attribution and license

Original design engineering guidance by **Emil Kowalski**. The upstream work and examples remain credited; this fork adapts them for Pavurel and corrects the reviewed issues. See the original [skill collection](https://github.com/emilkowalski/skills) and [author's site](https://emilkowal.ski/skill).

The existing [MIT license](LICENSE) is retained. Keep its copyright and permission notice with copies or substantial portions. Impeccable retains Apache-2.0 and Taste retains MIT plus applicable asset credits; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
