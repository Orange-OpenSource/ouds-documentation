A categorical tag separates categories mainly through colour. Users who cannot perceive the colours, or who use a screen reader, depend on the label alone, and the colour slots change with the theme or the local guidelines.

### Key Challenges

- Colour is the main differentiator: two tags with similar labels must still be told apart without it
- Five colour slots across several themes must all keep a readable contrast with the label
- The tag is not interactive: it must not be focusable or announced as a control
- Loading, Disabled and Skeleton states must be conveyed in text, not only by a spinner or a muted colour

### Critical Success Factors

1. Put the whole meaning in the label; colour, bullet and icon only reinforce it (WCAG 1.4.1)
2. Keep a 4.5:1 contrast ratio between the label and each categorical colour, in every theme (WCAG 1.4.3)
3. Expose the tag as plain text read with the content it qualifies, with no role, tab stop or pointer feedback
4. Let the label wrap and the tag grow when text is resized; never truncate the category