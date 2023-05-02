#!/bin/python
import obsidiantools.api as otools
import networkx as nx
import os
import json

path = os.getcwd()
print(path)

vault = otools.Vault(path).connect()
print(vault)

G = vault.graph  # networkx graph
print(G)

# Convert the graph to a JSON-compatible format
data = nx.readwrite.json_graph.node_link_data(G)

# Save the data as a standard JSON file
with open("graph.json", "w") as f:
    json.dump(data, f, indent=4)

print("saved graph as graph.json")
