#!/usr/bin/env python3
import json
import networkx as nx
import sys


def check_bipartite(graph):
    visited = {}
    for node in graph.nodes:
        if node not in visited:
            visited[node] = 0  # Assign 0 to the starting node
            queue = [node]
            while queue:
                current = queue.pop(0)
                for neighbor in graph.neighbors(current):
                    if neighbor not in visited:
                        visited[neighbor] = (
                            1 - visited[current]
                        )  # Assign opposite color
                        queue.append(neighbor)
                    elif visited[neighbor] == visited[current]:
                        return False
    return True


def check_stability(graph):
    if check_bipartite(graph):
        print("The graph is stable (bipartite).")
    else:
        print("The graph is unstable (not bipartite).")


def main():
    if len(sys.argv) < 2:
        print("Usage: ", sys.argv[0], "/path/to/graph.json")
        return

    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        data = json.load(f)

    graph = nx.readwrite.json_graph.node_link_graph(data)
    check_stability(graph)


if __name__ == "__main__":
    main()
