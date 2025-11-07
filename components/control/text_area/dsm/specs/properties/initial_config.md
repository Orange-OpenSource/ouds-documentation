### Initial Config

| Property | Default Value | Notes |
|----------|---------------|-------|
<<<<<<< HEAD
| Outlined | False | Standard filled appearance with bottom border is default; true provides outlined stroke style for lightweight contexts. |
| Rounded corner | False | Square corners are default for business contexts; true adds rounded corners for emotional or brand-specific interfaces. |
| Input status | Empty | Initial state showing no content or placeholder; can also start as Empty (Placeholder) or Filled based on context. |
| State | Enabled | Standard interactive state allowing user input; other states include Hover, Focus, Loading, Read only, Disabled, Skeleton. |
| Error | False | No validation error shown initially; true triggers red border and error message display when character limit is exceeded. |
| Scrolled | False | No internal scrolling initially; true indicates content exceeds visible height and scrollbar is available. |
| ⚠️ Label | True | Label is visible by default for accessibility; can be hidden only when purpose is clear through other UI context. |
| Helper text | False | Character counter and supporting text hidden by default; enable to show remaining character count or guidance. |
| Helper link | False | Additional help link hidden by default; enable when users need access to detailed guidelines or external resources. |
=======
<<<<<<< Updated upstream
| Outlined | False | Filled style with subtle background and bottom border is default for form contexts |
| Rounded corner | False | Square corners are default; rounded corners available for brand-specific emotional contexts |
| Input status | Empty | Field starts blank without placeholder unless placeholder text is explicitly configured |
| State | Enabled | Neutral appearance allowing immediate user interaction without restrictions |
| Error | False | Field begins in valid state; error status triggers only after validation failure |
| Scrolled | False | Scrollbar appears automatically only when content exceeds 240px maximum height |
| ⚠️ Label | True | Label is visible by default; hiding requires explicit choice with accessibility considerations |
| Helper text | False | Helper text is optional; enable when users need guidance about format or limits |
| Helper link | False | Additional help link is optional; use only when external resources or modals add value |
=======
| Outlined | False | Filled style with subtle background is the default for standard form contexts |
| Rounded corner | False | Square corners are default; rounded corners for emotional or brand-specific contexts |
| Input status | Empty | Field starts blank with no placeholder unless explicitly configured |
| State | Enabled | Interactive and ready for user input from initial render |
| Error | False | Field starts in valid state; error appears only after validation rules are violated |
| Scrolled | False | Scrollbar appears only when content exceeds maximum 240px height |
| ⚠️ Label | True | Label is visible by default to ensure clarity and accessibility |
| Helper text | False | Additional guidance is optional and shown only when needed |
| Helper link | False | Help link is optional supplementary feature for complex inputs |
>>>>>>> Stashed changes
>>>>>>> c9e8b9e (content: update)