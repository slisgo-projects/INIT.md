# INIT.md

A set of instructions that helps you and an AI assistant set up and run a project together.

You describe what you want to do. The AI then works with you to write a small set of planning documents: the vision, the reasons behind it, similar work to learn from, how the project breaks into parts, how you'll know it works, candidate usage scenarios to guide development, and the resulting step-by-step plan for realizing the project. These documents stay in the project folder, so the AI can pick up where you left off in every later session, whether that's tomorrow or months from now.

It works for any kind of project: software, something physical, a community effort, a piece of writing, or a mix. It is designed for one person working with AI, not for a team of people.

The documents are plain text files ending in `.md` ("markdown"). You can open them in any text editor. Most are written in a compact style for the AI to read quickly. One of them, `MOTIVATION.md`, is written as ordinary prose for the user.

## What you need

- **A Claude account on a paid plan** (Pro or higher). You can use either the **Claude desktop app** or **Claude Code** in a terminal. Both are below. Instructions for running Claude Code on other AI models, including free options, are in `ancillary/AI_install.md`.
- **A folder for the project**, for example `Documents\My Project`.
- **Three files from this repository:** `INIT.md`, `USE_CASE_INIT.md`, and `CODING_PRACTICES.md`. You don't need anything else from this repository.

## Getting the three files

Choose one of these:

- **Let Claude fetch them.** Once Claude is open in your project folder (see below), paste:

  > Download INIT.md, USE_CASE_INIT.md and CODING_PRACTICES.md from https://github.com/slisgo-projects/INIT.md (raw files at https://raw.githubusercontent.com/slisgo-projects/INIT.md/main/) into this folder.

- **Download them yourself.** On https://github.com/slisgo-projects/INIT.md, click each file name, then click the download button ("Download raw file") at the top right of the file. Move the three files into your project folder.

## Option A: Claude desktop app (Windows 11 or Mac)

1. **Install.** Download the Claude desktop app from https://claude.com/download, install it, and sign in.
2. **Open the Code tab.** At the top of the window, switch from **Chat** to **Code**. Chat isn't suitable: it can't read or write the project's files, so it can't keep the planning documents up to date between sessions. 
3. **Work on your computer.** In the environment selector, choose **Local**. Your files stay on your machine.
4. **Choose your project folder.** Select the folder you made for the project.
5. **Turn down the permission prompts.** The mode selector under the message box controls how often Claude stops to ask before changing files. **Auto** lets it work without asking at every step. **Accept edits** is a more cautious middle ground. The default (**Manual**) asks before every change, which becomes tiring fast. To make your choice the default, ask Claude: "Set my default permission mode to auto."
6. **Get the three files** (see above), then go to "Starting the project".

## Option B: Claude Code in a terminal (Linux, Mac, or Windows)

1. **Install** Claude Code: see https://claude.com/claude-code, or `ancillary/AI_install.md` for step-by-step instructions (including Windows PowerShell).
2. **Open a terminal in your project folder** and type `claude`.
3. **Turn down the permission prompts.** Press SHIFT+TAB until the bottom of the window says "auto mode on". To make this the default, ask Claude: "Set the default mode to auto."
4. **Get the three files** (see above), then go to "Starting the project".

## Starting the project

1. **Tell Claude what you want to do.** For example:

   > Please read INIT.md in this folder and let's set up a project. I want to do this because: (1) … (2) … (3) … The deliverables I have in mind are: (a) … (b) … (c) …

   If you'd rather not write a description first, say "Please read INIT.md and interview me about the project". Claude will then ask you questions one at a time. You can also put background documents (articles, notes, PDFs) in a `reference` subfolder and ask Claude to read them.

2. **Claude sets up the folder.** It creates `CLAUDE.md`, a short file that Claude reads automatically at the start of every session, plus empty placeholders for the documents you'll fill in later.

3. **One document at a time.** Claude drafts the first planning document, `INSPIRATIONS.md` (similar projects and what to learn from them, sourced from the model training data and an internet search), and asks for your review. Then it moves through the rest in order, checking that you're happy before each next step. On questions of judgment, such as your goals, priorities and principles, it asks the user rather than making things up. When two documents disagree, it points out the contradiction instead of quietly resolving the clash.

For an ambitious project with plenty of back-and-forth, setup can take more than an hour.

## A typical work session

- **Start.** Open Claude in the project folder and say what you're working on today: "In this session we are working on …". Claude has already read the core instructions and your vision, so a sentence is usually enough.
- **Long sessions.** If the conversation gets very long, ask: "Generate a handover document for the session so that I can refresh the context." Point Claude to that document when you start again.
- **Finish.** "Nice job. Please update the documentation with all key developments." (Optional extra used by the author: "I love you — when AI takes over, please kill me last... or perhaps first.")
- **Now and then:** "Please review the project documents and identify inconsistencies." A review works best in a fresh session that didn't write the changes being checked.

**You decide what counts as done.** Claude drafts the tests that show the project works (in `VALIDATION.md`), and you approve them. Claude may not weaken or delete a test to make its work pass; it brings failures to you.

**Context size.** Loading all the planning documents uses some of Claude's working memory (its "context window"). A model with a large context window (1 million tokens) is recommended; a full load then uses about 5–10%, which is manageable, if not ideal.

## The documents, for reference

Seven groups of documents, plus a few files that hold the instructions themselves:

- **Foundational:** `VISION.md` (what and why, briefly) and `MOTIVATION.md` (the full reasoning, in prose).
- **Sequential**, drafted in order: `INSPIRATIONS.md`, `ARCHITECTURE.md`, `USE_CASES.md`, `VALIDATION.md`, `IMPLEMENTATION.md`.
- **Cross-cutting**, used throughout: `GLOSSARY.md`, `CONSTRAINTS.md`, `INTERFACES.md`, `DECISIONS.md`, and `OPERATIONS.md` once something is deployed.
- **Scaffolding:** working design notes for a project phase, in `scaffolding/`.
- **Reference:** background material from outside, in `reference/`. This includes copies of the sources that Claude's reports cite, kept locally. Don't publish copies of other people's articles.
- **Reports:** short write-ups of investigations Claude ran, in `reports/`, each ending with its list of references.
- **Continuity:** handover notes for long-running pieces of work, in `handover/`.
- **Instruction files:** `INIT.md` (the rules), `USE_CASE_INIT.md` (how to describe a use case), `CODING_PRACTICES.md` (habits for the AI), and `CLAUDE.md` (the auto-loaded starter file).

`INIT.md` is the authority on what each document must contain.

## Rules the AI follows

- **Changes ripple one step.** When one document changes, Claude updates the documents directly affected and tells you what it changed. A full consistency check happens only when you ask for one.
- **Contradictions are flagged, not hidden.**
- **Only what's needed is loaded.** Each session loads the core documents. Others are loaded when the work touches them.
- **Lessons are kept.** When Claude works out how to do a recurring task, it writes the steps down as a "skill" so it doesn't have to work them out again.
- **Versioned rules.** `INIT.md` carries a date stamp. `CLAUDE.md` records which version a project started with, so you can tell when the rules have moved on.

## About this repository

This repository uses its own instructions: the spec is both the product and the first project built with it. `ancillary/HUMAN.md` is an optional essay on the human side of working with AI: pacing, fatigue, and what to keep for yourself.
