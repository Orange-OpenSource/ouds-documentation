# Alert message — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([alert_message.md](alert_message.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ To display important system feedback that requires user attention

✅ When communicating action outcomes (success, error, warning, information)

✅ In cases where the message must be highly visible and separated from content

✅ For scenarios that may require follow-up actions or dismissal

## Layout — do & don't

✅ **Do:** Use bottom action layout on mobile devices and narrow viewports to ensure readability.  
❌ **Don't:** Force trailing action layout on small screens where content becomes cramped.

✅ **Do:** Use trailing action layout for short, single-line alerts on desktop to maintain compact horizontal alignment.  
❌ **Don't:** Use trailing action layout when alert text spans multiple lines, as this creates visual imbalance.

✅ **Do:** Choose the without action layout for purely informational messages requiring no user response.  
❌ **Don't:** Include unnecessary actions on every alert just for visual consistency.

✅ **Do:** Use `<button>` elements styled as links for in-app actions that don't navigate to new pages.  
❌ **Don't:** Use `<a>` elements for actions that trigger modals or execute functions without navigation.

✅ **Do:** Position alerts contextually near the content they relate to for better user comprehension.  
❌ **Don't:** Place alerts far from the relevant content or action that triggered them.

## Status — do & don't

✅ **Do:** Use the correct semantic status to match the message's intent (e.g., negative for errors, positive for success).  
❌ **Don't:** Use warning status for error messages or info status for critical failures.

✅ **Do:** Always pair functional statuses with their dedicated icons to ensure accessibility and recognition.  
❌ **Don't:** Substitute decorative or custom icons for functional status icons.

✅ **Do:** Reserve negative status for critical issues that genuinely block user progress.  
❌ **Don't:** Overuse negative alerts for minor issues, which leads to alert fatigue.

✅ **Do:** Use neutral or accent status for non-critical informational content that doesn't require urgency.  
❌ **Don't:** Apply functional status colors to promotional or marketing content.

✅ **Do:** Ensure consistent status usage across your product to build user familiarity and trust.  
❌ **Don't:** Mix status meanings inconsistently across different screens or contexts.

## Rounded corner — do & don't

✅ **Do:** Use rounded corners consistently across consumer-facing interfaces to create a friendly, approachable feel.  
❌ **Don't:** Mix rounded and square corners within the same interface without clear design rationale.

✅ **Do:** Use square corners in enterprise or utility-focused interfaces where a professional tone is preferred.  
❌ **Don't:** Apply rounded corners to alerts in formal B2B contexts where they may feel out of place.

✅ **Do:** Match alert corner radius to other components in your interface for visual consistency.  
❌ **Don't:** Use drastically different corner radii between alerts and surrounding UI elements.

✅ **Do:** Consider emotional context when choosing corner style—rounded for reassurance, square for authority.  
❌ **Don't:** Ignore the psychological impact of visual styling on user perception of message severity.

✅ **Do:** Establish a design token or guideline governing corner radius usage across alert variants.  
❌ **Don't:** Allow individual designers to choose corner styles ad-hoc without system-level guidance.

## Close button — do & don't

✅ **Do:** Make alerts dismissible when the message is informational and doesn't require action.  
❌ **Don't:** Allow users to dismiss critical error alerts that block their workflow.

✅ **Do:** Keep mandatory alerts persistent until the underlying issue is resolved or context changes.  
❌ **Don't:** Force users to repeatedly see the same dismissible alert after they've acknowledged it.

✅ **Do:** Consider what happens after dismissal—should the alert reappear on next visit or stay hidden?  
❌ **Don't:** Implement dismissal behavior inconsistently across platforms or sessions.

✅ **Do:** Ensure the close button has adequate touch target size (minimum 44×44px) for accessibility.  
❌ **Don't:** Make close buttons too small or position them where they're easily triggered accidentally.

✅ **Do:** Provide visual feedback when the close button is focused or hovered for keyboard and mouse users.  
❌ **Don't:** Hide or obscure the close button in ways that prevent users from finding it.

## Icon — do & don't

✅ **Do:** Always include semantic icons for functional alerts (negative, positive, info, warning) to ensure accessibility.  
❌ **Don't:** Remove icons from functional alerts, as users rely on visual cues to quickly identify severity.

✅ **Do:** Use icons for neutral and accent alerts only when they add meaningful context or recognition.  
❌ **Don't:** Add decorative icons that don't contribute to message comprehension.

✅ **Do:** Ensure icons have sufficient color contrast and are not the sole indicator of status (use color and text too).  
❌ **Don't:** Rely only on icon color to convey meaning, as this fails users with color blindness.

✅ **Do:** Keep icon size proportional to the alert's text size for visual balance.  
❌ **Don't:** Use oversized or undersized icons that create visual hierarchy issues.

✅ **Do:** Use consistent icon styles (filled vs. outlined) that match your design system's iconography guidelines.  
❌ **Don't:** Mix icon styles within the same alert or across similar alert types.

## Description — do & don't

✅ **Do:** Keep description text to 1-2 short sentences maximum for optimal scannability.  
❌ **Don't:** Write lengthy paragraphs or "long-reads" within alert descriptions.

✅ **Do:** Omit description entirely if the label alone clearly conveys the complete message.  
❌ **Don't:** Add redundant description text that repeats what the label already states.

✅ **Do:** Provide actionable next steps when user action is required (e.g., "Check your settings").  
❌ **Don't:** Leave users without guidance when an error requires them to take corrective action.

✅ **Do:** Use plain, jargon-free language consistent with your brand's tone of voice.  
❌ **Don't:** Include technical error codes or developer-oriented messages in user-facing alerts.

✅ **Do:** Link to detailed information elsewhere if the message requires more explanation.  
❌ **Don't:** Overload the alert component with extensive details that belong on a separate page.

## Bullet list — do & don't

✅ **Do:** Limit bullet lists to 3-5 items for optimal readability and quick scanning.  
❌ **Don't:** Include more than 7 bullet points; link to a detailed page instead.

✅ **Do:** Introduce the list with a lead-in sentence that provides context for the items.  
❌ **Don't:** Start a bullet list without explaining what the items represent.

✅ **Do:** Keep each bullet item short—use sentence fragments or brief statements.  
❌ **Don't:** Write full paragraphs or complex sentences as bullet points.

✅ **Do:** Use parallel grammatical structure across all bullet items (start with same part of speech).  
❌ **Don't:** Mix verb forms, noun phrases, and complete sentences inconsistently.

✅ **Do:** Use bullet lists only when presenting multiple items of equal importance.  
❌ **Don't:** Use a bullet list for a single item—write it as a simple sentence instead.
