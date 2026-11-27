✅ **Do:** Use reverse layout for right-to-left (RTL) languages like Arabic and Hebrew  
❌ **Don't:** Use reverse layout arbitrarily without considering reading direction conventions

✅ **Do:** Apply reverse layout consistently across all radio buttons when supporting RTL interfaces  
❌ **Don't:** Mix LTR and RTL radio button layouts on the same page or within the same form

✅ **Do:** Position the radio indicator on the trailing edge (right side for LTR, left for RTL) for mobile list interfaces  
❌ **Don't:** Place indicators in inconsistent positions across different screen sizes

✅ **Do:** Ensure tab order and focus management work correctly regardless of visual layout direction  
❌ **Don't:** Assume visual order equals DOM order—verify keyboard navigation flows logically

✅ **Do:** Test reverse layouts with screen readers to confirm proper announcement order  
❌ **Don't:** Rely solely on visual testing when implementing layout variants