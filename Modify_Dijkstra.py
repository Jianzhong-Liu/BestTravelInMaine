from GraphStructure import Graph, Node
from TestData import GraphData
import heapq

def modified_dijkstra(graph, start_city):
    visited = {start_city}
    current_city = start_city
    tour = [start_city]
    total_distance = 0

    while len(visited) < len(graph.nodes):
        distances = {node.name: float('infinity') for node in graph.nodes.values() if node.name not in visited}
        distances[current_city] = 0
        priority_queue = [(0, current_city)]

        while priority_queue:
            current_distance, current_city = heapq.heappop(priority_queue)

            if current_city not in visited:
                tour.append(current_city)
                total_distance += current_distance
                visited.add(current_city)
                break

            for neighbor_node in graph.edges[graph.nodes[current_city]]:
                if neighbor_node.name in visited:
                    continue
                distance = current_distance + graph.get_distance(graph.nodes[current_city], neighbor_node)
                if distance < distances[neighbor_node.name]:
                    distances[neighbor_node.name] = distance
                    heapq.heappush(priority_queue, (distance, neighbor_node.name))

    # Add the distance from the last city back to the start
    total_distance += graph.get_distance(graph.nodes[tour[-1]], graph.nodes[start_city])
    tour.append(start_city)

    return tour, total_distance


# graph = GraphData.simple_circuit_graph
# tour, total_distance = modified_dijkstra(graph, "A")
# print("Tour:", " -> ".join(tour))
# print("Total Distance:", total_distance)
# main_city_graph = GraphData.main_city_graph
# tour, total_distance = modified_dijkstra(main_city_graph, "Portland")
# print("Tour:", " -> ".join(tour))
# print("Total Distance:", total_distance)
# print("++++++")
# random_graph = GraphData.random_graph
# tour, total_distance = modified_dijkstra(random_graph,"A")
# print("Tour:", " -> ".join(tour))
# print("Total Distance:", total_distance)
# print("=====")