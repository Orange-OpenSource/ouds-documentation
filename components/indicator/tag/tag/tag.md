# Guideline

## Intro 👈🤖

A tag is a compact, non-interactive element that displays labels, categories, or status information to help users quickly identify and organize content.

---

## Definition

A tag is a small element that shows short info like a label, keyword, or category.
It helps users quickly find, group, or understand content.

---

## Best for 👈🤔

✅ Displaying status indicators such as "Active," "Pending," or "Completed" in dashboards and lists

✅ Categorizing content items with keywords or labels for quick visual scanning

✅ Showing metadata like document types, priority levels, or content classifications

✅ Indicating system states such as success, warning, error, or informational messages

✅ Labeling items in data tables where space efficiency is important

✅ Highlighting new features, promotions, or important notices in product interfaces

✅ Communicating order or process statuses in e-commerce and workflow applications

✅ Differentiating between content types in card-based layouts and galleries

✅ Providing visual context for items in complex enterprise applications

✅ Grouping related items with color-coded classification systems

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Provides the visual boundary and background color for the tag | N |
| 2 | Label text | Displays the primary information or status text | N |
| 3 | Leading icon | Reinforces meaning with a visual symbol before the text | Y |
| 4 | Bullet indicator | Shows status or presence with a small circular element | Y |
| 5 | Loader | Indicates loading state with a spinning animation | Y |
| 6 | Skeleton overlay | Provides placeholder appearance during content loading | Y |

---

## Status

Tags have status depending on the context of the information they represent. Each state is designed to convey a specific meaning and ensure clarity in communication.

**Non fonctionnel** Non-functional tags are used to display categories, default states, or to draw attention without carrying a specific functional meaning (unlike functional tags such as success, info, warning, and error).
Icons related to the tag's context can be used to enhance recognition.

**`Neutral`** Default or inactive state. Used for standard labels, categories, or when no specific status needs to be communicated.

**`Accent`** Used to draw attention to new features, recommendations, or content suggestions. Invites users to explore and engage with new offerings, creating an exciting and engaging experience.

**Fonctional** Functional tags communicate specific statuses or system feedback (e.g., success, warning, error, information). Each tag must always be paired with its dedicated functional icon that matches the meaning of the tag.
**Other icons must not be used.**

**`Positive`** Indicates a successful or confirmed status, such as completed tasks or active states.
Always use the functional icon associated with success. ""

**`Warning`** Signals potential issues or actions that require user attention. Use with caution.
Always use the functional icon associated with warning. ""

**`Negative`** Communicates errors, failed actions, or negative outcomes.
Always use the functional icon associated with error. ""

**`Info`** Represents informational content, tips, or supportive context.
Always use the functional icon associated with information. ""

---

## status_do_&_dont 👈🤔

✅ **Do:** Use semantic colors consistently—green for success, yellow for warning, red for error, and blue for information  
❌ **Don't:** Mix semantic color meanings or use warning colors for positive statuses

✅ **Do:** Always pair functional tags with their dedicated functional icons to reinforce meaning  
❌ **Don't:** Use decorative or unrelated icons with functional status tags

✅ **Do:** Reserve functional tags for system feedback and use neutral/accent for categorization  
❌ **Don't:** Overuse functional colors for non-status information, diluting their semantic value

✅ **Do:** Ensure status colors meet WCAG AA contrast requirements (4.5:1 for text)  
❌ **Don't:** Rely solely on color to convey status—always include text labels and icons

✅ **Do:** Use neutral tags as the default when no specific status needs to be communicated  
❌ **Don't:** Apply accent or functional styling to generic labels that don't warrant attention

---

## Appearance

**`Muted`** A tag with a subtle, light, or semi-transparent background. Used for secondary or less prominent information. Muted tags blend more with the background, providing a softer visual emphasis compared to emphasized tags.

