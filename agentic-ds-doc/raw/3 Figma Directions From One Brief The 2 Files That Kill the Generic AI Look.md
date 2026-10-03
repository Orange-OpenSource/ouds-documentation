---
title: "3 Figma Directions From One Brief: The 2 Files That Kill the Generic AI Look"
source: "https://medium.com/design-bootcamp/3-figma-directions-from-one-brief-the-2-files-that-kill-the-generic-ai-look-1d67d2ecea7e"
author:
  - "[[Sumeet]]"
published: 2026-06-04
created: 2026-06-15
description: "More"
tags:
  - "clippings"
---
> The two markdown files that stop AI-generated Figma screens from coming out generic and drifting between directions.

~9 min read. For product designers who have tried generating Figma screens with Claude Code and the Figma MCP, found the output generic or inconsistent across screens, and want three coherent, on-brand directions in a single sitting. By the end you will have a filled `brief.md`, a filled `architecture.md`, and the exact @-mention generation prompt that feeds both into every Claude session.

![](https://miro.medium.com/v2/resize:fit:4800/format:webp/1*gMOim1973XI06P92S7bNOw.png)

## Why your AI Figma designs come out generic, and then drift

You have already done the setup. Claude Code is running, the Figma MCP is wired, you pulled three Dribbble references that actually look like the product you are designing. You fire off the prompt: “Generate a Figma design based on this reference.” You open three Claude sessions, one per reference, run them in parallel, and wait.

What comes back is technically impressive. Editable layers, auto-layout frames, components you can click into. And every single one looks like the same beige SaaS template wearing different accent colors. You pick the one that is closest and ask for screen two. It has different spacing on the card grid. The button style changed. There is a sidebar that was not there before.

That is not a one-off. It is the same result every time you run it without a specific setup. And here is what most demos gloss over: the references were not the problem.

The Figma reference was always doing one job: seeding a surface aesthetic. It was never going to tell Claude what your product actually does, who it is for, what your brand colors are, or how your screens relate to each other. Those gaps are what make the output generic. The structural drift between screens is a second, different gap, one the reference image has no ability to fill.

By the end of this article you will have built the two files that fill both gaps: a `brief.md` that carries your product and brand context into every generation, and an `architecture.md` that locks your screen structure so the second direction matches the first. You will also have the verbatim @-mention generation prompt that plugs both in.

## One complaint, two different failures

“My AI Figma output is bad” almost always collapses two distinct failures into one frustrated sentence. They look like the same problem because they show up in the same output, but they have different causes and need different fixes.

**Failure one: generic output.** The three directions all look like default SaaS. The colors are close to yours but not quite. The type size is not your type size. The component patterns are unfamiliar. This is a brand and system-context failure. The model generated UI without knowing your design system, your brand tokens, or the specific constraints of your product. As Builder.io documented in 2026, Figma AI “doesn’t fully understand your design system, generating a generic UI that looks nice but doesn’t match your brand colors, typography, spacing rules, or component patterns.” The same failure applies when you drive generation through Claude Code. If you do not provide system context, the model fills the gap with plausible defaults.

**Failure two: inconsistent output across screens.** Screen one of direction A has a certain card component, a certain nav structure, a certain spacing system. Screen two has different spacing on the cards. The nav acquired a sidebar. The button hierarchy shifted. This is a structure and architecture failure. The model has no memory of what it generated before unless you explicitly hand it that memory in every session. Prompting “respect the same visual direction” is a band-aid. It is prompt-side memory that degrades generation to generation.

Reuse the symptoms from the opening as the diagnostic: the different spacing, the new button style, the phantom sidebar that appeared between screens. That is Failure Two exactly. The beige-SaaS clones? That is Failure One. They look related because they appear in the same output, but they require separate files to fix.

One file per failure. `brief.md` for the generic problem. `architecture.md` for the drift problem. Both @-mentioned in every generation prompt.

## Why the reference image is the least important input

The counterargument is obvious: “I got better results when I used a better reference.” That is true and also misleading. What the reference controls is surface aesthetics: a rough color mood, a layout density, a typographic feel. It seeds style, and style is real.

What the reference cannot do: tell the model your brand color is `#1A1A2E` not `#1C1C3A`, that your body copy is Inter 14px/1.5 not SF Pro 15px/1.4, that your primary CTA is always a full-width pill on mobile, or that the settings flow has six screens and the third one is always a confirmation modal. Feed it three different references with roughly similar aesthetics and you will still get roughly similar generic output. The generic failure is not in the reference selection. It is in the absence of system context that no reference can supply.

The Sergei Chyrkov practitioner write-up from 2026 arrives at the same conclusion from the designer’s side: the fix for generic output is feeding the model project-specific context, not finding better reference images. That is the same diagnosis from two directions.

References are still in the workflow. They stay because they seed visual direction quickly and give you three starting points with genuine stylistic variety. But they are the last input in the chain. The seasoning, not the structure. The two grounding files are the structure.

## The 30-second setup (so the workflow is reproducible)

If you are already running Claude Code with the Figma MCP, skip this section. If you need to verify the connection is live before the files below will work, here is the two-command path.

**Plugin install (Figma Learn, 2026):**

```hs
claude plugin install figma@claude-plugins-official
```

Restart Claude Code, then type `/plugin` to open the marketplace, select Figma, complete browser auth, and type `/plugin` again to confirm.

**Direct MCP add (Figma Developer Docs, 2026):**

```hs
claude mcp add --transport http figma https://mcp.figma.com/mcp --scope user
```

The `--scope user` flag makes it available across all your projects. Verify with `/mcp`.

That is the floor. The workflow below assumes that connection is live.

## brief.md: the file that kills generic

Create a file called `brief.md` at the root of your Claude Code project directory. This is the file you @-mention in every generation session. It tells Claude what the references cannot tell it.

Here is the fillable template:

```hs
# Product brief
```
```hs
## Product
[One sentence: what the product does and who it is for. Be specific enough that an outsider could understand it.]
Example: "A task management app for remote engineering teams that need async standup tracking without daily calls."## Audience
[Role, context, technical fluency. One sentence.]
Example: "Engineering team leads at companies with 10–50 person teams; comfortable with Jira, resistant to another meeting tool."## Tone and personality
[Three adjectives + one sentence that grounds them.]
Example: "Calm, functional, focused. The visual language should feel like a tool, not a product — closer to Linear than to Notion."## Brand tokens### Colors
- Primary: [hex]
- Secondary: [hex]
- Background: [hex]
- Text: [hex]
- Error / warning / success: [hex each]### Typography
- Body: [Font, size, line height] — Example: Inter 14px / 1.5
- Heading 1: [Font, size, weight]
- Heading 2: [Font, size, weight]
- Labels: [Font, size, weight, letter spacing if relevant]### Spacing
- Base unit: [4px or 8px]
- Card padding: [value]
- Section gap: [value]### Component patterns
- Buttons: [shape, size, fill vs outline rules]
- Input fields: [border radius, label position]
- Navigation: [top bar / sidebar / tab bar — which pattern and when]## What this product is NOT
[One sentence naming the closest wrong direction — prevents the model from pulling toward a generic comparator.]
Example: "Not a consumer app — avoid playful colors, large illustrations, or social-proof UI patterns."
```

Every field has a job. The color tokens stop the model from choosing its own plausible defaults. The typography spec stops the size drift. The component patterns section is the one most designers skip and the one that causes the most obvious generic output. If you do not specify “full-width pill primary CTA,” the model will pick a rounded rectangle that looked right in its training data, not in your design system.

The “what this product is NOT” line is worth writing carefully. The model will pull toward the nearest recognizable pattern unless you explicitly exclude it. Naming the wrong direction is faster than describing every constraint that blocks it.

## architecture.md: the file that kills drift

Create a second file called `architecture.md` in the same directory. This is the structural memory that replaces the prompt-side "respect the same direction" instruction, which degrades every time you open a new window.

Here is the template:

```hs
# Screen architecture
```
```hs
## Screen inventory
List every screen in this direction by name and number.
- 01 — [Screen name]: [One sentence describing its function and what the user does here]
- 02 — [Screen name]: [Function + action]
- 03 — [Screen name]: [Function + action]
[...continue for all screens in scope]## Shared layout rules (apply to all screens)
- Navigation: [Describe the persistent nav — position, content, behavior]
- Header: [Height, content, behavior — fixed / sticky / none]
- Content area: [Max width, padding, column grid]
- Footer or bottom bar: [Present / absent, behavior if present]## Component reuse rules
- [Component name]: appears on screens [list screen numbers]. Use the same [width / color / hierarchy / label pattern] every time.
- Example: "Primary CTA button: appears on screens 01, 03, 05. Always full-width on mobile. Label is always a verb phrase."## Screen-specific notes (only for exceptions to the shared rules)
- Screen 03: [Note any exception to the shared rules and why]## What must NOT vary between screens
- [List the things that, if they change, the direction loses coherence.]
- Example: "Card corner radius must be 8px on every screen — do not let this shift."
- Example: "The left sidebar is present on all desktop views. Do not collapse it to a top bar."
```

Claude Code + Figma MCP direction generation ⬇

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*fVv4OTYyTNEizoR9j4ojNQ.png)

