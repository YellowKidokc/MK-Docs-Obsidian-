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
title: 'THEOPHYSICS Visual Knowledge System

  A quantum-spiritual desi...'
---
   
/*    
THEOPHYSICS Visual Knowledge System   
A quantum-spiritual design for David's research vault   
Combines Royal Velvet gradients with custom THEOPHYSICS elements   
*/   
   
/* ==========================================   
   THEOPHYSICS COLOR VARIABLES   
   ========================================== */   
   
:root {   
  /* Quantum-Spiritual Color Mapping */   
   
  --quantum-blue: hsl(220, 100%, 75%);   
  --spiritual-gold: hsl(45, 100%, 70%);   
  --bridge-purple: hsl(280, 100%, 75%);   
  --consciousness-white: hsl(0, 0%, 96%);   
  --entropy-red: hsl(10, 100%, 75%);   
  --grace-green: hsl(115, 100%, 75%);   
     
  /* Master Equation Component Colors */   
   
  --gravity-orange: hsl(35, 100%, 75%);   
  --motion-cyan: hsl(180, 100%, 75%);   
  --energy-yellow: hsl(60, 100%, 75%);   
  --time-silver: hsl(210, 20%, 80%);   
  --causality-violet: hsl(250, 100%, 75%);   
  --relativity-pink: hsl(330, 100%, 75%);   
  --forces-emerald: hsl(160, 100%, 75%);   
     
  /* Flow States */   
   
  --raw-capture: hsl(0, 50%, 70%);   
  --developing: hsl(60, 70%, 70%);   
  --crystallized: hsl(120, 70%, 70%);   
  --applied: hsl(240, 70%, 70%);   
}   
   
/* ==========================================   
   THEOPHYSICS CALLOUT SYSTEM   
   ========================================== */   
   
/* Master Equation Components */   
[data-callout="gravity"] .callout-icon { color: var(--gravity-orange); }   
[data-callout="motion"] .callout-icon { color: var(--motion-cyan); }   
[data-callout="energy"] .callout-icon { color: var(--energy-yellow); }   
[data-callout="entropy"] .callout-icon { color: var(--entropy-red); }   
[data-callout="time"] .callout-icon { color: var(--time-silver); }   
[data-callout="causality"] .callout-icon { color: var(--causality-violet); }   
[data-callout="relativity"] .callout-icon { color: var(--relativity-pink); }   
[data-callout="quantum"] .callout-icon { color: var(--quantum-blue); }   
[data-callout="forces"] .callout-icon { color: var(--forces-emerald); }   
[data-callout="consciousness"] .callout-icon { color: var(--consciousness-white); }   
   
/* Flow State Callouts */   
[data-callout="raw"] {   
  background: linear-gradient(135deg, var(--raw-capture), transparent);   
  border-left: 4px solid var(--raw-capture);   
}   
   
[data-callout="developing"] {   
  background: linear-gradient(135deg, var(--developing), transparent);   
  border-left: 4px solid var(--developing);   
}   
   
[data-callout="crystallized"] {   
  background: linear-gradient(135deg, var(--crystallized), transparent);   
  border-left: 4px solid var(--crystallized);   
}   
   
[data-callout="breakthrough"] {   
  background: linear-gradient(135deg, var(--quantum-blue), var(--spiritual-gold));   
  border: 2px solid var(--bridge-purple);   
  box-shadow: 0 0 20px rgba(280, 100%, 75%, 0.3);   
  animation: breakthrough-pulse 2s ease-in-out infinite;   
}   
   
@keyframes breakthrough-pulse {   
  0%, 100% { box-shadow: 0 0 20px rgba(280, 100%, 75%, 0.3); }   
  50% { box-shadow: 0 0 30px rgba(280, 100%, 75%, 0.6); }   
}   
   
