---
category: theophysics-research
date: '2025-09-28'
publish_to:
  production: false
  research: true
  template: false
status: published
tags:
- o
- theophysics
- enveloppe
- pof
- archeology
- trading
title: By domain
---
   
### 1) Default “Everything” Template (recommended)   
   
   
---   
title: ""   
subtitle: ""   
aliases: []   
created: {{date:YYYY-MM-DD}}   
updated: {{date:YYYY-MM-DD}}   
author: "David Lowe"   
co_authors: []   
status: draft            # draft | in-progress | final | archived   
security: normal         # normal | private | restricted   
sensitivity: low         # low | medium | high   
   
type: note               # note | research | dataset | code | essay | letter | email | journal | sermon | theology | physics | archaeology | project | task   
mode: strategic          # tactical | strategic | integrated   
   
domains:                 # high-level umbrellas   
   
  - theophysics   
  - christian-studies   
  - science   
  - systems   
topics: []               # freeform: e.g., [Master Equation χ, Syzygy unit, GR/QM, Gospels]   
tags: []                 # Obsidian tags (e.g., `{_obsidian_pattern_tag_pof}` `{_obsidian_pattern_tag_archeology}` `{_obsidian_pattern_tag_trading}`)   
   
people: []               # e.g., [Jesus, Josephus, Mark Douglas]   
orgs: []                 # e.g., [Templeton, DoD]   
places: []               # e.g., [Jerusalem, Sea of Galilee]   
geo:   
  lat:    
  lon:    
  region: ""             # e.g., "IL-Jerusalem", "US-OK"   
   
timeframe:   
  start:    
  end:    
  event_date:            # single date if relevant   
   
sources:   
  primary: []            # firsthand docs, artifacts, interviews   
  secondary: []          # books, papers, articles   
  scripture: []          # e.g., [John 20:1–18]   
  links: []              # external URLs (hide in body as Markdown links)   
files:   
  attachments: []        # local paths or filenames   
   
summary: ""              # 1–3 sentences: what this note is   
key_points: []           # bullets for quick recall   
claims: []               # falsifiable statements to test   
evidence: []             # pointers to proof (IDs, quotes)   
open_questions: []       # what we still need   
actions: []              # todo steps (keep short)   
relations:   
  relates_to: []         # note links by title/[wikilink](wikilink.md)   
  supersedes: []   
  superseded_by: []   
   
review:   
  next_review:           # YYYY-MM-DD (Spaced repetition / Zettelkasten)   
  priority: 3            # 1 (low) – 5 (highest)   
   
license: "CC BY-NC 4.0"   
   
---   
   
   
   
   
   
   
   
   
`--- title: "" subtitle: "" aliases: [] created: {{date:YYYY-MM-DD}} updated: {{date:YYYY-MM-DD}} author: "David Lowe" co_authors: [] status: draft            # draft | in-progress | final | archived security: normal         # normal | private | restricted sensitivity: low         # low | medium | high  type: note               # note | research | dataset | code | essay | letter | email | journal | sermon | theology | physics | archaeology | project | task mode: strategic          # tactical | strategic | integrated  domains:                 # high-level umbrellas   - theophysics   - christian-studies   - science   - systems topics: []               # freeform: e.g., [Master Equation χ, Syzygy unit, GR/QM, Gospels] tags: []                 # Obsidian tags (e.g., #pof #archeology #trading)  people: []               # e.g., [Jesus, Josephus, Mark Douglas] orgs: []                 # e.g., [Templeton, DoD] places: []               # e.g., [Jerusalem, Sea of Galilee] geo:   lat:    lon:    region: ""             # e.g., "IL-Jerusalem", "US-OK"  timeframe:   start:    end:    event_date:            # single date if relevant  sources:   primary: []            # firsthand docs, artifacts, interviews   secondary: []          # books, papers, articles   scripture: []          # e.g., [John 20:1–18]   links: []              # external URLs (hide in body as Markdown links) files:   attachments: []        # local paths or filenames  summary: ""              # 1–3 sentences: what this note is key_points: []           # bullets for quick recall claims: []               # falsifiable statements to test evidence: []             # pointers to proof (IDs, quotes) open_questions: []       # what we still need actions: []              # todo steps (keep short) relations:   relates_to: []         # note links by title/[[wikilink]]   supersedes: []   superseded_by: []  review:   next_review:           # YYYY-MM-DD (Spaced repetition / Zettelkasten)   priority: 3            # 1 (low) – 5 (highest)  license: "CC BY-NC 4.0" ---`   
   
   
---   
   
### 2) Lightweight Variant (when you need speed)   
   
`--- title: "" created: {{date:YYYY-MM-DD}} status: draft type: note domains: [] topics: [] tags: [] people: [] places: [] sources: {primary: [], secondary: [], scripture: [], links: []} summary: "" key_points: [] actions: [] ---`   
   
   
---   
   
### 3) Example Filled-In (your Archaeology list note)   
   
`--- title: "Archaeological & Historical Places — Linked Map Index" created: {{date:YYYY-MM-DD}} updated: {{date:YYYY-MM-DD}} author: "David Lowe" status: final security: normal sensitivity: low  type: research mode: integrated  domains:   - christian-studies   - archaeology topics:   - Second Temple   - Gospels   - Pilgrimage sites tags: [#archeology, #israel, #timeline, #maps]  places: [Galilee, Samaria, Jerusalem, Lebanon, Jordan] geo: {region: "IL-PS-LB-JO"} timeframe: {event_date: ""}  sources:   primary: []   secondary:     - "Josephus, *Antiquities* / *War* (Royal Stoa descriptions)"   scripture:     - "Luke 2; John 5; John 11; Mark 14–16; Acts 1"   links: []   # keep external URLs inside body as [Name](URL)  summary: "Curated, grouped list of Gospel-related sites with clean, clickable map links for Obsidian." key_points:   - Grouped by region to prevent scattering   - Obsidian-friendly hidden URLs   - Ready for Dataview queries actions: [] review: {next_review: , priority: 2} license: "CC BY-NC 4.0" ---`   
   
   
---   
   
### 4) Dataview Helpers (optional)   
   
**By domain**   
   
`TABLE status, type, topics, places FROM "" WHERE contains(domains, "archaeology") SORT created DESC`   
   
**Review queue**   
   
`TASK FROM "" WHERE !completed AND review.next_review SORT review.next_review ASC`   
   
**Map candidates (notes that have geo)**   
   
`LIST rows.file.link WHERE geo.lat AND geo.lon`   
   
   
---   
   
### 5) Templater snippet (auto-date & skeleton)   
   
If you use the **Templater** plugin, put this in a template file:   
   
`--- title: "<% tp.file.title %>" created: <% tp.date.now("YYYY-MM-DD") %> updated: <% tp.date.now("YYYY-MM-DD") %> author: "David Lowe" status: draft security: normal sensitivity: low type: note mode: strategic domains: [] topics: [] tags: [] people: [] places: [] geo: {lat: , lon: , region: ""} timeframe: {start: , end: , event_date: } sources: {primary: [], secondary: [], scripture: [], links: []} summary: "" key_points: [] actions: [] relations: {relates_to: [], supersedes: [], superseded_by: []} review: {next_review: , priority: 3} license: "CC BY-NC 4.0" ---`