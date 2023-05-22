#!/usr/bin/env python3
import json
import sys


class UnionFind:
    def __init__(self, nodes):
        self.parent = {}
        self.rank = {}

        for node in nodes:
            node_id = node["id"]
            self.parent[node_id] = node_id
            self.rank[node_id] = 0

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskals_algorithm(graph):
    edges = []
    for link in graph["links"]:
        source = link["source"]
        target = link["target"]
        weight = 1  # Assuming all edges have the same weight
        edges.append((source, target, weight))

    edges.sort(key=lambda x: x[2])  # Sort edges by weight

    mst = []
    uf = UnionFind(graph["nodes"])

    for edge in edges:
        source, target, weight = edge
        if uf.find(source) != uf.find(target):
            uf.union(source, target)
            mst.append(edge)

    return mst


def main():
    if len(sys.argv) < 2:
        print("Usage: ", sys.argv[0], "/path/to/graph.json")
        return

    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        data = json.load(f)

    mst = kruskals_algorithm(data)
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} -- {edge[1]}")


if __name__ == "__main__":
    main()
