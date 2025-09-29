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
- 0a0a0a
- ffffff
- 1e3a8a
- 3b82f6
- 60a5fa
- bfdbfe
- 22c55e
- 4ade80
- bbf7d0
- 581c87
- 8b5cf6
- a78bfa
- ddd6fe
- c2410c
- f97316
- fb923c
- fed7aa
- 1f2937
- fbbf24
- ec4899
- dc2626
- ef4444
title: "DOCTYPE html\nhtml langen\nhead\n    meta charsetUTF-8\n    meta..."
---
   
<!DOCTYPE html>   
<html lang="en">   
<head>   
    <meta charset="UTF-8">   
    <meta name="viewport" content="width=device-width, initial-scale=1.0">   
    <title>Modular Callout System + CSS Snippets</title>   
    <style>   
        body {   
            font-family: 'Georgia', serif;   
            background: `{_obsidian_pattern_tag_0a0a0a}`;   
            color: `{_obsidian_pattern_tag_ffffff}`;   
            padding: 20px;   
            line-height: 1.6;   
            max-width: 1200px;   
            margin: 0 auto;   
        }   
   
        /* ==================== MODULAR CALLOUT SYSTEM ==================== */   
        /* Base structure - same for all callouts */   
        .callout-base {   
            border-radius: 12px;   
            padding: 20px;   
            margin: 25px 0;   
            position: relative;   
            background: var(--callout-bg);   
            border: 2px solid var(--callout-border);   
            box-shadow: 0 6px 20px var(--callout-shadow);   
        }   
   
        .callout-base::before {   
            content: var(--callout-icon);   
            font-size: 1.5em;   
            position: absolute;   
            top: 15px;   
            right: 20px;   
            opacity: 0.8;   
        }   
   
        .callout-base h4 {   
            color: var(--callout-text);   
            margin-bottom: 15px;   
            font-size: 1.2em;   
            font-weight: bold;   
        }   
   
        .callout-content {   
            background: var(--callout-content-bg);   
            border-radius: 8px;   
            padding: 15px;   
            margin-top: 10px;   
            border-left: 4px solid var(--callout-border);   
        }   
   
        /* Color Schemes - just change these CSS variables */   
        .callout-blue {   
   
            --callout-bg: linear-gradient(135deg, `{_obsidian_pattern_tag_1e3a8a}`, `{_obsidian_pattern_tag_3b82f6}`);   
            --callout-border: `{_obsidian_pattern_tag_60a5fa}`;   
            --callout-shadow: rgba(96, 165, 250, 0.3);   
            --callout-text: `{_obsidian_pattern_tag_bfdbfe}`;   
            --callout-content-bg: rgba(30, 58, 138, 0.3);   
            --callout-icon: '🧭';   
        }   
   
        .callout-green {   
   
            --callout-bg: linear-gradient(135deg, #166534, `{_obsidian_pattern_tag_22c55e}`);   
            --callout-border: `{_obsidian_pattern_tag_4ade80}`;   
            --callout-shadow: rgba(74, 222, 128, 0.3);   
            --callout-text: `{_obsidian_pattern_tag_bbf7d0}`;   
            --callout-content-bg: rgba(22, 101, 52, 0.4);   
            --callout-icon: '✨';   
        }   
   
        .callout-purple {   
   
            --callout-bg: linear-gradient(135deg, `{_obsidian_pattern_tag_581c87}`, `{_obsidian_pattern_tag_8b5cf6}`);   
            --callout-border: `{_obsidian_pattern_tag_a78bfa}`;   
            --callout-shadow: rgba(167, 139, 250, 0.3);   
            --callout-text: `{_obsidian_pattern_tag_ddd6fe}`;   
            --callout-content-bg: rgba(88, 28, 135, 0.3);   
            --callout-icon: '⚛️';   
        }   
   
        .callout-orange {   
   
            --callout-bg: linear-gradient(135deg, `{_obsidian_pattern_tag_c2410c}`, `{_obsidian_pattern_tag_f97316}`);   
            --callout-border: `{_obsidian_pattern_tag_fb923c}`;   
            --callout-shadow: rgba(251, 146, 60, 0.3);   
            --callout-text: `{_obsidian_pattern_tag_fed7aa}`;   
            --callout-content-bg: rgba(194, 65, 12, 0.3);   
            --callout-icon: '🔥';   
        }   
   
        /* ==================== BONUS CSS SNIPPETS ==================== */   
   
        /* 1. Parallax Quote Boxes */   
        .parallax-quote {   
            background: linear-gradient(135deg, `{_obsidian_pattern_tag_1f2937}`, #374151);   
            border-left: 5px solid `{_obsidian_pattern_tag_fbbf24}`;   
            padding: 20px 25px;   
            margin: 30px 0;   
            position: relative;   
            transform-style: preserve-3d;   
            transition: transform 0.3s ease;   
            overflow: hidden;   
        }   
   
        .parallax-quote::before {   
            content: '"';   
            font-size: 4em;   
            color: rgba(251, 191, 36, 0.2);   
            position: absolute;   
            top: -10px;   
            left: 10px;   
            font-family: Georgia, serif;   
            transform: translateZ(-1px);   
        }   
   
        .parallax-quote:hover {   
            transform: rotateX(2deg) rotateY(1deg);   
        }   
   
        .parallax-quote-text {   
            font-style: italic;   
            font-size: 1.1em;   
            position: relative;   
            z-index: 2;   
        }   
   
        .parallax-quote-author {   
            text-align: right;   
            margin-top: 10px;   
            opacity: 0.8;   
            font-size: 0.9em;   
        }   
   
        /* 2. Glowing Progress Bars */   
        .progress-container {   
            background: rgba(255, 255, 255, 0.1);   
            border-radius: 20px;   
            padding: 4px;   
            margin: 20px 0;   
            position: relative;   
            overflow: hidden;   
        }   
   
        .progress-bar {   
            height: 20px;   
            border-radius: 16px;   
            background: linear-gradient(90deg, `{_obsidian_pattern_tag_3b82f6}`, `{_obsidian_pattern_tag_8b5cf6}`, `{_obsidian_pattern_tag_ec4899}`);   
            background-size: 200% 100%;   
            animation: shimmer 2s infinite;   
            position: relative;   
            transition: width 0.8s ease;   
        }   
   
        .progress-bar::after {   
            content: attr(data-label);   
            position: absolute;   
            top: 50%;   
            left: 50%;   
            transform: translate(-50%, -50%);   
            color: white;   
            font-size: 0.8em;   
            font-weight: bold;   
            text-shadow: 0 0 10px rgba(0,0,0,0.5);   
        }   
   
        @keyframes shimmer {   
            0% { background-position: -200% 0; }   
            100% { background-position: 200% 0; }   
        }   
   
        /* 3. Floating Action Cards */   
        .action-card {   
            background: rgba(255, 255, 255, 0.05);   
            border: 1px solid rgba(255, 255, 255, 0.1);   
            border-radius: 15px;   
            padding: 20px;   
            margin: 15px 0;   
            backdrop-filter: blur(10px);   
            transition: all 0.3s ease;   
            cursor: pointer;   
            position: relative;   
            overflow: hidden;   
        }   
   
        .action-card::before {   
            content: '';   
            position: absolute;   
            top: 0;   
            left: -100%;   
            width: 100%;   
            height: 100%;   
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);   
            transition: left 0.5s ease;   
        }   
   
        .action-card:hover {   
            transform: translateY(-5px);   
            box-shadow: 0 10px 30px rgba(255, 255, 255, 0.1);   
            border-color: rgba(255, 255, 255, 0.3);   
        }   
   
        .action-card:hover::before {   
            left: 100%;   
        }   
   
        .action-card-icon {   
            font-size: 2em;   
            margin-bottom: 10px;   
            display: block;   
        }   
   
        .action-card-title {   
            font-size: 1.2em;   
            margin-bottom: 8px;   
            color: `{_obsidian_pattern_tag_fbbf24}`;   
        }   
   
        /* 4. Typing Animation Text */   
        .typing-text {   
            border-right: 2px solid `{_obsidian_pattern_tag_fbbf24}`;   
            white-space: nowrap;   
            overflow: hidden;   
            animation: typing 3s steps(40, end), blink-caret 0.5s step-end infinite alternate;   
        }   
   
        @keyframes typing {   
            from { width: 0; }   
            to { width: 100%; }   
        }   
   
        @keyframes blink-caret {   
            50% { border-color: transparent; }   
        }   
   
        /* 5. Neumorphic Buttons */   
        .neuro-button {   
            background: `{_obsidian_pattern_tag_1f2937}`;   
            border: none;   
            border-radius: 15px;   
            padding: 15px 30px;   
            color: `{_obsidian_pattern_tag_ffffff}`;   
            font-size: 1em;   
            cursor: pointer;   
            transition: all 0.3s ease;   
            box-shadow:    
                6px 6px 12px rgba(0, 0, 0, 0.4),   
   
                -6px -6px 12px rgba(255, 255, 255, 0.1);   
            margin: 10px;   
        }   
   
        .neuro-button:hover {   
            box-shadow:    
                3px 3px 6px rgba(0, 0, 0, 0.4),   
   
                -3px -3px 6px rgba(255, 255, 255, 0.1);   
            transform: translateY(2px);   
        }   
   
        .neuro-button:active {   
            box-shadow: inset 3px 3px 6px rgba(0, 0, 0, 0.4);   
            transform: translateY(4px);   
        }   
   
        /* Demo sections */   
        .demo-section {   
            margin: 40px 0;   
            padding: 20px 0;   
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);   
        }   
   
        .demo-title {   
            color: `{_obsidian_pattern_tag_fbbf24}`;   
            font-size: 1.4em;   
            margin-bottom: 20px;   
            text-align: center;   
        }   
   
        .code-block {   
            background: #111827;   
            border: 1px solid #374151;   
            border-radius: 8px;   
            padding: 15px;   
            margin: 15px 0;   
            font-family: 'Courier New', monospace;   
            font-size: 0.9em;   
            overflow-x: auto;   
        }   
   
        .css-var { color: `{_obsidian_pattern_tag_8b5cf6}`; }   
        .css-prop { color: `{_obsidian_pattern_tag_60a5fa}`; }   
        .css-value { color: `{_obsidian_pattern_tag_4ade80}`; }   
    </style>   