/* Syzyxaia Moments - Special breakthrough styling */   
[data-callout="syzyxaia"] {   
  background: linear-gradient(45deg,    
    var(--quantum-blue) 0%,   
    var(--bridge-purple) 25%,   
    var(--spiritual-gold) 50%,   
    var(--bridge-purple) 75%,   
    var(--quantum-blue) 100%);   
  background-size: 400% 400%;   
  animation: syzyxaia-flow 4s ease-in-out infinite;   
  border: none;   
  color: white;   
  text-shadow: 1px 1px 2px rgba(0,0,0,0.7);   
}   
   
@keyframes syzyxaia-flow {   
  0%, 100% { background-position: 0% 50%; }   
  50% { background-position: 100% 50%; }   
}   
   
/* ==========================================   
   MASTER EQUATION DISPLAY   
   ========================================== */   
   
.master-equation {   
  font-family: 'Fira Code', monospace;   
  font-size: 1.5em;   
  text-align: center;   
  padding: 2em;   
  background: linear-gradient(135deg, var(--quantum-blue), var(--spiritual-gold));   
  border-radius: 15px;   
  margin: 2em 0;   
  color: white;   
  text-shadow: 2px 2px 4px rgba(0,0,0,0.5);   
}   
   
.equation-component {   
  display: inline-block;   
  margin: 0 0.2em;   
  padding: 0.3em 0.5em;   
  border-radius: 8px;   
  background: rgba(255,255,255,0.1);   
  transition: all 0.3s ease;   
  cursor: help;   
}   
   
.equation-component:hover {   
  background: rgba(255,255,255,0.3);   
  transform: scale(1.1);   
}   
   
/* ==========================================   
   THEOPHYSICS TABBED INTERFACE (Enhanced)   
   ========================================== */   
   
/* Enhanced Tabbed Callouts for THEOPHYSICS */   
[data-callout="tabbed"] {   
  outline: 2px solid var(--bridge-purple);   
  border-radius: 15px;   
  background: linear-gradient(135deg,    
    rgba(220, 100%, 75%, 0.05),    
    rgba(280, 100%, 75%, 0.05));   
  overflow: hidden;   
}   
   
[data-callout="tabbed"] > .callout-content {   
  padding: 0.5rem;   
  display: grid;   
  grid-template-columns: repeat(auto-fill, minmax(6rem, max-content));   
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
  padding: 0.5rem 1rem;   
  border-radius: 20px;   
  background: linear-gradient(135deg, var(--quantum-blue), var(--bridge-purple));   
  color: white;   
  text-align: center;   
  font-weight: bold;   
  font-size: 1rem;   
  cursor: pointer;   
  transition: all 0.3s ease;   
  border: 2px solid transparent;   
}   
   
[data-callout="tabbed"] > .callout-content label:hover {   
  background: linear-gradient(135deg, var(--spiritual-gold), var(--bridge-purple));   
  transform: translateY(-2px);   
  box-shadow: 0 4px 12px rgba(280, 100%, 75%, 0.3);   
}   
   
[data-callout="tabbed"] > .callout-content label:has(input:checked) {   
  background: linear-gradient(135deg, var(--spiritual-gold), var(--quantum-blue));   
  border-color: var(--consciousness-white);   
  box-shadow: 0 0 20px rgba(45, 100%, 70%, 0.6);   
  transform: translateY(-3px);   
}   
   
[data-callout="tabbed"] > .callout-content p:not(:has(label input:checked)) + blockquote {   
  display: none;   
}   
   
[data-callout="tabbed"] > .callout-content > blockquote {   
  order: 999;   
  grid-column: 1 / -1;   
  background: linear-gradient(135deg,    
    rgba(220, 100%, 75%, 0.03),    
    rgba(280, 100%, 75%, 0.03));   
  padding: 1.5rem;   
  border: 1px solid var(--bridge-purple);   
  border-radius: 10px;   
  margin-top: 1rem;   
  border-left: 4px solid var(--spiritual-gold);   
}   
   
/* ==========================================   
   PROPHECY MAPPING INTERFACE   
   ========================================== */   
   
