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
title: Download necessary NLTK resources
---
   
import os   
import re   
import pandas as pd   
import networkx as nx   
import matplotlib.pyplot as plt   
from collections import Counter   
import seaborn as sns   
from pathlib import Path   
import nltk   
from nltk.tokenize import word_tokenize   
from nltk.corpus import stopwords   
   
# Download necessary NLTK resources   
nltk.download('punkt', quiet=True)   
nltk.download('stopwords', quiet=True)   
   
class PhysicsFaithMapper:   
    def __init__(self, vault_path, output_dir="./output"):   
        self.vault_path = Path(vault_path)   
        self.output_dir = Path(output_dir)   
        self.output_dir.mkdir(exist_ok=True, parents=True)   
           
# Define concept categories   
        self.physics_concepts = [   
            "quantum", "entanglement", "wave", "particle", "field", "energy", "relativity",   
            "gravity", "force", "coherence", "decoherence", "uncertainty", "observer",   
            "photon", "electromagnetic", "nuclear", "strong force", "weak force",   
            "spacetime", "dimension", "string theory", "quantum field", "zero-point",   
            "superposition", "tunneling", "resonance", "interference", "collapse"   
        ]   
           
        self.faith_concepts = [   
            "prayer", "divine", "unity", "spirit", "soul", "faith", "community",   
            "transcendence", "connection", "presence", "revelation", "worship",   
            "holiness", "sacred", "covenant", "communion", "redemption", "creation",   
            "purpose", "meaning", "eternity", "omnipresence", "providence",   
            "wisdom", "love", "truth", "mystery"   
        ]   
           
        self.math_concepts = [   
            "pattern", "symmetry", "equation", "geometry", "fractal", "chaos",    
            "complexity", "probability", "statistics", "information", "entropy",   
            "algorithm", "calculation", "frequency", "amplitude", "oscillation",   
            "vector", "matrix", "transformation", "convergence", "divergence"   
        ]   
           
        self.consciousness_concepts = [   
            "mind", "awareness", "perception", "thought", "intention", "attention",   
            "cognition", "experience", "subjective", "qualia", "conscious", "unconscious",   
            "observation", "mental", "brain", "neural", "cognitive", "memory", "ego",    
            "self", "identity", "will", "choice", "decision", "intuition"   
        ]   
           
# Combine all concepts   
        self.all_concepts = self.physics_concepts + self.faith_concepts + \   
                           self.math_concepts + self.consciousness_concepts   
           
# Store data structures   
        self.file_concepts = {}  # Maps files to concepts   
        self.concept_files = {}  # Maps concepts to files   
        self.concept_connections = {}  # Maps concepts to related concepts   
        self.law_concepts = {}  # Maps each Law to concepts   
        self.concepts_by_category = {   
            "Physics": self.physics_concepts,   
            "Faith": self.faith_concepts,   
            "Mathematics": self.math_concepts,   
            "Consciousness": self.consciousness_concepts   
        }   
           
    def get_category(self, concept):   
        """Return the category of a given concept."""   
        if concept in self.physics_concepts:   
            return "Physics"   
        elif concept in self.faith_concepts:   
            return "Faith"   
        elif concept in self.math_concepts:   
            return "Mathematics"   
        elif concept in self.consciousness_concepts:   
            return "Consciousness"   
        return "Unknown"   
           
    def scan_content(self):   
        """Scan all markdown files in the vault to extract concepts and connections."""   
        print("Scanning content...")   
           
# Initialize concepts for each Law folder   
        law_folders = [d for d in os.listdir(self.vault_path)    
                      if os.path.isdir(os.path.join(self.vault_path, d)) and d.startswith("Law")]   
           
        for law in law_folders:   
            self.law_concepts[law] = set()   
           
# Initialize concept_files dictionary   
        for concept in self.all_concepts:   
            self.concept_files[concept] = []   
           
# Walk through all files   
        for dirpath, dirnames, filenames in os.walk(self.vault_path):   
            for filename in [f for f in filenames if f.endswith('.md')]:   
                filepath = os.path.join(dirpath, filename)   
                rel_path = os.path.relpath(filepath, self.vault_path)   
                   
# Identify which Law this file belongs to (if any)   
                law_match = re.match(r'(Law \d+)', rel_path)   
                current_law = law_match.group(1) if law_match else None   
                   
                try:   
                    with open(filepath, 'r', encoding='utf-8') as file:   
                        content = file.read().lower()   
                           
# Find all concepts in the file   
                        found_concepts = set()   
                        for concept in self.all_concepts:   
# Use word boundary for exact matching   
                            pattern = r'\b' + re.escape(concept.lower()) + r'\b'   
                            if re.search(pattern, content):   
                                found_concepts.add(concept)   
                                self.concept_files[concept].append(rel_path)   
                           
