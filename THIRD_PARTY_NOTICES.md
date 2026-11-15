# Third-party design guidance and resources

The repository's existing MIT license continues to cover the original Emil
Kowalski collection and the Pavurel-authored integration where applicable.
The imported skill directories retain their own licenses and notices; the root
MIT license does not replace them.

## Impeccable Design

- Upstream: https://github.com/pbakaus/impeccable
- Reviewed upstream revision: `2b86d9c07b97d4bed7de23583e1bd1e58dd2baae`
- Upstream skill version: 4.9.1.
- Included edition: the reference-only adaptation prepared on 15 November 2026.
- License and notices: [Apache-2.0](skills/impeccable/LICENSE) and
  [upstream notices](skills/impeccable/NOTICE.md).

The adapted entrypoint and six conceptual references reorganize and paraphrase
the design guidance. The Pavurel integration adds mandatory routing and its
bundled policy reference. No upstream engine, launcher, executable helpers, hooks,
live-editing setup or external agent definitions are included. Keep the stated
capability limits when using or updating this edition.

## Taste Skill

- Upstream: https://github.com/Leonxlnx/taste-skill
- Reviewed upstream revision: `f6b76575f949707b4e3c37cd86cb44b0b98643e8`
- Upstream skill version: 2.5.1.
- Included edition: the complete skill resources with the reviewed ChatGPT
  integration entrypoint; its provider-specific Stop hook is not registered.
- License: [MIT](skills/design-taste-frontend/LICENSE).

The upstream body and resources are retained. The Pavurel integration adds the
mandatory routing preamble and a bundled `references/skill-policy.md`. Its bounded
icon adaptation corrects licence metadata in the resolver, index, references and
credits, and copies the relevant notice beside newly generated icons. It does not
change source SVG resolution or drawing behavior.
The compatibility entrypoint preserves project authority, truthful content and
authorized execution. Per-image, font and other asset credits and terms remain
applicable; the skill's MIT license is not a blanket replacement for them.
Example assets are not evidence of Pavurel customers, facilities or capabilities.

### Imported icon notices

The 432 bundled Lucide SVGs retain the full
[Lucide ISC and Feather MIT notices](skills/design-taste-frontend/assets/icons/LUCIDE-LICENSE.txt),
copied from the author's [reviewed license](https://github.com/lucide-icons/lucide/blob/55782beff3a0133df79c417eb68f96e8f19e2404/LICENSE).

The 35 bundled VSCode SVG files (34 distinct icons) use the scoped terms documented
in the [VSCode icon notice](skills/design-taste-frontend/assets/icons/VSCODE-ICONS-NOTICE.md).
The pinned Iconify package labels its collection MIT, while the matching author's
version 12.14.0 [README](https://github.com/vscode-icons/vscode-icons/blob/e8980080a2c491d60073df937c0aece669ba1486/README.md#license)
distinguishes MIT source code, CC BY-SA 4.0 icons and branded icons' own terms.
The integration preserves that distinction instead of treating package metadata
as a blanket grant for every SVG. A `null` trademark field means the icon's branded
status has not been determined. Keep the credited sources, scoped terms and notice
files with reused assets.

## Snapshot maintenance

`packaging/pavurel-design/required-design-skills.json` records the reviewed
editions and an explicit SHA-256 file inventory. UI metadata is normalized for
the portable plugin format. Host-generated account metadata, presentation icons
and product restrictions are excluded from these source snapshots.

Update sources and their lock deliberately, preserve attribution, inspect
changed executable behavior, and run the repository's package tests. Updating
the source does not automatically update an account plugin or any application.
