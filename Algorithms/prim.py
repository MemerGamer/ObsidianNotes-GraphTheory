#!/usr/bin/env python3
import json
import sys
from heapq import heappop, heappush


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        self._priorities = {}

    def empty(self):
        return len(self._queue) == 0

    def put(self, item, priority):
        heappush(self._queue, (priority, self._index, item))
        self._index += 1
        self._priorities[item] = priority

    def get(self):
        return heappop(self._queue)[2]

    def get_priority(self, item):
        return self._priorities.get(item)


def prims_algorithm(graph):
    start_node = graph["nodes"][0]["id"]
    visited = set()
    mst = []
    pq = PriorityQueue()

    # Add the start node to the priority queue with priority 0
    pq.put(start_node, 0)

    while not pq.empty():
        current_node = pq.get()

        if current_node in visited:
            continue

        visited.add(current_node)

        # Find the minimum-weight edge from the current node to its neighbors
        neighbors = get_neighbors(graph, current_node)
        for neighbor, weight in neighbors:
            if neighbor not in visited:
                # Update the priority if a shorter path to the neighbor is found
                if pq.get_priority(neighbor) is None or weight < pq.get_priority(
                    neighbor
                ):
                    pq.put(neighbor, weight)
                    mst.append((current_node, neighbor, weight))

    return mst


def get_neighbors(graph, node):
    neighbors = []
    for link in graph["links"]:
        if "weight" in link:
            if link["source"] == node:
                target = link["target"]
                weight = link["weight"]
                neighbors.append((target, weight))
            elif link["target"] == node:
                source = link["source"]
                weight = link["weight"]
                neighbors.append((source, weight))
        else:
            if link["source"] == node:
                target = link["target"]
                neighbors.append((target, 1))
            elif link["target"] == node:
                source = link["source"]
                neighbors.append((source, 1))
    return neighbors


def main():
    if len(sys.argv) < 2:
        print("Usage: ", sys.argv[0], "/path/to/graph.json")
        return

    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        data = json.load(f)

    mst = prims_algorithm(data)
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(f"{edge[0]} -- {edge[1]}")


if __name__ == "__main__":
    main()
