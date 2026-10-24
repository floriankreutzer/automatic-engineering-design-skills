# Pavurel Design Engineering Skills

A curated fork of [Emil Kowalski's design engineering skills](https://github.com/emilkowalski/skills), adapted for Pavurel's Conference Manager website.

Use these skills to improve understandable sales pages, consistent brand presentation, accessible interactions and robust mobile behavior. The Pavurel profile supplies the project context; specialist skills handle a particular design or engineering task. Existing user decisions and target-project instructions take precedence over the collection's defaults.

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

## Install a reviewed version of this fork

This repository contains instructions and reference examples. Creating or editing it does not automatically install the skills in another project or deploy the website.

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

At the installer's **Installation scope** prompt, choose **Project** to install for the target project. Review the resulting changes before committing; preserve existing skills and instructions. Install an optional specialist with the same reviewed source path and its explicit `--skill` name.

The three `agents/openai.yaml` policies for `prototype`, `pick-ui-library` and `review-animations` preserve explicit invocation in Codex. If another supported agent is the target, choose it explicitly and configure its equivalent invocation policy; Codex metadata does not establish the same behavior in every host. See the target host's documentation, for example [Claude Code invocation controls](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill).

CLI syntax and version were checked against the official [skills 1.7.4 source](https://github.com/vercel-labs/skills/tree/a80e4c9d12d607631249d4d7d059f835d4b2f13a). The installer has its own network and telemetry behavior; see its [documentation](https://github.com/vercel-labs/skills/blob/a80e4c9d12d607631249d4d7d059f835d4b2f13a/docs/troubleshooting.md). Review a CLI update deliberately instead of silently switching to `@latest`.

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

A review-only request stays read-only. An implementation request permits the necessary scoped edits and checks without repeating approval for already authorized work. Fixtures, previews and library changes remain subject to the actual task and target-project rules. Keep publication and merge decisions within the user's authorization.

## Fork adaptations and maintenance

The fork started from upstream commit `2d228630ba1446365f614a108cb8252f1feda202`. The Pavurel adaptation:

- Adds a self-contained website profile with a dated public source map.
- Makes project brand, architecture, accessibility and user scope explicit across the skills.
- Corrects visibility/focus, progressive enhancement, gesture zoom and prototype-isolation guidance.
- Makes Motion performance advice version-aware and review heuristics contextual.
- Corrects the prototype picker, Sonner option reference and identified native example errors.
- Preserves the original collection for separately scoped tasks without installing it all by default.

When updating from upstream, inspect the diff against these adaptations. Verify library advice against installed versions and primary documentation. Validate changed skill frontmatter, bundled relative links and examples that contain behavior; use realistic task checks for substantial instruction changes. Keep README selection and UI metadata aligned with the actual skills. Do not add production dependencies or publishing workflows merely to distribute Markdown skills.

The Pavurel profile's public baseline was checked on 2026-10-24 against website commit `63c72fed1502bc43b4142900f87d052a8b967350`. It points to current target-project sources instead of treating that snapshot as a permanent product specification. Keep internal business and customer data outside this public repository.

## Attribution and license

Original design engineering guidance by **Emil Kowalski**. The upstream work and examples remain credited; this fork adapts them for Pavurel and corrects the reviewed issues. See the original [skill collection](https://github.com/emilkowalski/skills) and [author's site](https://emilkowal.ski/skill).

The existing [MIT license](LICENSE) is retained. Keep its copyright and permission notice with copies or substantial portions.
