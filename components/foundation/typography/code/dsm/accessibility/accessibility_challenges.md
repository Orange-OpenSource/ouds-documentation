Monospace technical text introduces specific challenges: it must keep sufficient contrast, remain resizable and reflowable (or scroll predictably for long lines), and its code-like meaning should be conveyed semantically rather than by appearance alone.

### Key Challenges

- Maintaining ≥4.5:1 contrast for code text on its background
- Handling long lines without trapping content off-screen
- Conveying "this is code" semantically, not by monospace styling alone
- Keeping code legible and resizable up to 200% zoom

### Critical Success Factors

1. Use semantic `<code>`/`<pre>` elements for inline and block code
2. Keep ≥4.5:1 contrast, including for syntax-colored tokens
3. Allow horizontal scroll within the code block rather than clipping content
4. Use relative units so code resizes with user settings