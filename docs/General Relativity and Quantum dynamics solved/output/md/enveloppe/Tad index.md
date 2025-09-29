---
category: theophysics-research
date: '2025-09-28'
publish_to:
  production: false
  research: true
  template: false
status: draft
tags:
- o
- theophysics
- enveloppe
title: "TABLE rowsfilelink AS Files\nFROM \nFLATTEN filetags AS tag\nGR..."
---
   
TABLE rows.file.link AS "Files"   
FROM ""   
FLATTEN file.tags AS tag   
GROUP BY tag   
SORT tag ASC