**`Emphasized`** A tag with a solid, high-contrast background. Used to draw strong attention to important labels or categories. Emphasized tags stand out prominently against the interface and are ideal for primary or high-priority information.

---

## appearance_do_&_dont 👈🤔

✅ **Do:** Use emphasized tags for primary status information that requires immediate attention  
❌ **Don't:** Use emphasized appearance for all tags, as it reduces the impact of important ones

✅ **Do:** Apply muted tags for secondary or supplementary information that shouldn't dominate the view  
❌ **Don't:** Use muted tags for critical statuses like errors or warnings that need visibility

✅ **Do:** Create visual hierarchy by combining muted and emphasized tags within the same context  
❌ **Don't:** Mix appearance styles inconsistently without a clear information hierarchy rationale

✅ **Do:** Consider the background surface when choosing appearance to ensure adequate contrast  
❌ **Don't:** Place muted tags on backgrounds where they become difficult to read or distinguish

✅ **Do:** Use emphasized tags sparingly to maintain their visual impact and draw focus effectively  
❌ **Don't:** Default to emphasized appearance when muted would suffice for the content's importance

---

## Layouts

**`Text only`** A tag that displays only text. Used for simple labels, categories, or keywords without additional visual elements.

**`Text + Bullet`** A tag with a small indicator (bullet) alongside the text. Used to show status, presence, or activity next to the label.

**`Text + Icon`** A tag that includes an icon before the text. Used to visually reinforce the meaning of the tag, such as status, type, or action.

---

## layouts_do_&_dont 👈🤔

✅ **Do:** Use text-only tags for simple categorization where additional visual cues aren't needed  
❌ **Don't:** Add icons or bullets to tags when they provide no additional meaningful information

✅ **Do:** Use the bullet layout to indicate presence, online status, or activity states  
❌ **Don't:** Use bullets for general categorization where they add no semantic value

✅ **Do:** Choose icons that clearly reinforce the tag's meaning and are universally understood  
❌ **Don't:** Use ambiguous or decorative icons that don't enhance comprehension

✅ **Do:** Maintain consistent layout choices across similar tag types within the same interface  
❌ **Don't:** Randomly alternate between layouts for tags serving the same purpose

✅ **Do:** Position icons before the text label to follow natural left-to-right reading patterns  
❌ **Don't:** Place icons after text or in inconsistent positions across tag instances

---

## Shape

**`Rounded corner=True`** A tag with fully rounded corners, creating a pill-shaped appearance. Rounded tags offer a softer and more approachable look, suitable for most modern interfaces.

**`Rounded corner=False`** A tag with sharp, square corners. Squared tags provide a more formal, structured, or technical feel. They are often used in business contexts to label promotions, offers, or important notices.

---

## shape_do_&_dont 👈🤔

✅ **Do:** Use rounded (pill-shaped) tags for consumer-facing interfaces where approachability matters  
❌ **Don't:** Mix rounded and square tags inconsistently within the same interface context

✅ **Do:** Apply square-cornered tags in formal business contexts like promotions, offers, or legal notices  
❌ **Don't:** Use square tags in casual or consumer applications where rounded shapes fit better

✅ **Do:** Maintain consistent shape choices across all tags within a single product or feature area  
❌ **Don't:** Alternate shapes based on personal preference rather than established design rationale

✅ **Do:** Consider the overall design language when selecting tag shape to ensure visual harmony  
❌ **Don't:** Choose tag shapes that conflict with the established border-radius patterns in your UI

✅ **Do:** Use shape as a secondary differentiator alongside color and content for tag categorization  
❌ **Don't:** Rely solely on shape to distinguish between different tag types or meanings

---

## Size

**`Default`** The standard tag size, using bold text to ensure strong visibility and readability.
Commonly used for promotional content, highlights, or key information, where emphasis and clarity are important.

**`Small`** A compact tag with medium text, designed for tables or complex components where space efficiency matters.
It helps maintain visual balance and prevents the interface from feeling overloaded with bold text.

