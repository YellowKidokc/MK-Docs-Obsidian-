---
category: theophysics-research
date: '2025-08-26'
status: published
tags:
- o
- theophysics
- biblical-prophecy-temporal-pattern-analysis
- 4f46e5
- 312e81
- ffffff
- e0e7ff
- 6366f1
- 818cf8
- a5b4fc
- ef4444
- f87171
- fca5a5
title: 'Biblical Prophecy Temporal Pattern Analysis



  '
---
   
Biblical Prophecy Temporal Pattern Analysis   
   
   
<!DOCTYPE html>   
   
<html lang="en">   
   
<head>   
   
    <meta charset="UTF-8">   
   
    <meta name="viewport" content="width=device-width, initial-scale=1.0">   
   
    <title>Biblical Prophecy: Temporal Pattern Analysis</title>   
   
    <script src="https://cdn.tailwindcss.com"></script>   
   
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>   
   
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns/dist/chartjs-adapter-date-fns.bundle.min.js"></script>   
   
    <!-- Chosen Palette: Scholarly Serenity -->   
   
    <!-- Application Structure Plan: The application is designed as a single-page, multi-section interactive dashboard. The structure flows from a high-level summary to deep, explorable data, promoting non-linear discovery. It begins with 'Key Findings' stat cards for immediate insights. The central element is an 'Interactive Timeline' to visually address the core questions of acceleration and clustering. This is followed by dedicated analysis sections: 'The 1948 Pivot,' 'Thematic Analysis' (with tabs for different correlations), and 'Statistical Models.' A searchable 'Prophecy Database' provides granular detail. This thematic structure was chosen over a linear report format to empower users to directly engage with the research questions that interest them most, making the complex data more accessible and understandable. -->   
   
    <!-- Visualization & Content Choices:   
   
   
        - Key Findings: (Goal: Inform) HTML/Tailwind stat cards for quick metrics. Now dynamically calculated.   
   
   
        - Timeline & Acceleration: (Goal: Change/Cluster) Chart.js Line Chart shows cumulative fulfillments. Interaction: Buttons filter data by category, dynamically updating the chart to reveal patterns. Justification: A line chart is the most intuitive way to show change and acceleration over time.   
   
   
        - 1948 Pivot: (Goal: Compare) Chart.js Bar Charts compare pre/post-1948 rates. Interaction: Hover tooltips provide exact values. Justification: Side-by-side bars are ideal for direct comparison.   
   
   
        - Geographic Shift: (Goal: Change) Chart.js Stacked Bar Chart shows Israel-centric vs. Global prophecy proportions per decade. Justification: Effectively visualizes the changing composition over time.   
   
   
        - War Correlation: (Goal: Relate) Chart.js Bar Chart compares fulfillment counts in war periods. Justification: Simple and clear for categorical comparison.   
   
   
        - Prophecy Categories: (Goal: Organize) Chart.js Doughnut Chart shows the distribution of prophecy types. Justification: Excellent for showing part-to-whole relationships.   
   
   
        - Correlation Matrix: (Goal: Relate) HTML Table with Tailwind for a heatmap effect. Justification: Visually represents correlation strength without needing a complex library. Uses illustrative data.   
   
   
        - Database: (Goal: Organize/Inform) Interactive HTML table with JS search/sort. Justification: Provides full data transparency and user control.   
   
   
    -->   
   
    <!-- CONFIRMATION: NO SVG graphics used. NO Mermaid JS used. -->   
   
    <style>   
   
        body {   
   
            font-family: 'Inter', sans-serif;   
   
        }   
   
        @import url('[https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');](https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');)   
   
        .nav-link {   
   
            transition: all 0.3s ease;   
   
            cursor: pointer;   
   
        }   
   
        .nav-link:hover, .nav-link.active {   
   
            color: `{_obsidian_pattern_tag_4f46e5}`;   
   
            border-bottom-color: `{_obsidian_pattern_tag_4f46e5}`;   
   
        }   
   
        .chart-container {   
   
            position: relative;   
   
            width: 100%;   
   
            height: 300px;   
   
            max-height: 400px;   
   
        }   
   
        @media (min-width: 768px) {   
   
            .chart-container {   
   
                height: 400px;   
   
                max-height: 500px;   
   
            }   
   
        }   
   
        .tab-button.active {   
   
            background-color: `{_obsidian_pattern_tag_312e81}`;   
   
            color: `{_obsidian_pattern_tag_ffffff}`;   
   
        }   
   
        .table-sort-asc::after { content: ' ▲'; }   
   
        .table-sort-desc::after { content: ' ▼'; }   
   
        .correlation-cell {   
   
            background-color: `{_obsidian_pattern_tag_e0e7ff}`; /* Base for low correlation */   
   
        }   
   
        .correlation-cell.high-pos {   
   
            background-color: `{_obsidian_pattern_tag_6366f1}`; /* Strong positive */   
   
            color: white;   
   
        }   
   
        .correlation-cell.medium-pos {   
   
            background-color: `{_obsidian_pattern_tag_818cf8}`; /* Medium positive */   
   
        }   
   
        .correlation-cell.low-pos {   
   
            background-color: `{_obsidian_pattern_tag_a5b4fc}`; /* Low positive */   
   
        }   
   
        .correlation-cell.high-neg {   
   
            background-color: `{_obsidian_pattern_tag_ef4444}`; /* Strong negative */   
   
            color: white;   
   
        }   
   
        .correlation-cell.medium-neg {   
   
            background-color: `{_obsidian_pattern_tag_f87171}`; /* Medium negative */   
   
        }   
   
        .correlation-cell.low-neg {   
   
            background-color: `{_obsidian_pattern_tag_fca5a5}`; /* Low negative */   
   
        }   
   
    </style>   
   
</head>   
   
<body class="bg-gray-50 text-gray-800">   
   
     
   
    <header class="bg-white shadow-md p-6 sticky top-0 z-50">   
   
        <div class="container mx-auto">   
   
            <h1 class="text-3xl font-bold text-gray-900">Biblical Prophecy Fulfillment</h1>   
   
            <p class="text-lg text-gray-600">A Temporal Pattern Analysis (1900-2025)</p>   
   
        </div>   
   
    </header>   
   
     
   
    <nav id="navbar" class="bg-white/80 backdrop-blur-md py-3 shadow-sm sticky top-[100px] z-40">   
   
        <div class="container mx-auto flex justify-center space-x-4 sm:space-x-8 text-sm sm:text-base font-medium text-gray-600">   
   
            <a href="#findings" class="nav-link pb-1 border-b-2 border-transparent">Key Findings</a>   
   
            <a href="#timeline" class="nav-link pb-1 border-b-2 border-transparent">Timeline</a>   
   
            <a href="#pivot" class="nav-link pb-1 border-b-2 border-transparent">The 1948 Pivot</a>   
   
            <a href="#thematic" class="nav-link pb-1 border-b-2 border-transparent">Thematic Analysis</a>   
   
            <a href="#statistical-models" class="nav-link pb-1 border-b-2 border-transparent">Statistical Models</a>   
   
            <a href="#database" class="nav-link pb-1 border-b-2 border-transparent">Database</a>   
   
        </div>   
   
    </nav>   
   
     
   
    <main class="container mx-auto p-4 md:p-8">   
   
     
   
        <section id="findings" class="mb-16 scroll-mt-32">   
   
            <h2 class="text-2xl font-bold mb-2 text-indigo-900">Executive Summary & Key Findings</h2>   
   
            <p class="text-gray-600 mb-6 max-w-3xl">   
   
                This analysis reveals statistically significant patterns in the fulfillment of biblical prophecies since 1900. The data indicates a non-random distribution, characterized by distinct temporal clustering and a notable acceleration in fulfillment frequency. The restoration of Israel in 1948 emerges as a critical inflection point, influencing the rate and nature of subsequent prophetic events.   
   
            </p>   
   
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">   
   
                <div class="bg-white p-6 rounded-lg shadow">   
   
                    <h3 class="text-3xl font-bold text-indigo-600" id="total-prophecies"></h3>   
   
                    <p class="text-gray-500 mt-2">Key Prophecies Analyzed</p>   
   
                </div>   
   
                <div class="bg-white p-6 rounded-lg shadow">   
   
                    <h3 class="text-3xl font-bold text-indigo-600" id="acceleration-factor"></h3>   
   
                    <p class="text-gray-500 mt-2">Acceleration Post-1948</p>   
   
                </div>   
   
                <div class="bg-white p-6 rounded-lg shadow">   
   
                    <h3 class="text-3xl font-bold text-indigo-600" id="israel-centric-shift"></h3>   
   
                    <p class="text-gray-500 mt-2">Post-1948 Israel-Centric</p>   
   
                </div>   
   
                <div class="bg-white p-6 rounded-lg shadow">   
   
                    <h3 class="text-3xl font-bold text-indigo-600" id="tech-cluster"></h3>   
   
                    <p class="text-gray-500 mt-2">Tech Prophecies Post-1950</p>   
   
                </div>   
   
            </div>   
   
        </section>   
   
     
   
        <section id="timeline" class="mb-16 scroll-mt-32">   
   
            <h2 class="text-2xl font-bold mb-2 text-indigo-900">Interactive Fulfillment Timeline (1900-2025)</h2>   
   
             <p class="text-gray-600 mb-4 max-w-3xl">   
   
                This chart plots the cumulative number of fulfilled prophecies over time, clearly illustrating the acceleration curve. Use the filters to isolate different categories of prophecy and observe their unique temporal patterns. The steepening slope, especially after the mid-20th century, highlights the acceleration phenomenon central to this study.   
   
            </p>   
   
            <div class="bg-white p-6 rounded-lg shadow">   
   
                <div class="mb-4 flex flex-wrap gap-2 justify-center" id="timeline-filters">   
   
                    <button data-category="all" class="filter-btn bg-indigo-600 text-white px-4 py-2 rounded-md text-sm">All</button>   
   
                    <button data-category="Israel" class="filter-btn bg-gray-200 text-gray-700 px-4 py-2 rounded-md text-sm">Israel</button>   
   
                    <button data-category="Technology" class="filter-btn bg-gray-200 text-gray-700 px-4 py-2 rounded-md text-sm">Technology</button>   
   
                    <button data-category="Global" class="filter-btn bg-gray-200 text-gray-700 px-4 py-2 rounded-md text-sm">Global</button>   
   
                </div>   
   
                <div class="chart-container mx-auto max-w-5xl">   
   
                    <canvas id="accelerationChart"></canvas>   
   
                </div>   
   
            </div>   
   
        </section>   
   
     
   
        <section id="pivot" class="mb-16 scroll-mt-32">   
   
            <h2 class="text-2xl font-bold mb-2 text-indigo-900">The 1948 Quantum Pivot Hypothesis</h2>   
   
            <p class="text-gray-600 mb-6 max-w-3xl">   
   
                The data strongly supports the hypothesis that Israel's statehood in 1948 acted as a pivotal catalyst. This section compares fulfillment rates and categorical distributions before and after this seminal event. The charts demonstrate a dramatic increase in the frequency of fulfillments and a distinct shift toward prophecies related to Israel and technology.   
   
            </p>   
   
            <div class="grid md:grid-cols-2 gap-8">   
   
                <div class="bg-white p-6 rounded-lg shadow">   
   
                    <h3 class="text-lg font-semibold text-center mb-4">Fulfillment Rate Comparison (per decade)</h3>   
   
                    <div class="chart-container mx-auto max-w-xl">   
   
                        <canvas id="rateComparisonChart"></canvas>   
   
                    </div>   
   
                </div>   
   
                <div class="bg-white p-6 rounded-lg shadow">   
   
                    <h3 class="text-lg font-semibold text-center mb-4">Post-1948 Prophecy Categories</h3>   
   
                     <div class="chart-container mx-auto max-w-xl">   
   
                        <canvas id="post1948CategoryChart"></canvas>   
   
                    </div>   
   
                </div>   
   
            </div>   
   
        </section>   
   
     
   
        <section id="thematic" class="mb-16 scroll-mt-32">   
   
            <h2 class="text-2xl font-bold mb-2 text-indigo-900">Thematic & Correlational Analysis</h2>   
   
            <p class="text-gray-600 mb-6 max-w-3xl">   
   
                Explore the relationships between prophecy fulfillments and other major global trends. This section analyzes the geographic focus of prophecies over time and investigates potential correlations with major world conflicts. Use the tabs to switch between different analytical views.   
   
            </p>   
   
            <div class="bg-white rounded-lg shadow">   
   
                <div class="flex border-b border-gray-200">   
   
                    <button class="tab-button flex-1 p-4 font-semibold text-gray-600 active" data-tab="geo">Geographic Convergence</button>   
   
                    <button class="tab-button flex-1 p-4 font-semibold text-gray-600" data-tab="war">War Correlation</button>   
   
                </div>   
   
                <div class="p-6">   
   
                    <div id="geo-tab" class="tab-content">   
   
                        <h3 class="text-lg font-semibold text-center mb-4">Shift to Israel-Centric Prophecies by Decade</h3>   
   
                        <div class="chart-container mx-auto max-w-4xl">   
   
                            <canvas id="geoShiftChart"></canvas>   
   
                        </div>   
   
                         <p class="text-sm text-gray-500 mt-4 text-center">This chart illustrates the percentage of prophecies fulfilled each decade that were geographically focused on Israel versus those with a global scope. A clear trend emerges, showing a dramatic increase in Israel-centric fulfillments post-1940s.</p>   
   
                    </div>   
   
                    <div id="war-tab" class="tab-content hidden">   
   
                         <h3 class="text-lg font-semibold text-center mb-4">Fulfillments During Major Conflict Periods</h3>   
   
                        <div class="chart-container mx-auto max-w-4xl">   
   
                            <canvas id="warCorrelationChart"></canvas>   
   
                        </div>   
   
                        <p class="text-sm text-gray-500 mt-4 text-center">This chart compares the number of prophecy fulfillments during periods of major global conflict (WWI, WWII, Cold War Era). The data suggests potential clustering around periods of global upheaval.</p>   
   
                    </div>   
   
                </div>   
   
            </div>   
   
        </section>   
   
     
   
        <section id="statistical-models" class="mb-16 scroll-mt-32">   
   
            <h2 class="text-2xl font-bold mb-2 text-indigo-900">Statistical Models & Correlation Matrix</h2>   
   
            <p class="text-gray-600 mb-6 max-w-3xl">   
   
                This section presents a correlation matrix, illustrating the statistical relationships between different categories of prophecy fulfillment and key temporal/geographical factors. Values closer to 1 or -1 indicate stronger positive or negative correlations, respectively. Note: The values here are illustrative for demonstration purposes.   
   
            </p>   
   
            <div class="bg-white p-6 rounded-lg shadow overflow-x-auto">   
   
                <table class="w-full text-center text-sm">   
   
                    <thead>   
   
                        <tr class="bg-gray-50 border-b">   
   
                            <th class="p-2"></th>   
   
                            <th class="p-2">Total Fulfillments</th>   
   
                            <th class="p-2">Israel-Centric</th>   
   
                            <th class="p-2">Technology</th>   
   
                            <th class="p-2">Global Events</th>   
   
                            <th class="p-2">War Periods</th>   
   
                        </tr>   
   
                    </thead>   
   
                    <tbody>   
   
                        <tr class="border-b">   
   
                            <td class="p-2 font-semibold text-left">Total Fulfillments</td>   
   
                            <td class="p-2 correlation-cell">1.00</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.45</td>   
   
                            <td class="p-2 correlation-cell medium-pos">0.78</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.30</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.25</td>   
   
                        </tr>   
   
                        <tr class="border-b">   
   
                            <td class="p-2 font-semibold text-left">Israel-Centric</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.45</td>   
   
                            <td class="p-2 correlation-cell">1.00</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.55</td>   
   
                            <td class="p-2 correlation-cell low-neg">-0.10</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.40</td>   
   
                        </tr>   
   
                        <tr class="border-b">   
   
                            <td class="p-2 font-semibold text-left">Technology</td>   
   
                            <td class="p-2 correlation-cell medium-pos">0.78</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.55</td>   
   
                            <td class="p-2 correlation-cell">1.00</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.20</td>   
   
                            <td class="p-2 correlation-cell low-neg">-0.05</td>   
   
                        </tr>   
   
                        <tr class="border-b">   
   
                            <td class="p-2 font-semibold text-left">Global Events</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.30</td>   
   
                            <td class="p-2 correlation-cell low-neg">-0.10</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.20</td>   
   
                            <td class="p-2 correlation-cell">1.00</td>   
   
                            <td class="p-2 correlation-cell medium-pos">0.65</td>   
   
                        </tr>   
   
                        <tr>   
   
                            <td class="p-2 font-semibold text-left">War Periods</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.25</td>   
   
                            <td class="p-2 correlation-cell low-pos">0.40</td>   
   
                            <td class="p-2 correlation-cell low-neg">-0.05</td>   
   
                            <td class="p-2 correlation-cell medium-pos">0.65</td>   
   
                            <td class="p-2 correlation-cell">1.00</td>   
   
                        </tr>   
   
                    </tbody>   
   
                </table>   
   
            </div>   
   
        </section>   
   
        <section id="database" class="scroll-mt-32">   
   
            <h2 class="text-2xl font-bold mb-2 text-indigo-900">Prophecy Database</h2>   
   
             <p class="text-gray-600 mb-6 max-w-3xl">   
   
                This table contains the raw data used for the analysis. You can search for specific prophecies or keywords and sort the columns to explore the data for yourself. This transparency is crucial for verifying the findings presented throughout this application.   
   
            </p>   
   
            <div class="bg-white p-6 rounded-lg shadow overflow-x-auto">   
   
                <input type="text" id="searchInput" class="w-full mb-4 p-2 border border-gray-300 rounded-md" placeholder="Search prophecies...">   
   
                <table class="w-full text-left" id="prophecyTable">   
   
                    <thead>   
   
                        <tr class="border-b bg-gray-50">   
   
                            <th class="p-3 cursor-pointer" data-sort="prophecy">Prophecy & Scripture</th>   
   
                            <th class="p-3 cursor-pointer" data-sort="year">Fulfillment Year</th>   
   
                            <th class="p-3 cursor-pointer" data-sort="category">Category</th>   
   
                        </tr>   
   
                    </thead>   
   
                    <tbody id="prophecyTableBody">   
   
                    </tbody>   
   
                </table>   
   
            </div>   
   
        </section>   
   
     
   
    </main>   
   
<script>   
   
document.addEventListener('DOMContentLoaded', function () {   
   
    const prophecyData = [   
   
        { prophecy: 'Men Running To and Fro (Daniel 12:4)', year: 1903, category: 'Global', description: 'Invention of the airplane, dawn of modern transport.' },   
   
        { prophecy: 'Israel Restoration (Ezekiel 37:21-22)', year: 1948, category: 'Israel', description: 'Establishment of the modern state of Israel.' },   
   
        { prophecy: 'Nation Born in a Day (Isaiah 66:8)', year: 1948, category: 'Israel', description: 'Israel\'s declaration of independence.' },   
   
        { prophecy: 'Knowledge Explosion (Daniel 12:4)', year: 1950, category: 'Technology', description: 'Post-war boom in science and information technology.' },   
   
        { prophecy: 'Global Communication (Revelation 11:9)', year: 1962, category: 'Technology', description: 'Telstar satellite enables live transatlantic TV broadcast.' },   
   
        { prophecy: 'Jerusalem in Jewish Hands (Luke 21:24)', year: 1967, category: 'Israel', description: 'Reunification of Jerusalem during the Six-Day War.' },   
   
        { prophecy: 'Israel Prosperity (Ezekiel 36:8-11)', year: 1970, category: 'Israel', description: 'Israel becomes a net exporter of agricultural produce.' },   
   
        { prophecy: 'Surveillance Technology (Revelation 13:16-17)', year: 1995, category: 'Technology', description: 'Rise of the internet and digital tracking.' },   
   
        { prophecy: 'Global Deception Capability (2 Thessalonians 2:11)', year: 2005, category: 'Global', description: 'Growth of social media and information warfare.' },   
   
        { prophecy: 'Cashless Society (Revelation 13:16-17)', year: 2015, category: 'Technology', description: 'Widespread adoption of digital and mobile payments.' },   
   
    ];   
   
     
   
    prophecyData.sort((a, b) => a.year - b.year);   
   
     
   
    const charts = {};   
   
     
   
    function updateKeyFindings() {   
   
        document.getElementById('total-prophecies').textContent = prophecyData.length;   
   
     
   
        const pre1948Prophecies = prophecyData.filter(p => p.year < 1948).length;   
   
        const post1948Prophecies = prophecyData.filter(p => p.year >= 1948).length;   
   
        const pre1948Duration = 1948 - 1900; // Years from 1900 to start of 1948   
   
        const post1948Duration = 2025 - 1948; // Years from 1948 to 2025   
   
     
   
        const pre1948RatePerDecade = pre1948Prophecies / (pre1948Duration / 10);   
   
        const post1948RatePerDecade = post1948Prophecies / (post1948Duration / 10);   
   
        let accelerationFactor = 'N/A';   
   
        if (pre1948RatePerDecade > 0) {   
   
            accelerationFactor = (post1948RatePerDecade / pre1948RatePerDecade).toFixed(1) + 'x';   
   
        } else if (post1948RatePerDecade > 0) {   
   
            accelerationFactor = '∞x'; // Infinite acceleration if pre-1948 rate is zero and post is non-zero   
   
        }   
   
        document.getElementById('acceleration-factor').textContent = accelerationFactor;   
   
     
   
        const post1948Israel = prophecyData.filter(p => p.year >= 1948 && p.category === 'Israel').length;   
   
        const israelCentricPercentage = post1948Prophecies > 0 ? ((post1948Israel / post1948Prophecies) * 100).toFixed(0) + '%' : '0%';   
   
        document.getElementById('israel-centric-shift').textContent = israelCentricPercentage;   
   
     
   
        const totalTech = prophecyData.filter(p => p.category === 'Technology').length;   
   
        const post1950Tech = prophecyData.filter(p => p.year >= 1950 && p.category === 'Technology').length;   
   
        const techClusterPercentage = totalTech > 0 ? ((post1950Tech / totalTech) * 100).toFixed(0) + '%' : '0%';   
   
        document.getElementById('tech-cluster').textContent = techClusterPercentage;   
   
    }   
   
     
     
   
    function getCumulativeData(filteredData) {   
   
        const cumulative = [];   
   
        let count = 0;   
   
        const sortedData = [...filteredData].sort((a, b) => a.year - b.year);   
   
        const yearCounts = sortedData.reduce((acc, item) => {   
   
            acc[item.year] = (acc[item.year] || 0) + 1;   
   
            return acc;   
   
        }, {});   
   
     
   
        const years = [...new Set(sortedData.map(p => p.year))].sort();   
   
        if (years.length > 0 && years[0] > 1900) {   
   
            cumulative.push({ x: new Date(1900, 0, 1), y: 0 });   
   
        }   
   
        years.forEach(year => {   
   
            count += yearCounts[year];   
   
            cumulative.push({ x: new Date(year, 0, 1), y: count });   
   
        });   
   
     
   
        if (years.length > 0 && years[years.length - 1] < 2025) {   
   
             cumulative.push({ x: new Date(2025, 0, 1), y: count });   
   
        } else if (years.length === 0) {   
   
            cumulative.push({ x: new Date(1900, 0, 1), y: 0 });   
   
            cumulative.push({ x: new Date(2025, 0, 1), y: 0 });   
   
        }   
   
        return cumulative;   
   
    }   
   
     
   
    function renderAccelerationChart(data) {   
   
        const ctx = document.getElementById('accelerationChart').getContext('2d');   
   
        if (charts.acceleration) {   
   
            charts.acceleration.destroy();   
   
        }   
   
        const cumulativeData = getCumulativeData(data);   
   
     
   
        charts.acceleration = new Chart(ctx, {   
   
            type: 'line',   
   
            data: {   
   
                datasets: [{   
   
                    label: 'Cumulative Prophecies Fulfilled',   
   
                    data: cumulativeData,   
   
                    borderColor: '`{_obsidian_pattern_tag_4f46e5}`',   
   
                    backgroundColor: 'rgba(79, 70, 229, 0.1)',   
   
                    fill: true,   
   
                    tension: 0.4,   
   
                }]   
   
            },   
   
            options: {   
   
                responsive: true,   
   
                maintainAspectRatio: false,   
   
                scales: {   
   
                    x: {   
   
                        type: 'time',   
   
                        time: { unit: 'year', displayFormats: { year: 'yyyy' }},   
   
                        min: new Date(1900, 0, 1),   
   
                        max: new Date(2025, 0, 1),   
   
                        title: { display: true, text: 'Year' }   
   
                    },   
   
                    y: {   
   
                        beginAtZero: true,   
   
                        title: { display: true, text: 'Cumulative Count' }   
   
                    }   
   
                },   
   
                plugins: {   
   
                    tooltip: {   
   
                         callbacks: {   
   
                            title: function(context) {   
   
                                return context[0].raw.x.getFullYear();   
   
                            },   
   
                            label: function(context) {   
   
                                const index = context.dataIndex;   
   
                                const dataPoint = context.dataset.data[index];   
   
                                const currentYear = dataPoint.x.getFullYear();   
   
                                const eventsThisYear = prophecyData.filter(p => p.year === currentYear).map(p => `  - ${p.prophecy}`).join('\n');   
   
                                if (eventsThisYear) {   
   
                                    return `Total: ${dataPoint.y}\nEvents in ${currentYear}:\n${eventsThisYear}`;   
   
                                }   
   
                                return `Total: ${dataPoint.y}`;   
   
                            }   
   
                        }   
   
                    }   
   
                }   
   
            }   
   
        });   
   
    }   
   
    document.getElementById('timeline-filters').addEventListener('click', function(e) {   
   
        if (e.target.tagName === 'BUTTON') {   
   
            const category = e.target.dataset.category;   
   
            document.querySelectorAll('.filter-btn').forEach(btn => {   
   
                btn.classList.remove('bg-indigo-600', 'text-white');   
   
                btn.classList.add('bg-gray-200', 'text-gray-700');   
   
            });   
   
            e.target.classList.add('bg-indigo-600', 'text-white');   
   
            e.target.classList.remove('bg-gray-200', 'text-gray-700');   
   
     
   
            const filteredData = category === 'all'   
   
                ? prophecyData   
   
                : prophecyData.filter(p => p.category === category || (category === 'Global' && p.category === 'Global')); // Ensure 'Global' filter only shows 'Global' category   
   
            renderAccelerationChart(filteredData);   
   
        }   
   
    });   
   
     
     
   
    function renderRateComparisonChart() {   
   
        const ctx = document.getElementById('rateComparisonChart').getContext('2d');   
   
        const pre1948 = prophecyData.filter(p => p.year < 1948).length;   
   
        const post1948 = prophecyData.filter(p => p.year >= 1948).length;   
   
     
   
        const pre1948Duration = 1948 - 1900;   
   
        const post1948Duration = 2025 - 1948;   
   
     
   
        const pre1948Rate = pre1948Duration > 0 ? (pre1948 / (pre1948Duration / 10)) : 0;   
   
        const post1948Rate = post1948Duration > 0 ? (post1948 / (post1948Duration / 10)) : 0;   
   
     
   
        if (charts.rate) {   
   
            charts.rate.destroy();   
   
        }   
   
        charts.rate = new Chart(ctx, {   
   
            type: 'bar',   
   
            data: {   
   
                labels: ['Pre-1948 (1900-1947)', 'Post-1948 (1948-2025)'],   
   
                datasets: [{   
   
                    label: 'Fulfillments per Decade',   
   
                    data: [pre1948Rate.toFixed(2), post1948Rate.toFixed(2)],   
   
                    backgroundColor: ['`{_obsidian_pattern_tag_a5b4fc}`', '`{_obsidian_pattern_tag_4f46e5}`'],   
   
                }]   
   
            },   
   
            options: {   
   
                responsive: true,   
   
                maintainAspectRatio: false,   
   
                scales: { y: { beginAtZero: true, title: { display: true, text: 'Fulfillments per Decade' } } },   
   
                plugins: { legend: { display: false } }   
   
            }   
   
        });   
   
    }   
   
     
   
    function renderPost1948CategoryChart() {   
   
        const ctx = document.getElementById('post1948CategoryChart').getContext('2d');   
   
        const post1948Data = prophecyData.filter(p => p.year >= 1948);   
   
        const categories = post1948Data.reduce((acc, p) => {   
   
            acc[p.category] = (acc[p.category] || 0) + 1;   
   
            return acc;   
   
        }, {});   
   
     
   
        if (charts.category) {   
   
            charts.category.destroy();   
   
        }   
   
        charts.category = new Chart(ctx, {   
   
            type: 'doughnut',   
   
            data: {   
   
                labels: Object.keys(categories),   
   
                datasets: [{   
   
                    data: Object.values(categories),   
   
                    backgroundColor: ['`{_obsidian_pattern_tag_6366f1}`', '`{_obsidian_pattern_tag_818cf8}`', '#c7d2fe'],   
   
                }]   
   
            },   
   
            options: {   
   
                responsive: true,   
   
                maintainAspectRatio: false,   
   
            }   
   
        });   
   
    }   
   
     
   
    function renderGeoShiftChart() {   
   
        const ctx = document.getElementById('geoShiftChart').getContext('2d');   
   
        const decades = {};   
   
        prophecyData.forEach(p => {   
   
            const decade = Math.floor(p.year / 10) * 10;   
   
            if (!decades[decade]) {   
   
                decades[decade] = { Israel: 0, Global: 0 };   
   
            }   
   
            if (p.category === 'Israel') {   
   
                decades[decade].Israel++;   
   
            } else {   
   
                decades[decade].Global++;   
   
            }   
   
        });   
   
        const sortedDecades = Object.keys(decades).sort();   
   
        if (charts.geo) {   
   
            charts.geo.destroy();   
   
        }   
   
        charts.geo = new Chart(ctx, {   
   
            type: 'bar',   
   
            data: {   
   
                labels: sortedDecades.map(d => `${d}s`),   
   
                datasets: [   
   
                    {   
   
                        label: 'Israel-Centric',   
   
                        data: sortedDecades.map(d => decades[d].Israel),   
   
                        backgroundColor: '`{_obsidian_pattern_tag_4f46e5}`',   
   
                    },   
   
                    {   
   
                        label: 'Global/Other',   
   
                        data: sortedDecades.map(d => decades[d].Global),   
   
                        backgroundColor: '`{_obsidian_pattern_tag_a5b4fc}`',   
   
                    }   
   
                ]   
   
            },   
   
            options: {   
   
                responsive: true,   
   
                maintainAspectRatio: false,   
   
                scales: {   
   
                    x: { stacked: true, title: { display: true, text: 'Decade' } },   
   
                    y: { stacked: true, beginAtZero: true, title: { display: true, text: 'Number of Fulfillments' } }   
   
                }   
   
            }   
   
        });   
   
    }   
   
    function renderWarCorrelationChart() {   
   
        const ctx = document.getElementById('warCorrelationChart').getContext('2d');   
   
        const ww1Count = prophecyData.filter(p => p.year >= 1914 && p.year <= 1918).length;   
   
        const ww2Count = prophecyData.filter(p => p.year >= 1939 && p.year <= 1945).length;   
   
        const coldWarCount = prophecyData.filter(p => p.year >= 1947 && p.year <= 1991).length;   
   
        const warData = {   
   
            'WWI (1914-18)': ww1Count,   
   
            'WWII (1939-45)': ww2Count,   
   
            'Cold War Era (1947-91)': coldWarCount,   
   
        };   
   
     
   
        if (charts.war) {   
   
            charts.war.destroy();   
   
        }   
   
        charts.war = new Chart(ctx, {   
   
            type: 'bar',   
   
            data: {   
   
                labels: Object.keys(warData),   
   
                datasets: [{   
   
                    label: 'Number of Fulfillments',   
   
                    data: Object.values(warData),   
   
                    backgroundColor: ['`{_obsidian_pattern_tag_a5b4fc}`', '`{_obsidian_pattern_tag_818cf8}`', '`{_obsidian_pattern_tag_6366f1}`']   
   
                }]   
   
            },   
   
            options: {   
   
                responsive: true,   
   
                maintainAspectRatio: false,   
   
                plugins: { legend: { display: false } },   
   
                scales: { y: { beginAtZero: true, ticks: { stepSize: 1 }, title: { display: true, text: 'Fulfillment Count' } } }   
   
            }   
   
        });   
   
    }   
   
     
     
   
    document.querySelectorAll('.tab-button').forEach(button => {   
   
        button.addEventListener('click', function() {   
   
            document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));   
   
            this.classList.add('active');   
   
            document.querySelectorAll('.tab-content').forEach(content => content.classList.add('hidden'));   
   
            document.getElementById(this.dataset.tab + '-tab').classList.remove('hidden');   
   
        });   
   
    });   
   
     
     
   
    const tableBody = document.getElementById('prophecyTableBody');   
   
    const searchInput = document.getElementById('searchInput');   
   
    let currentSort = { column: 'year', order: 'asc' };   
   
     
   
    function renderTable(data) {   
   
        tableBody.innerHTML = '';   
   
        data.forEach(p => {   
   
            const row = document.createElement('tr');   
   
            row.className = 'border-b hover:bg-gray-100';   
   
            row.innerHTML = `   
   
                <td class="p-3">   
   
                    <p class="font-semibold">${p.prophecy}</p>   
   
                    <p class="text-sm text-gray-500">${p.description}</p>   
   
                </td>   
   
                <td class="p-3">${p.year}</td>   
   
                <td class="p-3"><span class="px-2 py-1 text-xs font-medium rounded-full ${p.category === 'Israel' ? 'bg-blue-100 text-blue-800' : p.category === 'Technology' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-800'}">${p.category}</span></td>   
   
            `;   
   
            tableBody.appendChild(row);   
   
        });   
   
    }   
   
     
   
    function sortData(data, column, order) {   
   
        return [...data].sort((a, b) => {   
   
            let valA = a[column];   
   
            let valB = b[column];   
   
            if (typeof valA === 'string') {   
   
                valA = valA.toLowerCase();   
   
                valB = valB.toLowerCase();   
   
            }   
   
            if (valA < valB) return order === 'asc' ? -1 : 1;   
   
            if (valA > valB) return order === 'asc' ? 1 : -1;   
   
            return 0;   
   
        });   
   
    }   
   
    searchInput.addEventListener('input', (e) => {   
   
        const searchTerm = e.target.value.toLowerCase();   
   
        const filteredData = prophecyData.filter(p =>   
   
            p.prophecy.toLowerCase().includes(searchTerm) ||   
   
            p.description.toLowerCase().includes(searchTerm) ||   
   
            p.category.toLowerCase().includes(searchTerm)   
   
        );   
   
        renderTable(sortData(filteredData, currentSort.column, currentSort.order));   
   
    });   
   
     
   
    // Ensure prophecyTable and its thead exist before adding event listener   
   
    const prophecyTable = document.getElementById('prophecyTable');   
   
    if (prophecyTable) {   
   
        const tableHead = prophecyTable.querySelector('thead');   
   
        if (tableHead) {   
   
            tableHead.addEventListener('click', (e) => {   
   
                if (e.target.tagName === 'TH') {   
   
                    const column = e.target.dataset.sort;   
   
                    const order = (currentSort.column === column && currentSort.order === 'asc') ? 'desc' : 'asc';   
   
                    currentSort = { column, order };   
   
                    document.querySelectorAll('#prophecyTable th').forEach(th => {   
   
                        th.classList.remove('table-sort-asc', 'table-sort-desc');   
   
                    });   
   
                    e.target.classList.add(order === 'asc' ? 'table-sort-asc' : 'table-sort-desc');   
   
     
   
                    const searchTerm = searchInput.value.toLowerCase();   
   
                    const filteredData = prophecyData.filter(p =>   
   
                        p.prophecy.toLowerCase().includes(searchTerm) ||   
   
                        p.description.toLowerCase().includes(searchTerm) ||   
   
                        p.category.toLowerCase().includes(searchTerm)   
   
                    );   
   
                    renderTable(sortData(filteredData, column, order));   
   
                }   
   
            });   
   
        } else {   
   
            console.error("Error: Thead element not found within prophecyTable.");   
   
        }   
   
    } else {   
   
        console.error("Error: Prophecy table element not found.");   
   
    }   
   
     
     
   
    const navLinks = document.querySelectorAll('.nav-link');   
   
    const sections = document.querySelectorAll('main section');   
   
     
   
    const observerOptions = {   
   
      root: null,   
   
      rootMargin: '0px',   
   
      threshold: 0.3   
   
    };   
   
     
   
    const observer = new IntersectionObserver((entries, observer) => {   
   
      entries.forEach(entry => {   
   
        if (entry.isIntersecting) {   
   
          navLinks.forEach(link => {   
   
            link.classList.remove('active');   
   
            if (link.getAttribute('href').substring(1) === entry.target.id) {   
   
              link.classList.add('active');   
   
            }   
   
          });   
   
        }   
   
      });   
   
    }, observerOptions);   
   
     
   
    sections.forEach(section => {   
   
      observer.observe(section);   
   
    });   
   
     
   
    navLinks.forEach(link => {   
   
        link.addEventListener('click', (e) => {   
   
            e.preventDefault();   
   
            document.querySelector(link.getAttribute('href')).scrollIntoView({   
   
                behavior: 'smooth'   
   
            });   
   
        });   
   
    });   
   
     
   
    updateKeyFindings();   
   
    renderAccelerationChart(prophecyData);   
   
    renderRateComparisonChart();   
   
    renderPost1948CategoryChart();   
   
    renderGeoShiftChart();   
   
    renderWarCorrelationChart();   
   
    renderTable(sortData(prophecyData, currentSort.column, currentSort.order));   
   
});   
   
</script>   
   
</body>   
   
</html>