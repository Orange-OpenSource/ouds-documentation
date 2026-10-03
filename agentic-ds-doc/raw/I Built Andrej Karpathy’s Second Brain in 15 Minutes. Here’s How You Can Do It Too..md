---
title: "I Built Andrej Karpathy’s Second Brain in 15 Minutes. Here’s How You Can Do It Too."
source: "https://medium.com/@bagheshri/i-built-andrej-karpathys-second-brain-in-15-minutes-here-s-how-you-can-do-it-too-dd12f04d6c28"
author:
  - "[[Bagheshri Suresh Kumar]]"
published: 2026-04-16
created: 2026-06-15
description: "More"
tags:
  - "clippings"
---
**No RAG pipelines. No vector databases. Just markdown files, Claude Code, and 15 minutes.**

On April 3, 2026, Andrej Karpathy — co-founder of OpenAI, former Tesla AI Director, the person who coined “vibe coding” posted something on X that stopped me mid-scroll.

He wasn’t announcing a new model. He wasn’t dropping a benchmark.

He was describing how he uses LLMs to organize knowledge.

The post went viral. 19 million views. And after reading it, I understood why.

## What Is Karpathy’s Second Brain?

Most of us use LLMs the same way: ask a question, get an answer, close the tab. Next session, the LLM remembers nothing. You start from zero every time.

Karpathy’s insight was simple but powerful: **instead of asking the LLM questions, have the LLM build and maintain a wiki from your raw research material.**

The system has three folders:

