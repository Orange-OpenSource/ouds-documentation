# Guideline

## Intro

A badge is a compact visual indicator that highlights status, notifications, or categorization within an interface using color-coded labels.

---

## Definition

The Badge is a small UI element used to highlight status, notifications, or categorization within an interface. It is often displayed as a label or indicator with a distinct background color and text.

**Usage:**
• Renders as a static label without a number.
Used for status indicators (e.g., "New", "Pending", "Success").
The size remains unchanged despite the increase in the interface size.

---

## Best for

✅ Indicating system or item status (success, warning, error, info)

✅ Highlighting new features, updates, or content discoveries

✅ Showing approval or completion states in workflows

✅ Categorizing content with color-coded visual labels

✅ Drawing attention to important metadata without interrupting user flow

✅ Communicating urgency levels in dashboard or list views

✅ Displaying content states like "Draft", "Published", or "Archived"

✅ Supplementing navigation items with status context

✅ Providing quick visual feedback for data validation results

✅ Marking items requiring user attention in compact spaces

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | Pill-shaped background that holds the badge and applies semantic color | N |
| 2 | Background fill | Color surface indicating status type (neutral, accent, positive, info, warning, negative) | N |
| 3 | Border radius | Fully rounded corners (pill shape) for visual distinction | N |
| 4 | Size constraint | Fixed dimensions based on size variant (8px, 12px, 16px, 20px) | N |
| 5 | Disabled state styling | Reduced opacity/color to indicate inactive status | Y |

---

## State

**`Enabled`** The active state of a badge. Includes all possible visual statuses that represent the current state of the system or element (e.g., success, warning, error, information, etc.). Used when the badge should attract attention and convey meaningful information.

**`Disabled`** The inactive state of a badge. Used to indicate that the user isn't allowed to interact with an element, or when the status is unavailable. It appears less prominent and serves as a secondary indication.

---

## state_do_&_dont 👈🤔

✅ **Do:** Use the enabled state when the badge conveys actionable or relevant status information that users need to see.  
❌ **Don't:** Display enabled badges for outdated or irrelevant status that no longer applies.

✅ **Do:** Apply the disabled state when the associated element or feature is unavailable or inactive.  
❌ **Don't:** Use disabled badges as the primary way to hide information—consider removing the badge entirely if not needed.

✅ **Do:** Maintain consistent visual distinction between enabled and disabled states across all status variants.  
❌ **Don't:** Allow disabled badges to have the same visual weight as enabled badges, causing confusion.

✅ **Do:** Use disabled badges to indicate temporarily unavailable statuses that may become active later.  
❌ **Don't:** Use disabled state for permanent conditions—choose appropriate enabled status colors instead.

✅ **Do:** Ensure disabled badges still meet minimum contrast requirements for accessibility.  
❌ **Don't:** Make disabled badges so faint that users cannot perceive them at all.

---

## Status

Badges have seven states depending on the context of the information they represent. Each state is designed to convey a specific meaning and ensure clarity in communication.

**Non fonctionnel**

**`Neutral`** Used for general labels without specific emphasis.

**`Accent`** Employed to highlight discovery or exploration-related content.

**Fonctionnel**

**`Positive`** Indicates success, completion, or approval.

**`Info`** Provides informational context without urgency.

**`Warning`** Negatives the user to potential risks or cautionary messages.

**`Negative`** Draws attention to important or critical information.
Often used for errors, restrictions, or urgent messages, but not exclusively for failures.

---

## status_do_&_dont 👈🤔

✅ **Do:** Use semantic colors consistently—green for positive outcomes, red for errors, blue for informational content, yellow for warnings.  
❌ **Don't:** Use random colors that don't align with established semantic meanings in your design system.

✅ **Do:** Reserve negative (red) status for critical issues requiring immediate attention like errors or failures.  
❌ **Don't:** Overuse negative status badges, which desensitizes users to actual critical information.

✅ **Do:** Use neutral status for general labels that don't carry semantic weight or emotional connotation.  
❌ **Don't:** Use neutral badges when a specific status color would better communicate the intended meaning.

✅ **Do:** Apply accent status to highlight new features, discoveries, or promotional content that needs emphasis.  
❌ **Don't:** Use accent badges for system status information where functional colors (positive, warning, negative) are more appropriate.

✅ **Do:** Use info status for non-urgent informational context like "In Progress" or "Pending Review".  
❌ **Don't:** Use info badges for states that require user action—use warning or negative instead.

---

## Size

**`Xsmall`** A compact badge for minimal space usage, ideal for small UI elements like icons or tooltips.

**`Small`** A slightly larger badge that remains subtle but improves readability, often used for inline labels.

**`Medium`** The default size, providing a balance between visibility and space efficiency, suitable for most use cases.

**`Large`** A prominent badge for drawing more attention, often used in dashboards or highlighted sections.

---

## size_do_&_dont 👈🤔

✅ **Do:** Choose badge size proportional to the element it accompanies—use xsmall for icons, medium for standard UI components.  
❌ **Don't:** Use oversized badges that visually overpower the primary content they're meant to supplement.

✅ **Do:** Maintain consistent badge sizes within the same context or view for visual harmony.  
❌ **Don't:** Mix multiple badge sizes randomly within the same component or list.

✅ **Do:** Use larger badges (medium or large) when the badge conveys critical status information that must be noticed.  
❌ **Don't:** Use xsmall badges for important status information that users might easily miss.

✅ **Do:** Consider touch target requirements when badges appear in mobile or touch interfaces—ensure adequate size for accessibility.  
❌ **Don't:** Use xsmall badges as the only status indicator in touch-heavy interfaces without supporting context.

✅ **Do:** Scale badge size appropriately across responsive breakpoints while maintaining the fixed-size principle within each viewport.  
❌ **Don't:** Allow badges to dynamically resize based on interface scaling, which contradicts the component's design intent.

---

# Specs

## States

**`Enabled`** The active state of a badge. Includes all possible visual statuses that represent the current state of the system or element (e.g., success, warning, error, information, etc.). Used when the badge should attract attention and convey meaningful information.

**`Disabled`** The inactive state of a badge. Used to indicate that the user isn't allowed to interact with an element, or when the status is unavailable. It appears less prominent and serves as a secondary indication.

---

## Layout and spacing

🚧 Content to be added

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Oct 14, 2025 | 1.2.0 | • The component now has two states: Enabled and Disabled. • Documentation has been updated and published in Zeroeight, with use case examples provided for every state. • The colors and background tokens for the functional states of the positive and info statuses have been changed. • For the "Status neutral" variant, the surface token "color-surface-status-neutral-emphasized" has been replaced by the token "color-surface-inverse-high" | Anton Astafev |
| Jun 16, 2025 | 1.1.0 | • "Accent" variant added | Maxime Tonnerre |
| Mai 9, 2025 | 1.0.0 | • Component creation | Anton Astafev |