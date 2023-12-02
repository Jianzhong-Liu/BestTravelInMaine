from GraphStructure import Graph, Node
from TestData import GraphData
import time

'''
    Check if this vertex is an adjacent vertex 
    of the previously added vertex and is not 
    included in the path earlier 
'''


def is_safe(g: Graph, cur_city: str, path: list[str]) -> bool:
    # Check if current city and last city
    # in path are adjacent

    cur_node = g.nodes[cur_city]

    last_node = g.nodes[path[-1]]

    if last_node not in g.edges[cur_node]:
        return False

    # Check if current city not already in path
    for city in path:
        if city == cur_city:
            return False
    return True

# A recursive utility function to solve
# hamiltonian cycle problem


def ham_cycle_util(g: Graph, path: list[str], cur_city: str, start_city: str) -> bool:

    # base case: if all vertices are
    # included in the path
    if len(path) == len(g.nodes):
        if g.nodes[start_city] in g.edges[g.nodes[path[-1]]]:
            return True
        else:
            return False

    # Try different cities as a next candidate
    for city_name, city_node in g.nodes.items():
        if city_name == start_city:
            continue

        if is_safe(g, city_name, path):
            path.append(city_name)

            if ham_cycle_util(g, path, city_name, start_city):
                return True

            path.pop()

    return False


'''
A method that can print the Path
and calculate the total Distance 
'''


def print_solution(g: Graph, path: list[str]):
    print("Solution Exists: Following is the valid traveling route")

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


def hamiltonian_circuit_timed(g: Graph, start_city: str) -> bool:
    start_time = time.time()  # Capture the start time
    print("Hamiltonian circuit algo is running...")

    path = [start_city]

    if not ham_cycle_util(g, path, start_city, start_city):
        print("Solution doesn't exist\n")
        end_time = time.time()  # Capture the end time
        print(f"Elapsed Time: {end_time - start_time:.4f} seconds\n")
        return False
    path.append(path[0])
    print_solution(g, path)

    end_time = time.time()  # Capture the end time
    print(f"Elapsed Time: {end_time - start_time:.4f} seconds\n")
    return True


# Example usage:
graph = GraphData.simple_circuit_graph
res = hamiltonian_circuit_timed(graph, "A")

city_graph = GraphData.main_city_graph
city_res = hamiltonian_circuit_timed(city_graph, "Portland")

random_graph = GraphData.random_graph
random_res = hamiltonian_circuit_timed(random_graph, "A")

more_graph = GraphData.more_city_graph
more_graph_res = hamiltonian_circuit_timed(more_graph, "Portland")

g = GraphData.rectangle_circuit_graph
hamiltonian_circuit_timed(g, "A")




