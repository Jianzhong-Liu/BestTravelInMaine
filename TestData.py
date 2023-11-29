from GraphStructure import Graph
import networkx as nx
import matplotlib.pyplot as plt
import random


class NodeData:

    simple_circuit_locations = {
        "A": (1, 2),
        "B": (2, 3),
        "C": (3, 4),
        "D": (5, 6),
        "E": (10, 3),
    }

    simple_circuit_edges = [
        ("A", "B"),
        ("B", "C"),
        ("D", "E"),
        ("A", "E"),
        ("C", "D"),
        ("C", "E"),
        ("B", "E")
    ]

    main_city_locations = {
        "Portland": (43.6591, -70.2568),  # Portland, ME
        "Bangor": (44.8016, -68.7712),  # Bangor, ME
        "Augusta": (44.3106, -69.7795),  # Augusta, ME
        "Bar Harbor": (44.3876, -68.2039),  # Bar Harbor, ME
        "Lewiston": (44.1004, -70.2148),  # Lewiston, ME
        "Rockland": (44.1032, -69.1048),  # Rockland, ME
        "Kennebunkport": (43.3617, -70.4764),  # Kennebunkport, ME
        "Acadia National Park": (44.3386, -68.2733) # Acadia National Park, ME
    }

    # Define connections (edges) between cities
    main_city_edges = [
        ("Portland", "Augusta"),
        ("Portland", "Lewiston"),
        ("Portland", "Kennebunkport"),
        ("Bangor", "Augusta"),
        ("Bangor", "Bar Harbor"),
        ("Augusta", "Bangor"),
        ("Bar Harbor", "Acadia National Park"),
        ("Rockland", "Acadia National Park"),
        ("Lewiston", "Rockland"),
        ("Kennebunkport", "Rockland"),
        ("Kennebunkport", "Lewiston")
    ]

    # Generate random nodes
    random_locations = {chr(65 + i): (random.uniform(0, 100), random.uniform(0, 100)) for i in range(20)}

    # Generate random edges between nodes
    random_edges = []
    for i in range(20):
        for j in range(i + 1, 20):
            if random.random() < 0.3:  # Adjust the probability for connections
                random_edges.append((chr(65 + i), chr(65 + j)))


'''
  Store the graph as a static variable
'''


class GraphData:
    main_city_graph = Graph(NodeData.main_city_locations, NodeData.main_city_edges)
    random_graph = Graph(NodeData.random_locations, NodeData.random_edges)
    simple_circuit_graph = Graph(NodeData.simple_circuit_locations, NodeData.simple_circuit_edges)


'''
a method to visualize Graph data
'''


def print_visualized_graph(graph, title="Graph"):
    # Create a new graph, this visualized graph can be printed using nx.draw() and plt.show()
    g = nx.Graph()
    # Add nodes with data to the graph
    node_positions = {}
    for name, node in graph.nodes.items():
        g.add_node(name)
        node_positions[name] = (node.x, node.y)

    # add other edges from the data
    for from_node, to_node_node_list in graph.edges.items():
        for node in to_node_node_list:
            g.add_edge(from_node.name, node.name)

    plt.figure()
    plt.title(title)

    # Draw the graph
    nx.draw(g, pos=node_positions, with_labels=True, node_color='lightblue', edge_color='gray')
    plt.show()


# Print Graph Data in the GraphData class
print_visualized_graph(GraphData.main_city_graph, "City graph")
print_visualized_graph(GraphData.random_graph, "Random Graph")
print_visualized_graph(GraphData.simple_circuit_graph, "Simple Circuit Graph")
