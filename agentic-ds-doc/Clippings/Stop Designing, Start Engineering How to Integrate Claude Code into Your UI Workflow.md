---
title: "Stop Designing, Start Engineering: How to Integrate Claude Code into Your UI Workflow"
source: "https://medium.com/design-bootcamp/stop-designing-start-engineering-how-to-integrate-claude-code-into-your-ui-workflow-16144ec3f3b2"
author:
  - "[[Akio]]"
published: 2026-07-05
created: 2026-07-08
description: "Why moving from Figma to the terminal is the scariest but most necessary leap for modern product designers."
tags:
  - "clippings"
---
## Why moving from Figma to the terminal is the scariest but most necessary leap for modern product designers.

A few years ago I watched a senior designer on my team spend three weeks building a complex video editing interface in Figma. She built dozens of frames. She mapped out every icon, every hover state, and every transition. She used a sophisticated prototyping plugin to make the timeline scrubber actually move when you dragged it. It was a masterpiece of the craft. She presented it to the engineering team with quiet pride.

The lead engineer looked at it for a few minutes, sighed, and asked a single question. “How do we render three hundred video clips on a canvas without freezing the browser?”

The designer did not have an answer. She had designed the interface assuming the browser could handle an infinite number of DOM elements. The engineer explained that to make this performant, they would need to use a canvas element and manage the rendering manually in JavaScript. The carefully designed hover states and CSS transitions she spent weeks on were impossible. The entire prototype had to be thrown away. The team had to start over, this time with the engineer driving the design decisions based on technical constraints.

That moment captures the fundamental flaw in how we build digital products. Designers draw pictures of software. Engineers build software. The gap between the picture and the software is where projects go to die. We have spent two decades building tools to bridge this gap. We built Zeplin. We built Storybook. We built complex design systems in Figma hoping that if we just structured our pictures correctly, the translation would be flawless.

It never is. The translation is never flawless because a picture is fundamentally different from a system. A picture is static. A system is dynamic. A picture hides complexity. A system must manage complexity.

The arrival of agentic artificial intelligence tools like Claude Code is forcing a reckoning with this dynamic. Claude Code is not a snippet generator. It is an autonomous agent that lives in your terminal, reads your codebase, writes files, runs tests, and iterates on logic. It does not care about your Figma files. It cares about the reality of the code.

The title of this article says stop designing, start engineering. That is a provocative statement. I do not mean we should stop caring about the user experience. I mean the activity of designing as a separate, upstream discipline that produces static artifacts is no longer the most effective way to build software. The most effective way to build software is to integrate the design intent directly into the engineering process. And the only way to do that is for designers to step into the engineering workflow.

This is the story of how I integrated Claude Code into my UI workflow, the terror and liberation of leaving the canvas behind, and the practical lessons learned along the way.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*k3sTumoUDCcp8zKH21JUPA.jpeg)

Image by: Nano Banana 2

## The Figma Trap and the Illusion of Fidelity

To understand why moving to the terminal is necessary, we have to understand the trap we are in. Figma is a brilliant tool. It democratized design and made collaboration seamless. But it also created an illusion. It made us believe that high fidelity visual mockups equate to high fidelity software design.

When you design a dashboard in Figma, you are drawing a picture of a dashboard in its perfect, idealized state. The data fits perfectly in the table. The charts have exactly the right number of data points. The user is on a fast network. The API responded instantly. There are no errors.

This illusion is dangerous because it hides the actual work of building software. The actual work is not drawing the table. The actual work is deciding what happens when the table has ten thousand rows. The actual work is deciding what happens when the API times out. The actual work is managing the state of the selected rows when the user navigates to a detail page and comes back.

Figma cannot manage this state effectively. You can create variants for loading states and error states, but they are disconnected islands. There is no logic tying them together. You cannot feel the friction of navigating between them.

Designers who live entirely in Figma develop a blind spot for systemic logic. They think in screens, not in flows. They think in components, not in state machines. When they hand off their work to engineers, the engineers have to infer the logic. They have to guess what happens on the edge cases. Usually, they guess wrong, or they make pragmatic decisions that violate the designer intent because the designer was not there to consult.

The Figma trap is the belief that if you just draw enough frames, you can anticipate every possible state. You cannot. The combinatorial explosion of user actions, data states, and network conditions makes it impossible to draw every state. You have to define the rules, and let the machine render the states. That is what code does. That is what Figma cannot do.

