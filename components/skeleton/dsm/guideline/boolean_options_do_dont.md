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