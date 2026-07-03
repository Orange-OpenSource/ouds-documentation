A status icon carries meaning visually, so that meaning must also reach screen-reader users and not depend on color perception. Decorative duplicates must be hidden, and any animation must respect reduced-motion preferences.

### Key Challenges

- Conveying status meaning to assistive tech, not by color or shape alone
- Avoiding duplicate announcements when adjacent text already states the status
- Meeting non-text contrast for the icon against its background
- Respecting `prefers-reduced-motion` for the animated variant

### Critical Success Factors

1. Provide a text alternative for the status (or expose it via the surrounding message)
2. Hide the icon from assistive tech (`aria-hidden`) when adjacent text already conveys the status
3. Don't rely on color alone — pair it with the standardized symbol
4. Honor reduced-motion settings; the static state must convey the same meaning