# Guideline

## Intro 👈🤖

A social button is an icon-only button that gives quick access to a social network or a social action, such as sharing content.

---

## Definition

Social button provides quick access to a social network or social action, such as opening a profile, sharing content, or starting a conversation. It displays the icon of the selected social network and can be used either as a prominent action or as a more discreet secondary control.

Only the social networks available in the component can be selected.

---

## Best for 👈🤔

✅ Sharing a page, an article or an offer on a social network

✅ Linking to the brand’s profile or channel on a social network

✅ Starting a conversation in a messaging application, such as WhatsApp or Messenger

✅ Opening the user’s email client to send or share content

✅ Groups of social links in a footer, with the Minimal appearance

✅ A prominent share action at the end of a piece of content, with the Strong appearance

✅ Compact layouts where a row of recognisable network icons saves space

✅ Cards and contact sections that list several ways to reach a person or a service

✅ Networks whose logo is widely recognised by the audience

✅ Secondary actions only: the main action of a page keeps a labelled button

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Container | The round surface of the button, filled in the Strong appearance and transparent in Minimal | N |
| 2 | Social network icon | Identifies the network or the social action the button gives access to | N |
| 3 | Loading indicator | Replaces the icon while the action is being processed | Y |
| 4 | Focus indicator | Shows which button has keyboard focus | N |
| 5 | Minimum interactive area | The 48 px area that stays available whatever the visible size of the button | N |

---

## Appearance

**`Strong`** Used for primary or high-visibility actions. It uses bold styling and solid backgrounds, making the button stand out. Suitable for prominent placements where social interaction (sharing or following) is a key part of the user flow.

**`Minimal`** Offers a more subtle appearance with lighter backgrounds or outlines. Intended for secondary or less intrusive placements. Works well in footers, cards, or alongside other actions where a social button is not the primary action.

---

## appearance_do_&_dont 👈🤔

✅ **Do:** Use Strong where the social action is a key part of the flow, such as sharing an article  
❌ **Don't:** Use Strong for every social button on a page that already has a primary action

✅ **Do:** Use Minimal in footers, cards or next to other actions  
❌ **Don't:** Let a row of Strong social buttons compete with the main call to action

✅ **Do:** Keep the same appearance for all the social buttons of a group  
❌ **Don't:** Mix Strong and Minimal buttons in the same row

✅ **Do:** Keep the network icon as provided by the component  
❌ **Don't:** Recolour, rotate, crop or animate a network logo

✅ **Do:** Check the contrast of the icon and the container against the background  
❌ **Don't:** Place a Minimal button on a background where its icon is hard to see

---

## Size

**`Default`** Use Default in most situations. It provides the standard button size and interaction area.

**`Small`** Use Small when space is limited or when the button needs to appear with less visual emphasis. Avoid using the Small size when it would reduce the required touch target.

---

## size_do_&_dont 👈🤔

✅ **Do:** Use Default in most situations  
❌ **Don't:** Use Small only to fit more buttons into a row

✅ **Do:** Use Small when space is limited or the buttons need less visual emphasis  
❌ **Don't:** Use Small where it would reduce the required touch target

✅ **Do:** Keep the same size for all the social buttons of a group  
❌ **Don't:** Mix Default and Small buttons in the same row

✅ **Do:** Leave enough space between adjacent buttons so each one is easy to hit  
❌ **Don't:** Place Small buttons edge to edge with no gap

✅ **Do:** Keep the minimum interactive area of 48 px, even with the Small size  
❌ **Don't:** Shrink the interactive area to the visible size of the button

---

## Social network

**`Discord`** Links to or opens a Discord server or direct message for community-oriented sharing. Common in gaming or community-focused interfaces.

**`Email`** Opens the user’s default email client to compose a message, usually with pre-filled content or recipient.

**`Facebook`** Used for social engagement actions like sharing, liking, or following. Recognized by its distinctive branding and iconography.

**`Instagram`** Primarily used for linking to user profiles or triggering "follow" actions. Not typically used for direct sharing.

**`Line`** Used for direct messaging through Line, a popular messaging app. Typically opens a chat with a specific user or group.

**`Linkedin`** Used in professional or business contexts for sharing updates or navigating to profiles or company pages.

**`Messenger`** Provides quick access to Facebook Messenger for direct messaging.

**`Pinterest`** Enables users to save or “pin” content. Common in lifestyle, fashion, or visual content-heavy websites.

**`Snapchat`** Less commonly used; may link to public profiles or content. Suitable for media or entertainment platforms.

**`Threads`** Directs users to a Threads profile or conversation, enabling micro-blogging or text-based interactions.

**`Tiktok`** Directs users to TikTok profiles or specific video content. Common in entertainment or influencer-related use cases.

**`WhatsApp`** Enables quick messaging or content sharing directly through the application. Common in mobile interfaces.

**`X`** Commonly used in business or content-sharing interfaces. Offers sharing or reposting capabilities.

**`Youtube`** Used to direct users to a channel or video content. Often placed alongside other media-related actions.

---

## social_network_do_&_dont 👈🤔

✅ **Do:** Offer only the networks that are relevant to the content and the audience  
❌ **Don't:** Display every available network by default

✅ **Do:** Use only the networks available in the component  
❌ **Don't:** Draw a custom button for a network that is not provided

✅ **Do:** Give each button an accessible name that states the network and the action, such as “Share on Facebook”  
❌ **Don't:** Leave an icon-only button without a text alternative

✅ **Do:** Keep the same order of networks across the product  
❌ **Don't:** Reorder the networks from one page to the next

✅ **Do:** Tell users when a button opens another application or a new window  
❌ **Don't:** Send users to an external site without any warning

---

## Responsiveness and user zoom

