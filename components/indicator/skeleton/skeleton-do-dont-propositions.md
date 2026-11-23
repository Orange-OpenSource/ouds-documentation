# Skeleton — do & don't propositions

AI-generated propositions that no one has validated yet. They are not part of the documentation ([skeleton.md](skeleton.md)) and are not shown on zeroheight. Once a designer validates one, it moves into the full file.

## When to use

✅ To represent a loading state while content is being fetched or processed

✅ When it is important to preserve layout structure and avoid content shifts

✅ In scenarios where loading takes a noticeable amount of time

✅ To reduce perceived waiting time and improve performance perception

## Boolean options — do & don't

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
