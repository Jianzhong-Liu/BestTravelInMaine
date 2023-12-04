from GraphStructure import Graph, Node
from TestData import GraphData
from collections import deque
import time

def are_neighbors(graph,node1, node_name):

    if node_name in graph.nodes:
        node2 = graph.nodes[node_name]
        return node2 in graph.edges[node1]
    else:
        print(f"Node '{node_name}' not found in the graph.")
        return False
    
def breadth_first_search(graph, start_node_name):

    visited = set()
    queue = deque()

    start_node = graph.nodes.get(start_node_name)
    if start_node:
        queue.append(start_node)
        visited.add(start_node)

        while queue:
            current_node = queue.popleft()
            print(current_node.name)  # Do something with the node, like printing its name

            for neighbor in graph.edges[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
    else:
        print("Start node not found in the graph.")
    

def hamiltonian_path_bfs(graph, start_node_name):
    start_time = time.time()  # Start the timer

    
    queue = deque()
    visited = set()

    # Start by enqueueing a list containing the start node
    start_node = graph.nodes.get(start_node_name)
    if not start_node:
        print("Start node not found in the graph.")
        return

    queue.append((start_node, [start_node_name]))

    while queue:
        current_node, path = queue.popleft()

        # If all nodes have been visited and the path forms a Hamiltonian path
        if len(path) == len(graph.nodes) and are_neighbors(graph, current_node, start_node_name):
            path.append(start_node_name)
            print("Hamiltonian Path:", ' -> '.join(path))
            print_solution(graph, path)
            print("Time taken:", time.time() - start_time)
            return True

        # Enqueue all possible paths that can be formed by adding a neighbor
        for neighbor in graph.edges[current_node]:
            if neighbor.name not in path:  # Check if the neighbor is not in the path already
                new_path = path + [neighbor.name]
                queue.append((neighbor, new_path))

    print("No Hamiltonian Path found starting at", start_node_name)
    print("Time taken:", time.time() - start_time)
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


# Example usage:
graph = GraphData.simple_circuit_graph
res = hamiltonian_path_bfs(graph, "A")

city_graph = GraphData.main_city_graph
city_res = hamiltonian_path_bfs(city_graph, "Portland")

random_graph = GraphData.random_graph
random_res = hamiltonian_path_bfs(random_graph, "A")