## Enter Claude Code: The Terminal as the New Canvas

When I first heard about Claude Code, I was skeptical. I had used copilot style tools that auto completed lines of code in my editor. They were helpful for writing boilerplate, but they did not change the workflow. I still had to write the code. I still had to know the syntax.

Claude Code is different. It is a command line tool. You run it in your project directory. It has access to your files. You give it a task in natural language, and it goes to work. It reads your existing components to understand your patterns. It writes new files. It runs your test suite. If a test fails, it reads the error message and fixes its own code. It is an autonomous junior engineer living in your terminal.

The first time I used it to build a UI component, I felt a mix of terror and liberation. I typed a prompt describing a settings panel with a list of toggles and a save button. I told it to use our existing design system components. I hit enter.

The terminal started scrolling with text. Claude was searching the codebase. It found our button component. It found our toggle component. It created a new file called SettingsPanel.tsx. It wrote the React code. It imported the correct dependencies. It ran the linter. It found a typing error and fixed it. It asked me if I wanted to run the dev server to see it.

I opened my browser. There was the settings panel. It was not a picture. It was real, functioning code. It used our actual components. When I clicked a toggle, the state changed. When I clicked save, it fired a mock function.

I realized in that moment that the Figma file was obsolete for this task. I had skipped the drawing phase entirely. I had gone directly from intent to execution. The terminal was my new canvas.

This is a profound shift for a designer. The terminal is a hostile environment for visual thinkers. It is black and white. It is text heavy. It does not give you the immediate visual feedback of a canvas. But it gives you something more important. It gives you reality.

When the component renders in the browser, it is the truth. There is no ambiguity about how it will be built. It is built. The gap between design and engineering collapses to zero.

## The Mindset Shift: From Pixels to States

Using Claude Code effectively requires a fundamental mindset shift. You have to stop thinking in pixels and start thinking in states.

In Figma, if you want to design a form submission flow, you draw the empty form, the form with validation errors, the loading state, and the success state. You draw four frames. You hope the engineer connects them correctly.

In Claude Code, you do not draw anything. You define the logic. You write a prompt that says: “Create a form component with name and email fields. Validate that the email is correctly formatted on blur. If validation fails, show an error message in red below the field. On submit, set a loading state that disables the button and shows a spinner. If the submission succeeds, show a success toast and reset the form.”

This prompt describes a state machine. It defines the initial state, the transition triggers, the error states, and the success state. Claude Code writes the React logic to implement this state machine. It handles the conditional rendering. It manages the asynchronous submission.

The craft is no longer in the visual layout. The craft is in the rigor of the logic. If you forget to specify the loading state in your prompt, Claude Code might not include it. If you forget to specify what happens on success, the form might just sit there after submitting. The quality of the output is directly proportional to the completeness of your systemic thinking.

This forces designers to confront the edge cases they usually ignore. When you are drawing in Figma, it is easy to skip the error state because it is ugly and breaks the flow. When you are engineering in Claude Code, you cannot skip the error state because the code will not function without it. The tool forces you to be a complete thinker.

I noticed this shift in my own work. I stopped opening Figma to explore layouts. I started opening Claude Code to explore logic. I would build a rough version of a feature, play with it in the browser, and then iterate on the behavior. The visual layout became a secondary concern, handled largely by our existing design system. The primary concern became the interaction logic.

This is how it should be. The visual layout is a solved problem for most applications. We have design systems. We have established patterns. The differentiator in modern software is not the visual layout. It is the interaction logic. It is how the system responds to the user. Claude Code lets designers work directly in the differentiator.

## The Workflow Integration: A Step by Step Guide

Integrating Claude Code into a UI workflow is not as simple as typing prompts into a terminal. It requires a disciplined process to ensure the output is maintainable and aligns with the broader product strategy. Here is the workflow I developed over months of trial and error.

i. Context Seeding

Before Claude Code can build anything, it needs to understand your environment. If you just ask it to build a button, it will write a button from scratch. It will ignore your design system. The first step is context seeding.

I start every session by pointing Claude at the relevant files. I tell it to read our design system directory. I tell it to read our tailwind config. I tell it to read an example component that follows our best practices. I ask it to summarize the patterns it sees. This ensures the model internalizes our naming conventions, our state management approach, and our styling logic before it writes a single line of new code.

