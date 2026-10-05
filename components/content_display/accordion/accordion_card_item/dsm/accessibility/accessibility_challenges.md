An accordion hides content until users ask for it. Users who do not notice the control, or who cannot see the indicator change, may never find the content or may not know that it has appeared.

### Key Challenges

- The expanded or collapsed state is shown by an icon: it must also be exposed programmatically
- The whole trigger is one control: leading, trailing and slot content must not create extra, competing targets
- Collapsed content must be hidden from assistive technologies and from the focus order, not only visually
- Long labels, optional elements and zoom must not truncate the information users need to choose a section

### Critical Success Factors

1. Make each trigger a button inside a heading of the right level, with `aria-expanded` and `aria-controls` (WCAG 4.1.2)
2. Operate the trigger with Enter and Space, and keep Tab moving through triggers and visible content in page order
3. Keep collapsed content out of the accessibility tree and the tab sequence
4. Do not rely on the indicator or on colour alone to convey the state or the status of a section