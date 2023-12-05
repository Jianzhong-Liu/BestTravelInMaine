import TestData
import Hamiltonian
from  Traveling_Salesman import traveling_salesman_timed

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