ii. State Driven Prompting

Once the context is seeded, I write the prompt. But I do not write visual prompts. I write state driven prompts. I use a specific structure.

First, I define the component name and its purpose. Second, I list the props it accepts. Third, I describe the local state it needs to manage. Fourth, I list the user actions and the state transitions for each action. Fifth, I describe the layout using semantic terms, not pixel values. For example, I say “use a two column grid with the navigation on the left and the main content on the right” instead of “put a 200px sidebar on the left.”

This structure forces me to think through the entire lifecycle of the component before Claude starts writing. It prevents the common failure mode where the AI generates a beautiful UI that falls apart the first time a user interacts with it.

iii. The Local Verification Loop

Claude Code will write the code and often offer to run the dev server. I always accept. I need to see the component in the browser immediately.

This is where the real design work happens. I interact with the component. I try to break it. I enter invalid data. I click buttons rapidly. I check the mobile responsiveness using the browser dev tools.

I do not go back to Figma to note the issues. I go back to Claude Code. I tell it exactly what went wrong. “The error state does not clear when the user starts typing.” “The mobile layout stacks the columns but the spacing is too tight.” Claude reads the feedback, looks at the code it just wrote, and applies a fix.

This loop is incredibly fast. It takes seconds. The feedback is precise because it is based on real behavior, not a visual approximation. This local verification loop is the core of the new workflow. It replaces the design review meeting.

iv. The Boundary of Logic

A designer using Claude Code needs to know where their authority ends. It is tempting to use the tool to build everything, including the backend logic. But this leads to disaster.

The designer should use Claude Code to build the UI layer and the local state management. They should build the components, the hooks for data fetching, and the interaction logic. They should not use it to write database schemas, API endpoints, or complex business logic.

The boundary is the API contract. The designer builds the UI to consume an API. They can mock the API data using tools like MSW to test the UI. But the actual implementation of the API is the engineer domain.

I enforce this boundary by telling Claude exactly what data shape to expect. “Assume the API returns an array of user objects with id, name, and role properties. Do not implement the API route. Mock the fetch call.” This keeps the design work focused on the presentation layer and prevents the designer from accidentally creating technical debt in the backend.

v. The Pull Request as the Deliverable

When the component is finished, verified, and behaving correctly in the browser, the work is not handed off via a Figma link. The work is handed off via a pull request.

Claude Code can write the commit message and create the branch. The designer opens the PR. The engineer reviews the actual code. This is a massive upgrade in communication. The engineer does not have to interpret a picture. They just review code. They can run it locally. They can check the logic. They can suggest changes directly in the code.

This changes the dynamic between design and engineering. The designer is no longer a requirement generator. They are a code contributor. The engineer treats them with a different level of respect because they are speaking the same language. The handoff friction is almost entirely eliminated.

## A Case Study in the Trenches: Building a Complex Data Table

Let me share a specific example of how this workflow plays out in reality. We needed to build a complex data table for an admin dashboard. The table needed to support sorting, filtering, pagination, and inline editing. It also needed to handle optimistic updates and error rollback.

In the old workflow, I would have spent three days in Figma drawing the table in its various states. I would have drawn the empty state, the loading skeleton, the sorted state, the filtered state, and the inline editing state. I would have annotated the interactions with arrows and text. Then I would have handed it to an engineer who would have spent a week building it, and we would have gone back and forth on edge cases.

With Claude Code, the process was entirely different.

I started by seeding the context. I pointed Claude at our existing table component and our design system tokens. I asked it to read the code and understand how we currently handled styling and state.

Then I wrote the state driven prompt. I described a DataTable component that accepts a columns configuration and a data fetching function. I specified that it needed to manage local state for the current page, the sort key, and the sort direction. I described the inline editing behavior: when a user clicks an editable cell, it turns into an input. When they hit enter, it fires an onUpdate function. While the update is pending, the cell shows a loading spinner. If the update fails, the cell reverts to the original value and shows an error toast.

This was a long, detailed prompt. It took me twenty minutes to write. But it forced me to think through every edge case before any code was written.

Claude went to work. It created the component. It wrote the sorting logic. It wrote the pagination logic. It ran the linter. It took about two minutes.

I opened the browser. The table was there. It looked like our design system. I started testing. Sorting worked. Pagination worked.

