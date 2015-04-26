#!/usr/bin/env python3

class Graph:
    def __init__(self):
        self.graph = {}

    def is_empty(self):
        return True if not self.graph else False

    def add(self, node):
        if node in self.graph:
            raise Exception("Node is already in the graph")

        self.graph[node] = set()

    def add_edge(self, node_a, node_b):
        if node_a not in self.graph:
            self.add(node_a)
        elif node_b not in self.graph:
            self.add(node_b)

        self.graph[node_a].add(node_b)

    def get_neighbors_for(self, node):
        neighbours = set()
        all_nodes = self.graph
        for key in all_nodes:
            if key in all_nodes[node] or node in all_nodes[key]:
                neighbours.add(key)

        return list(neighbours)
        # return list(self.graph[node])

    def path_between(self, node_a, node_b):
        visited = set()
        queue = []
        queue.append(node_a)
        visited.add(node_a)
        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == node_b:
                return True

            for neighbour in self.graph[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return False
