### ⚠️ Specific focus state rules

In the Focus state, the border of the input field becomes thicker (2px instead of 1px). If the border were centered on the edge of the input, half of its thickness (0.5px inward and 0.5px outward) would increase the overall size of the component and could cause layout shifts or alignment issues with surrounding content.

To prevent this, the 2px border must expand inward rather than extending outward. This ensures:
• The component's outer dimensions remain constant, avoiding layout shifts.
• Visual consistency and alignment with adjacent elements.

**Practical implementation:**
• Use CSS techniques like box-sizing: border-box to ensure the border grows inward.
• Alternatively, create a pseudo-element (::before or ::after) positioned inside the component to simulate the thicker border without altering the component's box model.
• Avoid using outline, which may expand outward and cause unwanted misalignment, unless implemented with a negative offset.