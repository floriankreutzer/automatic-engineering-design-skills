# Pavurel Design Engineering Skills

A curated fork of [Emil Kowalski's design engineering skills](https://github.com/emilkowalski/skills), adapted for Pavurel's Conference Manager website, Customer application and Platform interface.

Use these profiles to locate and apply the target project's existing requirements. Specialists supply focused design and engineering methods. Read [AGENTS.md](AGENTS.md) when maintaining this collection.

## Development authority and documentation

GitHub is authoritative for development: read the target repository's current `AGENTS.md`, applicable nested instructions and the central design, coding, architecture, security, content and test documents they reference. Existing central requirements remain in their owning repositories; profiles do not replace them or duplicate token values, role models, API contracts or release gates. Host instructions and the user's explicit decisions retain precedence.

Confluence documents decisions, rationale, procedures, source links and evidence. It does not supply a competing development contract. Reconcile documentation with accepted GitHub sources, distinguish open PRs from main and deployed behavior, and keep private documentation out of public repositories.

| Target | Authoritative entry | Profile |
| --- | --- | --- |
| Marketing website | [Website AGENTS.md](https://github.com/floriankreutzer/conference-manager-website/blob/main/AGENTS.md) | `pavurel-web-design` |
| Customer and Platform UI | [Application AGENTS.md](https://github.com/floriankreutzer/conference-manager/blob/main/AGENTS.md) | `pavurel-app-design` |
| Trusted backend/API | [API AGENTS.md](https://github.com/floriankreutzer/conference-manager-api/blob/main/AGENTS.md) | Repository requirements; UI profiles only for a separately scoped companion UI task |
| Public developer documentation | [Developer AGENTS.md](https://github.com/floriankreutzer/conference-manager-developer/blob/main/AGENTS.md) | Repository requirements; no implicit transfer of marketing or app rules |

When a profile/example conflicts with a current repository rule, follow the repository and identify the discrepancy. Do not weaken a rule to adopt a component. A reference to a profile does not install it.

## Recommended website selection

Install the profile together with only the specialists you need. The initial website selection is:

| Skill | Purpose |
| --- | --- |
| [pavurel-web-design](skills/pavurel-web-design/SKILL.md) | Brand, customer questions, content ownership, demo CTA placement, qualified product/offer wording and Astro constraints. |
| [emil-design-eng](skills/emil-design-eng/SKILL.md) | General interaction craft and contextual motion decisions. |
| [break-ui](skills/break-ui/SKILL.md) | Long, missing and unusual content; synthetic stress cases when authorized. |
| [mobile-native](skills/mobile-native/SKILL.md) | Mobile web navigation, forms, touch, keyboard, zoom and native browser behavior. |
| [prototype](skills/prototype/SKILL.md) | A few comparable design variants in a preview excluded from production. |

Invoke the Pavurel profile for work on the marketing website and add a specialist only when its task fits. Installed skills are looked up by name; selective installation does not require copying the whole repository or assuming another skill is at a sibling path.

## Recommended Customer and Platform selection

| Skill | Purpose |
| --- | --- |
| [pavurel-app-design](skills/pavurel-app-design/SKILL.md) | Locate and apply current app standards, using separate Customer and Platform review references. |
| [emil-design-eng](skills/emil-design-eng/SKILL.md) | Form, action, feedback and interaction hierarchy. |
| [break-ui](skills/break-ui/SKILL.md) | Relevant synthetic data/state boundaries and robust layouts. |
| [mobile-native](skills/mobile-native/SKILL.md) | Mobile web forms, dialogs, keyboard, scrolling and zoom. |

Add `prototype` only for a concrete design choice and motion specialists only for a relevant task. The verified app architecture uses native ES modules; do not install React, Sonner, Expo or Swift tooling merely to follow an example. Read the current repository architecture on each later use.

## Optional 21st research

[21st-design-research](skills/21st-design-research/SKILL.md) adds a search-first research workflow for either UI profile. It discovers the tools actually available, records source provenance and adapts selected patterns to existing components and tokens. Source retrieval, hosted generation and installation are separate operations with their own scope, license, quota and cost checks.

The skill does not connect an account, install MCP software or add 21st calls to the product. A documented capability is not a tested connection. Existing repository components remain a valid fallback.

## Install a reviewed version of this fork

This repository contains instructions and reference examples. Creating or editing it does not automatically install the skills in another project or deploy an application.

1. Clone **this fork** into a source directory. Replace the example paths and `REVIEWED_COMMIT_SHA` with the approved full commit from the review.
2. Check out that exact commit and record it with the target project's skill update.
3. Run the pinned CLI from the **target project**, selecting the skills explicitly.

```bash
git clone https://github.com/floriankreutzer/automatic-engineering-design-skills.git /path/to/design-skills
git -C /path/to/design-skills checkout --detach REVIEWED_COMMIT_SHA
git -C /path/to/design-skills rev-parse HEAD
```

From the target project:

```bash
cd /path/to/conference-manager-website
npx skills@1.7.4 add /path/to/design-skills \
  --agent codex \
  --skill pavurel-web-design \
  --skill emil-design-eng \
  --skill break-ui \
  --skill mobile-native \
  --skill prototype
```

For Customer and Platform, run from their application checkout instead:

```bash
cd /path/to/conference-manager
npx skills@1.7.4 add /path/to/design-skills \
  --agent codex \
  --skill pavurel-app-design \
  --skill emil-design-eng \
  --skill break-ui \
  --skill mobile-native
```

For an authorized 21st research workflow, select `--skill 21st-design-research` separately using the same reviewed source checkout. Preserve existing installation conventions; do not configure an external account merely to install the Markdown instructions.

At the installer's **Installation scope** prompt, choose **Project** to install for the target project. Review the resulting changes before committing; preserve existing skills and instructions. Install an optional specialist with the same reviewed source path and its explicit `--skill` name.

The `agents/openai.yaml` policies for `prototype`, `pick-ui-library`, `review-animations` and `21st-design-research` preserve explicit invocation in Codex. If another supported agent is the target, choose it explicitly and configure its equivalent invocation policy; Codex metadata does not establish the same behavior in every host. See the target host's documentation, for example [Claude Code invocation controls](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill).

CLI syntax and version were checked against the official [skills 1.7.4 source](https://github.com/vercel-labs/skills/tree/a80e4c9d12d607631249d4d7d059f835d4b2f13a). The installer has its own network and telemetry behavior; see its [documentation](https://github.com/vercel-labs/skills/blob/a80e4c9d12d607631249d4d7d059f835d4b2f13a/docs/troubleshooting.md). Review a CLI update deliberately instead of silently switching to `@latest`.

## Private ChatGPT plugin package

The versioned manifest in `packaging/pavurel-design/plugin.json` and the network-free Python 3 builder package exactly three existing skills: `pavurel-web-design`, `pavurel-app-design` and `21st-design-research`. Their eleven source files are copied byte-for-byte, including references and agent metadata. Optional specialists remain separate. The original MIT license and attribution are included.

From a reviewed checkout of this repository, build the package with its full accepted commit SHA:

```bash
python3 scripts/package_pavurel_plugin.py \
  --source-ref REVIEWED_COMMIT_SHA \
  --output dist/pavurel-design-1.0.0.zip
```

Verify that the source inputs match that commit before building. The builder records the supplied source ref and hashes; it does not independently authenticate the commit. Its explicit file allowlist keeps unrelated skills and local files out of the package. Update that allowlist deliberately if a selected skill gains a required resource. Identical inputs produce the same archive with fixed entry ordering, timestamps and modes. Generated archives stay outside version control.

The private account package contains instructions and supporting files only. It adds no server, application runtime, account credentials or mandatory 21st connection. Preserve `21st-design-research`'s explicit-invocation policy. Its optional external research still requires the actual available tools and the user's task scope.

Save the inspected archive through the supported Plugin Creator account flow, then verify the returned scope, component inventory and installation state. Account storage, installation and availability in a new conversation are separate checks. Test the installed profiles with relevant read-only website and application tasks and a requested search-only 21st task. GitHub remains authoritative for development; copying this package does not establish automatic GitHub-to-account synchronization. Keep private plugin identifiers, account receipts and Confluence URLs out of this public repository.

## Optional specialists

| Skill | Use when |
| --- | --- |
| [animate](skills/animate/SKILL.md) | A justified transition or feedback animation needs implementation. |
| [animation-performance](skills/animation-performance/SKILL.md) | An observed animation problem needs diagnosis against the installed version and target browsers. |
| [review-animations](skills/review-animations/SKILL.md) | Existing motion needs a contextual review; function and accessibility come first. |
| [find-animation-opportunities](skills/find-animation-opportunities/SKILL.md) | A focused review may identify a small number of useful motion opportunities. |
| [improve-animations](skills/improve-animations/SKILL.md) | A larger application needs an organized audit and implementation plan. |
| [animation-vocabulary](skills/animation-vocabulary/SKILL.md) | A motion effect needs a precise shared name. |
| [apple-design](skills/apple-design/SKILL.md) | Selected interaction principles help a web task; the target brand retains priority over Apple aesthetics. |
| [pick-ui-library](skills/pick-ui-library/SKILL.md) | A real requirement calls for a library after checking the existing stack and native options. |
| [ask-sonner](skills/ask-sonner/SKILL.md) | The project actually uses or has approved Sonner; verify its installed types. |
| [animate-expo](skills/animate-expo/SKILL.md) | A separate React Native / Expo project needs native motion. |
| [write-swift](skills/write-swift/SKILL.md) | A separate Swift project needs toolchain-specific guidance. |

## How to use the selection

Examples:

- “Use `$pavurel-web-design` to review every German and English page for duplicate content and demo-request links. Report findings without editing.”
- “Use `$pavurel-web-design` and `$mobile-native` to implement the approved mobile navigation improvement within the existing Astro components.”
- “Use `$pavurel-web-design` and `$prototype` to compare two integration-overview layouts in a local preview.”
- “Use `$pavurel-web-design` and `$break-ui` to check the request form with long company names and missing optional values.”
- “Use `$pavurel-app-design` and `$mobile-native` to review the existing request wizard in German and English without editing.”
- “Use `$pavurel-app-design` to implement the approved Platform status-summary improvement using existing components and the current repository rules.”
- “Use `$21st-design-research` to search for relevant review-panel patterns. Return up to three source references; do not retrieve code or generate variants.”

A review-only request stays read-only. An implementation request permits the necessary scoped edits and checks without repeating approval for already authorized work. Fixtures, previews and library changes remain subject to the actual task and target-project rules. Keep publication and merge decisions within the user's authorization.

## Fork adaptations and maintenance

The fork started from upstream commit `2d228630ba1446365f614a108cb8252f1feda202`. The Pavurel adaptation:

- Adds website and application profiles with current central-source locators and dated verification provenance.
- Adds optional 21st research without a framework, account or runtime dependency.
- Keeps GitHub development requirements authoritative and Confluence documentation linked to them.
- Makes project brand, architecture, accessibility and user scope explicit across the skills.
- Corrects visibility/focus, progressive enhancement, gesture zoom and prototype-isolation guidance.
- Makes Motion performance advice version-aware and review heuristics contextual.
- Corrects the prototype picker, Sonner option reference and identified native example errors.
- Preserves the original collection for separately scoped tasks without installing it all by default.

When updating from upstream, inspect the diff against these adaptations. Verify library advice against installed versions and primary documentation. Validate changed skill frontmatter, bundled relative links and examples that contain behavior; use realistic task checks for substantial instruction changes. Keep README selection and UI metadata aligned with the actual skills. Do not add production dependencies or publishing workflows merely to distribute Markdown skills.

The public source maps were checked on 2026-10-24 against website `63c72fed1502bc43b4142900f87d052a8b967350` and application `03cc888b434deaada756447359703a166cd85c23`. They point to current target-project sources instead of treating those snapshots as permanent specifications. Keep internal business and customer data outside this public repository.

## Attribution and license

Original design engineering guidance by **Emil Kowalski**. The upstream work and examples remain credited; this fork adapts them for Pavurel and corrects the reviewed issues. See the original [skill collection](https://github.com/emilkowalski/skills) and [author's site](https://emilkowal.ski/skill).

The existing [MIT license](LICENSE) is retained. Keep its copyright and permission notice with copies or substantial portions.