</head>   
<body>   
    <h1>🎨 Modular CSS System + Bonus Snippets</h1>   
   
    <!-- ==================== MODULAR CALLOUT SYSTEM ==================== -->   
    <div class="demo-section">   
        <h2 class="demo-title">1. Modular Callout System</h2>   
           
        <p><strong>The Secret:</strong> One base structure + CSS variables = infinite color schemes!</p>   
   
        <div class="callout-base callout-blue">   
            <h4>🧭 Blue Epistemological</h4>   
            <div class="callout-content">   
                Same HTML structure, different CSS variables!   
            </div>   
        </div>   
   
        <div class="callout-base callout-green">   
            <h4>✨ Green Living Word</h4>   
            <div class="callout-content">   
                Just change the color scheme class.   
            </div>   
        </div>   
   
        <div class="callout-base callout-purple">   
            <h4>⚛️ Purple Quantum</h4>   
            <div class="callout-content">   
                Add as many colors as you want!   
            </div>   
        </div>   
   
        <div class="callout-base callout-orange">   
            <h4>🔥 Orange Revelation</h4>   
            <div class="callout-content">   
                Easy to create new themes.   
            </div>   
        </div>   
   
        <div class="code-block">   
<span class="css-prop">/* How to add a new color scheme: */</span>   
<span class="css-var">.callout-red</span> {   
    <span class="css-prop">--callout-bg:</span> <span class="css-value">linear-gradient(135deg, `{_obsidian_pattern_tag_dc2626}`, `{_obsidian_pattern_tag_ef4444}`)</span>;   
    <span class="css-prop">--callout-border:</span> <span class="css-value">#f87171</span>;   
    <span class="css-prop">--callout-shadow:</span> <span class="css-value">rgba(248, 113, 113, 0.3)</span>;   
    <span class="css-prop">--callout-text:</span> <span class="css-value">#fecaca</span>;   
    <span class="css-prop">--callout-content-bg:</span> <span class="css-value">rgba(220, 38, 38, 0.3)</span>;   
    <span class="css-prop">--callout-icon:</span> <span class="css-value">'🌋'</span>;   
}   
   
