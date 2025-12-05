# Guideline

## Intro 👈🤖

The skeleton component provides visual loading placeholders that represent content structure while data loads, reducing perceived wait time.

---

## Definition

The skeleton component is a visual element used to indicate that content is loading. It provides a smooth user experience by temporarily replacing content with gray areas or animations simulating the visual structure of the content to come.

---

## Best for 👈🤔

✅ Displaying loading states for container-based components like cards, tiles, and structured lists

✅ Progressive page loading where content appears incrementally as data becomes available

✅ Reducing perceived load time when fetching asynchronous data

✅ Maintaining layout structure during initial page render to prevent cumulative layout shift

✅ Loading states for data-driven content like tables, user profiles, and media galleries

✅ Placeholder previews when visual layout is known ahead of time

✅ Mobile and web applications where network latency affects content delivery

✅ Streaming content interfaces where items load in batches

✅ Dashboard widgets loading real-time data from multiple sources

✅ E-commerce product listings during catalog fetch operations

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Background | Provides the base visual placeholder shape with subtle gray fill | N |
| 2 | Shimmer/Gradient | Animated overlay creating horizontal wave effect to indicate active loading | Y |
| 3 | Security margin | Transparent padding preventing large uniform surfaces when components stack | Y |
| 4 | Container | Wrapper element defining skeleton dimensions and overflow behavior | N |
| 5 | Shape variants | Different geometric forms (rectangle, circle, text) matching content types | N |

---

## Boolean options

**Security margin** Depending on the position of components in the Skeleton screen template, two variants are possible:
• If a margin (spacing) is present between two or more components, apply the version "Security margin=False" to the affected components.
• If no spacing is present between two or more components, apply the version "Security margin=True" to the affected components.

The "Security margin=True" variant includes transparent padding (with 0% opacity) at the top and bottom of the skeleton component. This padding prevents the creation of excessively large uniform surfaces, maintaining a visually balanced and structured layout.

---

## boolean_options_do_&_dont 👈🤔

✅ **Do:** Use security margin=True when stacking skeletons without spacing to maintain visual separation between loading elements.  
❌ **Don't:** Apply security margin=True when components already have spacing between them, as this creates unnecessary extra padding.

✅ **Do:** Match the security margin setting consistently across all skeleton components within the same loading screen template.  
❌ **Don't:** Mix security margin variants inconsistently within a single loading view, creating an unbalanced visual appearance.

✅ **Do:** Consider the final loaded content layout when deciding security margin settings to ensure smooth transition without layout shift.  
❌ **Don't:** Ignore the relationship between adjacent components when selecting security margin variants.

✅ **Do:** Use security margin=False when components have defined spacing tokens applied between them in the design.  
❌ **Don't:** Use security margin=True as a default without evaluating the actual spacing context of your layout.

✅ **Do:** Test both variants in context to verify the skeleton accurately represents the structure of the content being loaded.  
❌ **Don't:** Assume one security margin setting works universally across all skeleton implementations.

---

# Specs

## States

🚧 Missing from source: States section in skeleton_overview.md

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

The skeleton component must meet WCAG 2.2 Level AA standards by properly communicating loading states to all users, including those using assistive technologies. For comprehensive accessibility guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Skeleton loaders present unique accessibility challenges because they are purely visual indicators that must communicate loading status to users who cannot see them. Screen readers need programmatic notification of loading states, and animations must respect user motion preferences.

### Key Challenges
- Conveying loading status to screen reader users who cannot perceive visual placeholders
- Preventing animation from causing discomfort for users with vestibular disorders
- Ensuring loading completion is announced when content replaces skeleton
- Maintaining low contrast that indicates placeholder status without causing visibility issues

### Critical Success Factors
1. Implement `aria-busy="true"` on container elements during loading (WCAG 4.1.3)
2. Provide visually hidden loading announcements via `role="status"` or `aria-live` regions
3. Respect `prefers-reduced-motion` media query for shimmer animations
4. Remove skeleton and update ARIA attributes when content loads

---

## Design Requirements

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

---

## Testing Checklist

### Screen Reader Testing
- [ ] Test with NVDA (Windows), JAWS (Windows), VoiceOver (macOS/iOS), TalkBack (Android)
- [ ] Verify "loading" announced on entry, "loaded" announced on completion, no skeleton shapes read

### Keyboard Testing
- [ ] Skeleton shapes are not focusable, focus moves naturally to loaded content
- [ ] No keyboard traps occur during loading state transitions

### Motion Testing
- [ ] Shimmer animation stops when `prefers-reduced-motion: reduce` is enabled in OS settings

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/test/)

---

## Key WCAG Criteria

- **1.4.11 Non-text Contrast** (AA): Skeleton shapes visible against background (≥3:1 not strictly required for loading indicators per WCAG)
- **2.2.2 Pause, Stop, Hide** (A): Shimmer animation can be paused or respects reduced motion preference
- **2.3.1 Three Flashes or Below Threshold** (A): Shimmer animation does not flash more than three times per second
- **4.1.2 Name, Role, Value** (A): Loading state communicated via ARIA attributes to assistive technology
- **4.1.3 Status Messages** (AA): Loading status announced without receiving focus via live regions

For complete reference: [Orange Accessibility Guidelines - Components](https://a11y-guidelines.orange.com/en/web/components-examples/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Dynamic Content](https://a11y-guidelines.orange.com/en/web/develop/dynamic-content/)
- [More Accessible Skeletons - Adrian Roselli](https://adrianroselli.com/2020/11/more-accessible-skeletons.html)
- [WCAG 2.2 Understanding Status Messages](https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html)
- [Carbon Design System - Loading Pattern](https://carbondesignsystem.com/patterns/loading-pattern/)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Dec 5, 2024 | 1.0.0 | • Component creation | Maxime Tonnerre |