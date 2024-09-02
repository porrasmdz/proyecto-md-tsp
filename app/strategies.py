from abc import ABC
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search
from graph import Graph

class TSPSolver(ABC):
    def __init__(self, graph: Graph, open_cycle= False):
        self.graph = graph
        self.name = ""
        if open_cycle:
            self.graph.distance_matrix.to_numpy()[:,0] = 0
    def findRoute(self):
        pass


class BruteForceSolver(TSPSolver):
    def __init__(self, graph: Graph, open_cycle=False):
        super().__init__(graph, open_cycle)
        self.name = "Algoritmo de Fuerza Bruta"
    def findRoute(self):
        permutation, distance = solve_tsp_brute_force(self.graph.get_distance_matrix())
        return (permutation, distance)
    
class NearestNeighborSolver(TSPSolver):    
    def __init__(self, graph: Graph, open_cycle=False):
        super().__init__(graph, open_cycle)
        self.name = "Algoritmo del Vecino Más Cercano"
    def findRoute(self):
        permutation, distance = solve_tsp_local_search(self.graph.get_distance_matrix())
        return (permutation, distance)