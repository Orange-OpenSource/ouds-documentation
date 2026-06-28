## Definition

A badge is a UI element that highlights system notifications, statuses, or the categorisation of information through colour alone. The badge is displayed as a coloured shape, without an icon, text, or number; its selected size remains constant, regardless of any changes to the interface size.

---

## State

**`Enabled`** The active state of a badge. Includes all possible visual statuses that represent the current state of the system or element (e.g., success, warning, error, information, etc.). Used when the badge should attract attention and convey meaningful information.

**`Disabled`** The inactive state of a badge. Used to indicate that the user isn't allowed to interact with an element, or when the status is unavailable. It appears less prominent and serves as a secondary indication.

---

## Status

Badges have seven states depending on the context of the information they represent. Each state is designed to convey a specific meaning and ensure clarity in communication.

Using a badge without icons may require additional context, such as a label or description, to ensure accessibility for users with color blindness. For more details, see 'Context of Color Usage (badge without icon)'.

**Not functional**

**`Neutral`** Used for general labels without specific emphasis.

**`Accent`** Employed to highlight discovery or exploration-related content.

**Functional**

**`Positive`** Indicates success, completion, or approval.

**`Info`** Provides informational context without urgency.

**`Warning`** Negatives the user to potential risks or cautionary messages.

**`Negative`** Draws attention to important or critical information. Often used for errors, restrictions, or urgent messages, but not exclusively for failures.

---

## Size

**`Xsmall`** A compact badge for minimal space usage, ideal for small UI elements like icons or tooltips.

**`Small`** A slightly larger badge that remains subtle but improves readability, often used for inline labels.

**`Medium`** The default size, providing a balance between visibility and space efficiency, suitable for most use cases.

**`Large`** A prominent badge for drawing more attention, often used in dashboards or highlighted sections.

---

## User zoom and responsiveness

**Max-width vs full-width**
This component have a max-width.
It is not possible to set this component to use the full available width (of the screen or the container).

**User zoom in/out**
- Componet must always scale proportionally with user zoom.
- In order to preserve the minimun interactive area during user zoom out, this component have:
  - Large size: a min-width and a min-height **of 20px**
  - Medium size: a min-width and a min-height **of 16px**
  - Small size: a min-width and a min-height **of 12px**
  - Xsmall size: a min-width and a min-height **of 8px**
- Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user's zoom level.

---

## Context of Color Usage

A color-only badge should not be used as the only way to show fonctional information.
It needs to be clearly visible on its background, with enough contrast and a readable size, especially for people with low vision or color blindness.

**Status context (badge + label)**

- Color alone doesn't explain meaning. It can support the interface visually, but it shouldn't be the only way to show a status or state. If multiple badge colors are used within the same interface, each color must have an accessible equivalent (e.g. visible text).
- In this example, the badge is used together with an Extra label that clearly conveys the status (positive and negative). The badge only reinforces this meaning visually, allowing multiple statuses to coexist within the same interface.

**Non-status context (badge only)**

- If it is not possible to provide an accessible alternative (text or label), the badge must be considered decorative and must not be used to convey information or differentiate states.
- In this context, the red badge is not used to indicate an error or negative status, but rather as a visual accent to draw attention. No other badge colors are used in the interface to avoid interpreting color as a carrier of meaning.

⚠️ Within a single interface, either a decorative or a functional color context should be used, but not both at the same time. This distinction ensures consistency and aligns with accessible design principles.
