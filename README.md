# OUDS documentation

Source content of the [Orange Unified Design System](https://unified-design-system.orange.com/) (OUDS) documentation:
one Markdown file per component, its images, the design tokens and their changelogs, and the indexes of links and
versions. The component pages of the OUDS hub are generated from these files, so what you read here is what the hub
shows. The files are plain Markdown, YAML and JSON, readable by people and by AI tools.

## Quick links

| What | Where |
|---|---|
| Component documentation (one file per component) | [components/](components/) · [list by category](#components) |
| Links to every component's documentation, design and code, per platform | [skills/ouds-doctor/Ouds-links.md](skills/ouds-doctor/Ouds-links.md) |
| Component versions in Figma and on each platform, with their design status | [skills/ouds-context/Ouds-versions.yaml](skills/ouds-context/Ouds-versions.yaml) |
| Design tokens, per brand (tables and JSON) | [tokens/md/](tokens/md/) · [tokens/jsonl-ai/](tokens/jsonl-ai/) · [details](#design-tokens) |
| Design token changelogs | [tokens/changelog/](tokens/changelog/) · [details](#token-changelogs) |
| Older Orange libraries (One-i, ODS) mapped to OUDS | [skills/ouds-doctor/Component-mapping.md](skills/ouds-doctor/Component-mapping.md) |
| AI skills | [OUDS Doctor](skills/ouds-doctor/SKILL-ouds-doctor.md) · [OUDS Component Workshop](skills/ouds-component-workshop/SKILL-ouds-component-workshop.md) |
| Research notes on agentic design systems | [agentic-ds-doc/](agentic-ds-doc/) |

## Components

Each folder `components/<name>/` holds:

- `<name>.md` — the full documentation of the component, in the order of its hub page: front matter (`id`,
  `category`, `family`), introduction, one `#` heading per page tab (Guideline, Specs, Accessibility, Develop,
  Changelog) and one `##` heading per section. It includes the Definition, Anatomy, every option and state, the
  accessibility rules, the developer links, the availability per platform and the Design changelog.
- `images/` — the images of the page (exported from Figma at 2×; a GIF replaces the PNG of an animation).
- `<name>-do-dont-propositions.md` (some components) — AI-written proposals (When to use, do & don'ts) that the team
  has not validated yet. They are not published on the hub.

| Category | Components |
|---|---|
| Action | [Assistant button](components/assistant_button/assistant_button.md) · [Assistant icon](components/assistant_icon/assistant_icon.md) · [Button](components/button/button.md) · [Expand button](components/expand_button/expand_button.md) · [Interactive icon](components/interactive_icon/interactive_icon.md) · [Navigation button](components/navigation_button/navigation_button.md) · [Social button](components/social_button/social_button.md) |
| Content display | [Accordion card item](components/accordion_card_item/accordion_card_item.md) · [Accordion list item](components/accordion_list_item/accordion_list_item.md) · [Accordion Q&A](components/accordion_qa/accordion_qa.md) · [Action card](components/action_card_container/action_card_container.md) · [Body](components/body/body.md) · [Bullet list](components/bullet_list/bullet_list.md) · [Card](components/content_card_container/content_card_container.md) · [Code](components/code/code.md) · [Display](components/display/display.md) · [Heading](components/heading/heading.md) · [Label](components/label/label.md) · [Static card item](components/static_card_item/static_card_item.md) · [Static list item](components/static_list_item/static_list_item.md) |
| Control | [Assistant chat input](components/assistant_chat_input/assistant_chat_input.md) · [Chat input](components/chat_input/chat_input.md) · [Checkbox](components/checkbox/checkbox.md) · [Checkbox item](components/checkbox-item/checkbox-item.md) · [Filter chip](components/filter_chip/filter_chip.md) · [Filter chip expand](components/filter_chip_expand/filter_chip_expand.md) · [Password input](components/password_input/password_input.md) · [Phone number input](components/phone_number_input/phone_number_input.md) · [PIN code input](components/pin_code_input/pin_code_input.md) · [Quantity input](components/quantity_input/quantity_input.md) · [Radio button](components/radio_button/radio_button.md) · [Radio button item](components/radio-button-item/radio-button-item.md) · [Select input](components/select_input/select_input.md) · [Suggestion chip](components/suggestion_chip/suggestion_chip.md) · [Switch](components/switch/switch.md) · [Switch item](components/switch-item/switch-item.md) · [Text area](components/text_area/text_area.md) · [Text input](components/text_input/text_input.md) |
| Dialog | [Alert banner](components/alert_banner/alert_banner.md) · [Alert message](components/alert_message/alert_message.md) · [Fullscreen dialog](components/fullscreen_dialog/fullscreen_dialog.md) · [Inline alert](components/inline_alert/inline_alert.md) · [Modal dialog](components/modal_dialog/modal_dialog.md) · [Side sheet](components/side_sheet/side_sheet.md) · [Toast](components/toast/toast.md) |
| Indicator | [Badge](components/badge/badge.md) · [Badge count](components/badge_count/badge_count.md) · [Badge icon](components/badge_icon/badge_icon.md) · [Categorical tag](components/categorical_tag/categorical_tag.md) · [Circular progress indicator](components/circular_progress_indicator/circular_progress_indicator.md) · [Input tag](components/input_tag/input_tag.md) · [Linear progress indicator](components/linear_progress_indicator/linear_progress_indicator.md) · [Skeleton](components/skeleton/skeleton.md) · [Status icon](components/status_icon/status_icon.md) · [Tag](components/tag/tag.md) |
| Layout | [Divider](components/divider/divider.md) |
| Navigation | [Android bars](components/navigation_bar_android/navigation_bar_android.md) · [Breadcrumb](components/breadcrumb/breadcrumb.md) · [Expand link](components/expand_link/expand_link.md) · [iOS bars](components/navigation_bar_ios/navigation_bar_ios.md) · [Link](components/link/link.md) · [Navigation card item](components/navigation_card_item/navigation_card_item.md) · [Navigation list item](components/navigation_list_item/navigation_list_item.md) |

## Design tokens

The tokens of each brand theme, as Markdown tables (semantic token, core token, raw value) and as JSON files for AI
tools. One file per token group: border, color (light and dark), elevation, font, grid, opacity, size, space, type.

| Brand | Tables | JSON |
|---|---|---|
| Orange | [tokens/md/orange/](tokens/md/orange/) | [tokens/jsonl-ai/orange/](tokens/jsonl-ai/orange/) |
| Orange Compact | [tokens/md/orange-compact/](tokens/md/orange-compact/) | [tokens/jsonl-ai/orange-compact/](tokens/jsonl-ai/orange-compact/) |
| Sosh | [tokens/md/sosh/](tokens/md/sosh/) | [tokens/jsonl-ai/sosh/](tokens/jsonl-ai/sosh/) |
| Wireframe | [tokens/md/wireframe/](tokens/md/wireframe/) | [tokens/jsonl-ai/wireframe/](tokens/jsonl-ai/wireframe/) |

### Token changelogs

Generated from the changelog tables of the [OUDS design tokens library](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Lib--Design-tokens) in Figma (one row per release: date, version, notes).

| Changelog | File |
|---|---|
| Core tokens | [ouds_core_tokens.md](tokens/changelog/ouds_core_tokens.md) |
| Semantic tokens | [ouds_semantic_tokens.md](tokens/changelog/ouds_semantic_tokens.md) |
| Component tokens | [ouds_component_tokens.md](tokens/changelog/ouds_component_tokens.md) |
| Component version tokens | [ouds_component_changelog_tokens.md](tokens/changelog/ouds_component_changelog_tokens.md) |
| Android system tokens | [ouds_android_system_tokens.md](tokens/changelog/ouds_android_system_tokens.md) |

## How the content is maintained

- The source of the design is the OUDS Figma libraries and each component's specification file. When a specification
  changes, the component's Markdown file is updated, its images are exported again, and its hub page is regenerated
  from the file as a draft that the OUDS team reviews before it is published.
- `Ouds-links.md` and `Ouds-versions.yaml` are refreshed from the team's links sheet and from the platform
  documentation (Web, Android, iOS, Flutter).
- Please do not edit the generated files by hand (token changelogs, component pages): open an issue or contact the
  OUDS team instead.
