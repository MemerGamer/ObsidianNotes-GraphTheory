#!/bin/env python3

import sys
import networkx as nx
import json
from collections import OrderedDict


def count_edges(graph):
    edge_counts = {}

    for link in graph["links"]:
        source = link["source"]
        target = link["target"]
        edge = (source, target)

        if edge in edge_counts:
            edge_counts[edge] += 1
        else:
            edge_counts[edge] = 1

    for link in graph["links"]:
        source = link["source"]
        target = link["target"]
        edge = (source, target)

        if edge in edge_counts:
            link["weight"] = edge_counts[edge]

    return graph


def save_graph_to_json(graph, file_name):
    G = nx.readwrite.json_graph.node_link_graph(graph)
    data = nx.readwrite.json_graph.node_link_data(G)
    reordered_data = reorder_json_keys(data)
    with open(file_name, "w") as f:
        json.dump(reordered_data, f, indent=4)


def reorder_json_keys(data):
    ordered_data = {
        "directed": data["directed"],
        "multigraph": data["multigraph"],
        "graph": data["graph"],
        "nodes": data["nodes"],
        "links": [],
    }

    for link in data["links"]:
        ordered_link = {
            "source": link["source"],
            "target": link["target"],
            "key": link["key"],
            "weight": link["weight"],
        }
        ordered_data["links"].append(ordered_link)

    return ordered_data


def main():
    # saving the file names
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    with open(input_file_name, "r") as f:
        data = json.load(f)

    updated_graph = count_edges(data)

    # Print the updated graph with edge weights
    print(json.dumps(updated_graph, indent=4))

    # Save the renamed graph to JSON file
    save_graph_to_json(updated_graph, output_file_name)


if __name__ == "__main__":
    main()
