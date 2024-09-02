from graph import Graph
from utils import print_travelling_route
from solvers import BnBSolver, DynamicProgrammingSolver, BruteForceSolver
from generators import generate_random_square_matrix
import constants

cities = list({
    "GYE", "UIO", "CUE", "SDO", "DUR", "MCH", "MTA", "PTV", "LOJ", "QVD",}) 

graph = Graph(size=10, random_values=False) 
# graph = Graph(cities=cities)
# graph = Graph(size=10, random_values=False) #<-Para q se repita siempre
graph.show_graph() #<- Funcion para ver el grafo

if __name__ == "__main__":
    is_open_route = constants.RTRN_OPEN_CYCLE  
    print(f"Resolviendo problema del viajero para:\n{graph}\n\n")
    brute_force_results = BruteForceSolver(graph=graph,open_cycle=is_open_route)
    dynamic_prog_solver = DynamicProgrammingSolver(graph=graph,open_cycle=is_open_route)
    bnb_solver = BnBSolver(graph=graph,open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=brute_force_results, open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=dynamic_prog_solver, open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=bnb_solver, open_cycle=is_open_route)