---

## size_do_&_dont 👈🤔

✅ **Do:** Use default size tags for standalone displays where visibility and readability are priorities  
❌ **Don't:** Use default size tags in dense data tables where they compete with primary content

✅ **Do:** Apply small tags in tables, lists, and compact layouts to maintain visual balance  
❌ **Don't:** Use small tags when they become difficult to read or interact with on mobile devices

✅ **Do:** Maintain consistent sizing within the same component or layout context  
❌ **Don't:** Mix default and small sizes arbitrarily within the same view or data grouping

✅ **Do:** Consider touch target requirements—small tags should still meet minimum accessibility standards  
❌ **Don't:** Reduce tag size below readable thresholds even in space-constrained environments

✅ **Do:** Choose tag size based on the information density and importance of surrounding content  
❌ **Don't:** Default to small size without considering the tag's visibility needs in context

---

# Specs

## States

Even though the Tag component is not interactive, it still includes several display states. This allows it to be flexible in different scenarios and ensures the user always sees the right visual feedback. The component supports four states: Enabled, Loading, Disabled, and Skeleton.

**`Enabled`** The default state of the tag, used to display the main information or status.

Use case:
• Displaying a ready status or category (e.g., Shipped, Active, New).

**`Loading`** A state where the tag shows a loader together with text.

Use case:
• Displaying status before API data is available. For example, while the system fetches the real value, the tag shows "Loading".
• Data updates or filtering. When a table or list is being updated (e.g., applying filters or refreshing data), the tag temporarily shows loading and is then replaced with the actual value.

**`Disabled`** A non-active state of the tag. It appears "dimmed" to indicate that it is unavailable or not relevant.

Use case:
• Used when a status is no longer valid (e.g., an order is canceled and the tag is no longer meaningful).
• When the tag is part of a status system but currently has no value to display.

**`Skeleton`** A placeholder state shown before the actual data is loaded.

Use case:
• Used to display the structure of the interface while waiting for data.
• Helps avoid abrupt interface changes and provides a smoother experience.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Tags must meet WCAG 2.2 Level AA requirements for color contrast, semantic structure, and screen reader compatibility. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Tags present unique accessibility challenges because they are non-interactive elements that convey status and categorical information through color, text, and icons. Ensuring that meaning is communicated through multiple channels—not color alone—is critical for users with visual impairments.

### Key Challenges

- Color-coded status meanings must be perceivable by users with color vision deficiencies
- Functional icons must have proper text alternatives for screen reader users
- Loading and skeleton states require appropriate announcements for assistive technology
- Text contrast must meet 4.5:1 ratio against both muted and emphasized backgrounds

### Critical Success Factors

1. Provide text labels alongside color and icons to convey status (WCAG 1.4.1)
2. Ensure 4.5:1 minimum contrast ratio between tag text and background (WCAG 1.4.3)
3. Use semantic HTML elements that convey the tag's role to assistive technology
4. Announce dynamic state changes (loading, skeleton) to screen readers using live regions

---

## Design Requirements

### Structure & Labels