The key move here is the “what must NOT vary” section. It is the explicit list of constraints that would make the reader of screen two say “that is a different product.” The phantom sidebar that appeared in the opening example? That is what happens when `architecture.md` does not exist and Claude fills in what seems structurally reasonable for a second screen.

Contrast this with the source video’s approach: prompting “respect the exact same visual direction as the first screen” inside a single session. That works for one generation in one window. When you open a second or third parallel window for a different direction option, that prompt-side memory is gone. An @-mentioned `architecture.md` travels with every window identically, because it is a file, not a conversation history.

## The generation prompt, and why three windows is a convenience, not the magic

With both files in place, here is the verbatim generation prompt to paste into each Claude Code session:

```hs
@brief.md @architecture.md
```
```hs
Reference image: [paste or attach your reference]Generate a Figma design for [Screen name and number from architecture.md].Apply the brand tokens from brief.md exactly — use the specified hex values, typography, and component patterns. Follow the shared layout rules in architecture.md. This is direction [A / B / C] — treat the reference as the visual mood, not the layout spec. The layout spec is architecture.md.When the screen is ready in Figma, confirm which elements used the brief.md tokens and flag any area where you had to make a judgment call not covered by either file.
```

The @-mention syntax is what routes Claude to the files as context before generation starts. `@brief.md` grounds the brand tokens. `@architecture.md` locks the structure. The reference image seeds the visual mood. That ordering is intentional: the files are the authority, the reference is the suggestion.

