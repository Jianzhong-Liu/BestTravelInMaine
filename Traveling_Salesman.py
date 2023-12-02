import Hamiltonian
import TestData
from GraphStructure import Graph, Node
from TestData import GraphData
import Hamiltonian


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
    cost, path = tsp_util(start_node, set([start_node_name]))
    return cost, path


simple_graph = TestData.GraphData.simple_circuit_graph
result, path = tsp_with_path(simple_graph, "A")
print("Minimum TSP Tour Cost:", result)
print("Tour Path:", " -> ".join(path))

main_city_graph = TestData.GraphData.main_city_graph
result, path = tsp_with_path(main_city_graph, "Portland")
print("Minimum TSP Tour Cost:", result)
print("Tour Path:", " -> ".join(path))

random_graph = TestData.GraphData.random_graph
result, path = tsp_with_path(random_graph, "A")
print("Minimum TSP Tour Cost:", result)
print("Tour Path:", " -> ".join(path))
