---
title: "How to Automate Design System Documentation"
source: "https://learn.thedesignsystem.guide/p/how-to-automate-design-system-documentation"
author:
  - "[[Romina Kavcic]]"
published: 2025-10-17
created: 2026-06-15
description: "From Figma to Mintlify"
tags:
  - "clippings"
---
👋 Get weekly insights, tools, and templates to help you build and scale design systems. More: [Design Tokens Mastery Course](https://thedesignsystem.guide/design-tokens-course) / [YouTube](https://www.youtube.com/@designsystemguide) / [My Linkedin](https://www.linkedin.com/in/rominakavcic/)

---

![](https://substackcdn.com/image/fetch/$s_!9dDC!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe9c6aa2-4c25-47ea-8c50-3c5d2d786ca1_1456x970.png)

**Your design system has a 3-week lag problem.**

Designer updates the button in Figma. The developer implements it. Someone remembers to update the docs in a week or two … (maybe).

And then:

- People waste hours hunting for the correct specs
- “Is this the latest version?” at least 12 times per sprint
- Implementation errors happen because of the outdated docs
- 30% of components are still using old tokens 6 months after migration

Another problem is that teams maintain multiple sources of truth. Some rely on Figma, some on **Storybook**, others have **Storybook + custom design system documentation**, or **3rd-party design system platforms** (where you are locked in).

But the storyline is always the same. Nobody has time to write the docs, update screenshots, and add guidelines and educational material.

Most teams try to solve this by improving their processes. Involve more people and rules. Have stricter update cadences. Automated reminders. Ohhh, **that’s optimizing the wrong thing.**

The only way to kill latency is to **connect your tools** so they document themselves.

This guide shows you how to do exactly that. 👇

---

## What we’re building

We’re connecting three systems: **Figma** (via API and MCP), **an AI tool** (choose your favourite one), and **Mintlify** for documentation.

**What is MCP?** Model Context Protocol (MCP) is a standard that lets AI tools like Claude Code directly read data from other applications. Instead of you manually copying specs from Figma, MCP lets Claude read them directly. Think of it as giving Claude read-only access to your design files.

![](https://substackcdn.com/image/fetch/$s_!Wokt!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b10e465-5877-4b10-857c-906b88bc2d91_2880x1620.png)

AI reads the current state of Figma in real-time AND your existing docs from the codebase. When you push updates, **Mintlify** (your documentation hosting platform) automatically rebuilds and deploys your docs site. No manual screenshot exports, no copy-paste specs, no documentation lag.

## How it works

![](https://substackcdn.com/image/fetch/$s_!Wz8c!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffee35775-4163-4f34-9d00-5182fa6c2d54_2880x1620.png)

What flows through the system:

**FROM FIGMA (via Personal Access Token + MCP):**

• Current component specifications (spacing, colors, typography)

• Exact token names from Figma Variables

• Component variants and interactive states

• High-res screenshots (2x PNG exports)

• Frame last modified timestamps

**FROM YOUR CODEBASE:**

• Existing documentation markdown files (.mdx)

• Usage guidelines and behavioral patterns

• Accessibility requirements you’ve written

• Code examples and edge cases

• Frame ID tracking comments: <!-- figma-frame:... -->

**TO MINTLIFY DOCS (via Git push):**

• Auto-updated screenshots from Figma frames

• Synced specifications (padding, colors, tokens)

• Generated components matching YOUR code patterns

• Updated tests based on documented behaviors

• Pull requests with before/after visual diffs

When we want to update documentation, we have two options. **On-demand** with copy-pasting our *Figma link* OR **automatically** (for example, every week on Monday).

![](https://substackcdn.com/image/fetch/$s_!BKBQ!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F75003f59-1875-488e-a2f1-342b2e65fe44_2880x1620.png)

**Flow 1: On-demand sync → designers share a Figma link in the AI tool**

```markup
Designer → Copies Figma frame URL
         ↓
Pastes in AI tool: “Update button docs from this frame”
         ↓
Claude Code → Reads Figma frame via Personal Access Token
            → Exports screenshot from Figma
            → Reads existing docs from codebase
            → Updates .mdx files with new screenshot + specs
         ↓
Git → Creates PR with visual diff 
         ↓
Mintlify → Auto-deploys updated docs when PR merges
```

🕐 Time: 30 seconds vs 30 minutes of manual work

**What gets updated:**

- Component screenshot (auto-exported from Figma frame)
- Visual specifications (spacing, colors, typography)
- Token references (reads Figma Variables)
- Component variants and states

**Flow 2: Automated Weekly Sync (GitHub Action)**

In your Mintlify docs, you track frame IDs. The comment `<!-- figma-frame: your-file-name/45-890 -->` tells the automation which Figma frame to check.

To make this work, you will need to create a **GitHub Action** that checks for tracked frames weekly. This would happen via the Figma API.

🕐 Time: Fully automated, zero manual work

---

Now let’s go through the setup. ✨

### Step 1: Set up a Mintlify account & GitHub repository

![](https://substackcdn.com/image/fetch/$s_!Yiog!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d786a14-0281-43ee-8ed3-22859b456fbb_1759x467.png)

**What is Mintlify?**

Mintlify (mintlify.com) is a documentation hosting platform that turns your markdown files into beautiful, searchable doc websites. Think of it as Vercel, but specifically for documentation. You write docs in `.mdx` files in your Git repo, push changes, and Mintlify automatically rebuilds and deploys your docs site in 2-3 minutes. It’s where you document how components behave, when to use them, and why.

**1\. First, create a Mintlify account**

Go to [mintlify.com](https://mintlify.com/) and click “Sign Up”. Choose “Sign up with GitHub”. This is the easiest method since Mintlify needs access to your docs repository anyway.

**2\. Authorize GitHub access**

Mintlify will ask for permission to:

- Read your repositories
- Write to repositories (for automatic deployments)
- Access webhooks (to trigger rebuilds on push)

Click “Authorize Mintlify”.

**3\. Create or connect your docs repository**

Option A: **Start from scratch and create a new GitHub repository**

- Click “Create new documentation”
- Choose “Start from template”
- Mintlify creates a new GitHub repo with starter docs
- Name it something like `design-system-docs`

Option B: **Use existing docs repo**

- Click “Import repository”
- Select your existing documentation repository
- Mintlify expects your `.mdx` files in a `docs/` or root folder
- Add a `mint.json` config file if you don’t have one

**5\. Get your docs URL**

After the first deploy (2-3 minutes), Mintlify provides:

- **Subdomain**: `your-project.mintlify.app` (free)

*The most important part* here is that you will have to *install the GitHub app* (in other words, connect Mintlify and GitHub with the extension), and you will see my screenshot below:

![](https://substackcdn.com/image/fetch/$s_!st9H!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f956162-5361-484a-973f-444cc5431339_1261x426.png)

**Your setup is complete when:**

- ✅ GitHub is connected to Mintlify
- ✅ Your docs repo is linked
- ✅ You can view your docs at `your-project.mintlify.app`
- ✅ Pushing to GitHub auto-deploys updates

### Step 2: Get Figma Personal Access Token

You need a Figma Personal Access Token to allow Claude Code to read your Figma files and export screenshots automatically.

1. Go to [Figma Settings → Account → Personal Access Tokens](https://www.figma.com/settings)
2. Click “Generate new token”
3. Name it: “Claude Code MCP”
4. Scopes needed: `File content` (read-only)
5. Copy the token (starts with `figd_...`)
6. **Important:** Save it securely - you won’t see it again

### Step 3: Connect Figma MCP

Now connect Figma to Claude Code so it can read your design specs and export screenshots.

If you are not sure how and where to add Figma MCP to your AI tool, watch my instructions video.

![](https://www.youtube.com/watch?v=g2_DIk2WkPQ)

Test it:

```markup
“List all components in (your figma link) ”
```

### Step 4: Use Claude Code to write documentation

Now everything’s connected. Let’s automate your first doc update.

I suggest you use Claude Code for writing your first sample page, for example, a dropdown.

```markup
Create documentation for the Dropdown component from this Figma frame:
https://figma.com/file/abc123?node-id=45-890

Include:
- Component description
- When to use it
- All variants and states
- Specifications (spacing, colors, tokens)
- Accessibility requirements
- Usage examples

Add a tracking comment <!-- figma-frame: FILE_ID/NODE_ID -->
so the weekly automation can check this frame for changes.
```

**What gets automated:**

- Screenshot export from Figma
- Spec extraction (spacing, colors, tokens)
- Documentation file creation/updates
- Git commit and PR creation
- Mintlify deployment

**🫶** If you intend to use Claude Code for writing your documentation, I suggest you create a Markdown file with your writing guidelines. Add tone and voice, rules for writing, examples for “dos and don’ts”, etc. This will help you achieve consistent results. If you are unsure what I’m talking about, read this article that explains how to create guideline folders. 👇

---

### Step 5: GitHub Actions Setup / Advanced

**What is GitHub Actions?**

GitHub Actions is GitHub’s built-in automation platform. Think of it as *a scheduled robot* that lives in your repository. You can tell it to run scripts every Monday morning, check for changes, and create pull requests automatically (no server setup required).

### Create the sync script

Write the code manually, or ask your AI tool to create a sync script (like I did).

```markup
Create a complete GitHub Actions workflow that automatically syncs Figma screenshots and specifications to my documentation. Here’s what I need:

Requirements:

1. Workflow Configuration
   - Runs every Monday at X am UTC
   - Can also be manually triggered via workflow_dispatch
   - Uses ubuntu-latest runner 

2. Core Functionality
   - Scan all \`.mdx\` files in my docs folder for HTML comments with format: \`<!-- figma-frame: FILE_ID/NODE_ID -->\`
   - For each tracked Figma frame:
     * Check if the Figma frame has been modified since the last screenshot was taken
     * If modified, export a new 2x PNG screenshot via Figma API
     * Read the frame specifications (spacing, colors, typography, tokens) via Figma API
     * Update the corresponding .mdx file with new specs
   - Create a pull request with all changes if any frames were updated
   - If no changes detected, exit silently without creating a PR
```

**Now it is time to add your API keys to GitHub secrets**

GitHub secrets are your secure “vault” on GitHub, where you store your API keys. When your automation runs, it can access these secrets, but:

- ✅ They’re encrypted and hidden from everyone
- ✅ They don’t appear in logs or code
- ✅ Only your workflows can access them
- ✅ You can update them anytime without changing code

That’s why you should not share them around!

1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add these two secrets:

**Secret 1: FIGMA\_PERSONAL\_ACCESS\_TOKEN**

- Name: `FIGMA_PERSONAL_ACCESS_TOKEN`
- Value: Your Figma token (starts with `figd_...`)

[Find the API key.](https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens)

![](https://substackcdn.com/image/fetch/$s_!zxRa!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52116714-3554-438e-8270-a53fb96d0a1a_463x373.png)

**Secret 2: ANTHROPIC\_API\_KEY**

- Name: `ANTHROPIC_API_KEY`
- Value: Your Claude API key from console.anthropic.com

![](https://substackcdn.com/image/fetch/$s_!cvoi!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48b2b970-4e96-4cb9-9aae-3ad18c2721dd_1751x279.png)

**After committing the workflow file:**

1. Go to your repository on GitHub
2. Click the **Actions** tab
3. Select “Sync Figma to Docs” workflow
4. Click **Run workflow** → **Run workflow**
5. Wait 1-2 minutes
6. Check if a PR was created

---

Ooookay, once you are done, you should check your live documentation. I used the shadcn dropdown component here.

![](https://substackcdn.com/image/fetch/$s_!WQzl!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F871c81d0-3e66-404f-8d76-8cdf15654cc7_1378x724.png)

By now, you know, you can’t process your way out of latency. Make a test account on Mintlify and start experimenting. Let me know how it goes. 😊

Stay tuned for more and enjoy exploring, ⚡️  
*Romina*

*— If you enjoyed this post, please tap the Like button below 💛 This helps me see what you want to read. Thank you.*

---

### 💎 Community Gems

**✨ Decode (just launched)**

Decode is a white-boarding agent that can design, build, and explain your product features.

**🔗 [Link](https://decode.dev/)**

**Claude just introduced Skills and a new model called Haiku**

Skills are packaged instructions that teach Claude your way of working.

**🔗 [Link](https://www.anthropic.com/news/skills)**

**How to set up Claude Code**

Beginner-friendly video

**🔗 [Link](https://youtu.be/g2_DIk2WkPQ)**