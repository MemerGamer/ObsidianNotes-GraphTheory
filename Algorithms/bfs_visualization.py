#!/usr/bin/env python3
import json
import networkx as nx
import sys
import matplotlib.pyplot as plt
import time


def bfs_with_visualization(graph, start, visited):
    queue = [start]
    visited.add(start)

    # Create a visualization of the graph
    pos = nx.spring_layout(graph)
    fig, ax = plt.subplots()
    plt.pause(1)  # Delay the start of the animation by 1 second

    while queue:
        node = queue.pop(0)
        print(node)
        neighbors = graph.successors(node)

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

        # Draw the graph with visited nodes in a different color
        node_colors = [
            "lightblue" if n not in visited else "green" for n in graph.nodes()
        ]
        nx.draw(
            graph, pos, with_labels=True, node_color=node_colors, node_size=1000, ax=ax
        )
        plt.pause(0.5)  # Add a pause to see the visualization at each step


def main():
    # checking for the correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: ", sys.argv[0], "/path/to/graph.json")
        exit(-1)

    # saving the file name
    file_name = sys.argv[1]

    # reading the json file
    with open(file_name, "r") as f:
        data = json.load(f)

    # creating the graph
    graph = nx.readwrite.json_graph.node_link_graph(data)

    visited = set()
    # Delay the start of the animation by 1 second
    time.sleep(1)

    # for disconnected graphs

    # since the graph created from my notes is disconnected, I will call this method as a default
    for node in graph.nodes():
        if node not in visited:
            bfs_with_visualization(graph, node, visited)

    # Display the final visualization
    plt.show()


if __name__ == "__main__":
    main()