<span class="css-prop">/* HTML usage: */</span>   
&lt;div class="<span class="css-var">callout-base callout-red</span>"&gt;   
    &lt;h4&gt;🌋 Red Passion&lt;/h4&gt;   
    &lt;div class="<span class="css-var">callout-content</span>"&gt;Your content here&lt;/div&gt;   
&lt;/div&gt;   
        </div>   
    </div>   
   
    <!-- ==================== BONUS SNIPPET 1: PARALLAX QUOTES ==================== -->   
    <div class="demo-section">   
        <h2 class="demo-title">2. Parallax Quote Boxes</h2>   
   
        <div class="parallax-quote">   
            <div class="parallax-quote-text">   
                "Reality is not what it appears to be, nor is it otherwise."   
            </div>   
            <div class="parallax-quote-author">— Ancient Wisdom</div>   
        </div>   
   
        <p><strong>Perfect for:</strong> Profound quotes, scripture verses, key insights that need visual impact.</p>   
    </div>   
   
    <!-- ==================== BONUS SNIPPET 2: PROGRESS BARS ==================== -->   
    <div class="demo-section">   
        <h2 class="demo-title">3. Glowing Progress Bars</h2>   
   
        <div class="progress-container">   
            <div class="progress-bar" style="width: 75%;" data-label="Consciousness Research 75%"></div>   
        </div>   
   
        <div class="progress-container">   
            <div class="progress-bar" style="width: 90%;" data-label="Quantum Framework 90%"></div>   
        </div>   
   
        <div class="progress-container">   
            <div class="progress-bar" style="width: 45%;" data-label="Practical Application 45%"></div>   
        </div>   
   
        <p><strong>Perfect for:</strong> Project progress, understanding levels, completion tracking.</p>   
    </div>   
   
    <!-- ==================== BONUS SNIPPET 3: ACTION CARDS ==================== -->   
    <div class="demo-section">   
        <h2 class="demo-title">4. Floating Action Cards</h2>   
   
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">   
            <div class="action-card">   
                <span class="action-card-icon">🧮</span>   
                <div class="action-card-title">Mathematical Framework</div>   
                <div>Explore the equations behind consciousness</div>   
            </div>   
   
            <div class="action-card">   
                <span class="action-card-icon">⚛️</span>   
                <div class="action-card-title">Quantum Mechanics</div>   
                <div>Dive into the physics of reality</div>   
            </div>   
   
            <div class="action-card">   
                <span class="action-card-icon">✨</span>   
                <div class="action-card-title">Spiritual Practice</div>   
                <div>Apply insights to daily life</div>   
            </div>   
        </div>   
   
        <p><strong>Perfect for:</strong> Navigation, feature highlights, call-to-action sections.</p>   
    </div>   
   
    <!-- ==================== BONUS SNIPPET 4: TYPING TEXT ==================== -->   
    <div class="demo-section">   
        <h2 class="demo-title">5. Typing Animation</h2>   
   
        <div class="typing-text" style="width: 400px; margin: 20px auto;">   
            The universe is a living algorithm...   
        </div>   
   
        <p><strong>Perfect for:</strong> Revealing key insights, dramatic emphasis, drawing attention.</p>   
    </div>   
   
    <!-- ==================== BONUS SNIPPET 5: NEUMORPHIC BUTTONS ==================== -->   
    <div class="demo-section">   
        <h2 class="demo-title">6. Neumorphic Buttons</h2>   
   
        <div style="text-align: center;">   
            <button class="neuro-button">Explore Consciousness</button>   
            <button class="neuro-button">Quantum Prayer</button>   
            <button class="neuro-button">Mathematical God</button>   
        </div>   
   
        <p><strong>Perfect for:</strong> Interactive elements, navigation, emphasizing actions.</p>   
    </div>   
   
    <!-- ==================== LLM INSTRUCTIONS ==================== -->   
    <div class="demo-section">   
        <h2 class="demo-title">📖 Instructions for LLMs</h2>   
   
        <div class="code-block">   
