#!/bin/env python3
import json
import networkx as nx
import matplotlib.pyplot as plt
import sys

# Checking for the correct number of arguments
if len(sys.argv) < 2:
    print("Usage: ", sys.argv[0], "/path/to/graph.json")
    exit(-1)

# Get the path to the JSON file
path = sys.argv[1]

# Load the graph from the JSON file
with open(path, "r") as f:
    data = json.load(f)

# Create a NetworkX graph from the data
G = nx.readwrite.json_graph.node_link_graph(data)

# Set up the plot
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 8))

# Draw the nodes and edges of the graph
nx.draw_networkx_nodes(G, pos, node_size=200, alpha=0.8)
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5)

# Label the nodes with their titles
labels = {node["id"]: node["id"] for node in data["nodes"]}
nx.draw_networkx_labels(G, pos, labels, font_size=10, font_family="sans-serif")

# Show the plot
plt.axis("off")
plt.tight_layout()
plt.show()