.prophecy-card {   
  background: linear-gradient(135deg,    
    rgba(45, 100%, 70%, 0.1),    
    rgba(330, 100%, 75%, 0.1));   
  border: 1px solid var(--spiritual-gold);   
  border-radius: 10px;   
  padding: 1rem;   
  margin: 0.5rem 0;   
  transition: all 0.3s ease;   
}   
   
.prophecy-card:hover {   
  border-color: var(--bridge-purple);   
  box-shadow: 0 4px 12px rgba(280, 100%, 75%, 0.2);   
  transform: translateY(-2px);   
}   
   
.prophecy-reference {   
  color: var(--spiritual-gold);   
  font-weight: bold;   
  font-family: 'Fira Code', monospace;   
}   
   
.prophecy-status {   
  display: inline-block;   
  padding: 0.2em 0.8em;   
  border-radius: 20px;   
  font-size: 0.8em;   
  font-weight: bold;   
  text-transform: uppercase;   
}   
   
.prophecy-status.fulfilled {   
  background: var(--grace-green);   
  color: white;   
}   
   
.prophecy-status.future {   
  background: var(--quantum-blue);   
  color: white;   
}   
   
.prophecy-status.partial {   
  background: linear-gradient(90deg, var(--grace-green), var(--quantum-blue));   
  color: white;   
}   
   
/* ==========================================   
   THEOPHYSICS SIDENOTE SYSTEM   
   ========================================== */   
   
/* Claude Collaboration Sidenotes */   
:is(.markdown-source-view .cm-callout, div:not([class])):has(   
    > .callout[data-callout-metadata*="aside"]   
  ) {   
  position: relative;   
  overflow: visible;   
  contain: none !important;   
}   
   
.callout[data-callout-metadata*="aside"] {   
   
  --aside-width: 280px;   
  --aside-offset: var(--size-4-4);   
  position: absolute;   
  background: linear-gradient(135deg,    
    rgba(220, 100%, 75%, 0.1),    
    rgba(280, 100%, 75%, 0.1));   
  border: 2px solid var(--bridge-purple);   
  border-radius: 12px;   
  box-shadow: 0 8px 25px rgba(280, 100%, 75%, 0.2);   
  backdrop-filter: blur(10px);   
  z-index: 10;   
}   
   
.callout[data-callout-metadata*="aside-l"] {   
  left: calc(-1 * (var(--aside-width) + var(--aside-offset)));   
  right: calc(100% + var(--aside-offset));   
}   
   
.callout[data-callout-metadata*="aside-r"] {   
  left: calc(100% + var(--aside-offset));   
  right: calc(-1 * (var(--aside-width) + var(--aside-offset)));   
}   
   
/* Special styling for Claude insights */   
.callout[data-callout="claude"][data-callout-metadata*="aside"] {   
  background: linear-gradient(135deg,    
    rgba(220, 100%, 75%, 0.15),    
    rgba(280, 100%, 75%, 0.15));   
  border-color: var(--quantum-blue);   
}   
   
.callout[data-callout="claude"][data-callout-metadata*="aside"]::before {   
  content: "🤖";   
  position: absolute;   
  top: -10px;   
  right: -10px;   
  font-size: 1.5em;   
  background: var(--quantum-blue);   
  border-radius: 50%;   
  padding: 0.2em;   
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);   
}   
   
@media (hover: hover) {   
  .markdown-source-view.mod-cm6   
    .cm-embed-block:has(> div > [data-callout-metadata*="aside"]):hover {   
    overflow: visible;   
  }   
}   
   
[data-callout="insight"] {   
  background: radial-gradient(circle at top left,    
    var(--quantum-blue),    
    var(--spiritual-gold),    
    var(--bridge-purple));   
  color: white;   
  text-shadow: 1px 1px 2px rgba(0,0,0,0.7);   
  border-radius: 15px;   
  padding: 1.5rem;   
  margin: 1rem 0;   
}   
   
