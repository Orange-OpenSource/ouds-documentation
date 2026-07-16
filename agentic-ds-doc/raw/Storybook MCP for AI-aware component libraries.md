---
title: "Storybook MCP for AI-aware component libraries"
source: "https://blog.logrocket.com/storybook-mcp-component-libraries/"
author:
  - "[[Ikeh Akinyemi]]"
published: 2026-07-06
created: 2026-07-16
description: "Learn how Storybook MCP lets AI agents understand your component library, reuse existing UI components, generate stories, and validate code with automated tests."
tags:
  - "clippings"
---
When an AI agent builds UI, it works from its training data and whatever happens to be in its prompt. It has no awareness of the components your team has already built, the prop contracts they expose, or the patterns your design system enforces. The result often looks close enough at first glance, but it relies on invented APIs and ignores decisions your codebase has already made.

The obvious workaround is to paste component source files into the prompt, but that falls apart quickly. A real design system contains dozens of components, each with its own variants, usage guidelines, and interaction states, far more than you can reliably fit into a model’s context window. Instead of querying a structured source of truth, the agent ends up pattern-matching against whatever text you’ve managed to provide.

The Storybook MCP server takes a different approach. It exposes your component library as a set of callable tools that an agent can query at runtime. Rather than relying on prompt context alone, the agent can discover which components exist, fetch documentation for specific components, generate stories, and run targeted tests against them. Think of it as a structured feedback loop instead of a one-shot prompt. Storybook 10.3 ships with `@storybook/addon-mcp`, making it easy to wire this workflow into your existing development server.

## Setup

