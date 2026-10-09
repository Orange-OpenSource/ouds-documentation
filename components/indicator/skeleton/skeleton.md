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

# Accessibility

## Motion & Animation accessibility rules

In terms of animation, there are accessibility criteria to consider: “Animation from Interactions” and “Pause, Stop, Hide.”
These two main criteria address different issues:

**Pause, Stop, Hide - WCAG 2.2.2**
This concerns moving, blinking, scrolling, or automatically updating content.
The question to ask is: does the animation start automatically and meet the criterion’s conditions?
When a relevant animation lasts more than 5 seconds, users must be able to pause, stop, or hide it.
The two criteria should therefore be evaluated independently.

**Reduced Motion (Animation from Interactions) - WCAG 2.3.3**
This primarily concerns motion-based animations triggered by user interaction.
The question to ask is: is the movement essential to the functionality or to the information being conveyed?
If not, the animation should be removed, reduced, or replaced when the user has enabled Reduced Motion.

ℹ️ The reduced motion preference can be configured by the user at the operating system level and is available to websites through the CSS prefers-reduced-motion media feature.

Concrete application to the Skeleton:

**Pause, Stop, Hide**
When a skeleton uses an automatic shimmer animation, it is recommended to keep the animation short and avoid looping it indefinitely when this is not necessary.
If the automatic animation meets the criterion's conditions, users must be able to pause, stop, or hide it.
A recommended alternative is to play a single short animation, then keep the skeleton blocks in a static state until the content has loaded.

**Reduced Motion**
Skeleton animation is not essential to conveying the information that content is currently loading.
When Reduced Motion is enabled, the skeleton animation should therefore be removed. The skeleton blocks should remain visible in a static state until the content has loaded.

---

# Changelog

| Date | Number | Notes | Designer |
|------|--------|-------|----------|
| Dec 5, 2024 | 1.0.0 | • Component creation | Maxime Tonnerre |