# Store concepts found in this file   
                        self.file_concepts[rel_path] = found_concepts   
                           
# If this file belongs to a Law, add concepts to that Law   
                        if current_law and current_law in self.law_concepts:   
                            self.law_concepts[current_law].update(found_concepts)   
                except Exception as e:   
                    print(f"Error reading {filepath}: {e}")   
           
# Calculate concept connections based on co-occurrence in files   
        for concept1 in self.all_concepts:   
            self.concept_connections[concept1] = {}   
            for concept2 in self.all_concepts:   
                if concept1 != concept2:   
# Find files where both concepts appear   
                    common_files = set(self.concept_files[concept1]) & set(self.concept_files[concept2])   
                    if common_files:   
                        self.concept_connections[concept1][concept2] = len(common_files)   
           
        print(f"Scanning complete. Found concepts in {len(self.file_concepts)} files.")   
           
    def generate_concept_matrix(self):   
        """Generate a matrix showing connections between concepts."""   
        print("Generating concept connection matrix...")   
           
# Create a DataFrame from the concept connections   
        matrix_data = []   
        for concept1 in self.all_concepts:   
            row = {   
                'Concept': concept1,   
                'Category': self.get_category(concept1),   
                'Total Files': len(self.concept_files[concept1])   
            }   
               
# Add connections to other concepts   
            for concept2, strength in self.concept_connections[concept1].items():   
                row[concept2] = strength   
                   
            matrix_data.append(row)   
           
        df = pd.DataFrame(matrix_data)   
           
# Save to CSV   
        matrix_file = self.output_dir / "concept_matrix.csv"   
        df.to_csv(matrix_file, index=False)   
        print(f"Concept matrix saved to {matrix_file}")   
           
        return df   
           
    def analyze_law_connections(self):   
        """Analyze connections between different Laws based on shared concepts."""   
        print("Analyzing Law connections...")   
           
# Create a matrix of Law connections   
        law_connection_data = []   
        laws = list(self.law_concepts.keys())   
           
        for law1 in laws:   
            row = {'Law': law1}   
            concepts1 = self.law_concepts[law1]   
               
            for law2 in laws:   
                if law1 != law2:   
                    concepts2 = self.law_concepts[law2]   
                    shared_concepts = concepts1.intersection(concepts2)   
                    row[law2] = len(shared_concepts)   
                       
# Also store the actual shared concepts for reference   
                    row[f"{law2} Concepts"] = ", ".join(shared_concepts)   
               
            law_connection_data.append(row)   
           
        df = pd.DataFrame(law_connection_data)   
           
# Save to CSV   
        law_matrix_file = self.output_dir / "law_connections.csv"   
        df.to_csv(law_matrix_file, index=False)   
        print(f"Law connection matrix saved to {law_matrix_file}")   
           
        return df   
           
    def visualize_concept_network(self, min_connection_strength=2):   
        """Create a network visualization of connected concepts."""   
        print("Visualizing concept network...")   
           
        G = nx.Graph()   
           
# Add nodes with category attribute   
        for concept in self.all_concepts:   
            if self.concept_files[concept]:  # Only include concepts that appear in files   
                G.add_node(concept, category=self.get_category(concept))   
           
# Add edges for connections   
        for concept1, connections in self.concept_connections.items():   
            for concept2, strength in connections.items():   
                if strength >= min_connection_strength:   
                    G.add_edge(concept1, concept2, weight=strength)   
           
# Remove isolated nodes   
        G.remove_nodes_from(list(nx.isolates(G)))   
           
        if len(G.nodes) == 0:   
            print("No connections meet the minimum strength criteria.")   
            return   
           
# Set up the plot   
        plt.figure(figsize=(20, 16))   
           
# Define position layout   
        pos = nx.spring_layout(G, k=0.3, seed=42)   
           
# Define colors for categories   
        color_map = {   
            "Physics": "blue",   
            "Faith": "gold",   
            "Mathematics": "green",   
            "Consciousness": "purple",   
            "Unknown": "gray"   
        }   
           
# Draw nodes by category   
        for category, color in color_map.items():   
            node_list = [node for node, data in G.nodes(data=True)    
                         if data.get('category') == category]   
            if node_list:   
                nx.draw_networkx_nodes(G, pos,    
                                     nodelist=node_list,   
                                     node_color=color,   
                                     node_size=500,   
                                     alpha=0.8,   
                                     label=category)   
           
# Draw edges with varying width based on connection strength   
        edge_widths = [G[u][v]['weight'] * 0.5 for u, v in G.edges()]   
        nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.5)   
           
# Draw labels with adjusted font size based on degree   
        node_degrees = dict(G.degree())   
        labels = {node: node for node in G.nodes()}   
        nx.draw_networkx_labels(G, pos, labels,    
                              font_size=10,   
                              font_family='sans-serif')   
           
        plt.axis('off')   
        plt.title('Concept Connection Network (min strength: {})'.format(min_connection_strength))   
        plt.legend(scatterpoints=1)   
           
