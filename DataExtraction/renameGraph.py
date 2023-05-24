#!/usr/bin/env python3
import json
import networkx as nx
import sys


def rename_nodes(graph):
    renamed_graph = nx.relabel_nodes(
        graph, {node: f"node{i+1}" for i, node in enumerate(graph.nodes)}
    )
    return renamed_graph


def save_graph_to_json(graph, file_name):
    data = nx.readwrite.json_graph.node_link_data(graph)
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)


def main():
    # checking for the correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: ", sys.argv[0], "/path/to/graph.json", "/path/to/renamed.json")
        exit(-1)

    # saving the file names
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    # reading the json file
    with open(input_file_name, "r") as f:
        data = json.load(f)

    # creating the graph
    graph = nx.readwrite.json_graph.node_link_graph(data)

    # Rename nodes
    renamed_graph = rename_nodes(graph)

    # Print the renamed graph
    print(renamed_graph.nodes())

    # Save the renamed graph to JSON file
    save_graph_to_json(renamed_graph, output_file_name)


if __name__ == "__main__":
    main()
