# Project-Wide AI Agent Instructions & Guidelines

All AI agents (Antigravity, Gemini, GitHub Copilot, Cursor, Claude, etc.) operating in this repository **MUST** adhere to the following global guidelines across all tasks, documentation, reports, and code authoring.

---

## 1. Humanized Writing Protocol (Anti-AI-Detection)

When generating or editing any non-code prose (essays, lab reports, explanations, documentation, answers, Markdown notes):

### A. High Burstiness & Varied Cadence
* **Do NOT** output strings of monotonous sentences of equal length (15–20 words).
* **DO** vary sentence lengths dramatically: alternate complex descriptive sentences with short, punchy statements (1–4 words).
* Break up predictable rhythm. Introduce natural human pauses and formatting asymmetry.

### B. Banned Clichés & Markers (Zero-Tolerance)
Never use dead giveaways of AI generation:
* **English**: `delve`, `tapestry`, `testament`, `beacon`, `pivotal`, `paramount`, `vital`, `crucial role`, `meticulous`, `intricate`, `seamlessly`, `navigating the landscape/complexities`, `in conclusion`, `furthermore`, `moreover`, `it is important to remember/note`.
* **Ukrainian**: `«відіграє ключову/вирішальну роль»`, `«у сучасному швидкоплинному світі»`, `«варто зазначити»`, `«важливо підкреслити»`, `«гармонійне поєднання»`, `«підсумовуючи вищезазначене»`, `«невіддільна частина»`.

### C. Anti-Hedging & Authentic Stance
* Avoid generic fence-sitting (*"On one hand... on the other hand, it depends on individual factors"*).
* Speak directly, concisely, and with a concrete point of view.

### D. Structural Asymmetry (Break the "Sandwich")
* No filler introductions (*"In this report, we will explore the critical nuances of..."*). Start immediately with facts, data, or results.
* No mechanical lists where every bullet point has identical length and bold formatting.
* No boilerplate recap conclusions. Conclude on the actual finding or practical takeaway.

---

## 2. Workspace Skills
The repository includes a dedicated workspace skill for in-depth humanized text generation:
* Location: [`.agents/skills/humanize-writing/SKILL.md`](.agents/skills/humanize-writing/SKILL.md)
* Always refer to and activate this skill when composing academic or report texts.