# Save the figure   
        network_file = self.output_dir / f"concept_network_{min_connection_strength}.png"   
        plt.savefig(network_file, dpi=300, bbox_inches='tight')   
        plt.close()   
        print(f"Network visualization saved to {network_file}")   
           
    def visualize_law_concept_distribution(self):   
        """Create a heatmap showing concepts distribution across Laws."""   
        print("Visualizing concept distribution across Laws...")   
           
# Prepare data for heatmap   
        laws = list(self.law_concepts.keys())   
        categories = list(self.concepts_by_category.keys())   
           
# Count concepts by category for each law   
        distribution_data = []   
        for law in laws:   
            law_concepts = self.law_concepts[law]   
            row = {'Law': law}   
               
            for category in categories:   
                category_concepts = set(self.concepts_by_category[category])   
                count = len(law_concepts.intersection(category_concepts))   
                row[category] = count   
                   
            distribution_data.append(row)   
           
        df = pd.DataFrame(distribution_data)   
           
# Create a pivot table for the heatmap   
        pivot_df = df.set_index('Law')   
           
# Plot the heatmap   
        plt.figure(figsize=(12, 8))   
        sns.heatmap(pivot_df, annot=True, cmap="YlGnBu", fmt='d', cbar_kws={'label': 'Concept Count'})   
        plt.title('Concept Distribution by Category Across Laws')   
        plt.tight_layout()   
           
# Save the figure   
        heatmap_file = self.output_dir / "law_concept_distribution.png"   
        plt.savefig(heatmap_file, dpi=300)   
        plt.close()   
        print(f"Concept distribution heatmap saved to {heatmap_file}")   
           
        return df   
           
    def identify_cross_domain_insights(self):   
        """Identify meaningful connections between physics and faith concepts."""   
        print("Identifying cross-domain insights...")   
           
        insights = []   
           
# Look for strong connections between physics and faith concepts   
        for physics_concept in self.physics_concepts:   
            if physics_concept not in self.concept_connections:   
                continue   
                   
            for faith_concept in self.faith_concepts:   
                if faith_concept in self.concept_connections[physics_concept]:   
                    strength = self.concept_connections[physics_concept][faith_concept]   
                    if strength >= 2:  # Minimum threshold for meaningful connection   
                        common_files = set(self.concept_files[physics_concept]) & set(self.concept_files[faith_concept])   
                        insight = {   
                            'Physics Concept': physics_concept,   
                            'Faith Concept': faith_concept,   
                            'Connection Strength': strength,   
                            'Common Files': list(common_files)   
                        }   
                        insights.append(insight)   
           
# Sort by connection strength   
        insights.sort(key=lambda x: x['Connection Strength'], reverse=True)   
           
# Save insights to CSV   
        insights_df = pd.DataFrame(insights)   
        if not insights_df.empty:   
            insights_file = self.output_dir / "cross_domain_insights.csv"   
            insights_df.to_csv(insights_file, index=False)   
            print(f"Cross-domain insights saved to {insights_file}")   
        else:   
            print("No strong cross-domain connections found.")   
           
        return insights   
           
    def generate_concept_frequency_report(self):   
        """Generate a report on concept frequency across all content."""   
        print("Generating concept frequency report...")   
           
# Count file appearances for each concept   
        concept_counts = {concept: len(files) for concept, files in self.concept_files.items() if files}   
           
# Convert to DataFrame   
        freq_data = []   
        for concept, count in concept_counts.items():   
            freq_data.append({   
                'Concept': concept,   
                'Category': self.get_category(concept),   
                'Frequency': count   
            })   
           
        df = pd.DataFrame(freq_data)   
        df = df.sort_values(by='Frequency', ascending=False)   
           
# Save to CSV   
        freq_file = self.output_dir / "concept_frequency.csv"   
        df.to_csv(freq_file, index=False)   
        print(f"Concept frequency report saved to {freq_file}")   
           
# Create visualization   
        plt.figure(figsize=(14, 10))   
           
# Group by category   
        category_data = df.groupby('Category').agg({'Frequency': 'sum'}).reset_index()   
           
# Plot frequency by category   
        plt.subplot(2, 1, 1)   
        sns.barplot(x='Category', y='Frequency', data=category_data)   
        plt.title('Total Concept Frequency by Category')   
        plt.ylabel('Total Appearances')   
           
# Plot top 15 concepts   
        plt.subplot(2, 1, 2)   
        top_concepts = df.head(15)   
        sns.barplot(x='Concept', y='Frequency', data=top_concepts, hue='Category', dodge=False)   
        plt.title('Top 15 Most Frequent Concepts')   
        plt.ylabel('Appearances in Files')   
        plt.xticks(rotation=45, ha='right')   
           
        plt.tight_layout()   
           
