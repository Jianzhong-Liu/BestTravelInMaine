from GraphStructure import Graph, Node
from TestData import GraphData
import time
def depth_first_search(graph, start_node_name):
    visited = set()

    def dfs_helper(node):
        visited.add(node)
        print(node.name)  # Do something with the node, like printing its name

        for neighbor in graph.edges[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    start_node = graph.nodes.get(start_node_name)
    if start_node:
        dfs_helper(start_node)
    else:
        print("Start node not found in the graph.")


def are_neighbors(graph,node1, node_name):
    if node_name in graph.nodes:
        node2 = graph.nodes[node_name]
        return node2 in graph.edges[node1]
    else:
        print(f"Node '{node_name}' not found in the graph.")
        return False
'''
A method that can print the Path
and calculate the total Distance 
'''
def print_solution(g: Graph, path: list[str]):

    total_distance = 0
    pre_node = None
    for vertex in path:
        if pre_node:
            total_distance += g.get_distance(pre_node, g.nodes[vertex])
        pre_node = g.nodes[vertex]
    print("Total Distance is", total_distance, "\n")

def hamiltonian_path(graph, start_node_name):
    start_time = time.time()  # Start the timer

    path = []
    visited = set()

    def dfs_helper(node):
        visited.add(node)
        path.append(node.name)

        # If all nodes have been visited and the path forms a Hamiltonian path
        if len(visited) == len(graph.nodes) and are_neighbors(graph, node, start_node_name):
            path.append(start_node_name)
            print("Hamiltonian Path:", ' -> '.join(path))

            print_solution(graph, path)
            print("Time taken:", time.time() - start_time)
            return True  # Return True indicating success

        for neighbor in graph.edges[node]:
            if neighbor not in visited:
                if dfs_helper(neighbor):  # If a path is found, return True
                    return True
                visited.remove(neighbor)  # Backtrack

        path.pop()  # Remove the node from the path if the path is not Hamiltonian
        return False  # Return False indicating that the path was not found

    start_node = graph.nodes.get(start_node_name)
    if start_node:
        if not dfs_helper(start_node):

            print("Time taken:", time.time() - start_time)
            print("No Hamiltonian Path found starting at", start_node_name)
    else:
        
        print("Start node not found in the graph.")


# Example usage:
# graph = GraphData.simple_circuit_graph
# res = hamiltonian_path(graph, "A")

# city_graph = GraphData.main_city_graph
# city_res = hamiltonian_path(city_graph, "Portland")

# random_graph = GraphData.random_graph
# random_res = hamiltonian_path(random_graph, "A")