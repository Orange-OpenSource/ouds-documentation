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
