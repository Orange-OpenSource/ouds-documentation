## Definition

List allows users to view individual, but related, text items grouped together.

It usually begins with either a number or a bullet, also known as Unordered list or Ordered list.

By default, **this component is not interactive**, although it is possible to add a hypertext link to the content.

---

## Type

**`Unordered`** Collects related items that don't need to be in a specific order or sequence. List items are typically marked with bullets, but it is also possible to use a tick or any Solaris icon.

**`Ordered`** Collects related items with numeric order or sequence. Numbering starts at 1 with the first list item and increases by increments of 1 for each successive ordered list item.

**`Bare`** An unordered list without any bullets or alphanumeric sequence. It still have left-padding, so list items will appear indented. This is the default and is also known as undecorated "Unstyled" list.

---

## Text style

List can be used with different font sizes, these sizes are based on our body font-size.
Today, list is available with two text styles: Body large and body Medium.

**`Body Large`** Make sure to use this reference if the text accompanying the list component is the Body Large text.
This variant is designed for more visual, engaging experiences.

**`Body Medium`** Make sure to use this reference if the text accompanying the list component is the Body Medium text.
This variant is best suited for functional, task-oriented experiences.

---

## Nested level

Lists can include nested items to indicate hierarchy or subcategories, with indentation distinguishing each level. Arrange ordered list items logically, such as ranking by importance, highest to lowest values, or in alphabetical/numeric order.

**`Nested level: 0`** Level 0 list items define the main structure.
Unordered level 0 list items are marked with full squares.
Ordered level 0 list items are marked with numbers.

**`Nested level: 1`** Level 1 (nested) list items provide hierarchy or subcategories.
Unordered level 1 list items are marked with outlined squares.
Ordered level 1 list items are marked with uppercase letters.

**`Nested level: 2`** Level 2 (nested) list items provide hierarchy or subcategories.
Unordered level 2 list items are marked with dashes.
Ordered level 2 list items are marked with lowercase letters.

Ordered lists can be combined with unordered items in the same list as well.

Note that, in this context, even though the Unordered list item is placed at nested level 1, it is rendered as if it were at nested level 0 (full square) because, in the technical implementation, **the combination of Ordered and Unordered lists is not incremental.**

Conversely, **in a context using only Unordered lists, the incrementing does apply** even if the choice of nested items differs (bullet items with ticks or Solairs icons).

In the technical implementation, **Bar lists are considered as Unordered lists**. The incrementing between lists does apply.

---

## Other boolean options

**`Bold`** The label text can be bolded.

**`Skeleton`** Improves the perceived loading time by providing a visual cue of where switch will appear once fully loaded.
Uses the "Skeleton" component, variant "Security marge=True".

Even if the "Bold" option is not active, it is also possible to add a hyperlink in the content of a list. In terms of design, and depending on the chosen text style, the typographic reference "Body/Large/Underline" or "Body/Medium/Underline" must be used.

---

## Multiline and responsiveness

**Multiline**
This component allows multi-line text editing. The number of lines is not limited.

**Max-width**
The max-width must be applied at the bullet list container level, not on individual list items. This ensures consistent alignment, readable line lengths, and a coherent vertical structure.
List items must naturally wrap within the parent container
The max-width value depends on the maximum width value assigned to the typographic reference used.
Since the component is standalone, it is up to the designer to manually add a max-width to the group of multiple bullet lists.
For the "body large" variant, the global max-width token will be: **size-max-width-body-large**
For the "body medium" variant, the global max-width token will be: **size-max-width-body-medium**

**User zoom in/out**
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.
* The text must always scale proportionally with user zoom. Text resizing must never be blocked.
* Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.
* The component's height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
* Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.
* In order to preserve the same display rendering, numbers, uppercase/lowercase letters, and bullet points follow the same rules as the text.

---

## Rich text

**Bold option is false**

* **Text style Body Large**
  * **Strong text**
    * Strong text can be used sparingly within alert messages to highlight key information. Rich text must use the **Body/Large/Strong** token only.
    * No other text styles or custom font weights should be used.
  * **Underlined text** and **hyperlink**
    * Underlined text must not be used for emphasis, as it is commonly associated with links.
    * If a **hyperlink** is needed within the content, the typographic reference **Body/Large/Underline** must be used.
* **Text style Body Medium**
  * **Strong text**
    * Strong text can be used sparingly within alert messages to highlight key information. Rich text must use the **Body/Medium/Strong** token only.
    * No other text styles or custom font weights should be used.
  * **Underlined text** and **hyperlink**
    * Underlined text must not be used for emphasis, as it is commonly associated with links.
    * If a **hyperlink** is needed within the content, the typographic reference **Body/Medium/Underline** must be used.

**Bold option is true**

* **Text style Body Large**
  * **Underlined text** and **hyperlink**
    * Underlined text must not be used for emphasis, as it is commonly associated with links.
    * If a hyperlink is needed within the content, the typographic reference **Body/Large/Underline** must be used.
* **Text style Body Medium**
  * **Underlined text** and **hyperlink**
    * Underlined text must not be used for emphasis, as it is commonly associated with links.
    * If a hyperlink is needed within the content, the typographic reference **Body/Medium/Underline** must be used.

---

## Behaviour and accessibility

**Semantics and Structure**
Use `<ul>` for unordered lists (without a specific hierarchy).
Use `<ol>` for ordered lists (with a logical sequence or hierarchy).
Each list item must be a `<li>`.

**Consistent Hierarchy and Nesting**
Avoid nesting too many list levels (maximum 2-3 levels).
If a sublist exists, it must be a direct child of a `<li>`.

**ARIA Role Management**
Avoid adding unnecessary ARIA roles (`role="list"` and `role="listitem"` are not needed, as HTML tags already provide this information).

**Keyboard Navigation**
Lists are not keyboard operable, unless the list items themselves are operable. In such a situation, the list items will retain the component's default keyboard interaction. For example, in a list of links, each link will be in the tab order and can be activated by Enter.

**Screen Reader Compatibility**
Ensure that the list is correctly announced by screen readers.
Add explicit labels if necessary (`aria-labelledby` or `aria-label` on `<ul>`/`<ol>` if the context is unclear).
We recommend using a label prop in all lists. The label will be announced by the screenreader describing the purpose or contents of the list. Even though text preceding the list can introduce the list, screenreaders will read both pieces of information in sequential order. When using the label prop, the information is embedded into the list announcement supporting the comprehension of the list.

**Alternative Text**
If the list contains icons or images, they must have relevant alt text or be hidden from screen readers (`aria-hidden="true"` if decorative).

**Hypertext link**
The component's row padding is calculated in such a way that vertically stacked (listed) links have a line height of at least 24 pixels.

---