- [ ] **Semantic markup**: Use `<span>` with appropriate `role` or descriptive context for status tags
- [ ] **Text alternatives**: Provide `aria-label` for icon-only tags or hidden text for screen readers
- [ ] **Meaningful labels**: Keep tag text concise (1-3 words) while remaining descriptive ([Writing accessible content](https://a11y-guidelines.orange.com/en/editorial-content/))

### Visual Design

- [ ] **Color contrast**: Minimum 4.5:1 ratio for text on both muted and emphasized backgrounds ([Color contrast](https://a11y-guidelines.orange.com/en/web/design/colors-and-contrasts/))
- [ ] **Don't rely on color alone**: Pair status colors with text labels and/or icons
- [ ] **Focus indicator**: Not required for non-interactive tags; ensure adjacent interactive elements have visible focus

### Content

- [ ] **Clear status text**: ❌ "New" alone / ✅ "New feature" or provide context via surrounding content
- [ ] **Icon meaning**: Functional icons must match their semantic purpose (success, warning, error, info)

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify tag text is announced correctly, icons have alternatives, status is communicated

### Keyboard Testing

- [ ] Tags are non-interactive—ensure they don't receive focus unexpectedly
- [ ] Verify adjacent interactive elements maintain proper focus order around tags

### Dynamic State Testing

- [ ] Loading and skeleton states announce appropriately via `aria-live` regions when content updates

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **1.4.1 Use of Color** (A): Status information conveyed through color must also be available via text or icons
- **1.4.3 Contrast (Minimum)** (AA): Tag text must have ≥4.5:1 contrast ratio against background
- **1.4.11 Non-text Contrast** (AA): Icon and indicator elements must have ≥3:1 contrast against adjacent colors
- **1.3.1 Info and Relationships** (A): Tag structure and relationships must be programmatically determinable
- **4.1.2 Name, Role, Value** (A): Icon-only tags must have accessible names via `aria-label` or hidden text

For complete reference: [Orange Accessibility Guidelines - WCAG Criteria](https://a11y-guidelines.orange.com/en/web/wcag-criteria/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Web Components](https://a11y-guidelines.orange.com/en/web/components-examples/)
- [WCAG 2.2 Understanding - Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html)
- [WCAG 2.2 Understanding - Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Nov 12, 2025 | 1.5.0 | • Label text with bold replaced by medium for small size of the component | Anton Astafev |
| Oct 10, 2025 | 1.4.0 | For the "Status neutral muted" variant: • The content token "color-content-on-status-neutral-muted" has been replaced by the token "color-content-default" • The surface token "color-surface-status-neutral-muted" has been renamed "color-surface-secondary" For the "Status neutral emphasized" variant: • The content token "color-content-on-status-neutral-emphasized" has been replaced by the token "color-content-inverse" • The surface token "color-surface-status-neutral-emphasized" has been replaced by the token "color-surface-inverse-high" | Maxime Tonnerre |
| Oct 1, 2025 | 1.3.0 | • Loading and Skeleton are no longer treated as separate tag statuses. Instead, they are now included as states alongside Enabled and Loading for each tag status. • Documentation has been updated and published in Zeroeight, with use case examples provided for every state. • The colors and background tokens for the functional states of the positive and info statuses have been changed. • The icon Warning has been replaced with a triangular shape, and for the muted Status it now uses two colors to enhance visual contrast for improved accessibility. • The minimum required contrast ratio has been corrected from 3:1 to 4.5:1 between text and background for both Muted and Emphasized variants, as well as for Tag: Input. • Updated information has been added for the use cases of Rounded Corner Tags and Square Corner Tags. • Functional tags (Positive, Warning, Negative, Info) differ from non-functional ones: in the layout text + iconconfiguration, they can only use functional icons, while non-functional icons are not supported. • The name of the "Hierarchy" variant has been replaced to "Apprearance" | Anton Astafev |
| Sep 8, 2025 | 1.2.0 | • Modified version of the Text + Loader Tag component • For all variants Text + Loader Tag, the background color has been changed to **ouds/color/surface/status/neutral/muted**. • For all variants Text + Loader Tag, the content color has been changed to **ouds/color/content/default**. • Added use case description for this variant | Anton Astafev |
| Jul 21, 2025 | 1.1.0 | • Several design token updates: [Component tokens changelog 1.3.0](https://www.figma.com/design/Co2t6wHMf4GB9NJVGs2Hes/-OUDS-Core-Lib--Design-tokens?m=auto&node-id=9280-2568&t=HLVB4jOd35DWr8Bj-1) • The "Shape" variant becomes "Rounded corner" with a boolean approach | Maxime Tonnerre |
| Mai 20, 2025 | 1.0.0 | • Component creation | Anton Astafev |