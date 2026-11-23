# Badge count — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([badge_count.md](badge_count.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ To display numeric values (notifications, unread items)

✅ When it is important to draw quick attention to a count

✅ In navigation, icons, or lists where the badge augments a primary element

✅ For values that update frequently

## Status — do & don't

✅ **Do:** Use semantic status colors consistently throughout the application to establish clear visual language for users  
❌ **Don't:** Use red/negative status for non-critical information, as it creates unnecessary alarm and diminishes urgency perception

✅ **Do:** Reserve the Accent status for highlighting promotional or discovery-related counts that encourage exploration  
❌ **Don't:** Mix status meanings across contexts—a color should always represent the same semantic meaning

✅ **Do:** Use Neutral status as the default when the count doesn't require semantic emphasis or urgency  
❌ **Don't:** Overuse Warning or Negative statuses, as they lose impact when applied to non-urgent information

✅ **Do:** Apply Positive status to communicate successful completions, approvals, or beneficial counts  
❌ **Don't:** Use multiple different status colors in close proximity without clear contextual differentiation

✅ **Do:** Consider colorblind users by ensuring status meaning is conveyed through context, not color alone  
❌ **Don't:** Rely solely on status color to communicate critical information—pair with labels or icons when essential

## Size — do & don't

✅ **Do:** Use Medium size (16px) as the default for most interface contexts where badges appear alongside icons or text  
❌ **Don't:** Use Large size in compact layouts where it may crowd adjacent elements or disrupt visual hierarchy

✅ **Do:** Choose Large size (20px) for dashboards, cards, or areas where the count requires prominent visibility  
❌ **Don't:** Mix badge sizes inconsistently within the same component or navigation pattern

✅ **Do:** Ensure badge size is proportional to the parent element it's associated with (icons, buttons, avatars)  
❌ **Don't:** Use badges so small they become illegible or difficult to distinguish from decorative dots

✅ **Do:** Consider touch target requirements when badges are placed on interactive elements in mobile contexts  
❌ **Don't:** Increase badge size solely to draw attention—use status colors or positioning instead

✅ **Do:** Maintain consistent size selection across similar use cases throughout the application  
❌ **Don't:** Choose Large size for single-digit counts where Medium provides sufficient visibility
