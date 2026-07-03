Because Display is purely visual, its accessibility depends on the surrounding markup and color: large text must keep sufficient contrast, must scale when users zoom, and must map to a meaningful heading structure rather than relying on size alone to imply importance.

### Key Challenges

- Conveying importance semantically, not just through large size
- Maintaining contrast against backgrounds, including imagery and gradients
- Supporting text resize and zoom up to 200% without loss of content
- Allowing reflow so large text doesn't force horizontal scrolling

### Critical Success Factors

1. Map Display text to a correct semantic element (e.g. `<h1>`) when it acts as a heading
2. Keep contrast ≥3:1 for large text (≥4.5:1 where the size could fall below the large-text threshold)
3. Use relative units so text scales with user and browser settings
4. Allow content to reflow to a single column at 320px-equivalent width