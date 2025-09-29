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
title: Never Too Many Callouts?
---
   
# Never Too Many Callouts?   
   
> [!task]- Task, Checkmark, Checkbox, Checkcircle   
> Contents   
   
> [!read]- Read, Book, Lecture   
> Contents   
   
> [!show]- Watch, TV, Show, Serie   
> Contents   
   
> [!music]- Listen, Music, Lyrics, Song, Songs   
> Contents   
   
> [!doing]- Doing, Heartbeat, Activity   
> Contents   
   
> [!reading]- Reading   
> Contents   
   
> [!watching]- Watching, Netflix, Chill   
> Contents   
   
> [!listening]- Listening   
> Contents   
   
> [!date]- Date, Meeting, Calendar   
> Contents   
   
   
   
It _adds gradient colors_ to all of the vault. I actually stripped this from [Royal Velvet Theme](https://github.com/caro401/royal-velvet). And **_I’m not a pro at CSS_**, so it might conflict with the theme you are using.   
   
You don't need to add the CSSclasses property for this to work.   
   
## Example:   
   
   
- The colors in this vault are all **achieved with the help of this CSS**   
   
## Source   
   
   
- [caro401/royal-velvet: A dark theme for obsidian.md (github.com)](https://github.com/caro401/royal-velvet)   
   
## Code   
   
```

/* @settings

name: Royal Velvet
id: royal-velvet
settings:
  -
    id: inline-document-title-color
    title: Inline Document Title Color
    description: Change the color of the inline document title to match another heading or a custom hue.
    type: class-select
    allowEmpty: false
    default: doc-title-h1
    options:
      -
        label: Disabled
        value: doc-title-disable
      -
        label: Accent Color (hue)
        value: doc-title-accent
      -
        label: Rainbow
        value: doc-title-rainbow
      -
        label: Heading 1
        value: doc-title-h1
      -
        label: Heading 2
        value: doc-title-h2
      -
        label: Heading 3
        value: doc-title-h3
      -
        label: Heading 4
        value: doc-title-h4
      -
        label: Heading 5
        value: doc-title-h5
      -
        label: Heading 6
        value: doc-title-h6
*/

/*Fonts*/

@import url("https://fonts.googleapis.com/css2?family=Fira+Code&family=Fira+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap");

:root {
  --default-font: "Fira Sans", "Inter", sans-serif; /*Note and Settings Text*/
  --font-monospace: "Fira Code", "Source Code Pro", monospace; /*Code block text*/
}

body {
  --font-monospace-theme: "Fira Code", "Source Code Pro", monospace; /*Code block text*/
}

/*Dark Theme Variables*/
.theme-dark {
  --layer-0: hsl(var(--layer-hue-sat), 9%);
  --layer-1: hsl(var(--layer-hue-sat), 13%);
  --layer-2: hsl(var(--layer-hue-sat), 15%);
  --layer-3: hsl(var(--layer-hue-sat), 19%);
  --layer-4: hsl(var(--layer-hue-sat), 30%);
  --on-layer-tuple: 60, 30%, 96%;

  --red-hue: 10;
  --orange-hue: 35;
  --yellow-hue: 60;
  --green-hue: 115;
  --blue-hue: 170;
  --purple-hue: 250;
  --purple-pink-hue: 285;
  --pink-hue: 330;

  --primary-sat: 100%;
  --secondary-sat: 100%;

  --primary-lit: 75.1%;
  --secondary-lit: 90%;

}
/*Light Theme Variables*/
.theme-light {
  --layer-0: hsl(var(--layer-hue-sat), 89%);
  --layer-1: hsl(var(--layer-hue-sat), 99%);
  --layer-2: hsl(var(--layer-hue-sat), 96%);
  --layer-3: hsl(var(--layer-hue-sat), 83%);
  --layer-4: hsl(var(--layer-hue-sat), 80%);
  --on-layer-tuple: 234, 14%, 15%;

  --red-hue: 0;
  --orange-hue: 30;
  --yellow-hue: 40;
  --green-hue: 105;
  --blue-hue: 200;
  --purple-hue: 300;
  --purple-pink-hue: 310;
  --pink-hue: 330;

  --primary-sat: 100%;
  --secondary-sat: 80%;

  --primary-lit: 43%;
  --secondary-lit: 50%;
}

/*Common Variables*/
.theme-dark,
.theme-light {
  --layer-hue-sat: 235, 15%;

  --on-layer: hsl(var(--on-layer-tuple));
  --on-layer-600: hsla(var(--on-layer-tuple), 0.6);
  --on-layer-400: hsla(var(--on-layer-tuple), 0.4);

  /* red */
  --red-tuple: var(--red-hue), var(--primary-sat), var(--primary-lit);
  --red: hsl(var(--red-tuple));
  --red-900: hsla(var(--red-tuple), 0.9);

  --red-secondary-tuple: var(--red-hue), var(--secondary-sat), var(--secondary-lit);

  /* orange */
  --orange-tuple: var(--orange-hue), var(--primary-sat), var(--primary-lit);
  --orange: hsl(var(--orange-tuple));
  --orange-100: hsla(var(--orange-tuple), 0.1);

  --orange-secondary-tuple: var(--orange-hue), var(--secondary-sat), var(--secondary-lit);
  --orangeSecondary: hsl(var(--orange-secondary-tuple));

  /* yellow */
  --yellow-tuple: var(--yellow-hue), var(--primary-sat), var(--primary-lit);
  --yellow: hsl(var(--yellow-tuple));
  --yellow-100: hsla(var(--yellow-tuple), 0.1);
  --yellow-700: hsla(var(--yellow-tuple), 0.7);

  --yellow-secondary-tuple: var(--yellow-hue), var(--secondary-sat), var(--secondary-lit);

  /* green */
  --green-tuple: var(--green-hue), var(--primary-sat), var(--primary-lit);
  --green: hsl(var(--green-tuple));
  --green-200: hsla(var(--green-tuple), 0.2);

  --green-secondary-tuple: var(--green-hue), var(--secondary-sat), var(--secondary-lit);
  --greenSecondary: hsl(var(--green-secondary-tuple));

  /* blue */
  --blue-tuple: var(--blue-hue), var(--primary-sat), var(--primary-lit);
  --blue: hsl(var(--blue-tuple));
  --blue-600: hsla(var(--blue-tuple), 0.6);

  --blue-secondary-tuple: var(--blue-hue), var(--secondary-sat), var(--secondary-lit);

  /* purple */
  --purple-tuple: var(--purple-hue), var(--primary-sat), var(--primary-lit);
  --purple: hsl(var(--purple-tuple));
  --purple-200: hsla(var(--purple-tuple), 0.2);

  --purple-secondary-tuple: var(--purple-hue), var(--secondary-sat), var(--secondary-lit);

  /* purple-pink */
  --purple-pink-tuple: var(--purple-pink-hue), var(--primary-sat), var(--primary-lit);
  --purple-pink: hsl(var(--purple-pink-tuple));

  --purple-pink-secondary-tuple: var(--purple-pink-hue), var(--secondary-sat), var(--secondary-lit);

  /* pink */
  --pink-tuple: var(--pink-hue), var(--primary-sat), var(--primary-lit);
  --pink: hsl(var(--pink-tuple));
  --pink-100: hsla(var(--pink-tuple), 0.1);
  --pink-300: hsla(var(--pink-tuple), 0.3);
  --pink-400: hsla(var(--pink-tuple), 0.4);

  --pink-secondary-tuple: var(--pink-hue), var(--secondary-sat), var(--secondary-lit);
  --pinkSecondary: hsl(var(--pink-secondary-tuple));

  --gradientDegree: 135deg;

  --background-modifier-cover: var(--layer-0); /*Obsidian Title Bar Bg*/
  --background-primary: var(--layer-2); /*Note background*/
  --background-primary-alt: var(--layer-1); /*Note Title background active*/
  --background-secondary: var(--layer-1); /*Sidebar background*/
  --background-secondary-alt: var(--layer-0); /*Sidebar Title background*/

  --background-modifier-border: var(--layer-1); /*Border outline of quotes, tables, line breaks*/
  --background-modifier-form-field: var(--pink-100);
  --background-modifier-form-field-highlighted: var(--pink-300);
  --background-modifier-box-shadow: var(--layer-3);
  --background-modifier-success: var(--green-200);
  --background-modifier-error: var(--red-900);
  --background-modifier-error-rgb: 61, 0, 0;
  --background-modifier-error-hover: var(--red);

  --text-normal: var(--on-layer); /*Text body of note*/
  --text-muted: var(
    --on-layer-600
  ); /*Text darker for sidebar, toggles, inactive, tags, etc*/
  --text-accent: var(--pink); /*Links*/
  --text-accent-hover: var(--pinkSecondary); /*Links hover*/
  --text-faint: var(--on-layer-600); /*Link brackets color & Gutter Numbers*/
  --text-error: var(--red);
  --text-error-hover: var(--redSecondary);

  --text-highlight-bg: var(--yellow-100); /*Search Matches*/
  --text-highlight-bg-active: var(--orange-100); /*Active Search Match (Preview Mode)*/
  --text-selection: var(--purple-200); /*Text Selections*/

  /* other custom vars */
  --indentation-guide-opacity: 10%;

  /* --Obsidian Variables-- */
  --interactive-normal: var(--layer-1); /*Button Color*/
  --interactive-hover: var(--layer-0); /*Button Hovered Color*/
  --interactive-accent: var(--pink); /*Workspace Note Title Underline*/
  --interactive-accent-hover: var(--orange); /*Menu Button Hover*/
  --interactive-success: var(--green);

  --scrollbar-bg: var(--layer-2); /*Scrollbar Gutter Background*/
  --scrollbar-thumb-bg: var(--pink-100); /*Scrollbar Color*/
  --scrollbar-active-thumb-bg: var(--pink-300); /*Scrollbar Dragged Color*/
  --indentation-guide: var(--layer-4);

  --blockquote-border: var(--red);
  --link-color: var(--orange); /* internal link */
  --link-color-hover: var(--orangeSecondary);
  --link-unresolved-color: var(--yellow-700);
  --link-unresolved-hover: var(--yellow);
  --link-external-color: var(--green);
  --link-external-color-hover: var(--greenSecondary);
  --table-header-color: var(--layer-2);
  --text-on-accent: var(--layer-2);

  --background-modifier-border-hover: transparent;
  --modal-border-color: transparent;
  --prompt-border-color: transparent;
  --background-modifier-border-focus: transparent; /* border around active input boxes */
  --background-modifier-border: transparent; /* separator lines in eg. setting menu */
  --input-shadow: none;
  --blockquote-border-color: none;
  --ribbon-background: var(--background-secondary-alt);
  --ribbon-background-collapsed: var(--background-secondary-alt);
  --code-normal: var(--purple-pink);
  --code-size: 100%;

  --hr-color: var(--orange); /* Horizontal Line */
}

/*Setting Dropdown*/
.theme-dark .dropdown {
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%22292.4%22%20height=%22292.4%22%3E%3Cpath%20d=%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%20fill=%22hsl(60,%2030%25,%2096.1%25)%22/%3E%3C/svg%3E");
}
.theme-light .dropdown {
  background-image: url("data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20width=%22292.4%22%20height=%22292.4%22%3E%3Cpath%20d=%22M287%2069.4a17.6%2017.6%200%200%200-13-5.4H18.4c-5%200-9.3%201.8-12.9%205.4A17.6%2017.6%200%200%200%200%2082.2c0%205%201.8%209.3%205.4%2012.9l128%20127.9c3.6%203.6%207.8%205.4%2012.8%205.4s9.2-1.8%2012.8-5.4L287%2095c3.5-3.5%205.4-7.8%205.4-12.8%200-5-1.9-9.2-5.5-12.8z%22%20fill=%22hsl(234,%2014%25,%2015%25)%22/%3E%3C/svg%3E");
}
.dropdown {
  font-family: var(--default-font);
}

.menu-item-icon {
  color: var(--green);
}



/*--Workspace: Notes--*/
/*Note Title Bar*/
.workspace-leaf .view-header {
  border-bottom: 5px solid var(--layer-2);
}

.view-header-title {
  color: var(--pinkSecondary);
}

.workspace-split.mod-root
  > .workspace-leaf:first-of-type:last-of-type
  .view-header,
.view-header {
  border-bottom: 5px solid var(--layer-2);
}
/*Active Note Titlebar*/
/*Note Title Bar: Text*/
.workspace-leaf.mod-active .view-header-title {
  color: var(--pink);
}

/*--Emphasis--*/
strong,
.cm-s-obsidian .cm-strong,
.cm-s-obsidian .cm-quote.cm-strong {
  color: var(--pink);
}

em,
.cm-s-obsidian .cm-em,
.cm-s-obsidian .cm-quote.cm-em {
  color: var(--blue);
}

.cm-em.cm-strong,
strong > em {
  color: var(--red);
}

/*Highlight*/
.markdown-preview-view mark,
.cm-s-obsidian .cm-highlight,
.cm-s-obsidian .cm-highlight.cm-quote,
.cm-s-obsidian .cm-formatting-highlight {
  color: var(--yellow);
  font-weight: 500;
}

.cm-strikethrough,
del {
  color: var(--on-layer-400);
}

/*--Headers/Headings--*/
body:not(.doc-title-disable) .inline-title {
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
}

body.doc-title-accent .inline-title {
  background-image: linear-gradient(
    var(--gradientDegree),
    hsl(calc(var(--accent-h) + 30), var(--primary-sat), var(--primary-lit)) 0,
    hsl(calc(var(--accent-h) - 30), var(--primary-sat), var(--primary-lit)) 100%
  );
}

body.doc-title-rainbow .inline-title {
  background-image: linear-gradient(
    var(--gradientDegree),
    var(--pink) 0,
    var(--orange) 8.33%,
    var(--yellow) 16.66%,
    var(--green) 25%,
    var(--blue) 33.33%,
    var(--purple) 41.66%,
    var(--pink) 50%,
    var(--orange) 58.33%,
    var(--yellow) 66.66%,
    var(--green) 75%,
    var(--blue) 83.33%,
    var(--purple) 91.66%,
    var(--pink) 100%
  );
}

h1,
.cm-header-1,
body.doc-title-h1 .inline-title,
body:not([class*="doc-title"]) .inline-title {
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  background-image: linear-gradient(
    var(--gradientDegree),
    var(--pink) 0,
    var(--orange) 100%
  );
} /*Source Mode*/

h2,
.cm-header-2,
body.doc-title-h2 .inline-title {
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  background-image: linear-gradient(
    var(--gradientDegree),
    var(--orange) 0,
    var(--yellow) 100%
  );
} /*Source Mode*/

h3,
.cm-header-3,
body.doc-title-h3 .inline-title {
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  background-image: linear-gradient(
    var(--gradientDegree),
    var(--yellow) 0,
    var(--green) 100%
  );
} /*Source Mode*/

h4,
.cm-header-4,
body.doc-title-h4 .inline-title {
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  background-image: linear-gradient(
    var(--gradientDegree),
    var(--green) 0,
    var(--blue) 100%
  );
} /*Source Mode*/

h5,
.cm-header-5,
body.doc-title-h5 .inline-title {
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  background-image: linear-gradient(
    var(--gradientDegree),
    var(--blue) 0,
    var(--purple) 100%
  );
} /*Source Mode*/

h6,
.cm-header-6,
body.doc-title-h6 .inline-title {
  -webkit-text-fill-color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  background-image: linear-gradient(
    var(--gradientDegree),
    var(--purple) 0,
    var(--pink) 100%
  );
} /*Source Mode*/


```
   
   
   
   
   
   
Styles the divider in your notes   
   
## Example:   
   
![10529.png](app://ffcc6168e0897c134529286867512b4cdc73/O:/CSS%20Snippets%20Vault/Attachments/10529.png?1750907582411)   
   
## Source   
   
   
- [https://forum.obsidian.md/t/creating-fancy-horizontal-rule-lines/63700](https://forum.obsidian.md/t/creating-fancy-horizontal-rule-lines/63700)   
   
## Code   
   
```css
body {
    --hr-line-offset: 25%;
    --hr-color: lightsalmon;
}

:root hr {
    border-image-slice: 1;
    border-image-source: linear-gradient(
        to right,
        transparent,
        var(--hr-color) calc(50% - var(--hr-line-offset)),
        var(--hr-color) calc(50% + var(--hr-line-offset)),
        transparent
    );
}
```
   
   
   
   
   
## What this does?   
   
Love the cards style of minimal them with dataview query. This CSS will help you get those with any theme. Just add this CSS to your vault.   
   
You need to add the CSSclasses property for this to work.   
   
## Example:   
   
   
- [All CSS Snippets](app://obsidian.md/All%20CSS%20Snippets): This page itself is using cards CSS   
   
## Source   
   
   
- [Reddit - Dive into anything](https://www.reddit.com/r/ObsidianMD/comments/rw5jw1/minimal_44_cards_layout/)   
   
## Code   
   
```/*
Cards snippet for Obsidian
author: @kepano
version: 2.0.0
Support my work:
https://github.com/sponsors/kepano
*/
:root {
  --cards-min-width: 180px;
  --cards-max-width: 1fr;
  --cards-mobile-width: 120px;
  --cards-image-height: 400px;
  --cards-padding: 1.2em;
  --cards-image-fit: contain;
  --cards-background: transparent;
  --cards-border-width: 1px;
  --cards-aspect-ratio: auto;
  --cards-columns: repeat(auto-fit, minmax(var(--cards-min-width), var(--cards-max-width))); }

@media (max-width: 400pt) {
  :root {
    --cards-min-width:var(--cards-mobile-width); } }
.cards.table-100 table.dataview tbody,
.table-100 .cards table.dataview tbody {
  padding: 0.25rem 0.75rem; }

.cards table.dataview tbody {
  clear: both;
  padding: 0.5rem 0;
  display: grid;
  grid-template-columns: var(--cards-columns);
  grid-column-gap: 0.75rem;
  grid-row-gap: 0.75rem; }
.cards table.dataview > tbody > tr {
  background-color: var(--cards-background);
  border: var(--cards-border-width) solid var(--background-modifier-border);
  display: flex;
  flex-direction: column;
  margin: 0;
  padding: 0 0 calc(var(--cards-padding)/3) 0;
  border-radius: 6px;
  overflow: hidden;
  transition: box-shadow 0.15s linear;
  max-width: var(--cards-max-width); }
.cards table.dataview > tbody > tr:hover {
  border: var(--cards-border-width) solid var(--background-modifier-border-hover);
  box-shadow: 0 4px 6px 0px rgba(0, 0, 0, 0.05), 0 1px 3px 1px rgba(0, 0, 0, 0.025);
  transition: box-shadow 0.15s linear; }
.cards table.dataview tbody > tr > td {
  /* Paragraphs */
  /* Links */
  /* Buttons */
  /* Lists */
  /* Images */ }
  .cards table.dataview tbody > tr > td:first-child {
    font-weight: var(--bold-weight); }
  .cards table.dataview tbody > tr > td:first-child a {
    padding: 0 0 calc(var(--cards-padding)/3);
    display: block; }
  .cards table.dataview tbody > tr > td:not(:first-child) {
    font-size: 90%;
    color: var(--text-muted); }
  .cards table.dataview tbody > tr > td .el-p {
    display: block;
    width: 100%; }
  .cards table.dataview tbody > tr > td > *:not(.el-embed-image) {
    padding: calc(var(--cards-padding)/3) 0; }
  .cards table.dataview tbody > tr > td:not(:last-child):not(:first-child) > .el-p:not(.el-embed-image) {
    border-bottom: 1px solid var(--background-modifier-border);
    width: 100%; }
  .cards table.dataview tbody > tr > td a {
    text-decoration: none; }
  .cards table.dataview tbody > tr > td > button {
    width: 100%;
    margin: calc(var(--cards-padding)/2) 0; }
  .cards table.dataview tbody > tr > td:last-child > button {
    margin-bottom: calc(var(--cards-padding)/6); }
  .cards table.dataview tbody > tr > td > ul {
    width: 100%;
    padding: 0.25em 0 !important;
    margin: 0 auto !important; }
  .cards table.dataview tbody > tr > td:not(:last-child) > ul {
    border-bottom: 1px solid var(--background-modifier-border); }
  .cards table.dataview tbody > tr > td .el-embed-image {
    background-color: var(--background-secondary);
    display: block;
    margin: 0 calc(var(--cards-padding)/-2) 0 calc(var(--cards-padding)/-2);
    width: calc(100% + var(--cards-padding)); }
  .cards table.dataview tbody > tr > td img {
    aspect-ratio: var(--cards-aspect-ratio);
    width: 100%;
    object-fit: var(--cards-image-fit);
    max-height: var(--cards-image-height);
    background-color: var(--background-secondary);
    vertical-align: bottom; }

.markdown-source-view.mod-cm6.cards .dataview.table-view-table > tbody > tr > td,
.trim-cols .cards table.dataview tbody > tr > td {
  white-space: normal; }

.cards .dataview.table-view-table > tbody > tr > td,
.cards table.dataview tbody > tr > td,
.markdown-source-view.mod-cm6.cards .dataview.table-view-table > tbody > tr > td,
.markdown-source-view.mod-cm6.cards table.dataview tbody > tr > td {
  border-bottom: none;
  padding: 0 !important;
  line-height: 1.2;
  width: calc(100% - var(--cards-padding));
  margin: 0 auto;
  overflow: visible !important;
  max-width: 100%;
  display: flex; }

.links-int-on .cards table.dataview tbody > tr > td a {
  text-decoration: none; }

/* Block button */
.markdown-source-view.mod-cm6.cards .edit-block-button {
  top: 0px; }

/* ------------------- */
/* Sorting menu */
.cards.table-100 table.dataview thead > tr,
.table-100 .cards table.dataview thead > tr {
  right: 0.75rem; }

.table-100 .cards table.dataview thead:before,
.cards.table-100 table.dataview thead:before {
  margin-right: 0.75rem; }

.theme-light .cards table.dataview thead:before {
  background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 100 100"><path fill="black" d="M49.792 33.125l-5.892 5.892L33.333 28.45V83.333H25V28.45L14.438 39.017L8.542 33.125L29.167 12.5l20.625 20.625zm41.667 33.75L70.833 87.5l-20.625 -20.625l5.892 -5.892l10.571 10.567L66.667 16.667h8.333v54.883l10.567 -10.567l5.892 5.892z"></path></svg>'); }

.cards .el-pre + .el-lang-dataview .table-view-thead {
  padding-top: 8px; }
.cards table.dataview thead {
  user-select: none;
  width: 180px;
  display: block;
  float: right;
  position: relative;
  text-align: right;
  height: 24px;
  padding-bottom: 4px; }
.cards table.dataview thead:hover:before {
  opacity: 0.5;
  background-color: var(--background-modifier-hover); }
.cards table.dataview thead:before {
  content: '';
  position: absolute;
  right: 0;
  top: 0;
  width: 10px;
  height: 16px;
  background-repeat: no-repeat;
  cursor: var(--cursor);
  text-align: right;
  padding: var(--size-4-1) var(--size-4-2);
  margin-bottom: 2px;
  border-radius: var(--radius-s);
  font-weight: 500;
  font-size: var(--font-adaptive-small);
  opacity: 0.25;
  background-position: center center;
  background-size: 16px;
  background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 100 100"><path fill="white" d="M49.792 33.125l-5.892 5.892L33.333 28.45V83.333H25V28.45L14.438 39.017L8.542 33.125L29.167 12.5l20.625 20.625zm41.667 33.75L70.833 87.5l-20.625 -20.625l5.892 -5.892l10.571 10.567L66.667 16.667h8.333v54.883l10.567 -10.567l5.892 5.892z"></path></svg>'); }
.cards table.dataview thead > tr {
  top: -1px;
  position: absolute;
  display: none;
  z-index: 9;
  border: 1px solid var(--background-modifier-border-hover);
  background-color: var(--background-secondary);
  box-shadow: var(--shadow-s);
  padding: 6px;
  border-radius: var(--radius-m);
  flex-direction: column;
  margin: 26px 0 0 0;
  width: 100%; }
.cards table.dataview thead:hover > tr {
  display: flex; }
.cards table.dataview thead > tr > th {
  display: block;
  padding: 3px 30px 3px 6px !important;
  border-radius: var(--radius-s);
  width: 100%;
  font-weight: 400;
  color: var(--text-normal);
  cursor: var(--cursor);
  border: none;
  font-size: var(--font-ui-small); }
.cards table.dataview thead > tr > th[sortable-style="sortable-asc"],
.cards table.dataview thead > tr > th[sortable-style="sortable-desc"] {
  color: var(--text-normal); }
.cards table.dataview thead > tr > th:hover {
  color: var(--text-normal);
  background-color: var(--background-modifier-hover); }

/* ------------------- */
/* Helper classes */
.cards.cards-16-9 {
  --cards-aspect-ratio: 16/9; }
.cards.cards-1-1 {
  --cards-aspect-ratio: 1/1; }
.cards.cards-2-1 {
  --cards-aspect-ratio: 2/1; }
.cards.cards-2-3 {
  --cards-aspect-ratio: 2/3; }
.cards.cards-cols-1 {
  --cards-columns: repeat(1, minmax(0, 1fr)); }
.cards.cards-cols-2 {
  --cards-columns: repeat(2, minmax(0, 1fr)); }
.cards.cards-cover table.dataview tbody > tr > td img {
  object-fit: cover; }
.cards.cards-align-bottom table.dataview tbody > tr > td:last-child {
  align-items: flex-end;
  flex-grow: 1; }

@media (max-width: 400pt) {
  .cards table.dataview tbody > tr > td:not(:first-child) {
    font-size: 80%; } }
@media (min-width: 400pt) {
  .cards-cols-3 {
    --cards-columns: repeat(3, minmax(0, 1fr)); }

  .cards-cols-4 {
    --cards-columns: repeat(4, minmax(0, 1fr)); }

  .cards-cols-5 {
    --cards-columns: repeat(5, minmax(0, 1fr)); }

  .cards-cols-6 {
    --cards-columns: repeat(6, minmax(0, 1fr)); }

  .cards-cols-7 {
    --cards-columns: repeat(7, minmax(0, 1fr)); }

  .cards-cols-8 {
    --cards-columns: repeat(8, minmax(0, 1fr)); } }
```
   
   
   
## What this does?   
   
Displays the callout as a sidenote   
   
## Example:   
   
![89388.png](app://ffcc6168e0897c134529286867512b4cdc73/O:/CSS%20Snippets%20Vault/Attachments/89388.png?1750907582310)   
   
### Implementation like this:   
   
Bug   
   
your text here   
   
Bug   
   
your text here   
   
## Source   
   
   
- [https://discord.com/channels/686053708261228577/702656734631821413/1155147566615367680](https://discord.com/channels/686053708261228577/702656734631821413/1155147566615367680)   
   
## Code   
   
```css
/*
author: sailKite
source: https://discord.com/channels/686053708261228577/702656734631821413/1155147566615367680
*/

/* aside functionality as a custom callout */
:is(.markdown-source-view .cm-callout, div:not([class])):has(
    > .callout[data-callout-metadata*="aside"]
  ) {
  position: relative;
  overflow: visible;
  contain: none !important;
}
.callout[data-callout-metadata*="aside"] {
  --aside-width: 200px;
  --aside-offset: var(--size-4-4);
  position: absolute;
}
.callout[data-callout-metadata*="aside-l"] {
  left: calc(-1 * (var(--aside-width) + var(--aside-offset)));
  right: calc(100% + var(--aside-offset));
}
.callout[data-callout-metadata*="aside-r"] {
  left: calc(100% + var(--aside-offset));
  right: calc(-1 * (var(--aside-width) + var(--aside-offset)));
}
@media (hover: hover) {
  .markdown-source-view.mod-cm6
    .cm-embed-block:has(> div > [data-callout-metadata*="aside"]):hover {
    overflow: visible;
  }
}
```
   
   
   
## What this does?   
   
Creates a tab like view by creating callouts and subcallouts.   
   
Implementation like this. **Will only work when the CSS enabled**   
   
Tabbed   
   
Firstl   
   
> Lorem, ipsum dolor sit amet consectetur, adipisicing elit. (First)     
> [Internal Link](app://obsidian.md/Obsidian%20CSS) > > **bold** _italic_   
   
Second   
   
> Lorem, ipsum dolor sit amet consectetur, adipisicing elit. (Second)     
> [External Link](https://google.com/) > >    
   
Thirdl   
   
> Lorem, ipsum dolor sit amet consectetur, adipisicing elit. (Third)   
>    
> - bullet item   
> - [ ] checkbox   
> - [x] [#tag](app://obsidian.md/index.html#tag)   
   
## Example:   
   
   
- ![](https://camo.githubusercontent.com/2f37d3b8068c1b5c1eb15506b200a44f2b14b11706e11b1c6cc26206f05d4c26/68747470733a2f2f692e696d6775722e636f6d2f616936783848612e676966)   
   
## Source   
   
   
- [https://discord.com/channels/686053708261228577/702656734631821413/1092995965583114341](https://discord.com/channels/686053708261228577/702656734631821413/1092995965583114341)   
   
## Code   
   
```css
/*
author: FireIsGood
source: https://discord.com/channels/686053708261228577/702656734631821413/1092995965583114341
*/

[data-callout="tabbed"] {
  outline: 1px solid var(--color-base-30);
  border-radius: 0.5rem;
}
[data-callout="tabbed"] > .callout-content {
  padding: 0.25rem;

  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(5rem, max-content));
  gap: 0 1rem;
}
[data-callout="tabbed"] > .callout-title {
  display: none;
}
[data-callout="tabbed"] > .callout-content p {
  margin: 0;
}
[data-callout="tabbed"] > .callout-content label > input {
  display: none;
}
[data-callout="tabbed"] > .callout-content label {
  width: 100%;
  display: inline-block;
  padding: 0.15rem 0.75ch;
  border-radius: 1rem;

  color: #ccc;
  background-color: #2e7d32;

  text-align: center;
  font-weight: bold;
  font-size: 1.15rem;
  cursor: pointer;
}
[data-callout="tabbed"] > .callout-content label:has(input:checked) {
  color: white;
  background-color: #8bc34a;
}
[data-callout="tabbed"]
  > .callout-content
  p:not(:has(label input:checked))
  + blockquote {
  display: none;
}
[data-callout="tabbed"] > .callout-content > blockquote {
  order: 999;
  grid-column: 1 / -1;

  background-color: transparent;
  padding-left: 0;
  border: 0;
}
```
   
   
his custom CSS adds a custom background. You can change the wallpaper by changing the URL in the CSS.   
   
You don't need to add the CSSclasses property for this to work.   
   
## Example   
   
   
- [Kanban Background](app://obsidian.md/Live%20Examples/Kanban%20Background)     
    ![1281.png](app://ffcc6168e0897c134529286867512b4cdc73/O:/CSS%20Snippets%20Vault/Attachments/1281.png?1750907582303)   
   
## Source   
   
   
- [Add background to kanban plugin - Share & showcase - Obsidian Forum](https://forum.obsidian.md/t/add-background-to-kanban-plugin/47248)   
   
## Code:   
   
```
.theme-dark .view-content .kanban-plugin::after {
  content: "";
  position: fixed;
  background-image: url(http://m.gettywallpapers.com/wp-content/uploads/2021/05/4k-Wallpaper-Cool-2048x1152.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  filter: blur(1px) brightness(70%) saturate(100%);
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  z-index: -1;
}

.theme-light .view-content .kanban-plugin::after {
  content: "";
  position: fixed;
  background-image: url(http://m.gettywallpapers.com/wp-content/uploads/2021/05/4k-Wallpaper-Cool-2048x1152.jpg);
  background-repeat: no-repeat;
  background-size: cover;
  filter: blur(1px) brightness(70%) saturate(100%);
  left: 0;
  top: 0;
  right: 0;
  bottom: 0;
  z-index: -1;
}
```
   
   
   
I hear you it's cold hard it's a hard market but I'm trying yeah the cool thing didn't take long to resolve julie's only got Monday available and those things are really work on Monday because the bars not open in the restaurant they don't serve poolside kind of takes the fun out of the whole thing we got to work this sucks