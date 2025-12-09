### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify badge context announced correctly, count values read accurately, status meaning communicated

### Keyboard Testing
- [ ] Confirm badge does not receive focus (non-interactive)
- [ ] Verify associated interactive element (icon, button) is keyboard accessible and announces badge context

### Live Region Testing
- [ ] Verify count changes announced via `aria-live="polite"` when updates occur dynamically
- [ ] Confirm announcements don't interrupt critical user tasks

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)