<span class="css-prop">/* MODULAR CALLOUT SYSTEM FOR AI */</span>   
   
<span class="css-prop">1. BASE STRUCTURE:</span>   
   Use class="callout-base callout-{color}" for any callout   
      
<span class="css-prop">2. COLOR SCHEMES AVAILABLE:</span>   
   
   - callout-blue (epistemological, analytical)   
   - callout-green (living word, growth, life)   
   - callout-purple (quantum, mysterious, deep)   
   - callout-orange (revelation, energy, action)   
      
<span class="css-prop">3. TO ADD NEW COLORS:</span>   
   Create new CSS variables following the pattern:   
   
   --callout-bg, --callout-border, --callout-shadow,    
   --callout-text, --callout-content-bg, --callout-icon   
      
<span class="css-prop">4. HTML TEMPLATE:</span>   
   &lt;div class="callout-base callout-{color}"&gt;   
       &lt;h4&gt;{icon} {title}&lt;/h4&gt;   
       &lt;div class="callout-content"&gt;{content}&lt;/div&gt;   
   &lt;/div&gt;   
   
<span class="css-prop">5. BONUS SNIPPETS:</span>   
   
   - .parallax-quote for profound statements   
   - .progress-bar for tracking completion   
   - .action-card for interactive elements   
   - .typing-text for dramatic reveals   
   - .neuro-button for actions   
        </div>   
    </div>   
   
</body>   
</html>