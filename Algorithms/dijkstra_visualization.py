#!/usr/bin/env python3
import json
import sys
import networkx as nx
import matplotlib.pyplot as plt


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.G = nx.Graph()
        for link in self.graph["links"]:
            self.G.add_edge(link["source"], link["target"], weight=link["weight"])

        # Calculate the layout once at the beginning
        self.pos = nx.spring_layout(self.G)

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

            # Visualize the current state of the graph
            self.visualize_graph(distances, visited)

        return distances

    def visualize_graph(self, distances, visited):
        # Create a color map for nodes
        node_colors = [
            "green" if node == min(visited, key=lambda x: distances[x]) else "lightblue"
            for node in self.graph["nodes"]
        ]

        # Create a color map for edges
        edge_colors = [
            "green"
            if self.G.edges[edge]["weight"] == distances[edge[1]] - distances[edge[0]]
            else "gray"
            for edge in self.G.edges()
        ]

        # Clear the previous plot
        plt.clf()

        # Draw nodes with colors
        nx.draw(
            self.G,
            self.pos,
            with_labels=True,
            node_color=node_colors,
            node_size=1000,
            font_size=10,
        )

        # Draw edges with colors
        nx.draw(self.G, self.pos, edge_color=edge_colors, width=2)

        # Draw edge labels
        edge_labels = {
            (edge[0], edge[1]): self.G.edges[edge]["weight"] for edge in self.G.edges()
        }
        nx.draw_networkx_edge_labels(
            self.G, self.pos, edge_labels=edge_labels, font_size=8
        )

        # Pause to see the visualization at each step
        plt.pause(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: ", sys.argv[0], "/path/to/graph.json")
        return

    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        data = json.load(f)

    dijkstra = Dijkstra(data)
    # Get the first node in the graph
    start_node = data["nodes"][0]["id"]
    shortest_paths = dijkstra.find_shortest_paths(start_node)

    print("Shortest Paths from", start_node + ":")
    for node, distance in shortest_paths.items():
        print(f"{node}: {distance}")


if __name__ == "__main__":
    main()
