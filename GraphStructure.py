import math

'''
Node Structure and Graph structure for data 
Define a class for nodes with name, x, and y coordinates
'''


class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distance_to(self, other_node):
        return math.sqrt((self.x - other_node.x) ** 2 + (self.y - other_node.y) ** 2)


'''
Define a class for the graph structure
'''


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = {}
        self.edges = {}

        # Add nodes to the graph
        for city, coords in nodes.items():
            self.add_node(Node(city, coords[0], coords[1]))

        # Add edges to the graph
        for from_city, to_city in edges:
            self.add_edge(self.nodes[from_city], self.nodes[to_city])

    # Add nodes to the graph
    def add_node(self, node):
        self.nodes[node.name] = node
        self.edges[node] = []

    # Add edges to the graph
    def add_edge(self, from_node, to_node):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)

    def get_distance(self, from_node, to_node):
        if from_node.name in self.nodes and to_node.name in self.nodes:
            return from_node.distance_to(to_node)
        else:
            return None

    def __str__(self):
        graph_str = "Graph:\n"
        for node in self.edges:
            connections = ", ".join([f"{neighbor.name} (distance: {self.get_distance(self.nodes[node.name], neighbor):.2f})"
                                     for neighbor in self.edges[node]])
            graph_str += f"{node.name} -> {connections}\n"
        return graph_str
