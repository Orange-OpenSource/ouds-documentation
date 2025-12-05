### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify "loading" announced on entry, "loaded" announced on completion, no skeleton shapes read

### Keyboard Testing
- [ ] Skeleton shapes are not focusable, focus moves naturally to loaded content
- [ ] No keyboard traps occur during loading state transitions

### Motion Testing
- [ ] Shimmer animation stops when `prefers-reduced-motion: reduce` is enabled in OS settings

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)