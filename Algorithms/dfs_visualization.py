#!/usr/bin/env python3
import json
import networkx as nx
import sys
import matplotlib.pyplot as plt


def dfs_with_visualization(graph, start, visited):
    stack = [start]
    visited.add(start)

    # Create a visualization of the graph
    pos = nx.spring_layout(graph)
    fig, ax = plt.subplots()
    plt.pause(1)  # Delay the start of the animation by 1 second

    while stack:
        node = stack.pop()
        print(node)
        neighbors = list(graph.successors(node))
        neighbors.reverse()  # Reverse the order of neighbors

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

        # Draw the graph with visited nodes in a different color
        node_colors = [
            "lightblue" if n not in visited else "green" for n in graph.nodes()
        ]
        nx.draw(
            graph, pos, with_labels=True, node_color=node_colors, node_size=1000, ax=ax
        )
        plt.pause(0.5)  # Add a pause to see the visualization at each step


def main():
    if len(sys.argv) < 2:
        print("Usage: ", sys.argv[0], "/path/to/graph.json")
        return

    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        data = json.load(f)

    graph = nx.readwrite.json_graph.node_link_graph(data)

    visited = set()
    # Delay the start of the animation by 1 second
    plt.pause(1)

    for node in graph.nodes:
        if node not in visited:
            dfs_with_visualization(graph, node, visited)

    # Display the final visualization
    plt.show()


if __name__ == "__main__":
    main()
