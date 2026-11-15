---
name: impeccable
description: "Design guidance adapted from Impeccable for reviewing, planning and improving websites, application screens, dashboards, forms and components. Use for critique, UI quality audits, polish, typography, layout, color, responsive behavior, UX copy, onboarding, resilient states and purposeful motion. This edition provides reference workflows only; it has no Impeccable runtime or automatic detector."
---

# Impeccable Design

## Mandatory skill routing

Read and follow [the mandatory skill policy](references/skill-policy.md) before
this workflow. Assess the complete catalog, load and apply every relevant skill
without waiting for a separate request, and record applied, not-applicable or
blocked coverage. Reuse matching sources already read; do not recurse between
profiles. User scope and current project requirements remain authoritative.

A reference-only adaptation of Paul Bakaus's [Impeccable](https://github.com/pbakaus/impeccable), version 4.9.1, revision `2b86d9c07b97d4bed7de23583e1bd1e58dd2baae`. Modified on 15 November 2026: reorganized and paraphrased the design guidance for use through the host's existing tools. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).

This edition contains design knowledge and manual workflows. It does not install or provide the upstream engine, automatic detector, command shortcuts, hooks, live browser editing, external agents or background services. Do not report those capabilities as available. The workflow names below identify design tasks, not executable commands.

## Start with the actual product

1. Read the applicable repository AGENTS.md and the current target before proposing or changing code. Follow its architecture, testing, accessibility and design requirements.
2. Read existing product context, design documentation, tokens, shared components and nearby screens. Missing documentation does not mean that the product has no established identity.
3. Resolve the requested outcome, audience, scope and evidence. Reuse settled decisions; ask only about a material ambiguity that cannot be resolved from the brief or repository.
4. Preserve the user's requirements, factual content and approved brand. For Pavurel work, apply the relevant Pavurel Design skill and its established brand alongside this guidance.
5. Select the appropriate workflow below. Use only tools already available and authorized for the task. This skill requires no additional software or setup.

## Select the surface's mode

| Mode | Visitor's goal | Design priority |
|---|---|---|
| Operate | Complete a task in an app, dashboard, form or admin screen | Clear state, familiar controls, efficient paths, consistent components |
| Read | Understand documentation, an article or help content | Comprehension, navigation, readable type and stable structure |
| Persuade | Evaluate an offer and decide what to do | Clear proposition, truthful evidence, deliberate hierarchy and action |
| Experience | Explore a portfolio, gallery or expressive work | Let the work lead; make navigation understandable and unobtrusive |

Choose the mode per surface. A product's marketing page and its booking form have different jobs. Scale expression to that job; an operational interface earns quality through precision and familiarity.

## Choose a workflow

| Request | Read |
|---|---|
| Critique, audit or prioritize UI findings | [Review and evidence](references/review.md) |
| Typeset, layout, colorize or adapt | [Visual foundations](references/visual-foundations.md) |
| Harden, clarify or onboard | [States, content and resilience](references/states-and-content.md) |
| Shape a new surface, redesign, document or extract a design system | [Planning and design systems](references/planning-and-systems.md) |
| Animate, delight, make bolder, quieter or simpler | [Expression and motion](references/expression-and-motion.md) |
| Polish, optimize or verify completion | [Finish and verify](references/finish-and-verify.md) |

Read only the references needed for the request. A review produces findings; implementation follows the user's requested scope. Refinement preserves the established visual language. A redesign changes that language only when requested, while preserving product truth and required behavior.

## Apply the quality floor

Make the primary task and current state clear. Group related content through proximity and hierarchy before adding containers. Use existing semantic tokens, components, type roles and icon conventions. Give controls complete interaction and recovery states. Preserve keyboard access, visible focus, reading order, text scaling and adequate contrast.

Use real or clearly labeled illustrative content. Do not invent commercial claims, security assurances, customer logos or operating data. Keep meaningful labels available when icons or color carry information.

Inspect the rendered result at representative sizes and with realistic content when the environment supports it. Source review and screenshots are useful evidence but do not prove complete interaction or accessibility coverage. State the limits of the evidence used.

## Deliver a concrete result

Lead with the outcome. For findings, identify the affected target, observed behavior, user impact, priority, proposed fix and evidence. For changes, explain what changed, why, how it was checked and what remains unresolved. Run the repository's required validation and relevant regression and progression checks when changing code; report only checks that actually ran.
