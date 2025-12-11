### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify badge count and purpose are announced, status context communicated, dynamic updates spoken

### Keyboard Testing

- [ ] Confirm badge does not receive focus (non-interactive element)
- [ ] Verify parent interactive element announces badge information when focused

### Dynamic Updates Testing

- [ ] Verify `aria-live="polite"` announces count changes without interrupting user tasks
- [ ] Test that screen readers announce meaningful updates (e.g., "3 new notifications")

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)