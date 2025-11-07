### Content
<<<<<<< HEAD
- [ ] **Error specificity**: ❌ "Too many characters" / ✅ "You've exceeded the limit by 45 characters—please shorten to submit" ([Orange Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/accessible-forms/))
- [ ] **Clear instructions**: Labels and helper text use plain language explaining expected input, character limits, and formatting requirements
=======
- [ ] **Actionable error messages**: ❌ "Character limit exceeded" / ✅ "Please remove 23 characters. Consider shortening your response or splitting into multiple comments." ([Orange A11y - Error Messages](https://a11y-guidelines.orange.com/en/web/components-examples/forms/#error-messages))
- [ ] **Realistic placeholder examples**: Show specific format rather than generic hints: "Example: I clicked the submit button but received error code 502" vs "Enter description here"
=======

- [ ] **Visible label**: Positioned above input, using `<label>` element with `for` attribute matching input `id` ([Orange Forms Guidelines](https://a11y-guidelines.orange.com/en/web/components-examples/forms/))
- [ ] **Helper text connection**: Link helper text with `aria-describedby` referencing helper text `id`
- [ ] **Error message association**: Link error messages with `aria-describedby`, replace helper text ID when error state activates