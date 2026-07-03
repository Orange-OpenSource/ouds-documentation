The AI assistant icon is especially challenging because it has no visible label and no button container: the sparkle icon is the only cue, state is conveyed by color alone, and the small, container-less hit area must still be reachable and operable for everyone.

### Key Challenges

- Providing an accessible name when there is no visible text label
- Conveying interactive state without a background — color transitions only
- Keeping an adequate interactive target despite the container-less, custom size
- Announcing the Loading state so users know the AI is processing their request

### Critical Success Factors

1. Use a native `<button>` element wrapping the icon for keyboard and screen-reader support
2. Give every Assistant icon a descriptive accessible name via `aria-label`
3. Preserve a minimum 28px interactive area (larger where touch is the primary input)
4. Provide a visible focus indicator with ≥3:1 contrast against adjacent colors