Then I tested the inline editing. I clicked a cell, changed the value, and hit enter. The spinner appeared. The mock API resolved, and the cell updated. Success.

But I noticed an edge case. If I clicked a cell, started typing, and then hit the escape key, the cell stayed in edit mode. I had not specified the escape behavior in my prompt.

I went back to Claude. “Update the DataTable component. When a user is editing a cell and presses the Escape key, cancel the edit and revert the cell to its original value. Remove focus from the input.”

Claude read the existing code, found the keydown handler, and added the escape logic. It took ten seconds.

I tested the optimistic update rollback. I intentionally made the mock API fail. The cell showed the spinner, then reverted to the original value, and the error toast appeared. It worked flawlessly. Claude had inferred the rollback logic from my initial description.

The entire process, from prompt to verified working component, took forty five minutes. I did not open Figma once. The engineer reviewed the PR in ten minutes, merged it, and wired up the real API. We shipped the feature two days ahead of schedule.

The practical lesson here is not that Claude Code is fast. It is that the state driven workflow produces better outcomes. Because I was forced to define the state machine explicitly, the resulting code was robust. It handled edge cases that would normally have been discovered during QA or, worse, in production. The tool forced me to be a systems thinker.

## Navigating the Cultural Shock and Developer Relations

Introducing this workflow into an existing team is politically complex. Engineers are naturally skeptical of designers writing code. They have seen designers try to code before and make a mess. They fear they will have to clean up poorly architected spaghetti code.

The key to overcoming this skepticism is discipline. As a designer using Claude Code, you must respect the architectural boundaries of the engineering team. You must not refactor core logic. You must not introduce new dependencies without asking. You must use the tools and patterns the engineers have established.

Claude Code makes this easier because it can read the codebase. If you tell it to follow existing patterns, it usually will. But you have to verify this. Before I open a PR, I read every line of code Claude generated. If I do not understand a line of code, I ask Claude to explain it. If the code looks hacky or overengineered, I ask Claude to simplify it or align it with the existing patterns.

I also make it clear to the engineers that my PRs are suggestions, not mandates. I tell them, “I built this UI component using our design system. The logic is mocked. Please review the structure and let me know if I need to adjust anything to fit your architecture.”

The engineers initially reviewed my PRs with intense scrutiny. They found minor issues. I fixed them using Claude Code. Over time, they realized the PRs were high quality. They started trusting the workflow. Eventually, they started asking me to build UI components for them because it was faster than doing it themselves.

This cultural shift is significant. The boundary between design and engineering softens. The designer becomes a specialized frontend contributor. The engineer focuses on the backend and the complex business logic. The handoff friction disappears.

But this requires the designer to level up their technical understanding. You cannot use Claude Code effectively if you do not understand basic React concepts, if you do not understand state management, and if you do not understand the command line. The tool abstracts away the syntax, but it does not abstract away the concepts. You have to know what you are asking the machine to do.

## Mentoring the Next Generation in a Code First World

This shift has massive implications for design education and mentorship. For the last decade, design bootcamps and university programs have focused heavily on Figma, visual design, and prototyping. They taught designers how to draw pictures.

That skill set is no longer sufficient. The junior designers entering the workforce today need to be systems thinkers. They need to understand code concepts. They need to be comfortable in the terminal.

When I mentor junior designers now, I tell them to close Figma for the first month. I tell them to use Claude Code to build UIs from scratch. I make them learn how to read a React component. I make them understand how state works. I make them deal with the browser dev tools.

They struggle initially. The terminal is intimidating. The error messages are frustrating. But within a few weeks, they have a profound realization. They realize that by understanding the code, they have complete control over the experience. They do not have to beg an engineer to change a padding value. They do not have to wait for a handoff meeting to see if their design works. They just change the code and see the result.

This empowerment changes the designer psychology. They stop viewing engineering as an obstacle. They start viewing engineering as a medium.

The new design education should focus on three things.

First, systems thinking. How to map a user journey into a state machine. How to identify edge cases. How to define rules rather than drawing frames.

Second, technical literacy. Understanding the Document Object Model. Understanding component lifecycle. Understanding data binding. Understanding asynchronous operations. Designers do not need to write code from scratch, but they need to read it and understand it.

Third, prompt engineering for code. How to write precise, state driven prompts that produce robust logic. How to context seed an AI agent. How to iterate on AI output using natural language.

