from abc import ABC, abstractmethod
from decimal import Decimal
import time
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search
from stopit import ThreadingTimeout
import math
from graph import Graph
import constants

class TimeoutException(Exception):
    pass

class TSPSolver(ABC):
    def __init__(self, graph: Graph, open_cycle= False, timeout=10):
        self.graph = graph
        self.timeout = timeout #En segundos
        self.name = ""
        if open_cycle:
            self.graph.distance_matrix.to_numpy()[:,0] = 0
        self.last_execution_time = 0  
    
    @abstractmethod
    def findRoute(self ):
        pass

    def timedFindRoute(self):
        print("Ejecutando algoritmo")
        start_time = time.time()
        with ThreadingTimeout(constants.ALGORITHM_TIMEOUT) as timeout_ctx:
            try:
                result = self.findRoute()
            except:
                size = self.graph.distance_matrix.shape[0]
                print("Tiempo de espera agotado. Muchas iteraciones")
                print(f"El algoritmo necesitaria iterar: {size}! = {'%.2E' % Decimal(math.factorial(size))} veces")
                print("AJUSTE EL TIEMPO DE ESPERA O UTILICE OTRO ALGORITMO")
                return None
            finally:
                end_time = time.time()
                execution_time = end_time - start_time
                self.last_execution_time = execution_time
                
        end_time = time.time()
        execution_time = end_time - start_time
        self.last_execution_time = execution_time
            
        return result
    



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