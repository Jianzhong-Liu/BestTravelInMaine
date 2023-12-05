import TestData
import Hamiltonian
from  Traveling_Salesman import traveling_salesman_timed
from BFS import hamiltonian_path_bfs
from DFS import hamiltonian_path as hamiltonian_path_dfs
from Modify_Dijkstra import hamiltonian_path_dijkstra
import time
import threading

simple_graph = TestData.GraphData.simple_circuit_graph


main_city_graph = TestData.GraphData.main_city_graph


random_graph = TestData.GraphData.random_graph

rectangle_circuit_graph = TestData.GraphData.rectangle_circuit_graph

more_cities_graph = TestData.GraphData.more_city_graph

print("Simple_graph")
Hamiltonian.hamiltonian_circuit_timed(simple_graph, "A")
print("Main_city_graph")
Hamiltonian.hamiltonian_circuit_timed(main_city_graph, "Portland")
print("radom_graph")
Hamiltonian.hamiltonian_circuit_timed(random_graph, "A")
print("rectangle_circuit_graph")
Hamiltonian.hamiltonian_circuit_timed(rectangle_circuit_graph, "A")
print("more cities graph")
Hamiltonian.hamiltonian_circuit_timed(more_cities_graph, "Portland")


print("Simple_graph")
traveling_salesman_timed(simple_graph, "A")
print("Main_city_graph")
traveling_salesman_timed(main_city_graph, "Portland")
print("radom_graph")
traveling_salesman_timed(random_graph, "A")
print("rectangle_circuit_graph")
traveling_salesman_timed(rectangle_circuit_graph, "A")
print("more cities graph")
# traveling_salesman_timed(more_cities_graph, "Portland") it timed out always



timeout_threshold = 60  # 60 seconds threshold

graphs = [
    ("Simple_graph", simple_graph, "A"),
    ("Main_city_graph", main_city_graph, "Portland"),
    ("random_graph", random_graph, "A"),
    ("rectangle_circuit_graph", rectangle_circuit_graph, "A"),
    ("more_cities_graph", more_cities_graph, "Portland")
]
def run_with_timeout(graph, start, timeout):
    # Create a thread to run the hamiltonian_path_bfs function
    bfs_thread = threading.Thread(target=hamiltonian_path_bfs, args=(graph, start))

    # Start the thread
    bfs_thread.start()

    # Wait for the thread to finish or timeout
    bfs_thread.join(timeout)

    # If the thread is still alive after the timeout, it means it didn't finish in time
    if bfs_thread.is_alive():
        print("Timeout")
        return False  # Indicate that we hit the timeout
    else:
        return True  # Indicate that the function finished before the timeout

print("**TESTING BENCHMARK FOR BFS**")
for name, graph, start in graphs:
    print("Testing BFS on", name)
    start_time = time.time()
    
    # Run the function with a timeout
    success = run_with_timeout(graph, start, timeout_threshold)
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    if not success:
        print(f"{name} took too long and was stopped after {timeout_threshold} seconds.")
        print("--------------------------------------------------")
    else:
        print(f"{name} completed in {elapsed_time:.6f} seconds.")
        print("--------------------------------------------------")

def dfs_timeout(graph, start, timeout):
    # Create a thread to run the hamiltonian_path_bfs function
    dfs_thread = threading.Thread(target=hamiltonian_path_dfs, args=(graph, start))

    # Start the thread
    dfs_thread.start()

    # Wait for the thread to finish or timeout
    dfs_thread.join(timeout)

    # If the thread is still alive after the timeout, it means it didn't finish in time
    if dfs_thread.is_alive():
        print("Timeout")
        return False  # Indicate that we hit the timeout
    else:
        return True  # Indicate that the function finished before the timeout

print("**TESTING BENCHMARK FOR DFS**")
for name, graph, start in graphs:
    print("Testing DFS on", name)
    start_time = time.time()
    
    # Run the function with a timeout
    success = dfs_timeout(graph, start, timeout_threshold)
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    if not success:
        print(f"{name} took too long and was stopped after {timeout_threshold} seconds.")
        print("--------------------------------------------------")
    else:
        print(f"{name} completed in {elapsed_time:.6f} seconds.")
        print("--------------------------------------------------")

def djs_timeout(graph, start, timeout):
    # Create a thread to run the hamiltonian_path_bfs function
    djs_thread = threading.Thread(target=hamiltonian_path_dijkstra, args=(graph, start))

    # Start the thread
    djs_thread.start()

    # Wait for the thread to finish or timeout
    djs_thread.join(timeout)

    # If the thread is still alive after the timeout, it means it didn't finish in time
    if djs_thread.is_alive():
        print("Timeout")
        return False  # Indicate that we hit the timeout
    else:
        return True  # Indicate that the function finished before the timeout
    
print("**TESTING BENCHMARK FOR Dijkstra**")
for name, graph, start in graphs:
    print("Testing Dijkstra on", name)
    start_time = time.time()
    
    # Run the function with a timeout
    success = dfs_timeout(graph, start, timeout_threshold)
    
    end_time = time.time()
    elapsed_time = end_time - start_time

    if not success:
        print(f"{name} took too long and was stopped after {timeout_threshold} seconds.")
        print("--------------------------------------------------")
    else:
        print(f"{name} completed in {elapsed_time:.6f} seconds.")
        print("--------------------------------------------------")