[data-callout="bridge"] {   
  background: linear-gradient(90deg,    
    var(--quantum-blue) 0%,    
    var(--bridge-purple) 50%,    
    var(--spiritual-gold) 100%);   
  border: none;   
  color: white;   
  text-shadow: 1px 1px 2px rgba(0,0,0,0.7);   
  position: relative;   
  overflow: hidden;   
}   
   
[data-callout="bridge"]::before {   
  content: "🌉";   
  position: absolute;   
  top: 0.5rem;   
  right: 0.5rem;   
  font-size: 1.5em;   
}   
   
/* ==========================================   
   CARDS LAYOUT FOR CONCEPTS   
   ========================================== */   
   
.theophysics-cards table.dataview tbody {   
  display: grid;   
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));   
  gap: 1rem;   
  padding: 1rem;   
}   
   
.theophysics-cards table.dataview tbody > tr {   
  background: linear-gradient(135deg,    
    rgba(220, 100%, 75%, 0.1),    
    rgba(280, 100%, 75%, 0.1));   
  border: 2px solid var(--bridge-purple);   
  border-radius: 15px;   
  padding: 1.5rem;   
  transition: all 0.3s ease;   
  position: relative;   
  overflow: hidden;   
}   
   
.theophysics-cards table.dataview tbody > tr:hover {   
  border-color: var(--spiritual-gold);   
  box-shadow: 0 8px 25px rgba(280, 100%, 75%, 0.3);   
  transform: translateY(-5px);   
}   
   
.theophysics-cards table.dataview tbody > tr::before {   
  content: "";   
  position: absolute;   
  top: 0;   
  left: 0;   
  right: 0;   
  height: 4px;   
  background: linear-gradient(90deg,    
    var(--quantum-blue),    
    var(--bridge-purple),    
    var(--spiritual-gold));   
}   
   
/* ==========================================   
   DASHBOARD STYLING   
   ========================================== */   
   
.theophysics-dashboard {   
  display: grid;   
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));   
  gap: 1.5rem;   
  margin: 2rem 0;   
}   
   
.dashboard-section {   
  background: linear-gradient(135deg,    
    rgba(220, 100%, 75%, 0.05),    
    rgba(280, 100%, 75%, 0.05));   
  border: 1px solid var(--bridge-purple);   
  border-radius: 15px;   
  padding: 1.5rem;   
  transition: all 0.3s ease;   
}   
   
.dashboard-section:hover {   
  border-color: var(--spiritual-gold);   
  box-shadow: 0 4px 15px rgba(45, 100%, 70%, 0.2);   
}   
   
.dashboard-section h3 {   
  background: linear-gradient(90deg, var(--quantum-blue), var(--spiritual-gold));   
   
  -webkit-background-clip: text;   
  -webkit-text-fill-color: transparent;   
  background-clip: text;   
  margin-bottom: 1rem;   
}   
   
/* ==========================================   
   STATUS INDICATORS   
   ========================================== */   
   
.status-badge {   
  display: inline-flex;   
  align-items: center;   
  padding: 0.3rem 0.8rem;   
  border-radius: 20px;   
  font-size: 0.8rem;   
  font-weight: bold;   
  margin: 0.2rem;   
}   
   
.status-badge.raw {   
  background: var(--raw-capture);   
  color: white;   
}   
   
.status-badge.developing {   
  background: var(--developing);   
  color: black;   
}   
   
.status-badge.crystallized {   
  background: var(--crystallized);   
  color: white;   
}   
   
.status-badge.breakthrough {   
  background: linear-gradient(90deg, var(--quantum-blue), var(--spiritual-gold));   
  color: white;   
  animation: badge-glow 2s ease-in-out infinite;   
}   
   
@keyframes badge-glow {   
  0%, 100% { box-shadow: 0 0 5px rgba(45, 100%, 70%, 0.5); }   
  50% { box-shadow: 0 0 15px rgba(45, 100%, 70%, 0.8); }   
}   
   
/* ==========================================   
   RESPONSIVE DESIGN   
   ========================================== */   
   
