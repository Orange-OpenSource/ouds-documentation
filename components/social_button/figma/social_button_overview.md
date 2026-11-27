## Definition

Social button provides quick access to a social network or social action, such as opening a profile, sharing content, or starting a conversation. It displays the icon of the selected social network and can be used either as a prominent action or as a more discreet secondary control.

Only the social networks available in the component can be selected.

---

## Appearance

**`Strong`** Used for primary or high-visibility actions. It uses bold styling and solid backgrounds, making the button stand out. Suitable for prominent placements where social interaction (sharing or following) is a key part of the user flow.

**`Minimal`** Offers a more subtle appearance with lighter backgrounds or outlines. Intended for secondary or less intrusive placements. Works well in footers, cards, or alongside other actions where a social button is not the primary action.

---

## Size

**`Default`** Use Default in most situations. It provides the standard button size and interaction area.

**`Small`** Use Small when space is limited or when the button needs to appear with less visual emphasis. Avoid using the Small size when it would reduce the required touch target.

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

## States

**`Enabled`** The default interactive state. The button is available and ready to be activated.

**`Hover`** Displayed when a pointer moves over the button. It provides visual feedback that the element is interactive.

**`Focus`** Displayed when the button receives keyboard focus. A visible focus indicator helps users identify the currently focused element.

**`Pressed`** Displayed while the button is being activated, for example while the user presses a mouse button or touches the control.

**`Loading`** Indicates that the action has been triggered and is still being processed. The social network icon is temporarily replaced by a loading indicator.

**`Disabled`** Indicates that the action is temporarily unavailable. The button is not interactive and uses a visually muted appearance.

**`Skeleton`** Represents the button while its content or surrounding interface is loading. The skeleton state is not interactive and should only be displayed temporarily.

---

## Responsiveness and user zoom

**Responsiveness**
The Social button is an icon-only component and does not support multiline content. Its width and height remain proportional to preserve the button shape and the correct alignment of the social network icon. The component should not stretch to fill the available width. When several Social buttons are displayed together, the surrounding layout should allow them to wrap onto another line when there is not enough horizontal space, rather than reducing or compressing their size.

**User zoom in/out**
• The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.
• In order to preserve the minimum interactive area during user zoom out, this component have a min-width and a min-height of 48px.
• Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.
• During user zoom, visual elements such as the icon or loader scale with the component. However, the defined padding and spacing values remain unchanged.
