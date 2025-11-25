• **Character limit not exceeded**
The character counter, located in the helper text area, displays in real time (with each keystroke) the number of characters the user can still enter before reaching the field's allowed limit.

⚠️ It is impossible to provide a recommendation for the maximum number of characters, as this depends too specifically on the constraints (or lack thereof) of each project.

• **Character limit exceeded**
If the user exceeds the set limit, the field enters an error state, but input is not blocked. The character counter then shows the user, still in real time, how many characters have been entered beyond the field's allowed limit.

The user must reduce the number of characters entered for the text area to exit the error state.

**Do & don'ts**

✅ **Do:** Display character counters in real-time to give users immediate feedback on remaining capacity

❌ **Don't:** Wait until form submission to inform users they've exceeded character limits

✅ **Do:** Position character counters in the helper text area where users naturally look for field-related information

❌ **Don't:** Place character counters in locations that are hard to notice or that interrupt the typing flow

✅ **Do:** Show "X characters remaining" format to help users gauge how much more they can write

❌ **Don't:** Only show total character count without indicating the limit, forcing users to do mental math

✅ **Do:** Transition to error state when limits are exceeded, using clear visual indicators like color change

❌ **Don't:** Block user input when the limit is reached; allow typing and show the overflow amount instead

✅ **Do:** Use clear, accessible language in character counters like "15 characters remaining" rather than just numbers

❌ **Don't:** Rely solely on color to communicate limit status; include text and icons for accessibility

✅ **Do:** Set character limits based on actual content requirements and database constraints, not arbitrary numbers

❌ **Don't:** Use unnecessarily restrictive character limits that frustrate users trying to provide complete information

✅ **Do:** Update character counter announcements for screen readers using ARIA live regions

❌ **Don't:** Make character counter changes completely silent to assistive technology users

✅ **Do:** Allow users to see and edit content that exceeds the limit so they can make informed decisions about what to cut

❌ **Don't:** Truncate or delete user content automatically when limits are exceeded