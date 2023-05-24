#!/usr/bin/env python3
import json
import sys


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def find_shortest_paths(self, start_node):
        distances = {node["id"]: float("inf") for node in self.graph["nodes"]}
        distances[start_node] = 0
        visited = set()

        while len(visited) < len(self.graph["nodes"]):
            min_distance = float("inf")
            min_node = None

            for node in self.graph["nodes"]:
                node_id = node["id"]
                if node_id not in visited and distances[node_id] < min_distance:
                    min_distance = distances[node_id]
                    min_node = node_id

            if min_node is None:
                break

            visited.add(min_node)

            for link in self.graph["links"]:
                source = link["source"]
                target = link["target"]
                try:
                    weight = link["weight"]
                except KeyError:
                    weight = 1  # Assuming all edges have the same weight

                if source == min_node and target not in visited:
                    new_distance = distances[min_node] + weight
                    if new_distance < distances[target]:
                        distances[target] = new_distance

        return distances


def main():
    if len(sys.argv) < 2:
        print("Usage: ", sys.argv[0], "/path/to/graph.json")
        return

    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        data = json.load(f)

    dijkstra = Dijkstra(data)
    # Get the first ndode in the graph
    start_node = data["nodes"][0]["id"]
    shortest_paths = dijkstra.find_shortest_paths(start_node)

    print("Shortest Paths from", start_node + ":")
    for node, distance in shortest_paths.items():
        print(f"{node}: {distance}")


if __name__ == "__main__":
    main()
