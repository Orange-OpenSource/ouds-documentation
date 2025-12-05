### Structure & Labels
- [ ] **Container aria-busy**: Set `aria-busy="true"` on loading container, `false` when loaded ([Orange status messages](https://a11y-guidelines.orange.com/en/web/develop/dynamic-content/))
- [ ] **Loading announcement**: Include visually hidden text "Loading" within skeleton or via `aria-live` region
- [ ] **Hide decorative shapes**: Apply `aria-hidden="true"` to skeleton visual shapes

### Visual Design
- [ ] **Reduced motion**: Disable shimmer animation when `prefers-reduced-motion: reduce` is set ([Orange animations](https://a11y-guidelines.orange.com/en/web/design/animations/))
- [ ] **Visible placeholder**: Background color provides sufficient visibility on page background
- [ ] **No focus trap**: Skeleton elements do not receive keyboard focus

### Content
- [ ] **Completion announcement**: Announce "Content loaded" or equivalent when loading completes
- [ ] **Timeout handling**: Provide fallback messaging if loading exceeds 5 seconds