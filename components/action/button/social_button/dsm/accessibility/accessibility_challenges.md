A social button shows only a logo. Users who cannot see it, or who do not recognise the network, depend entirely on its text alternative, and small buttons placed in a row are easy to miss or to hit by mistake.

### Key Challenges

- An icon-only control has no visible label: without a text alternative it is announced as an unnamed button or link
- The logo names the network but not the action: sharing, following and opening a profile look the same
- Several small buttons in a row need enough size and spacing to be activated reliably
- Loading, Disabled and Skeleton states must be conveyed to assistive technologies, not only visually

### Critical Success Factors

1. Give every button an accessible name that states the network and the action, such as "Share on Facebook" (WCAG 4.1.2)
2. Use a link for navigation to a profile or site and a button for an in-page action such as sharing
3. Keep the 48 px minimum interactive area and leave space between adjacent buttons (WCAG 2.5.8)
4. Announce the Loading state and keep the accessible name while the icon is replaced by the loader