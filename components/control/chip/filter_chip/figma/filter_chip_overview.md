## Definition

A filter chip is a compact UI element used in a design system to represent a filter option that can be selected or deselected by the user. Filter chips allow users to refine content or data by applying one or more filters in a visually accessible and interactive way.

Purpose: Allows users to filter content by selecting or deselecting specific categories or attributes.
Behavior: Can be toggled on/off to refine displayed results. Selected chips remain visually distinct to indicate active filters.

---

## Selected

**`True`** Visually distinct to indicate an active filter.
Changes in color and includes a tick mark to signify selection.

**`False`** Maintains a neutral appearance, indicating an available filter option.

---

## Layouts

**`Text + icon`** Combines text with an icon to enhance clarity and recognition.
Ideal when a visual cue helps reinforce the filter's meaning.

**`Text only`** Displays only text, offering a clean and minimalistic look.
Best suited for category-based filters that do not require additional visual elements.

**`Icon only`** Uses only an icon, making it a compact option for limited space.
Works well with universally recognized symbols, such as a heart for favorites or a checkmark for selection.

---

## States

**`Enabled`** The chip is active and available for interaction.
It is displayed in its standard style without additional effects.

**`Hover`** The appearance of the chip changes when the cursor hovers over it.
This includes a color change for the border and the chip's content.

**`Pressed`** The active state when the chip is being pressed.
Accompanied by a color change in the content and border.

**`Disabled`** The chip is unavailable for interaction.
It is visually represented with a muted color change in the content and border (reduced brightness and contrast).

**`Focus`** The state when the chip receives focus (e.g., during keyboard navigation).
It features a triple contrasting border to indicate the active element.

**`Skeleton`** Displays a placeholder chip while the content is loading.
It appears as a semi-transparent gray block without content.

---

## Multiline and responsiveness

**Multiline**
This component doesn't allows multi-line text editing. This is a design recommendation, technically, and for several reasons (responsive behavior, user zoom, etc.), multiline remains possible.

**Max-width vs full-width**
For greater flexibility, this component doesn't have a default max-width. To avoid exceeding a width that would degrade readability and the perception of a compact interactive element, we recommend applying **a max-width of around 240px.**
It is not possible to set this component to use the full available width (of the screen or the container).

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* In order to preserve the minimun interactive area during user zoom out, this component have a min-width **of 52px** and a min-height **of 48px**.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* As the tick icon is functional, it must follow the same rules as text.
* In its "Text + icon" variant, user zoom in/out doesn't affect the size of the icons; they remain fixed in size (decorative use).
* As the text is missing, in its "Icon only" variant, the icons follow the same rules as the text.

---

## Behaviour and accessibility

**Keyboard Navigation**
Tab – Move focus between Chips.
Space / Enter – Activate a Chip (select a filter).
Backspace / Delete – Remove a focused Chip (if dismissible).
Arrow Keys – Navigate through Chips in a group.

**Accessibility aria**
Use aria-selected for selected Chips.
Add aria-label for the close button (Remove {chip content}).
Selectable Chips should be announced as radio button or checkbox for screen readers.

**Visible Focus**
When navigating via keyboard (Tab key), chip must display a visible focus style.

**Microcopy Guidelines**
Chip text should be concise and precise.
The ideal length is one word, max width: 20 characters or 1 to 3 words.
Text should not wrap or be truncated.

**Layout and Arrangement**
Wrapping: Chips are often arranged using a Wrap widget, allowing them to flow within a container and wrap to the next line when needed.
Spacing: Proper spacing between chips and between lines of chips ensures a clean and uncluttered layout.

**Interaction**
Avoid placing more than two rows of Chips to prevent overwhelming users.
Do not use Chips for navigation; use buttons instead.

**Responsiveness**
When the screen resolution changes or the device's scaling settings are adjusted, text-based Chips will adapt by increasing or decreasing in size, while icon-only Chips remain the same size.

**Color Contrast (Applicable for Enabled, Hover, and Focus States)**
Proper contrast ensures accessibility, especially for visually impaired users. Chips should meet WCAG 2.1 AA standards:
* Text Contrast: Minimum 4.5:1 against the background.
* Icon Contrast: At least 3:1 for visibility.

**Screen Reader Accessibility**
For Chips, designers must provide a clear and understandable description for screen readers to ensure accessibility for users who rely on assistive technologies. This is especially important for icon-only Chips.
Additionally, Chips with text should include extra descriptions when necessary to help users understand the context.
By following these principles, designers ensure that icon-only Chips remain accessible and provide a seamless user experience for all, including those who use VoiceOver, TalkBack, and other screen readers.

**Screen Reader Accessibility in Chip Groups**
For Chip groups, it is important to first define the group container with a context explanation for screen readers before assigning labels to each individual Chip. This helps users of assistive technologies, such as VoiceOver and TalkBack, correctly perceive the Chips as a unified set.

---