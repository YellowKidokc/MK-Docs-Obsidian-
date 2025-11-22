---
book: {{book_name}}
book_code: {{book_code}}
chapter: {{chapter_num}}
type: bible-chapter
translation: KJV
verse_count: {{verse_count}}
---

<div class="bible-chapter-layout">

<!-- LEFT SIDEBAR: Structured Data -->
<div class="sidebar-left">

### 📍 People in This Chapter

```dataview
TABLE WITHOUT ID
  entity_name as "Name",
  entity_type as "Type"
FROM "Entities/People"
WHERE contains(this.file.content, entity_name)
LIMIT 10
```

---

### 🗺️ Places Mentioned

```dataview
TABLE WITHOUT ID
  entity_name as "Location"
FROM "Entities/Places"
WHERE contains(this.file.content, entity_name)
LIMIT 5
```

---

### ⏱️ Timeline

```dataviewjs
// Extract timeline events for this chapter
const events = dv.pages('"Bible"')
    .where(p => p.file.name == dv.current().file.name)
    .flatMap(p => p.events || []);

if (events.length > 0) {
    dv.list(events.map(e => `${e.date}: ${e.description}`));
} else {
    dv.paragraph("*No timeline events*");
}
```

---

### 🔗 Cross References

```dataview
LIST
FROM "Bible"
WHERE file != this.file
  AND contains(cross_references, this.book_code)
LIMIT 5
```

</div>

<!-- MAIN CONTENT: Bible Text -->
<div class="main-content">

# {{book_name}} {{chapter_num}}

<!-- Translation selector -->
<div class="translation-selector">
  <select id="translation-select">
    <option value="KJV" selected>King James (KJV)</option>
    <option value="ESV" disabled>ESV (Coming Soon)</option>
    <option value="NIV" disabled>NIV (Coming Soon)</option>
    <option value="NASB" disabled>NASB (Coming Soon)</option>
  </select>
</div>

<!-- Layer controls -->
<div class="layer-controls">
  <button class="layer-toggle-btn active" data-layer="1">
    📖 Read
  </button>
  <button class="layer-toggle-btn" data-layer="2">
    🔍 Explore
  </button>
  <button class="layer-toggle-btn" data-layer="3">
    🎯 Deep Dive
  </button>
</div>

<!-- Reading view -->
<div class="bible-reading-view">

{{#each verses}}
<span class="verse-number" data-verse="{{verse_num}}" onclick="toggleVerseDetails('{{uid}}')">{{verse_num}}</span> <span class="verse-text" data-uid="{{uid}}" data-entities="{{entities}}" data-topics="{{topics}}" data-lexicon="{{lexicon}}">{{text}}</span>

<div class="verse-details" id="details-{{uid}}" style="display:none">

{{#if entities}}
**People/Places:**
{{#each entities}}
- [[Entities/{{type}}/{{name}}]]
{{/each}}
{{/if}}

{{#if topics}}
**Topics:**
{{#each topics}}
- [[Topics/{{name}}]]
{{/each}}
{{/if}}

{{#if lexicon}}
**Word Study:**
{{#each lexicon}}
- **{{word}}** ({{strongs}}): {{definition}}
{{/each}}
{{/if}}

</div>

{{/each}}

</div>

---

## Chapter Summary

*Add your personal notes and insights here*

---

## Dataview Queries

### Verse Statistics

```dataview
TABLE WITHOUT ID
  verse_count as "Total Verses",
  length(entities) as "Entities",
  length(topics) as "Topics"
WHERE file = this.file
```

</div>

<!-- RIGHT SIDEBAR: Custom/AI -->
<div class="sidebar-right">

### 📝 Personal Notes

*Click to add your notes for this chapter*

```button
name Add Note
type note({{file.name}})
action obsidian://new?file=Notes/{{book_name}}-{{chapter_num}}-Note
```

---

### 🤖 AI Insights

*AI-generated observations will appear here*

```dataviewjs
// Future: Query AI insights for this chapter
dv.paragraph("*AI insights coming soon*");
```

---

### 💬 Community Discussion

*Forum discussions will appear here when enabled*

```dataviewjs
// Future: Show forum threads for this chapter
dv.paragraph("*Enable in Settings to view discussions*");
```

---

### 🎯 Key Questions

- What is the main theme?
- Who are the key figures?
- What can I apply today?

*Add your own questions*

---

### 📖 Related Reading

```dataview
LIST
FROM "Bible"
WHERE book = this.book
  AND chapter != this.chapter
  AND contains(themes, this.themes)
LIMIT 3
```

</div>

</div>

<!-- JavaScript for interactivity -->
```js
// Toggle verse details
function toggleVerseDetails(uid) {
    const details = document.getElementById('details-' + uid);
    if (details) {
        details.style.display = details.style.display === 'none' ? 'block' : 'none';
    }
}

// Layer toggle functionality
document.querySelectorAll('.layer-toggle-btn').forEach(btn => {
    btn.addEventListener('click', function() {
        const layer = this.dataset.layer;

        // Toggle active state
        document.querySelectorAll('.layer-toggle-btn').forEach(b => b.classList.remove('active'));
        this.classList.add('active');

        // Apply layer styles
        document.body.className = '';
        if (layer === '2') {
            document.body.classList.add('layer-2-enabled');
        } else if (layer === '3') {
            document.body.classList.add('zoom-mode');
            // Auto-expand all verse details
            document.querySelectorAll('.verse-details').forEach(d => d.style.display = 'block');
        }
    });
});

// Translation selector
document.getElementById('translation-select')?.addEventListener('change', function() {
    // Future: Load different translation
    new Notice('Translation switching coming soon!');
});
```

---

**Navigation**: [[{{prev_chapter}}|← Previous]] | [[{{book_name}}|Book Index]] | [[{{next_chapter}}|Next →]]