Designers who graduate with these skills will be ten times more valuable than designers who only know how to use Figma. They will be able to operate at the speed of thought, unencumbered by the translation layer between design and code.

## The Limits of the Machine and the Human Anchor

Claude Code is an incredibly powerful tool, but it is not infallible. It makes mistakes. It hallucinates APIs that do not exist. It sometimes writes code that works locally but fails in a production build. It can get stuck in loops, trying to fix an error and making it worse.

The designer using the tool must be the human anchor. They must provide the oversight the machine lacks. This means you cannot blindly accept the output. You have to verify everything.

I have a rule: I never merge code I do not understand. If Claude generates a complex regex pattern to validate an email, I do not just accept it because it works. I ask Claude to explain the regex to me. If I still do not understand it, I ask Claude to simplify it or use a library. I am responsible for the code that ships under my name. The AI is a tool, not a scapegoat.

This is particularly important when it comes to accessibility. Claude Code is good at basic accessibility, like adding alt tags and aria labels. But it does not understand the nuances of screen reader navigation. It might build a custom dropdown that looks great but is completely unusable with a keyboard.

The designer must be the accessibility champion. They must test the AI generated code with keyboard navigation. They must test it with a screen reader. If it fails, they must prompt the AI to fix it. “This custom dropdown is not accessible. Rewrite it using the Radix UI dropdown primitive so it handles keyboard focus and aria attributes correctly.”

The human anchor is also responsible for the user experience nuances the machine cannot feel. The AI does not know if a loading spinner feels too aggressive. The AI does not know if an error message sounds too accusatory. The designer has to feel the experience and direct the AI to adjust the tone and the timing.

The limit of the machine is that it optimizes for functional correctness. The limit of the human is that they cannot process millions of lines of code instantly. The magic happens when the human provides the taste and the context, and the machine provides the execution.

## The End of the Handoff Document

The ultimate consequence of integrating Claude Code into the UI workflow is the death of the handoff document. The redline tool, the Figma annotation, the Zeplin spec, these are all artifacts of a broken process. They exist because the designer and the engineer lived in different worlds and needed a translator.

When the designer works in the codebase, the handoff document is obsolete. The code is the document. The component is the source of truth. If the engineer needs to know how a state transition works, they read the code. If they need to see the visual design, they run the dev server.

This eliminates the massive amount of waste associated with handoffs. The spec writing, the review meetings, the misinterpretations, the rework. All of it disappears. The energy previously spent on translation is redirected to actual problem solving.

I have stopped writing design specs entirely. When I build a feature, I write a brief that outlines the user problem and the business goal. Then I build the feature using Claude Code. I record a short Loom video showing the feature working in the browser and explaining the key logic decisions. I attach the Loom video to the pull request. That is the entire handoff.

The engineers love this. They would rather watch a two minute video of working software than read a five page Figma annotation document. And they would rather review code than interpret a picture.

## Redefining Craft in the Age of Agentic AI

Every time a new abstraction layer is introduced to design, there is a mourning period for the old craft. When we moved from Photoshop to Sketch, people mourned the pixel level control. When we moved from Sketch to Figma, people mourned the local file management. Now, as we move from Figma to code generation, people are mourning the visual layout craft.

But craft is not about the tool. Craft is about the care and rigor applied to the work. The craft of the future is not aligning pixels. The craft of the future is writing precise, comprehensive state machines. It is prompting an AI agent to build a system that is robust, accessible, and elegant. It is reading generated code and spotting the logical flaws. It is iterating on behavior in real time.

This is a higher level of craft. It requires more cognitive load. It requires a deeper understanding of the medium. But it produces better products.

The designers who cling to the canvas will find themselves increasingly marginalized. They will be the people drawing pictures of software while the rest of the team is building it. Their work will be treated as suggestive, not definitive.

The designers who embrace the terminal will become the architects of the product. They will define the logic, the behavior, and the experience in the medium where it actually lives. They will work at the speed of engineering, unencumbered by translation layers.

Stop designing. Start engineering. The terminal is waiting. The agent is ready. The only thing standing in the way is the comfort of the old canvas and the fear of learning a new medium. Overcoming that fear is the only way to stay relevant in the next era of software development.

The people who succeed will not be the ones who simply learn every new tool. They will be the ones who understand when and why to use them, and how to anchor the raw power of agentic AI in deep, human centered systemic thinking.