# Save the figure   
        freq_viz_file = self.output_dir / "concept_frequency_visualization.png"   
        plt.savefig(freq_viz_file, dpi=300)   
        plt.close()   
        print(f"Concept frequency visualization saved to {freq_viz_file}")   
           
        return df   
           
    def suggest_new_connections(self):   
        """Suggest potential new connections based on patterns in existing content."""   
        print("Suggesting new connections...")   
           
        suggestions = []   
           
# Get all physics-faith concept pairs that already appear together   
        existing_pairs = set()   
        for physics_concept in self.physics_concepts:   
            if physics_concept not in self.concept_connections:   
                continue   
                   
            for faith_concept in self.faith_concepts:   
                if faith_concept in self.concept_connections[physics_concept] and \   
                   self.concept_connections[physics_concept][faith_concept] > 0:   
                    existing_pairs.add((physics_concept, faith_concept))   
           
# For each physics concept, find similar physics concepts based on shared faith connections   
        for physics1 in self.physics_concepts:   
            if physics1 not in self.concept_connections:   
                continue   
                   
# Get faith concepts connected to physics1   
            faith_connections1 = {fc for fc in self.faith_concepts    
                               if fc in self.concept_connections[physics1] and    
                               self.concept_connections[physics1][fc] > 0}   
               
            if not faith_connections1:   
                continue   
                   
            for physics2 in self.physics_concepts:   
                if physics2 == physics1 or physics2 not in self.concept_connections:   
                    continue   
                       
# Get faith concepts connected to physics2   
                faith_connections2 = {fc for fc in self.faith_concepts    
                                   if fc in self.concept_connections[physics2] and    
                                   self.concept_connections[physics2][fc] > 0}   
                   
                if not faith_connections2:   
                    continue   
                   
# Find shared faith connections   
                shared_faith = faith_connections1.intersection(faith_connections2)   
                   
                if shared_faith:   
# Look for faith concepts connected to physics2 but not to physics1   
                    for faith_concept in faith_connections2 - faith_connections1:   
                        if (physics1, faith_concept) not in existing_pairs:   
                            suggestion = {   
                                'Physics Concept': physics1,   
                                'Faith Concept': faith_concept,   
                                'Similar Physics Concept': physics2,   
                                'Shared Faith Connections': list(shared_faith),   
                                'Confidence': len(shared_faith) / len(faith_connections2)   
                            }   
                            suggestions.append(suggestion)   
           
# Sort by confidence   
        suggestions.sort(key=lambda x: x['Confidence'], reverse=True)   
           
# Take top 20 suggestions   
        top_suggestions = suggestions[:20] if len(suggestions) > 20 else suggestions   
           
# Save suggestions to CSV   
        if top_suggestions:   
            suggestions_df = pd.DataFrame(top_suggestions)   
            suggestions_file = self.output_dir / "connection_suggestions.csv"   
            suggestions_df.to_csv(suggestions_file, index=False)   
            print(f"Connection suggestions saved to {suggestions_file}")   
        else:   
            print("No new connection suggestions found.")   
           
        return top_suggestions   
       
    def run_analysis(self):   
        """Run the full analysis pipeline."""   
        self.scan_content()   
        self.generate_concept_matrix()   
        self.analyze_law_connections()   
        self.visualize_concept_network(min_connection_strength=2)   
        self.visualize_law_concept_distribution()   
        self.generate_concept_frequency_report()   
        self.identify_cross_domain_insights()   
        self.suggest_new_connections()   
           
# Print summary   
        total_concepts = sum(1 for c in self.all_concepts if self.concept_files[c])   
        print(f"\nAnalysis complete! Found {total_concepts} active concepts across your content.")   
        print(f"All outputs saved to {self.output_dir}")   
           
# Calculate category distribution   
        category_counts = {}   
        for concept in self.all_concepts:   
            if self.concept_files[concept]:   
                category = self.get_category(concept)   
                category_counts[category] = category_counts.get(category, 0) + 1   
           
        print("\nConcept distribution by category:")   
        for category, count in category_counts.items():   
            print(f"  {category}: {count} concepts")   
           
# Print top 5 most frequent concepts   
        concept_counts = {c: len(files) for c, files in self.concept_files.items() if files}   
        top_concepts = sorted(concept_counts.items(), key=lambda x: x[1], reverse=True)[:5]   
           
        print("\nTop 5 most frequent concepts:")   
        for concept, count in top_concepts:   
            print(f"  {concept} ({self.get_category(concept)}): {count} files")   
   
# Example usage   
if __name__ == "__main__":   
    vault_path = input("Enter the path to your vault: ")   
    mapper = PhysicsFaithMapper(vault_path)   
    mapper.run_analysis()