**Responsiveness**
The Social button is an icon-only component and does not support multiline content. Its width and height remain proportional to preserve the button shape and the correct alignment of the social network icon. The component should not stretch to fill the available width. When several Social buttons are displayed together, the surrounding layout should allow them to wrap onto another line when there is not enough horizontal space, rather than reducing or compressing their size.

**User zoom in/out**
• The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
• In order to preserve the minimum interactive area during user zoom out, this component have a min-width and a min-height of 48px.
• Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.
• During user zoom, visual elements such as the icon or loader scale with the component. However, the defined padding and spacing values remain unchanged.

---

## responsiveness_and_user_zoom_do_&_dont 👈🤔

✅ **Do:** Keep the width and the height of the button proportional  
❌ **Don't:** Stretch the button to fill the available width

✅ **Do:** Let a group of buttons wrap onto another line when space runs out  
❌ **Don't:** Shrink or compress the buttons to keep them on one line

✅ **Do:** Let the icon and the loader scale with the button when users zoom  
❌ **Don't:** Fix the size of the button so it ignores user zoom

✅ **Do:** Keep the minimum width and height of 48 px when users zoom out  
❌ **Don't:** Let the interactive area fall below the minimum size

✅ **Do:** Check the group at 200% zoom and at a 320 px wide viewport  
❌ **Don't:** Assume a row that fits at the default size fits at every zoom level

---

# Specs

## States

**`Enabled`** The default interactive state. The button is available and ready to be activated.

**`Hover`** Displayed when a pointer moves over the button. It provides visual feedback that the element is interactive.

**`Focus`** Displayed when the button receives keyboard focus. A visible focus indicator helps users identify the currently focused element.

**`Pressed`** Displayed while the button is being activated, for example while the user presses a mouse button or touches the control.

**`Loading`** Indicates that the action has been triggered and is still being processed. The social network icon is temporarily replaced by a loading indicator.

**`Disabled`** Indicates that the action is temporarily unavailable. The button is not interactive and uses a visually muted appearance.

**`Skeleton`** Represents the button while its content or surrounding interface is loading. The skeleton state is not interactive and should only be displayed temporarily.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Social button components must meet WCAG 2.2 Level AA standards so that all users can identify the network, understand the action and activate the button using keyboard, pointer or assistive technologies. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

A social button shows only a logo. Users who cannot see it, or who do not recognise the network, depend entirely on its text alternative, and small buttons placed in a row are easy to miss or to hit by mistake.

### Key Challenges

- An icon-only control has no visible label: without a text alternative it is announced as an unnamed button or link
- The logo names the network but not the action: sharing, following and opening a profile look the same
- Several small buttons in a row need enough size and spacing to be activated reliably
- Loading, Disabled and Skeleton states must be conveyed to assistive technologies, not only visually

### Critical Success Factors

1. Give every button an accessible name that states the network and the action, such as "Share on Facebook" (WCAG 4.1.2)
2. Use a link for navigation to a profile or site and a button for an in-page action such as sharing
3. Keep the 48 px minimum interactive area and leave space between adjacent buttons (WCAG 2.5.8)
4. Announce the Loading state and keep the accessible name while the icon is replaced by the loader

---

## Design Requirements

### Structure & Labels

- [ ] **Accessible name**: A visually hidden label or `aria-label` names the network and the action; the icon itself is hidden from assistive technologies ([Orange ARIA guidelines](https://a11y-guidelines.orange.com/en/web/develop/textual-content/))
- [ ] **Group label**: A row of social buttons is a list or a group with a name such as "Share this page"
- [ ] **External destination**: The name or a hint says when the button opens another application or a new window

### Visual Design

- [ ] **Focus indicator**: 3:1 minimum contrast ratio with ≥2px visible border ([Focus visibility](https://a11y-guidelines.orange.com/en/web/design/focus-visibility/))
- [ ] **Non-text contrast**: The icon and, for Strong, the container meet 3:1 against the background in every interactive state
- [ ] **Target size**: At least 48 × 48 px of interactive area, with spacing between adjacent buttons

### Content

- [ ] **Explicit names**: ❌ "Facebook" / ✅ "Share on Facebook" ([Clear labels](https://a11y-guidelines.orange.com/en/web/design/content/))
- [ ] **Consistent wording**: The same pattern is used for every network, such as "Share on [network]" or "[Brand] on [network]"

---

## Testing Checklist

### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify each button announces its role, network and action, and that Loading and Disabled states are announced

### Keyboard Testing

- [ ] Tab reaches every button in visual order; Enter activates links, Enter and Space activate buttons
- [ ] Focus indicator visible (≥3:1 contrast) on both appearances and both sizes

### Functional Testing

- [ ] Verify the buttons wrap onto another line at 200% zoom and 320 px width without shrinking below the minimum interactive area

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **1.1.1 Non-text Content** (A): The network icon has a text alternative that serves the same purpose
- **4.1.2 Name, Role, Value** (A): Each button exposes its name, its role (link or button) and its state
- **2.5.8 Target Size (Minimum)** (AA): Targets are at least 24 × 24 CSS px or sufficiently spaced; the component keeps a 48 px interactive area
- **2.4.7 Focus Visible** (AA): Visible focus indicator with ≥3:1 contrast on every button
- **1.4.11 Non-text Contrast** (AA): Icon and container keep a 3:1 contrast ratio against adjacent colours

For complete reference: [Orange Accessibility Guidelines - Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Textual content](https://a11y-guidelines.orange.com/en/web/develop/textual-content/)
- [WCAG 2.2 Understanding - Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [WCAG 2.2 Understanding - Non-text Content](https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| 17 Sep, 2025 | 1.0.0 | **Version 2.7 of the design tokens is required for the development of this update.**<ul><li>Component creation</ul> | Anton Astafev |
