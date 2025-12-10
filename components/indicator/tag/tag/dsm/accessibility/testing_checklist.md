### Screen Reader Testing

- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify tag text is announced correctly, icons have alternatives, status is communicated

### Keyboard Testing

- [ ] Tags are non-interactive—ensure they don't receive focus unexpectedly
- [ ] Verify adjacent interactive elements maintain proper focus order around tags

### Dynamic State Testing

- [ ] Loading and skeleton states announce appropriately via `aria-live` regions when content updates

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)