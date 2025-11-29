**`Trailing`** It places both the increment and decrement buttons on the right side of the input field, either stacked vertically or positioned side by side. This layout is compact and visually streamlined, making it ideal for dense interfaces or mobile views.

**`Split`** It positions the decrement button to the left of the input and the increment button to the right. It provides a more balanced and intuitive interaction model, especially in use cases like e-commerce where users frequently adjust quantities.

### Do & don'ts

✅ **Do:** Use split placement for e-commerce quantity selectors where users frequently adjust values in both directions  
❌ **Don't:** Use trailing placement when the decrease action is equally important as increase—split provides better balance

✅ **Do:** Apply trailing placement in compact table cells or data grids where horizontal space is limited  
❌ **Don't:** Force split placement in narrow containers where it causes the input field to become too small

✅ **Do:** Consider trailing placement for RTL (right-to-left) interfaces where it may provide more natural interaction  
❌ **Don't:** Ignore localization requirements when choosing button placement

✅ **Do:** Use split placement when touch targets need to be easily distinguishable for mobile users  
❌ **Don't:** Use trailing placement with stacked buttons if users struggle to tap the correct control

✅ **Do:** Test both placements with real users to determine which reduces errors in your specific context  
❌ **Don't:** Assume one placement universally outperforms the other without user research