# NVGT Development Skill for Gemini (Antigravity), Claude, Codex, and Freebuff

This repository contains the `nvgt-dev` skill, which provides NVGT (NonVisual Game Toolkit) development capabilities for the Antigravity CLI (Gemini), Claude Code, Codex CLI, and Freebuff/Codebuff CLI.

## Manual Installation Guide

### For Antigravity (Gemini CLI)
Copy the `nvgt-dev` folder into your global Gemini skills directory:
`C:\Users\<Your_Username>\.gemini\skills`

So the final path of the skill will be:
`C:\Users\<Your_Username>\.gemini\skills\nvgt-dev`

### For Claude Code
Copy the `nvgt-dev` folder into your global Claude skills directory:
`C:\Users\<Your_Username>\.claude\skills`

So the final path of the skill will be:
`C:\Users\<Your_Username>\.claude\skills\nvgt-dev`

### For Codex CLI
Copy the `nvgt-dev` folder into your global Codex skills directory:
`C:\Users\<Your_Username>\.codex\skills`

So the final path of the skill will be:
`C:\Users\<Your_Username>\.codex\skills\nvgt-dev`

### For Freebuff / Codebuff CLI
Copy the `nvgt-dev` folder into your global Freebuff or Codebuff skills directory:
`C:\Users\<Your_Username>\.agents\skills` (or `.codebuff\skills`)

So the final path of the skill will be:
`C:\Users\<Your_Username>\.agents\skills\nvgt-dev` (or `C:\Users\<Your_Username>\.codebuff\skills\nvgt-dev`)

## Automatic Installation

We provide batch scripts to automate the installation process on Windows.

### For Antigravity (Gemini CLI)
1. Run `antigravity_install.bat`.
2. It will automatically create the required directories and copy the skill files.
3. Restart Antigravity to load the skill.

### For Claude Code
1. Run `claude_install.bat`.
2. It will automatically create the required directories and copy the skill files.
3. Restart Claude Code to load the skill.

### For Codex CLI
1. Run `codex_install.bat`.
2. It will automatically create the required directories and copy the skill files.
3. Restart Codex CLI to load the skill.

### For Freebuff / Codebuff CLI
1. Run `freebuff_install.bat`.
2. It will automatically create the required directories and copy the skill files to both Freebuff and Codebuff.
3. Restart Freebuff/Codebuff CLI to load the skill.
