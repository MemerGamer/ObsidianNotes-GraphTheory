#!/usr/bin/env python3
import json
import networkx as nx
import sys


def bfs(graph, start, visited):
    queue = [start]
    visited.add(start)
    while queue:
        node = queue.pop(0)
        print(node)
        neighbors = graph.successors(node)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def main():
    # checking for the correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: ", sys.argv[0], "/path/to/graph.json")
        exit(-1)

    # saving the file name
    file_name = sys.argv[1]

    # reading the json file
    with open(file_name, 'r') as f:
        data = json.load(f)

    # creating the graph
    graph = nx.readwrite.json_graph.node_link_graph(data)

    visited = set()
    # for connected graphs
    # bfs(graph, list(graph.nodes())[0], visited)

    # for disconnected graphs

    # since the graph created from my notes is disconnected i will call this method as a default
    for node in graph.nodes():
        if node not in visited:
            bfs(graph, node, visited)


if __name__ == '__main__':
    main()
