• **Default display**
By default, the height of **the input text container is set to 72px, which allows 3 lines of text** to be displayed without expanding the component. This height helps distinguish the field from other text inputs, prevents discouraging users with an overly large field, and keeps the layout compact at the start of a form.

• **Auto-resize (automatic expansion)**
Above 3 lines of text, the field automatically increases in height as the user types their comment.

• **Vertical scrollbar**
If expansion is disabled or **the maximum height is reached at 240px, corresponding to about 10 lines of text**, an internal scrollbar appears allowing the user to scroll through the overflowing text. This choice prevents breaking the layout but has the drawback, on mobile, of creating a scroll within a scroll (text area scroll inside a page scroll).

**⚠️ No manual resize (by the user)**
On both desktop and mobile, we have chosen to disable manual resizing to avoid behaviors inconsistent with the design system.

**Do & don'ts**

✅ **Do:** Start with a reasonable default height (3 lines) that signals multi-line input without overwhelming users

❌ **Don't:** Show a single-line height initially, as it fails to communicate that multi-line input is expected

✅ **Do:** Allow text areas to auto-expand as users type to show all content without requiring scrolling for most use cases

❌ **Don't:** Force users to scroll within small text areas when auto-expansion would provide a better experience

✅ **Do:** Set a maximum height to prevent text areas from consuming excessive screen space in long-form inputs

❌ **Don't:** Allow unlimited expansion on small screens, as it makes navigation and form completion difficult

✅ **Do:** Disable manual resize handles to maintain consistent layout and prevent users from breaking the design

❌ **Don't:** Allow users to resize text areas arbitrarily, especially on mobile, as it causes layout problems

✅ **Do:** Test auto-resize behavior across different devices to ensure smooth transitions without layout shifts

❌ **Don't:** Create jarring resize animations that distract users or cause content to jump unexpectedly

✅ **Do:** Provide clear visual feedback when maximum height is reached and scrolling becomes necessary

❌ **Don't:** Hide the fact that content has been truncated; make scrollability obvious with visible scrollbars

✅ **Do:** Consider the typical length of expected responses when setting default and maximum heights

❌ **Don't:** Use the same height settings for all text areas regardless of their purpose or expected content length

✅ **Do:** Ensure auto-resize respects container boundaries and doesn't break parent layout constraints

❌ **Don't:** Allow text areas to overflow their containers or overlap with adjacent content during expansion