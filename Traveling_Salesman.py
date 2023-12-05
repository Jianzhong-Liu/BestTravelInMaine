import TestData
from GraphStructure import Graph, Node
import time
from TestData import GraphData


def tsp_with_path(graph, start_node_name):
    memo = {}

    def tsp_util(current_node, visited):
        if len(visited) == len(graph.nodes) and graph.get_distance(current_node, start_node):
            return graph.get_distance(current_node, start_node), [current_node.name, start_node.name]

        visited_key = tuple(sorted(visited))
        if (current_node, visited_key) in memo:
            return memo[(current_node, visited_key)]

        min_cost = float('inf')
        min_path = []

        for neighbor in graph.edges[current_node]:
            if neighbor.name not in visited:
                visited.add(neighbor.name)
                cost, path = tsp_util(neighbor, visited)
                cost += graph.get_distance(current_node, neighbor)
                visited.remove(neighbor.name)

                if cost < min_cost:
                    min_cost = cost
                    min_path = [current_node.name] + path

        memo[(current_node, visited_key)] = (min_cost, min_path)
        return min_cost, min_path

    start_node = graph.nodes[start_node_name]
    print("Tsp algo is running...")
    cost, path = tsp_util(start_node, set([start_node_name]))
    return cost, path


def print_solution(g: Graph, path: list[str]):

    edge_number = 0

    for edge_list in g.edges.values():
        edge_number += len(edge_list)

    print("Solution Exists: Following is the valid traveling route for the number of", len(g.nodes), "nodes and", edge_number, "edges")

    total_distance = 0
    pre_node = None
    path_str = ""

    for i, vertex in enumerate(path):
        if pre_node:
            total_distance += g.get_distance(pre_node, g.nodes[vertex])
        pre_node = g.nodes[vertex]

        # Add city to path string, avoid adding arrow after last city
        if i < len(path) - 1:
            path_str += vertex + " -> "
        else:
            path_str += vertex

    print(path_str)
    print("Total Distance is", total_distance)


def traveling_salesman_timed(g: Graph, start_city: str) -> bool:
    start_time = time.time()  # Capture the start time
    res, path = tsp_with_path(g, start_city)

    if len(path) != len(g.nodes) + 1:
        print("Solution doesn't exist\n")
        end_time = time.time()  # Capture the end time
        print(f"Elapsed Time: {end_time - start_time:.4f} seconds\n")
        return False

    print_solution(g, path)
    end_time = time.time()  # Capture the end time
    print(f"Elapsed Time: {end_time - start_time:.4f} seconds\n")
    return True


simple_graph = TestData.GraphData.simple_circuit_graph


main_city_graph = TestData.GraphData.main_city_graph


random_graph = TestData.GraphData.random_graph

rectangle_circuit_graph = TestData.GraphData.rectangle_circuit_graph

more_cities_graph = TestData.GraphData.more_city_graph

# traveling_salesman_timed(simple_graph, "A")
# traveling_salesman_timed(main_city_graph, "Portland")
# traveling_salesman_timed(random_graph, "A")
# traveling_salesman_timed(rectangle_circuit_graph, "A")
# traveling_salesman_timed(more_cities_graph, "Portland")