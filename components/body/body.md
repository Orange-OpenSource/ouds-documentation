---
id: typography-body
category: Content display
family: Typography
---

# Body

A body is a UI element that styles typography for common text content like paragraphs, descriptions, and informational messages.

# Guideline

<img src="images/hero_image_body.png" alt="hero_image_body" width="864">

## Anatomy

<img src="images/body@anatomy_img.png" alt="body@anatomy_img" width="864">

| # | Element | Purpose | Optional |
|---|---------|---------|----------|
| 1 | Body container | The component: the text block whose width and alignment are set by its container | No |
| 2 | Body text | The text itself, styled with the Body type scale | No |

## Definition

A body is a UI element that styles typography for common text content like paragraphs, descriptions, and informational messages.

The body features multiple size options, to allow content importance to be expressed while maintaining consistency. Variants automatically adjust across breakpoints to ensure optimal readability on all devices. Body prioritize readability and provide a comfortable reading experience.

## Size

<!-- zh-row -->

**`Large`** The most prominent body text size, ideal for introductory paragraphs, highlighted content, or situations where enhanced readability is desired.

**`Medium`** The default body text size, providing an optimal balance between readability, information density, and visual hierarchy across most use cases.

**`Small`** A compact body text size intended for supporting information, secondary content, and dense layouts where space efficiency is important.

<img src="images/body@size_img.png" alt="body@size_img" width="433">

## Weight

<!-- zh-row -->

**`Default`** The default weight provides the standard level of typographic emphasis for Body and Label styles. It is designed for optimal readability and neutral hierarchy, making it the baseline for most interface content. Use it whenever no additional emphasis is required.

**`Moderate`** Moderate weight increases visual presence while remaining balanced and readable. It is used to reinforce hierarchy within Body and Label typography without introducing strong emphasis. Suitable for highlighting important information or improving scanability.

**`Strong`** Strong weight provides the highest level of emphasis for Body and Label styles. It is intended for critical information, key actions, or elements that must stand out within dense content. Use it sparingly to preserve its impact and avoid visual overload.

<img src="images/body@weight_img.png" alt="body@weight_img" width="433">

## Multiline and responsiveness

<!-- zh-row -->

### Multiline
This component allows multi-line text editing. The number of lines is not limited.

&nbsp;

### Max-width vs full-width
This component has a default max-width.  
For the “Body large” variant, the global max-width token will be: size-max-width-body-large  
For the “Body medium” variant, the global max-width token will be: size-max-width-body-medium  
For the “Body small” variant, the global max-width token will be: size-max-width-body-small

&nbsp;

### User zoom in/out
The behavior of the text during user zoom in/out must follow a fundamental principle: the text must remain readable, accessible, and must never break the structure or lose information.  
  • The text must always scale proportionally with user zoom. Text resizing must never be blocked.  
  • Zooming must never cause text to be truncated or hidden. The component must expand vertically to allow line wrapping.  
  • The component’s height and width must be flexible, never fixed, in order to automatically adapt its dimensions according to the level of zoom.  
  • Even if, the component has a max-height or a max-width for resizing control purposes, technically, during user zoom in, these limitations are not fixed but must be scalable in order to adapt to the user’s zoom level.

<img src="images/body@multiline_and_responsiveness_img.png" alt="body@multiline_and_responsiveness_img" width="433">

# Specs

## Layout and spacing

<img src="images/body@spec_layout_spacing.png" alt="body@spec_layout_spacing" width="864">

# Accessibility

Work is in progress to deliver this content.

# Develop

## OUDS-Web example

[Components/Typography › Typography 4](https://web.unified-design-system.orange.com/storybook/?path=/story/components-typography--typography-4)

## Developer documentation

| Platform | Developer documentation |
|---|---|
| OUDS Web | [S-ouds-web-typography-body](https://r.orange.fr/r/S-ouds-web-typography-body) |
| OUDS Android | [S-ouds-android-typography-body](https://r.orange.fr/r/S-ouds-android-typography-body) |
| OUDS iOS | [S-ouds-ios-typography-body](https://r.orange.fr/r/S-ouds-ios-typography-body) |
| OUDS Flutter | [S-ouds-flutter-typography-body](https://r.orange.fr/r/S-ouds-flutter-typography-body) |

# Changelog

## Availability

| Platform | Resource | Status | Version |
|---|---|---|---|
| Figma | [Body component](https://r.orange.fr/r/S-ouds-design-typography-body) | Live | 1.0.0 |
| OUDS Web (former Boosted) | [Web dev documentation](https://r.orange.fr/r/S-ouds-web-typography-body) | Live | 1.0.0 |
| OUDS Android - Jetpack Compose | [Android dev documentation](https://r.orange.fr/r/S-ouds-android-typography-body) | Live | 1.0.0 |
| OUDS iOS - Swift | [iOS dev documentation](https://r.orange.fr/r/S-ouds-ios-typography-body) | Live | 1.0.0 |
| OUDS Flutter | [Flutter dev documentation](https://r.orange.fr/r/S-ouds-flutter-typography-body) | Live | 1.0.0 |

## Design changelog

| Date | Number | Notes |
|------|--------|-------|
| Jun 16, 2026 | 1.0.0 | <ul><li>Component creation</ul> |
