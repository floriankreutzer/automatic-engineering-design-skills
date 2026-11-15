# Visual foundations

Modified adaptation of Impeccable 4.9.1 typography, layout, color and responsive-design guidance. Runtime-dependent procedures have been replaced with evidence-based manual review.

## Typography

Identify the established families, weights and roles before proposing replacements. For operational products, one well-tuned family can provide enough hierarchy. For marketing or expressive work, a distinctive display role may serve the brief.

Define roles such as page title, section heading, body, label, metadata and tabular value. Make adjacent roles distinguishable through a deliberate combination of size, weight, spacing and tone. Keep repeated roles consistent across screens and states.

Set a comfortable measure and line height for the actual language, font and container. Keep long prose distinct from dense data. Use aligned numerals where comparison matters. Treat code-like styling as a content decision, not a generic technology motif.

Check long headings, translation expansion, missing font weights, fallback fonts, narrow containers, browser zoom and platform text scaling. Inspect actual labels for optical alignment. Preserve readability during loading and avoid unnecessary font variants.

## Layout and rhythm

Before editing, describe the primary reading or task path, meaningful groups, leading element, desired density and responsive transformation. Choose the simplest layout model that expresses those relationships.

Use proximity to group related content and larger intervals to separate distinct groups. Follow the project's spacing scale. Prefer shared layout primitives over isolated magic values. Make optical corrections after inspecting the rendered result.

Avoid turning every group into a card. Use containers when they explain containment, interaction or hierarchy. Repetition should support recognition; vary the structure when content or priority changes. Keep primary actions predictably positioned across comparable screens.

Check long content, empty groups, nested scrolling, sticky elements, overlays and safe areas. Ensure the visual order agrees with reading and focus order. A compact icon can still require a generous interactive target.

## Color

Read brand commitments, semantic tokens, themes and existing states first. Choose a strategy that serves the surface: color may carry broad visual expression on a marketing page, while operational surfaces usually need disciplined semantic roles.

Define color by purpose: canvas, raised surface, main and secondary text, action, focus, selection, separator, success, warning, error and data category. Reserve strong emphasis for elements that deserve attention. Avoid scattering accent color through unrelated decoration.

Keep semantic meaning stable across themes and states. Compose dark surfaces intentionally rather than mechanically inverting a light theme. Check the actual foreground and background combinations, including overlays and imagery. Supplement color with labels, shape, position or iconography where it communicates status or categories.

Use measured contrast and the project's required accessibility criteria. Inspect hover, focus, selected and disabled appearances, while distinguishing accessibility requirements from discretionary visual preferences.

## Responsive behavior

Adapt structure to available space and input method. Decide which groups reflow, which navigation collapses, how dense data remains accessible, and where essential actions stay reachable. Preserve the user's task and information priority through each transformation.

Test representative narrow, intermediate and wide layouts rather than only two screenshots. Also check long translations, zoom, expanded controls, keyboard appearance and dynamic content. Use component-container constraints where the same component appears in different contexts.

For native surfaces, follow the repository's platform conventions and supported device classes. Apply current platform guidance when a specific native behavior needs verification.

## Evidence of completion

Record the target sizes and states checked. Show that the main task remains clear, repeated roles stay consistent, content does not disappear and focus order remains usable. Treat an unresolved loading or overflow defect as incomplete work even when the default screenshot looks finished.