Three parallel windows running this same prompt, each with a different reference image, is the parallel-fan-out approach from the source video. It is a genuinely useful mechanic for getting three simultaneous options without waiting. But the design tokens come from `brief.md`. The structural coherence comes from `architecture.md`. Remove both files and three parallel windows just produce three inconsistent clones faster. The windows are a convenience layer on top of the grounding pair. Not the quality mechanism.

## What you actually get back, and when to fix vs re-prompt

The output is explorable design directions and first-draft layouts, not handoff-ready screens. That is what the workflow is for.

Builder.io’s 2026 analysis of the Claude Code to Figma pipeline names the maturity gaps plainly: round-trips lose business logic and state, the workflow involves roughly five context switches with information loss, the `get_code` tool struggles when elements carry annotations, and Code Connect has limits on non-enterprise plans. The auto-layout structure of generated frames is described as editable components by both Figma (Figma Blog, 2026) and Builder.io (2026), but exact auto-layout fidelity varies per generation. Treat it as observed, not guaranteed.

The source video claims three directions in approximately three minutes. That is the creator’s benchmark from one recorded session, not an independent measurement. In practice, generation time varies with prompt complexity and connection speed. What is reproducible is the structure: one grounded sitting, three coherent directions, same session.

The practitioner decision the demos skip is what to do when a direction comes back wrong. Here is the rule:

**Close but visually off:** fix it in Figma. Move a component, adjust spacing, swap a color from the brand token list in `brief.md`. This is the normal case. The direction is right; a detail drifted.

**Structurally wrong:** re-prompt Claude with a screenshot of the Figma result plus `@architecture.md`. The prompt: "This is what was generated. Screen 03 has a sidebar that should not be there. architecture.md shows this screen has no sidebar. Fix it." The screenshot gives Claude the visual state; `architecture.md` gives it the authority to judge what is wrong. This loop takes one exchange in most cases.

The refinement loop is where the grounding files pay off a second time. Without `architecture.md`, you would be describing the problem in the prompt from memory. With it, you point to the file and the file is the spec.

**Thinking exercise:** Before you touch a reference image for your current project, write your own `brief.md` and `architecture.md` first. Open a new file, fill in the brand tokens section for real: hex values, not placeholders. Then list every screen in the flow you are designing and write one sentence for each. Do this before the first generation prompt. Notice what you did not know off the top of your head. Those are the gaps the model would have filled with plausible defaults.

## The files are the asset, not the references

References are disposable. You will search for better ones next project, maybe even next screen. The `brief.md` and `architecture.md` you build for this project are reusable. Update the brand tokens once when the design system changes. Add screens to the architecture file when scope expands. These files do not expire.

Figma’s own product direction validates the mechanism. In 2026, Figma shipped “Skills,” described in their documentation as reusable instruction sets that “provide guidance for how an agent should complete specific tasks, using a combination of MCP tool calls and detailed instructions.” That is the same structural bet: persistent, structured context beats one-off asset references for making agent output coherent. Figma named it for design-system workflows; the `brief.md` plus `architecture.md` pair applies the same logic to direction-generation.

The dominant framing in most Claude Code + Figma demos, including the video that prompted this article, treats the parallel-window trick and the reference selection as the levers to pull. They are conveniences layered on top of the actual mechanism. The grounding pair is what separates three coherent, on-brand client-ready directions from three Dribbble clones with different accent colors. Build the files once. They travel with every generation, every window, every project that shares the same design system.