**Icon** Use an icon to reinforce the meaning of the item or help users identify a familiar category, object or status.

**Size**
Controls the visual prominence of the icon.

⚠️ Use the same icon size for comparable cards within the same card collection.
Do not mix sizes arbitrarily. Different sizes may suggest a hierarchy or importance that does not exist.

**`Medium`** Use for standard and compact cards. This is the preferred size when the icon provides secondary visual support.

**`Large`** Use when the icon needs stronger prominence or when the card has a larger height, multiline content or additional supporting information.

**Status**
Defines the semantic colour applied to the icon.

**`Not functional`**

**`Neutral`** Use when the icon does not communicate a specific semantic status.

**`Functional`** ⚠️ Use semantic statuses only when the icon represents the same meaning as the status. Do not use a semantic colour only for decoration or visual variety.

**`Positive`** Use for successful, completed or beneficial states.

**`Info`** Use for neutral information that requires additional attention.

**`Warning`** Use for situations that may require caution or user awareness.

**`Negative`** Use for errors, failures, destructive outcomes or critical problems.

**Badge**
Controls whether an additional badge is displayed with the icon.

**`False`** Display the icon without a badge.

**`True`** Display a badge when a notification must be associated with the icon.

**`Image`** Use an image when visual identification is important, for example for a product, service, destination, article or media item.
Do not use an image when it does not add useful information.

**Size**
Controls the dimensions and visual prominence of the image.

⚠️ Use the same image size for comparable cards within the same card collection.
Do not mix sizes arbitrarily. Different sizes may suggest a hierarchy or importance that does not exist.

**`Medium`** Use in compact or information-dense card layouts where the image remains secondary to the text.

**`Large`** Use in standard cards where visual identification is important.

**`Xlarge`** Use when the image is a significant part of the card content, such as a product or media preview.

**Ratio**
Defines the aspect ratio of the image container.

⚠️ Do not crop meaningful content in a way that makes the image difficult to understand. Use an appropriate focal point when the source image is cropped automatically.

**`1x1`** Use for square visual content such as products, logos, album covers or profile-related imagery.

**`16x9`** Use for landscape content such as editorial images or wide media thumbnails.

**Rounded corner**
Defines whether the image is displayed with square or rounded corners. The corner style should reflect the type of content and remain consistent with the visual language used elsewhere in the product.

**`False`** Displays the image with square corners.

**`True`** Displays the image with rounded corners.

**Animated**
Defines whether the image can contain animated content. Use animation only when it provides meaningful value to the user and does not distract from the primary content or interaction.

**`False`** Displays a static image. Use when animation does not provide meaningful information or when a still representation is sufficient.

**`True`** Displays animated content, such as a GIF or WEBP file. Use when the animation provides meaningful visual information or helps communicate the nature of the content.

**⚠️ Motion & Animation accessibility rules**
The use of motion and animation in our products and components requires particular attention to the accessibility guidelines available in the dedicated section of this documentation.

**`Avatar`** Use an avatar to represent a person, profile, team, organisation or account. An avatar supports visual recognition but must always be accompanied by a visible text label identifying the represented entity.

**Size**

**`Medium`** Use in compact cards or when the avatar is secondary to the content.

**`Large`** Use in standard profile, people or account cards.

**`Xlarge`** Use when identity is a primary part of the card or when additional avatar details must remain visible.

**Type**
Defines the content displayed inside the avatar.

**`Image`** Use when a profile image, portrait or organisation logo is available. Avoid images containing small text or complex details.

**`Initials`** Use as a fallback when no suitable image is available. Initials should be generated consistently from the displayed name. Use a predictable rule, such as the first letters of the first and last names. Do not rely on initials alone to identify the person, as several users may share the same initials.

**`Icon`** Use for generic accounts, anonymous profiles, teams or entities that do not have an individual image or initials.

**Badge**
Controls whether a badge is displayed on the avatar.

**`False`** Display the avatar without additional status information.

**`True`** Display a badge when a secondary status must be associated with the avatar, such as availability, verification or account state.

⚠️ Do not use the badge as the only way to communicate an important state. The same information should be available through text or assistive technology.
When Badge is enabled, additional properties become available.

**Badge type**
Defines the visual content used in the avatar.

**`Badge`** Use for simple state indicators. Do not rely on colour alone to communicate a functional status. Provide an additional text label or accessible description.

**`Badge Icon`** Use when the badge carries important or specific information. The icon must support understanding without relying on colour alone and should have an accessible description when required.

⚠️ For Neutral and Accent statuses, the icon can be adapted to the context. For functional statuses, the icon is predefined and must not be changed, ensuring consistent and accessible status communication across the design system.

**Badge status**
Defines the semantic colour of the badge.

⚠️ Colour alone must not communicate the state. Provide a visible label, description, tooltip where appropriate, or an accessible text equivalent in implementation.

**`Non functional`**

**`Neutral`** Use for non-semantic or inactive information.

**`Accent`** Use to highlight a branded or selected state that is not positive, negative or informational.

**`Functional`**

**`Positive`** Use for available, active, verified or successful states.

**`Info`** Use for additional neutral information.

**`Warning`** Use for a state requiring attention or caution.

**`Negative`** Use for unavailable, failed, blocked or notification states.

**`Flag`** Use a flag to represent a country, territory or regional context. A flag may support visual recognition, but it must not replace the corresponding country, territory or language name. Flags should be used carefully because countries, languages and nationalities do not always have a one-to-one relationship.

⚠️ Always provide the corresponding country, territory or language name as visible text.
The accessible name should describe the represented country or territory, not the visual appearance of the flag.

**`Slot`** Use Slot for custom leading content that cannot be represented by Icon, Image, Avatar or Flag.
Slot provides flexibility for specific product requirements, but it should be used as an exception rather than the default solution.

**⚠ Interaction**
The Static card item is non-interactive. Custom Slot content must not contain:
• Buttons
• Links
• Checkboxes
• Radio buttons
• Toggles
• Menus
• Any independently focusable element