@media (max-width: 768px) {   
  .theophysics-dashboard {   
    grid-template-columns: 1fr;   
  }   
     
  .theophysics-cards table.dataview tbody {   
    grid-template-columns: 1fr;   
  }   
     
  .master-equation {   
    font-size: 1.2em;   
    padding: 1.5em;   
  }   
}   
   
/* ==========================================   
   THEOPHYSICS HEADING SYSTEM   
   ========================================== */   
   
/* Master Equation Component Indicators */   
:is(h1, h2, h3, h4, h5, h6,    
    .HyperMD-header-1, .HyperMD-header-2, .HyperMD-header-3,   
    .HyperMD-header-4, .HyperMD-header-5, .HyperMD-header-6)::before {   
  font-size: 0.8em;   
  margin-right: 0.5em;   
  opacity: 0.8;   
  font-weight: normal;   
}   
   
/* Component-specific icons */   
h1[data-component="gravity"]::before, .HyperMD-header-1[data-component="gravity"]::before { content: "🌍 G"; color: var(--gravity-orange); }   
h1[data-component="motion"]::before, .HyperMD-header-1[data-component="motion"]::before { content: "⚡ M"; color: var(--motion-cyan); }   
h1[data-component="energy"]::before, .HyperMD-header-1[data-component="energy"]::before { content: "⚡ E"; color: var(--energy-yellow); }   
h1[data-component="entropy"]::before, .HyperMD-header-1[data-component="entropy"]::before { content: "🔥 S"; color: var(--entropy-red); }   
h1[data-component="time"]::before, .HyperMD-header-1[data-component="time"]::before { content: "⏰ T"; color: var(--time-silver); }   
h1[data-component="causality"]::before, .HyperMD-header-1[data-component="causality"]::before { content: "🔗 K"; color: var(--causality-violet); }   
h1[data-component="relativity"]::before, .HyperMD-header-1[data-component="relativity"]::before { content: "🌌 R"; color: var(--relativity-pink); }   
h1[data-component="quantum"]::before, .HyperMD-header-1[data-component="quantum"]::before { content: "⚛️ Q"; color: var(--quantum-blue); }   
h1[data-component="forces"]::before, .HyperMD-header-1[data-component="forces"]::before { content: "💪 F"; color: var(--forces-emerald); }   
h1[data-component="consciousness"]::before, .HyperMD-header-1[data-component="consciousness"]::before { content: "👁️ C"; color: var(--consciousness-white); }   
   
/* Colorful heading underlines */   
h1::after, .HyperMD-header-1::after,   
h2::after, .HyperMD-header-2::after,   
h3::after, .HyperMD-header-3::after,   
h4::after, .HyperMD-header-4::after,   
h5::after, .HyperMD-header-5::after,   
h6::after, .HyperMD-header-6::after {   
  margin-top: 0.3em;   
  content: "";   
  width: auto !important;   
  display: flex !important;   
  height: 0.2em;   
  border-radius: 10px;   
  background: linear-gradient(90deg,   
    var(--quantum-blue) 0%,   
    var(--bridge-purple) 25%,   
    var(--spiritual-gold) 50%,   
    var(--bridge-purple) 75%,   
    var(--quantum-blue) 100%);   
}   
   
/* Heading level indicators */   
h1::after { background: linear-gradient(90deg, var(--quantum-blue), var(--spiritual-gold)); }   
h2::after { background: linear-gradient(90deg, var(--spiritual-gold), var(--grace-green)); }   
h3::after { background: linear-gradient(90deg, var(--grace-green), var(--bridge-purple)); }   
h4::after { background: linear-gradient(90deg, var(--bridge-purple), var(--quantum-blue)); }   
h5::after { background: linear-gradient(90deg, var(--quantum-blue), var(--entropy-red)); }   
h6::after { background: linear-gradient(90deg, var(--entropy-red), var(--spiritual-gold)); }   
   
.fade-in {   
  animation: fadeIn 1s ease-in-out;   
}   
   
@keyframes fadeIn {   
  from { opacity: 0; transform: translateY(20px); }   
  to { opacity: 1; transform: translateY(0); }   
}