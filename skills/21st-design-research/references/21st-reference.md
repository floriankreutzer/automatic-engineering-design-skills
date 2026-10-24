# 21st capability reference

Checked against official documentation on 2026-10-24. Recheck the current service, exposed schema and relevant account response before relying on a capability or allowance. This package contains no credentials, MCP configuration or automatic connection.

## Documented capabilities

| Purpose | Documented examples | Use boundary |
| --- | --- | --- |
| Catalog discovery | Search; optional host-supported visual picker | Default for a research request |
| Source inspection | Component source and demo retrieval | Separate action; verify current allowance and provenance |
| AI exploration | Generate and refine saved drafts | Uses credits; verify scope and applicable cost authorization |
| Installation | CLI component installation | Changes project files/dependencies; not part of search |
| Account/usage | Tier, access and allowance information where exposed | Verify actual returned fields; do not infer billing state |

The [official MCP reference](https://help.21st.dev/ai/mcp) describes the current tools. The [official legacy Magic repository](https://github.com/21st-dev/magic-mcp) explains its compatibility role. Do not hardcode historical tool names as if every host exposes them.

## Output and architecture

The [generation-mode documentation](https://21st.mintlify.app/ai/generation) distinguishes HTML/Tailwind sketches from React/shadcn code output. Neither output is an automatic match for an existing native ES-module or Astro component. Inspect and adapt it within the target project's design and architecture requirements.

The [CLI find/install documentation](https://21st.mintlify.app/cli/find) describes retrieval and installation. Installing a catalog item is a dependency/source change, not a read-only design lookup. Optional [project-aware context](https://help.21st.dev/cli/design-runtime) remains a derived aid; it cannot replace central repository instructions or justify exposing private material.

## Allowances, costs and provenance

Consult [current pricing](https://21st.dev/pricing) and the observed account response for current limits. Catalog search, component retrieval and hosted AI work have different entitlement/usage rules. Avoid freezing prices, daily quotas or credit balances into this skill. A returned AI-enabled flag alone does not prove a sufficient balance or an authorized expense.

Review the chosen component's source license and attribution. The [service terms](https://docs.21st.dev/terms) distinguish component code from catalog presentation, preview media and other content. Do not infer a blanket license from marketplace availability or copy preview assets into the product without the appropriate rights.

## Minimal research record

Record only the fields supported by the result: candidate ID or slug, canonical source URL, author/source attribution, review date, intended use, useful design observation, stack/dependency fit and license/asset-rights evidence. Keep unknowns explicit. Use original analysis instead of republishing catalog descriptions.

Record connection tests and quota/account observations only in the appropriate private evidence location. A documentation review is not a successful live connection test.
