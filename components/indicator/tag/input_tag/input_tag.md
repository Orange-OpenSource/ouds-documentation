# Guideline

## Intro 👈🤖

Input tag allows users to enter and manage multiple values as removable tags within a text input field.

---

## Definition

A Input tag is a component that allows users to enter multiple values, each represented as a tag. As users type and submit values (usually by pressing enter, comma, or tab), each value is transformed into a Tag. Input tags are often used for adding labels, categories, or participants.

---

## Best for 👈🤔

✅ Adding multiple email recipients in a compose or sharing interface

✅ Creating user-defined labels, categories, or keywords for content organization

✅ Selecting multiple participants, assignees, or collaborators from a list

✅ Building custom filters or search criteria with multiple terms

✅ Tagging content with metadata for categorization and discoverability

✅ Managing skill sets, interests, or attributes in profile forms

✅ Creating comma-separated lists that benefit from visual token representation

✅ Situations where users need to easily add and remove multiple discrete values

✅ Forms requiring multiple selections from an open-ended set of options

✅ Interfaces where entered values need clear visual distinction from pending input

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Provides the visual boundary with rounded pill shape and holds all tag elements | N |
| 2 | Label text | Displays the user-entered value as readable text within the tag | N |
| 3 | Close icon | Enables users to remove the tag by clicking or tapping | N |
| 4 | Border | Indicates the tag boundary and changes appearance based on state | N |
| 5 | Background | Provides visual distinction and changes color based on interaction state | N |
| 6 | Focus ring | Indicates keyboard focus state for accessibility compliance | Y |

---

# Specs

## States

**`Enabled`** The default state of the Input tag. The tag is fully interactive, allowing users to read the label and remove the tag if needed.

**`Hover`** Displayed when a user hovers the cursor over the tag. Visual cues (such as a highlighted border) indicate that the tag is interactive and can be removed.

**`Pressed`** Shown when the tag is actively being clicked or tapped. The tag appears pressed or highlighted, providing feedback that the action is being performed.

**`Disabled`** Indicates that the tag is non-interactive. The tag appears faded or greyed out, and users cannot interact with it or remove it.

**`Focus`** Appears when the tag is focused, typically via keyboard navigation or screen reader. A distinct outline or highlight indicates that the tag is in focus, supporting accessibility.

**`Skeleton`** A placeholder state displayed while content is loading. The tag appears as a simplified, greyed-out shape without label text, indicating to users that tags will soon be available.

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Nov 12, 2025 | 1.2.0 | • Label text with bold replaced by medium | Anton Astafev |
| Jul 21, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.3.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) | Maxime Tonnerre |
| Mai 20, 2025 | 1.0.0 | • Component creation | Anton Astafev |