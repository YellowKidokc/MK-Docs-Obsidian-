---
type: settings
version: 1.0
---

# Bible Vault Settings

Configure your reading experience and sidebar preferences.

## Display Preferences

### Layer Settings

```dataviewjs
// Layer toggle controls
const settings = {
    layer1: true,  // Clean reading (always on)
    layer2: false, // Entity highlights
    layer3: false  // Auto-expand details
};

// Save to localStorage
dv.el("button", "Toggle Layer 2", {
    onclick: () => {
        document.body.classList.toggle('layer-2-enabled');
        settings.layer2 = !settings.layer2;
        localStorage.setItem('bibleVaultSettings', JSON.stringify(settings));
    }
});
```

**Layer 1 (Reading)**: Clean text, minimal distractions
**Layer 2 (Highlighting)**: Show entity markers and highlights
**Layer 3 (Details)**: Auto-expand detailed information

### Translation Selection

**Default Translation**:
- [ ] KJV (King James Version)
- [ ] ESV (English Standard Version)
- [ ] NIV (New International Version)
- [ ] NASB (New American Standard Bible)
- [ ] NKJV (New King James Version)

*Note: Multiple translations coming soon!*

## Sidebar Configuration

### Left Sidebar Sections

Choose what appears in the left sidebar (structured data):

Priority | Section | Visible
---|---|---
1 | People | ✓
2 | Places | ✓
3 | Timeline | ✓
4 | Events | ✓
5 | Cross References | ✓

Drag to reorder, uncheck to hide.

### Right Sidebar Sections

Choose what appears in the right sidebar (custom/AI):

Priority | Section | Visible
---|---|---
1 | Personal Notes | ✓
2 | AI Insights | ✓
3 | Commentary | ✓
4 | Questions | ✓
5 | Application | ✓

### Sidebar Layout

**Width**:
- [ ] Narrow (200px)
- [x] Medium (250px)
- [ ] Wide (300px)

**Behavior**:
- [x] Sticky (follows scroll)
- [ ] Static (scrolls with page)
- [ ] Collapsible (can be hidden)

## Entity Highlighting

Configure which entity types are highlighted in Layer 2:

Entity Type | Color | Show
---|---|---
People | Blue | ✓
Places | Green | ✓
Events | Orange | ✓
Topics | Yellow | ✓
Lexicon | Purple | ✓

## Zoom Mode Preferences

When clicking into a verse for deep study:

- [x] Show all relationships
- [x] Display lexicon entries
- [x] Include cross-references
- [x] Show parallel translations
- [ ] Display commentary
- [ ] Show discussion threads (future)

## Data Query Preferences

### Entity Display

**Maximum entities shown per verse**: 5

**Sort entities by**:
- [x] Importance/relevance
- [ ] Alphabetical
- [ ] Type (people, places, etc.)

### Topic Display

**Maximum topics shown per verse**: 3

**Filter topics by category**:
- [x] Theological
- [x] Historical
- [x] Prophetic
- [ ] Cultural
- [ ] Geographical

### Lexicon Display

**Show Strong's numbers**: ✓
**Include transliteration**: ✓
**Show pronunciation**: ✓
**Definition length**:
- [ ] Brief (50 chars)
- [x] Medium (150 chars)
- [ ] Full

## Performance Settings

**Lazy load verse details**: ✓
**Cache entity queries**: ✓
**Preload adjacent chapters**: ✓

**Query timeout**: 5000ms

## Future Features (Coming Soon)

### Community Integration

- [ ] Enable forum discussions per verse
- [ ] Show community commentary
- [ ] Display upvoted insights
- [ ] Reputation system for contributors

### Advanced Features

- [ ] Custom highlighting colors
- [ ] Personal verse collections
- [ ] Study plans
- [ ] Reading schedules
- [ ] Export to PDF/Word
- [ ] Audio narration

### Collaboration

- [ ] Shared notes with friends
- [ ] Group study mode
- [ ] Comment on shared insights

---

## Apply Settings

Click **Save** to apply your preferences. Settings are stored locally in your vault.

```dataviewjs
dv.el("button", "Save Settings", {
    cls: "save-settings-btn",
    onclick: () => {
        // Save all settings to localStorage
        new Notice("Settings saved!");
    }
});

dv.el("button", "Reset to Defaults", {
    cls: "reset-settings-btn",
    onclick: () => {
        if (confirm("Reset all settings to defaults?")) {
            localStorage.removeItem('bibleVaultSettings');
            new Notice("Settings reset!");
        }
    }
});
```

---

**Last modified**: `= this.file.mtime`
