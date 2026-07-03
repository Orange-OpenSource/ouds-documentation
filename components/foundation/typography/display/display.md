# Guideline

## Intro 👈🤖

Display is the largest type style, reserved for high-impact moments — hero headlines and key messages that must capture immediate attention.

---

## Definition

Display styles are intended for high-impact content such as landing pages, marketing campaigns, and key messages. Their large type sizes help capture attention and establish strong visual emphasis.
Variants automatically adapt across breakpoints to maintain a consistent visual hierarchy on every screen size.
Use them sparingly to preserve their impact and effectiveness.

---

## Best for 👈🤔

✅ Hero sections and above-the-fold headlines on landing pages

✅ Marketing campaign banners and promotional key messages

✅ Splash screens and onboarding statements that set the tone

✅ Large numeric or statistic callouts that must dominate the page

✅ Editorial covers or feature headers with strong visual emphasis

✅ Empty-state or success screens needing a confident focal point

✅ Brand moments where typography carries the visual identity

✅ Responsive page headers that must scale gracefully across breakpoints

✅ Establishing the single largest element in a page's visual hierarchy

✅ Short, punchy phrases — never long paragraphs of running text

---

## Anatomy 👈🤖

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Font family | Theme `display` font-family token defining the typeface | N |
| 2 | Font weight | Weight applied to Display styles (bold) | N |
| 3 | Font size | Type size per variant — Large 40px, Medium 36px, Small 32px | N |
| 4 | Line height | Vertical rhythm per variant — Large 48px, Medium 44px, Small 40px | N |
| 5 | Letter spacing | Negative tracking that keeps large sizes optically tight | N |
| 6 | Responsive scaling | Automatic adaptation across breakpoints to preserve hierarchy | N |

---

## Size

**`Large`** The largest Display size, intended for maximum visual impact. Use it for hero sections, key messages, and high-priority content that requires immediate attention.

**`Medium`** A prominent Display size that provides strong emphasis while maintaining a more balanced visual presence. Suitable for major content areas and featured messages.

**`Small`** The most compact Display size, offering visual impact in space-constrained layouts. Use it when a display style is needed without overwhelming surrounding content.

---

## size_do_&_dont 👈🤔

✅ **Do:** Reserve Display styles for the single most important message on a screen.  
❌ **Don't:** Place multiple Display styles in the same view, diluting their impact.

✅ **Do:** Use Large for hero or high-priority content that must grab attention immediately.  
❌ **Don't:** Use Large in space-constrained layouts where it overwhelms surrounding content.

✅ **Do:** Step down to Medium or Small as available space or hierarchy decreases.  
❌ **Don't:** Force a Display size that causes awkward wrapping or truncation.

✅ **Do:** Let Display variants adapt across breakpoints to keep hierarchy consistent.  
❌ **Don't:** Hard-code pixel sizes that break the responsive type scale.

✅ **Do:** Pair Display with calmer Heading and Body styles to preserve hierarchy contrast.  
❌ **Don't:** Combine Display with other oversized styles that compete for attention.

---

# Specs

## States

🚧 Not applicable — Display is a non-interactive typography style and has no interactive states.

---

## Layout and spacing

🚧 Content to be added

---

# Accessibility 👈🤖

## Accessibility intro

Display styles must meet WCAG 2.2 Level AA, staying legible and resizable for everyone regardless of how the text is enlarged or reflowed. For comprehensive guidance, see the [Orange Unified Design System Accessibility Overview](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability).

---

## Accessibility Challenges

Because Display is purely visual, its accessibility depends on the surrounding markup and color: large text must keep sufficient contrast, must scale when users zoom, and must map to a meaningful heading structure rather than relying on size alone to imply importance.

### Key Challenges

- Conveying importance semantically, not just through large size
- Maintaining contrast against backgrounds, including imagery and gradients
- Supporting text resize and zoom up to 200% without loss of content
- Allowing reflow so large text doesn't force horizontal scrolling

### Critical Success Factors

1. Map Display text to a correct semantic element (e.g. `<h1>`) when it acts as a heading
2. Keep contrast ≥3:1 for large text (≥4.5:1 where the size could fall below the large-text threshold)
3. Use relative units so text scales with user and browser settings
4. Allow content to reflow to a single column at 320px-equivalent width

---

## Design Requirements

### Structure & Labels

- [ ] **Semantic heading**: Apply Display to a real heading element when it introduces content ([Heading guidance](https://a11y-guidelines.orange.com/en/web/develop/page-structure/))
- [ ] **Hierarchy**: Don't skip heading levels to obtain a particular size — choose the style independently from the level
- [ ] **One per view**: Reserve a single Display as the top of the visual hierarchy

### Visual Design

- [ ] **Contrast**: Meet ≥3:1 for large text against its background ([Contrast guidance](https://a11y-guidelines.orange.com/en/web/design/color-and-contrast/))
- [ ] **Over imagery**: Add a scrim or solid backing when Display sits on photos or gradients
- [ ] **Resize**: Use relative units so text scales to 200% without clipping

### Content

- [ ] **Concise**: ❌ Long sentences / ✅ Short, punchy phrases ([Content guidance](https://a11y-guidelines.orange.com/en/web/design/textual-content/))
- [ ] **No size-as-meaning**: Don't rely on size alone to communicate priority to assistive tech

---

## Testing Checklist

### Zoom & Reflow Testing

- [ ] Zoom to 200% and 400%; confirm no content loss, clipping, or horizontal scroll
- [ ] Verify Display reflows to a single column at a 320px-equivalent width

### Contrast Testing

- [ ] Check Display contrast against every background it appears on, including imagery

### Structure Testing

- [ ] Confirm Display headings expose a correct, non-skipping heading outline to screen readers

Resources: [Orange Accessibility Testing Guide](https://a11y-guidelines.orange.com/en/web/testing/)

---

## Key WCAG Criteria

- **1.4.3 Contrast (Minimum)** (AA): Text meets minimum contrast; large text may use the ≥3:1 ratio
- **1.4.4 Resize Text** (AA): Text can be resized to 200% without loss of content or function
- **1.4.10 Reflow** (AA): Content reflows to a single column without horizontal scrolling
- **1.4.12 Text Spacing** (AA): No loss of content when users adjust spacing
- **1.3.1 Info and Relationships** (A): Heading roles conveyed programmatically, not by size alone

For complete reference: [Orange Accessibility Guidelines](https://a11y-guidelines.orange.com/en/web/)

---

## Additional Resources

- [Orange Accessibility Guidelines - Typography](https://a11y-guidelines.orange.com/en/web/design/typography/)
- [W3C WAI - Text Resize](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)
- [WCAG 2.2 Understanding Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html)
- [Orange Design System - Accessibility & Sustainability](https://unified-design-system.orange.com/472794e18/p/88ebab-accessibility-and-sustainability)

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Jun 16, 2026 | 1.0.0 | <ul><li>Component creation</ul> | Maxime Tonnerre<br>Jérôme Regnier |
