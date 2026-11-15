# Design Skills Repository Instructions

Read this file and `README.md` before reviewing or changing this collection. Preserve the original attribution and license. Keep repository instructions and skill bodies in English.

## Authority and scope

- Jira owns internal work management and delivery status for Conference Manager; GitHub owns engineering requirements, source code and native technical evidence. In a target project, read its current root `AGENTS.md`, applicable nested instructions, and the central design, coding, architecture, security, content and test sources they reference. These sources take precedence over every profile, specialist, example and external component in this collection, subject to host instructions and the user's explicit decisions.
- Keep those existing central requirements in their owning repositories. Profiles describe how to apply and find them; do not transfer or duplicate normative token values, role matrices, publication rules, test gates or API contracts into skills.
- Confluence documents decisions, rationale, procedures, source links and evidence. It does not override GitHub development requirements. A documented proposal is not merged implementation or a release approval. Follow the space's documentation governance when actually editing Confluence.
- Resolve the current accepted `main` and the exact work ref. Use the checkout's applicable instructions for the change, identify unmerged proposals explicitly, and report relevant discrepancies. Do not overwrite newer decisions with a dated skill snapshot.
- When a skill conflicts with a current target requirement, follow the target requirement and report or fix the skill within the authorized scope. Do not weaken project gates to accommodate a skill. Ask only about a genuinely unresolved product or authority decision.
- Skill maintenance, installation in a target repository, application implementation, merge and deployment are separate actions. Perform only what the user's task authorizes; do not repeat approval already supplied.

## Profile and reference maintenance

- Route marketing website work to `pavurel-web-design`; route authenticated Customer and Platform UI work to `pavurel-app-design`. Keep backend/API and developer-documentation ownership with their own repositories.
- Every skill in this repository is mandatory when its scope applies. Read `SKILL_POLICY.md`, assess the complete catalog and load/apply each relevant skill without a separate user opt-in. For Pavurel UI design tasks, use its defined baseline and all other matching specialists. Keep a complete applied/not-applicable/blocked coverage record; unavailability is not non-applicability.
- Keep each skill's `references/skill-policy.md` byte-identical to the root policy. Resolve required skills by installed name from the reviewed release or inspect actual files in the same reviewed checkout; do not assume arbitrary sibling paths. A name mention does not install or load a skill. Missing applicable sources or required research leave the skill gate incomplete; continue independent authorized work and report the blocker.
- Use the accepted Impeccable reference-only edition and reviewed Taste snapshot. Mandatory skill use does not authorize every helper, effect, engine, hook, account, browser profile, paid operation, framework or runtime. Preserve application behavior and architecture and all current brand, content, accessibility, security and test requirements.
- Keep source maps as locators and dated verification evidence, not parallel specifications. Prefer current central source links for instructions and immutable refs for evidence.
- Apply `21st-design-research` as required by the policy, starting with focused read-only search through the actual available connection. If unavailable, report that required step as blocked instead of silently skipping it. Preserve source/license provenance and adapt patterns to the target architecture. Search does not authorize installation, paid generation or production dependencies.
- Do not commit private Confluence URLs, credentials, customer records, account balances, internal provider evidence or other unnecessary internal material to this public repository.

## Validation and delivery

Read each existing file before editing it. Keep changes bounded and preserve unrelated work. Validate changed skill frontmatter, names, bundled references and agent metadata; check Markdown and diffs. Forward-test substantial instruction changes using realistic tasks and minimal context. Execute behavioral examples when their code changes; do not claim application/browser tests ran when only instructions changed. Use Python 3 and Node 22+ for the full validation suite; imported-helper behavior tests must use offline synthetic inputs.

When changing the collection or its package, update the full catalog in `packaging/pavurel-design/skill-catalog.json` and the imported-resource lock in `packaging/pavurel-design/required-design-skills.json` deliberately. Every skill must have implicit invocation enabled, a policy link and the matching bundled policy. Package all catalogued skills and necessary resources; reject an omitted or unreviewed entrypoint. Preserve upstream revisions, editions, all necessary resources and per-source licenses. Do not copy host-generated account metadata into this public source. Run `python3 -m unittest discover -s tests -v` and build with `python3 scripts/package_pavurel_plugin.py --source-ref REVIEWED_COMMIT_SHA --output dist/pavurel-design-1.1.0.zip` using the actual reviewed full commit. The builder checks resource hashes and package boundaries without executing the imported helpers. Check imported executable syntax and run relevant behavior tests whenever those executables change.

Record exact reviewed refs and actual checks in the pull request. Keep installed, proposed, merged and deployed states distinct. Use the existing pull-request workflow; do not bypass reviews, checks or cost controls. Save completed skill changes in this Git repository and synchronize the reviewed branch before reporting them saved.

## Automatic engineering knowledge workflow

For engineering tasks performed for the repository owner, use the available
`use-agent-knowledge` skill by default, without waiting for a separate reminder.
This owner-agent workflow is supplementary; it is not a dependency for external
contributors or API consumers.

1. Read this repository's current required instructions and standards first.
   With the existing authorized GitHub connection, resolve the current default
   branch of `floriankreutzer/automatic-engineering-agent-knowledge` and read its
   `AGENTS.md`, `README.md`, `INDEX.md`, `projects.json` and matching project
   entry point. Use this source workflow directly if the skill is unavailable.
2. Retrieve only relevant verified entries before implementation, debugging,
   review or validation. Check scope, evidence and review dates; verify mutable
   claims against the current owning sources. Repeat when the task or repository
   scope changes. These entries do not override this repository's requirements.
3. After a meaningful verified result and before handover, automatically capture
   new durable, reusable learning in that private knowledge repository. Routine
   knowledge maintenance is part of the owner's requested project workflow.
   Deduplicate or update existing entries; record evidence and limitations;
   follow the knowledge repository's format, validation and pull-request rules.
   Make no write when there is no new useful conclusion.
4. An explicit read-only or no-persistence request takes precedence. Do not infer
   unrelated permissions, installations, deployments or spending authority from
   stored notes. If the skill, connection or knowledge access is unavailable,
   report that limit and continue work permitted by this repository; never claim
   unread knowledge was used or an unverified write was saved.
5. Keep private knowledge, transcripts, credentials and customer data out of this
   public repository. Report briefly which learning IDs informed the work and
   which knowledge commit or pull request was actually saved.

## Jira-led delivery governance

- Reuse the originating `CO-*` Jira work item when a design-skill change is derived from Conference Manager product work.
- Create a dedicated Jira task only when the design-skill system itself is the work item.
- Use the Jira key in branch and pull-request titles where practical.
- Pull requests remain concise engineering-review artifacts; work status, acceptance and audit coordination belong in Jira.
- Do not create GitHub Issues or Milestones for new internal Conference Manager work.

