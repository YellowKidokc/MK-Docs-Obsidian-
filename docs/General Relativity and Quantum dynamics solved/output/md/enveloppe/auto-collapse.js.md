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
title: "appworkspaceonfile-open   \n    appcommandsexecuteCommandById..."
---
   
app.workspace.on('file-open', () => {   
    app.commands.executeCommandById("editor.foldAll");   
});   
   
app.workspace.on('workspace-leave', () => {   
    app.commands.executeCommandById("editor.foldAll");   
});