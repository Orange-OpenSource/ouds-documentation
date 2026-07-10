---
title: "How to Connect Figma to Claude (MCP Setup Guide – 2026)"
source: "https://medium.com/@garimaagarwal1200/claude-desktop-figma-console-mcp-complete-setup-guide-2026-babba46b12a0"
author:
  - "[[Garima Agarwal]]"
published: 2026-04-08
created: 2026-06-30
description: "More"
tags:
  - "clippings"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*awiHZgaCKAsHBCND)

> The most powerful design tool today is not software alone, but the collaboration between human creativity and AI systems.

I spent hours hitting every possible error trying to connect Claude to Figma. Not because it’s hard. Because the instructions are scattered across GitHub repos, Reddit threads, and Discord channels. Half of them are outdated. The other half assume you know what an MCP server is.

If you’re trying to connect Figma with Claude using MCP (Model Context Protocol), this guide shows the exact step-by-step process to connect Figma Desktop, Figma Console MCP, and Claude Desktop correctly.

## What You’ll Build

Once connected, you can tell Claude things like:

- *“Create a login page from this frame”*
- *“Add a navbar with these brand colors”*
- *“Turn this component into React code”*

And watch it happen, directly inside your Figma file. No copy-pasting. No back-and-forth. Claude reads and writes your designs.

## What you need:

- Figma Desktop (not the browser version): Download from [figma.com/downloads](http://figma.com/downloads)
- Claude Desktop (not the web app): Download from [claude.ai/download](http://claude.ai/download)
- A Figma account (free tier works, but Pro is recommended for higher usage limits)
- Node.js installed (version 18 or higher): Get it from [nodejs.org](http://nodejs.org/)

If you’re missing any of these, stop and install them first. The MCP connection won’t work without the desktop versions.

## Step 1: Verify Node.js Installation

Open your terminal (Windows: PowerShell, Mac: Terminal) and type:

```c
node --version
```

If you see a version number like v20.11.0 or higher, you’re good. If not, install Node.js from [nodejs.org](http://nodejs.org/) and try again.

## Step 2: Generate a Figma Personal Access Token

Now Claude needs permission to access your Figma files. You’ll do this with a Personal Access Token.

1. Open Figma (desktop or browser)
2. Go to Settings → Security
3. Find Personal access tokens
4. Click “Generate new token”

The token will start with:

> *figd\_*

Security note: Treat this like a password. Don’t share it. Don’t commit it to GitHub

## Step 3: Install the Figma MCP Package

Open your terminal and run:

```c
npm install -g figma-console-mcp@latest
```

This installs the MCP server and the Figma Desktop Bridge plugin globally.

Verify it worked:

```c
npm root -g
```

This shows where npm installed the package. You’ll need this path in Step 5.

## Step 4: Configure Claude Desktop

Claude Desktop uses a config file to know which MCP servers to run.

On Windows:

1. Press Win + R
2. Type: %APPDATA%\\Claude
3. Press Enter
4. Open claude\_desktop\_config.json in Notepad. If it does not exist, create it

On Mac:

1. Open Finder
2. Press Cmd + Shift + G
3. Type: ~/Library/Application Support/Claude
4. Press Enter
5. Open claude\_desktop\_config.json in Notepad. If it does not exist, create it

If the folder doesn’t exist, create it. Inside that folder, create a file called claude\_desktop\_config.json

Paste this:

```c
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-figma"
      ],
      "env": {
        "FIGMA_PERSONAL_ACCESS_TOKEN": "YOUR_TOKEN_HERE"
      }
    }
  }
}
```

Replace YOUR\_TOKEN\_HERE with the token you copied in Step 2.

Save the file.

## Step 5: Allow Network Access in Claude Desktop

Claude needs permission to download and run the MCP server. Without this, the connection to Figma won’t work.

Here’s how to enable it:

1. Open Claude Desktop
2. Go to Settings
3. Click Capabilities in the left sidebar
4. Scroll down to find “Allow network egress”
5. Toggle it ON
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*dkHJ3FCS1UCMjHKb)

What this does: Lets Claude connect to Figma’s API and download the MCP server package.

If you skip this: Nothing will work. Claude will just ignore your Figma prompts.

## Step 6: Install the Figma Desktop Bridge Plugin

1. Open Figma Desktop
2. Create or open a Design file (not FigJam, not Slides)
3. Go to Plugins → Development → Import plugin from manifest…

Navigate to the plugin folder:

Windows:

```c
C:\Users\YOURNAME\AppData\Roaming\npm\node_modules\figma-console-mcp\figma-desktop-bridge
```

(Replace YOURNAME with your Windows username)

Mac:

```c
/usr/local/lib/node_modules/figma-console-mcp/figma-desktop-bridge
```

Or use the path from npm root -g in Step 3, then add /figma-console-mcp/figma-desktop-bridge

1. Select manifest.json
2. Click Open

## Step 7: Run the Desktop Bridge Plugin

1. In your Design file, go to Plugins → Development → Figma Desktop Bridge
2. Click to run it
3. A small plugin window will appear
4. You should see “MCP ready” with a green dot

Keep this plugin running while you work with Claude. If you close it, the connection breaks.

![](https://miro.medium.com/v2/resize:fit:1100/format:webp/0*qBQ1Q-kPDhKsuSfi)

## Step 10: Restart Claude Desktop and Test

1. Fully quit Claude Desktop
2. Reopen Claude Desktop
3. Type in the chat:
```c
List MCP tools
```

If Claude returns a list of Figma tools, you’re connected!

## Every Session Checklist

Every time you want to use Claude with Figma, follow this quick checklist:

1. Open Figma Desktop
2. Open a Design file (not FigJam or Slides)
3. Run Figma Desktop Bridge plugin (Plugins → Development → Figma Desktop Bridge)
4. Confirm “MCP ready” status in the plugin window
5. Open Claude Desktop and start chatting

## What This Actually Means

This isn’t about replacing designers. It’s about compressing the mechanical work so you can focus on the decisions that actually matter.

Instead of spending 2 hours building variations of a dashboard layout, you spend 15 minutes generating options and 2 hours refining the one that works.

The bottleneck shifts from execution to judgment. Which is exactly where it should be.

What would you build first with this? Dashboard templates, landing pages, or something else?