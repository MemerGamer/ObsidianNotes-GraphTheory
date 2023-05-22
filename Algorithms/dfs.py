#!/usr/bin/env python3
import json
import networkx as nx
import sys


def dfs(graph, start, visited):
    stack = [start]
    visited.add(start)
    while stack:
        node = stack.pop()
        print(node)
        neighbors = list(graph.successors(node))
        neighbors.reverse()  # Reverse the order of neighbors
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)


def main():
    if len(sys.argv) < 2:
        print("Usage: ", sys.argv[0], "/path/to/graph.json")
        return

    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        data = json.load(f)

    graph = nx.readwrite.json_graph.node_link_graph(data)

    visited = set()
    for node in graph.nodes:
        if node not in visited:
            dfs(graph, node, visited)


if __name__ == "__main__":
    main()