The [MCP server](https://blog.logrocket.com/introducing-the-logrocket-mcp/) ships as part of `@storybook/addon-mcp` and runs inside your Storybook development server. There’s no separate server to manage and no external service to configure.

Start by scaffolding a React TypeScript project and initializing Storybook:

```bash
npm create vite@latest storybook-mcp-demo -- --template react-ts
cd storybook-mcp-demo
npm install
npx storybook@latest init
```

During `init`, Storybook 10.4 asks whether you want to enable AI features. Choosing Yes installs and registers `@storybook/addon-mcp` automatically, along with the Vitest and accessibility addons. If you skip the prompt or you’re adding it to an existing project, you can install and register it manually by running `npx storybook add @storybook/addon-mcp`.

Once Storybook is running, the MCP server is available at `http://localhost:6006/mcp`. Opening that URL in your browser displays the available tools along with a link to the manifest debugger. In the terminal, you’ll also see confirmation that the documentation toolset is active with the message: `Experimental components manifest feature detected — registering component tools.`

![Storybook sidebar showing Badge, Button, TextInput under COMPONENTS](https://paper-attachments.dropboxusercontent.com/s_5854C4FD8652B0CE659BBC59B11E67A79A9BC6F73B2C5145B90D9DA442DCE3A1_1779591485466_telegram-cloud-photo-size-4-5805572221483814653-y.jpg)

With the MCP server running, the next step is to connect your AI agent to it. If you’re using Claude Code, run:

```bash
npx mcp-add --type http --url "http://localhost:6006/mcp" --scope project
```

`mcp-add` is a small CLI utility that writes the MCP server configuration to your project. With `--scope project,` it creates a `.mcp.json` file in the project root, scoping the server to this project only. You will be prompted to name the server; use something specific like `storybook-mcp-demo,` since the name is what your agent references when calling the tools.

The last piece is an `AGENTS.md` file at the project root. This is the instruction file Claude Code reads before acting on any prompt. Without it, the agent has no guidance to use the MCP tools, even though they are available.

Create `.claude/AGENTS.md` with the following:

```markdown
When working on UI components, always use the \`storybook-mcp-demo\` MCP tools 
to access Storybook's component and documentation knowledge before answering 
or taking any action.

- CRITICAL: Never hallucinate component properties. Before using any property 
  on a component, use the MCP tools to check if it is documented for that component.
- Run \`list-all-documentation\` to get a list of all components.
- Run \`get-documentation\` for a specific component to see its props and examples.
- Only use properties that are explicitly documented or shown in example stories.
- Use \`get-storybook-story-instructions\` before creating or modifying any story file.
- Check your work by running \`run-story-tests\` after generating components or stories.
```

To verify Claude Code can reach the server, make sure Storybook is running, then open Claude Code and send the prompt “List all documented components using the storybook-mcp-demo MCP.” You should see a call to `list-all-documentation` return the component index.

![Claude Code listing the components index](https://paper-attachments.dropboxusercontent.com/s_5854C4FD8652B0CE659BBC59B11E67A79A9BC6F73B2C5145B90D9DA442DCE3A1_1779592968736_telegram-cloud-photo-size-4-5805572221483814654-y.jpg)

## What the server exposes

The [MCP](https://blog.logrocket.com/mcp-is-replacing-the-browser/) server provides six tools across three toolsets. The docs toolset (`list-all-documentation`, `get-documentation`, `get-documentation-for-story`) handles component discovery and prop lookup. The dev toolset (`get-storybook-story-instructions`, `preview-stories`) handles story authoring and live previews. The testing toolset (`run-story-tests`) executes component and accessibility tests against stories and returns structured results.

### Docs toolset

`list-all-documentation` returns a flat index of every component registered in your Storybook with its ID. The agent uses those IDs to call `get-documentation`, which returns the first three stories as rendered code snippets, the full TypeScript prop contract, and an index of remaining variants. When those three stories aren’t enough, `get-documentation-for-story` fetches a specific variant in isolation.

Here is the actual `get-documentation` response for our Button component:

```markdown
# Button  ID: components-button

## Stories

### Primary  Story ID: components-button--primary
const Primary = () => <Button label="Button" variant="primary" size="md" />;

### Other Stories
- Disabled (components-button--disabled)
- Small (components-button--small)  
- Large (components-button--large)

## Props
label: string;
variant?: 'primary' | 'secondary' | 'destructive' = 'primary';
size?: 'sm' | 'md' | 'lg' = 'md';
disabled?: boolean = false;
onClick?: () => void;
```

The agent sees the exact type of contract and real usage examples before writing any code, hence preventing prop hallucination.

### Dev and testing toolsets

`get-storybook-story-instructions` returns a detailed instruction document covering correct import paths, play function patterns, mocking strategies, and a hard rule to `run-story-tests` after every change. `preview-stories` returns live story URLs, and in agents that support MCP Apps, the rendered component embeds directly in the chat. `run-story-tests` runs the vitest-powered test runner against specific story IDs, and returns pass/fail status plus structured accessibility violation reports.

---

![](https://blog.logrocket.com/wp-content/uploads/2023/07/Screen-Shot-2023-07-06-at-7.43.53-AM.png)

## [Over 200k developers use LogRocket to create better digital experiences](https://lp.logrocket.com/blg/learn-more)

---

The docs toolset is backed by component manifests, a structured JSON generated from your stories and component metadata at build time. This is currently React-only, which is why the docs toolset is limited to React projects while dev and testing toolsets work across frameworks.

![Browser view of http://localhost:6006/mcp showing the tool list page](https://paper-attachments.dropboxusercontent.com/s_5854C4FD8652B0CE659BBC59B11E67A79A9BC6F73B2C5145B90D9DA442DCE3A1_1779593878518_telegram-cloud-photo-size-4-5805572221483814658-y.jpg)

## Agent behavior before and after

The most direct way to see what the MCP server changes is to give an agent the same prompt twice. Once without a component context, and another with it connected.

### Without MCP

With no `AGENTS.md` and no MCP tools available, Claude Code read the project file tree, noted that Button and TextInput components existed, and immediately wrote a fully self-contained component anyway. The output was 263 lines of inline `<input>` and `<button>` elements with their own validation logic and bespoke Tailwind classes, none of which match the prop contracts or visual patterns of the design system components sitting in `src/components`.

```tsx
// LoginFormBasic.tsx — built without MCP
<input
  id="email"
  type="email"
  className="w-full rounded-lg border px-3.5 py-2.5 text-sm ..."
  aria-invalid={!!errors.email}
/>
<button
  type="submit"
  className="mt-2 w-full rounded-lg bg-blue-600 px-4 py-2.5 ..."
>
  Sign in
</button>
```

The agent made zero tool calls. It had no structured way to query what components exist, what props they accept, or what variants they support, so it built everything from scratch.

![Claude Code terminal showing output with zero MCP and fully self-contained component note](https://paper-attachments.dropboxusercontent.com/s_5854C4FD8652B0CE659BBC59B11E67A79A9BC6F73B2C5145B90D9DA442DCE3A1_1779595916594_telegram-cloud-photo-size-4-5805572221483814669-y.jpg)

### With MCP

With `AGENTS.md` restored and Storybook running, the same prompt produced a completely different sequence. Before writing any code, [Claude Code](https://blog.logrocket.com/getting-started-claude-4-api-developers-walkthrough/) made six MCP tool calls:

1. **`get-storybook-story-instructions`** — fetched story writing conventions and the requirement to run tests after every change
2. **`list-all-documentation`** — retrieved the full component index and identified Button and TextInput as candidates
3. **`get-documentation` for `components-button`** — fetched prop types and the first three story examples
4. **`get-documentation` for `components-textinput`** — fetched prop types and usage examples
5. Read the existing `LoginFormBasic.tsx` and a Button story file for structural reference
6. Confirmed `@storybook/react-vite` as the installed framework package

Only after those six calls did it write the component with 188 lines that import and compose the actual design system components:

```tsx
// LoginFormMCP.tsx — built with MCP
import { Button } from '../components/Button/Button';
import { TextInput } from '../components/TextInput/TextInput';

<TextInput
  label="Email address"
  type="email"
  placeholder="you@example.com"
  value={values.email}
  onChange={handleChange('email')}
  error={errors.email}
  disabled={isSubmitting}
/>
<Button
  label={isSubmitting ? 'Signing in…' : 'Sign in'}
  variant="primary"
  size="lg"
  disabled={isSubmitting}
  onClick={performSubmit}
/>
```

Every prop (`variant`, `size`, `error`, `onChange`) matches the documented contract exactly because the agent read it from `get-documentation` before writing. The agent also caught mid-generation that `Button` renders with `type="button"` and would not natively trigger the form’s `onSubmit`, so it split submit logic into a `performSubmit` function wired to both the button’s `onClick` and the form’s `onSubmit` handler.

![Claude Code terminal showing tool call sequence before any code is written](https://paper-attachments.dropboxusercontent.com/s_5854C4FD8652B0CE659BBC59B11E67A79A9BC6F73B2C5145B90D9DA442DCE3A1_1779595740122_telegram-cloud-photo-size-4-5805572221483814662-y.jpg)

After writing the component, the agent immediately generated a story file with five interaction tests covering the default state, validation errors, invalid email format, short password, and successful submission. It then calls `preview-stories` and `run-story-tests` in parallel, which is where the self-healing loop begins.

## The self-healing test loop

The first `run-story-tests` call returned 3 failed, 2 passed across the five stories. The agent read the failure output and identified the cause. `getByLabelText('Email address')` was failing because the `TextInput` component did not link its `<label>` to its `<input>` via `htmlFor` and `id`. This is both a test failure and an accessibility violation.

---

### More great articles from LogRocket:

- Don't miss a moment with [The Replay](https://lp.logrocket.com/subscribe-thereplay), a curated newsletter from LogRocket
- [Learn](https://blog.logrocket.com/rethinking-error-tracking-product-analytics/) how LogRocket's Galileo AI watches sessions for you and proactively surfaces the highest-impact things you should work on
- Use React's useEffect [to optimize your application's performance](https://blog.logrocket.com/understanding-react-useeffect-cleanup-function/)
- Switch between [multiple versions of Node](https://blog.logrocket.com/switching-between-node-versions-during-development/)
- [Discover](https://blog.logrocket.com/using-react-children-prop-with-typescript/) how to use the React children prop with TypeScript
- [Explore](https://blog.logrocket.com/creating-custom-mouse-cursor-css/) creating a custom mouse cursor with CSS
- Advisory boards aren’t just for executives. [Join LogRocket’s Content Advisory Board.](https://lp.logrocket.com/blg/content-advisory-board-signup) You’ll help inform the type of content we create and get access to exclusive meetups, social accreditation, and swag

---

The agent classified this as a semantic fix with no visual change and applied it automatically without prompting the developer. It updated `TextInput.tsx` to derive an `inputId` from the label text when no explicit `id` prop is provided, wired `htmlFor={inputId}` to the label, added `id={inputId}` to the input element, and added `aria-invalid` and `aria-describedby` attributes for screen reader support.

```tsx
// TextInput.tsx — after agent's autonomous a11y fix
const inputId = id ?? label.toLowerCase().replace(/\s+/g, '-');
const errorId = error ? \`${inputId}-error\` : undefined;

<label htmlFor={inputId} className="text-sm font-medium text-gray-700">
  {label}
</label>
<input
  id={inputId}
  aria-invalid={error ? true : undefined}
  aria-describedby={errorId}
  ...
/>
{error && (
  <span id={errorId} role="alert" className="text-xs text-red-600">
    {error}
  </span>
)}
```

With that fix applied, the agent called `run-story-tests` again. All 5 stories passed.

![Terminal showing first test run and second test run after the a11y fix](https://paper-attachments.dropboxusercontent.com/s_5854C4FD8652B0CE659BBC59B11E67A79A9BC6F73B2C5145B90D9DA442DCE3A1_1779596234066_storybook-server.webp)

The fix the agent made was not to the login form, but to the shared `TextInput` component in the design system. Every other story that uses `TextInput` now also benefits from the corrected accessibility semantics. That is the concrete value of the test loop, as the agent’s scope of correction is not limited to what it just wrote.

![Claude Code summary showing LoginFormMCP done](https://paper-attachments.dropboxusercontent.com/s_5854C4FD8652B0CE659BBC59B11E67A79A9BC6F73B2C5145B90D9DA442DCE3A1_1779596485349_telegram-cloud-photo-size-4-5805572221483814667-y.jpg)

## Conclusion

The Storybook MCP server closes the gap between what an agent can generate and what your codebase already has. With a running Storybook instance and three setup steps, an agent gains a structured, queryable view of your component library and the tools to verify its own output before you ever see it. That is a meaningfully different starting point for [AI-assisted UI](https://blog.logrocket.com/designcoder-ai-ui/) development than a prompt and a blank file. Find the source files for this article set up on [GitHub](https://github.com/Ikeh-Akinyemi/vigilant-fishstick).

[View all posts](https://blog.logrocket.com/)

Hey there, want to help make our blog better?

Join LogRocket’s Content Advisory Board. You’ll help inform the type of content we create and get access to exclusive meetups, social accreditation, and swag.

[Sign up now](https://lp.logrocket.com/blg/content-advisory-board-signup)