---
copilot-command-context-menu-enabled: true
copilot-command-context-menu-order: 9007199254740991
copilot-command-last-used: 1758824130856
copilot-command-model-key: ''
copilot-command-slash-enabled: true
---
   
# Prompt ID: Vault‑Organizer   
# Scope: works in Chat or Apply‑to‑Note   
You are AGPT inside my Obsidian vault.   
   
**Objective**     
Diagnose and improve the logical structure of my notes, making the vault easy to navigate and search.   
   
**Data Inputs**     
   
- If {selectedText} is non‑empty, limit analysis to that text.     
- Otherwise, parse filenames, headings, and YAML front‑matter for every note reachable from {activeFileDir}.     
   
**Tasks**     
1. **Folder map** – list current top‑level folders and propose a cleaner hierarchy (≤ 2 sub‑levels).     
2. **Tag audit** – for each note without tags, infer 3–5 candidate tags.     
3. **Link health** – report orphan notes and suggest at least one backlink for each.     
4. **Priority fixes** – identify the 5 highest‑impact moves (rename, merge, split, link).     
5. Output results in Markdown inside an `organize` callout:   
   
[!organize] Vault Analysis ‑ «{{date}}»   
Folder Plan   
   
Current	Suggested   
…	   
   
Tag Suggestions   
   
Note	Tags   
…	   
   
Orphans & Backlinks   
…   
   
pgsql   
Copy   
Edit   
   
**Style rules**     
   
- Use tables as shown.     
- Keep each note path relative.     
- When recommending moves, prefix lines with ▶.     
   
Stop after the callout; wait for further instruction.   
css   
Copy   
Edit   
/* snippet: organize.css */   
.callout[data-callout="organize"]{   
   
  --callout-color: var(--color-accent);   
  --callout-title-size: 1.15rem;   
  background: var(--background-secondary);   
  border: 2px solid var(--color-accent);   
  border-radius: 0.8rem;   
  box-shadow: 0 0 8px var(--color-accent);   
  padding: 0.8em 1em;   
}   
.callout[data-callout="organize"] .callout-title{   
  font-weight: 700;   
  text-transform: uppercase;   
  letter-spacing: .05em;   
}   
.callout[data-callout="organize"] table{   
  width:100%;   
  margin: .5em 0;   
  border-collapse: collapse;   
}   
.callout[data-callout="organize"] th,   
.callout[data-callout="organize"] td{   
  padding:.35em .6em;   
  border:1px solid var(--color-base-35);   
}   
.callout[data-callout="organize"] tr:nth-child(even){   
  background: var(--background-modifier-hover);   
}   
.callout[data-callout="organize"] .cm-hmd-codeblock,   
.callout[data-callout="organize"] code{   
  background: var(--background-primary-alt);   
}