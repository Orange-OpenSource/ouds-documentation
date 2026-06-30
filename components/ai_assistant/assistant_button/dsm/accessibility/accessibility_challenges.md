AI assistant buttons present specific accessibility challenges: the AI icon is often the only cue that an action is AI-powered, the "Icon only" layout has no visible label, and the Loading state must communicate that the AI is working without trapping focus or hiding progress from assistive technology.

### Key Challenges

- Providing an accessible name when the "Icon only" layout shows no visible label
- Conveying the AI-powered nature of the action beyond the decorative sparkle icon
- Announcing the Loading state so users know the AI is processing their request
- Maintaining a visible focus indicator and an adequate touch target at every size

### Critical Success Factors

1. Use a native `<button>` element for built-in keyboard and screen-reader support
2. Give every "Icon only" button a descriptive accessible name via `aria-label`
3. Announce processing with `aria-live` / `aria-busy` during the Loading state
4. Provide a visible focus indicator with ≥3:1 contrast against adjacent colors