- **raw/** — your source documents, append-only, never edited
- **wiki/** — markdown articles the LLM writes and maintains
- **outputs/** — query responses and synthesized reports

You drop a PDF, an article, or a set of notes into `raw/`. The LLM reads it, extracts key concepts, creates or updates wiki articles, adds backlinks between related ideas, and maintains an index. You never write a single wiki article yourself.

Karpathy’s own research wiki on a single topic grew to 100 articles and 400,000 words, without him writing a word of it.

## Why I Built One

I’m an AI engineer. Over the past year I’ve been deep in technical preparation — interview prep, project documentation, research documentation, research papers, certification study material — across dozens of conversations with AI tools.

The problem: **all of that knowledge was scattered and disconnected.**

Notes from one session. Code decisions from another. Framework comparisons buried in a third. Every time I needed something, I was hunting through old conversations, re-explaining context, rediscovering things I’d already figured out.

That’s exactly the problem a second brain solves. **Knowledge that compounds instead of evaporates.**

So I built one. Here’s exactly how.

## What Goes Into Your raw/ Folder

The first step isn’t technical. It’s figuring out what knowledge you already have that’s worth preserving.

**Technical preparation material** Behavioral story frameworks. System design patterns. Coding problem approaches and solutions. Technology comparisons you’ve researched. Concept explanations you’ve written out for yourself. Notes from mock interviews or study sessions. Anything you’ve had to look up more than once.

**Project documentation** For each project you’ve built: what it does, the tech stack, the key architectural decisions you made and why, challenges you hit, what you’d do differently. This is the material that gets forgotten fastest and is most valuable to have structured.

**Articles and research papers** Any paper you read that shaped how you think. Any article that changed your approach. Your own writing — blog posts, LinkedIn posts, notes. Don’t just save the link. Drop the content into `raw/` so the LLM can actually reason over it.

**Domain study material** Certification prep notes. Course materials. Any structured body of knowledge you’ve studied, whatever your domain is.

The rule: **if you’ve spent time learning it and you’d be annoyed to have to relearn it, it belongs in raw/.**

## Step 1: Install Obsidian

Obsidian is the “IDE” for your wiki — a local markdown editor with a graph view that renders the connections between your articles. Everything stays on your machine. Nothing goes to the cloud unless you want it to.

Go to [**obsidian.md/download**](http://obsidian.md/download) and download the installer for your operating system (Windows, Mac, or Linux). Run the installer — it takes under a minute.

Once installed, open Obsidian → **Create new vault** → name it `knowledge` → set location to your home folder.

Then create the three folders. On Mac/Linux:

```c
mkdir -p ~/knowledge/raw ~/knowledge/wiki ~/knowledge/outputs
```

On Windows (PowerShell):

```c
mkdir C:\Users\yourname\knowledge\raw
mkdir C:\Users\yourname\knowledge\wiki
mkdir C:\Users\yourname\knowledge\outputs
```

Drop your raw files into `raw/`.

## Step 2: Create Your CLAUDE.md Schema File

This is the most important file in the system. It tells the LLM the rules — how to ingest sources, what the index format looks like, how to generate backlinks, what a linting pass checks for.

Create a file called `CLAUDE.md` in the root of your vault and paste this in:

```c
# Knowledge Base Schema
```
```c
## Directories
- raw/: Source documents. Append-only. Never edit these files.
- wiki/: LLM-authored articles. One .md file per concept or project.
- outputs/: Query responses and synthesized reports.## On ingesting a new source in raw/:
1. Read wiki/INDEX.md to understand existing articles.
2. Identify new concepts not yet in the wiki.
3. Create or update wiki/ articles for each concept.
4. Add [[wikilinks]] to related existing articles.
5. Update wiki/INDEX.md with any new entries.## Index format (wiki/INDEX.md):
- One line per article: [Article Title](filename.md) - one-sentence summary## On answering a query:
1. Read wiki/INDEX.md.
2. Identify and read relevant articles.
3. Write answer to outputs/YYYY-MM-DD-query-slug.md with citations.## On a linting pass:
1. Read all wiki articles.
2. Flag contradictions, missing wikilinks, orphaned concepts.
3. Create stubs for any missing articles.
```

You can customize this schema over time. The human’s primary editorial role in this system isn’t writing articles — it’s writing and refining the rules that tell the LLM how to write them.

## Step 3: Install Claude Code

Claude Code is Anthropic’s CLI agent, the LLM that reads your schema, processes your raw files, and writes your wiki.

```c
npm install -g @anthropic-ai/claude-code
```

Navigate to your vault and launch it:

```c
cd ~/knowledge
claude
```

Log in with your [Claude.ai](http://claude.ai/) account. Select **“Yes, I trust this folder.”**

## Step 4: Run the Compilation

Paste this prompt into Claude Code:

```c
Read the CLAUDE.md schema file in this directory. I have added new 
source files to the raw/ folder. Please compile them into the wiki/ 
directory. Create one markdown article per concept, project, framework, 
and pattern. Add [[wikilinks]] between related articles. Create 
wiki/INDEX.md with a one-line summary per article.
```

When it asks for permission to create files, select **“Yes, allow all edits during this session”** — otherwise it will ask for approval on every single file.

Then watch it build.

Mine ran for about 10 minutes and created 35 interconnected wiki articles organized into categories covering projects, interview preparation, frameworks and technologies, concepts and patterns, and research papers.

Every article has \[\[wikilinks\]\] connecting it to related articles. The [INDEX.md](http://index.md/) has a one-line summary of every article in the vault.

## Step 5: See the Graph

Open Obsidian → click the **graph view icon** in the top right.

You’ll see your entire knowledge base as a visual network — every node an article, every line a wikilink connection. Projects connected to the frameworks they use. Preparation material connected to the concepts it covers. Research papers connected to the projects they inform.

Switch to dark mode (**Settings → Appearance → Dark**) for the full effect.

That’s your second brain.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*4v1B0WDl3b2HI8VRK5bPgw.jpeg)

## How I Actually Use It

**For interview preparation**, instead of hunting through old notes, I query the wiki directly:

*“Based on the wiki, what story should I use if asked about handling conflict on a team, and what values does it map to?”*

The response came back with the specific story to use, why it fits the question, which interviewer’s evaluation criteria it aligns with, the exact closing line to deliver, and a backup story if the follow-up reframes the question. It reasoned across multiple wiki articles simultaneously and gave me an interview-ready answer in seconds.

**For project documentation**, when I need to explain a past project:

*“Based on the wiki, summarize the key architectural decisions I made in \[project\] and why I made them.”*

Instead of trying to remember details from months ago, the wiki surfaces the exact decisions, the tradeoffs, and the outcomes — all in one place.

**For framework comparisons**, when evaluating a new tool:

*“Based on the wiki, how does my experience with X compare to what I know about Y? What are the gaps?”*

The wiki surfaces what I actually know from hands-on experience, not what the docs say.

**For content creation**, when writing about a technical topic:

*“Based on the wiki, write a summary of my experience with \[topic\] I can use in a cover letter.”*

It synthesizes across multiple projects and produces a coherent narrative — not a list of bullet points, but a story.

## Why This Beats RAG for Personal Use

The standard approach to personal knowledge management is RAG: chunk your documents, embed them into a vector database, run similarity search at query time.

The problem: **nothing accumulates.** Every query starts from zero. The LLM pieces together fragments from scratch. Cross-document reasoning is weak. And maintaining a vector database for personal use is overkill.

The second brain approach is different. The LLM reads your raw material once and writes structured wiki articles. At query time, it reads the wiki index and pulls in the specific articles it needs. The wiki gets richer over time.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*K8IFc4F_CnhiL5V2UEZibQ.png)

## How to Keep It Growing

Every time you want to add something new:

1. Drop the file into `raw/`
2. Open Claude Code in your `knowledge/` folder
3. Type: *“New files have been added to raw/. Please compile them into the wiki.”*

For a periodic health check: *“Run a linting pass on my wiki — flag contradictions, missing backlinks, and concepts mentioned but lacking their own article.”*

Install the **Obsidian Web Clipper** browser extension for one-click saving of any web page directly into `raw/` as clean Markdown.

## Who This Is For

Anyone whose knowledge is currently scattered.

Engineers, product managers, researchers, students, consultants, founders, writers, lawyers — if you consume information and want it to actually compound instead of evaporate, this is for you.

The second brain doesn’t add new effort. It makes your existing effort compound.

## The Bottom Line

Stop using LLMs as search engines. Start using them as knowledge architects.

Your past conversations, your projects, your prep, your research — it’s all already there. The second brain just makes it compound.