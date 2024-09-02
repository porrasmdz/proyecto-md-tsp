from abc import ABC, abstractmethod
from decimal import Decimal
import time
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force, solve_tsp_branch_and_bound
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search, solve_tsp_record_to_record
from stopit import ThreadingTimeout
import math
from graph import Graph
import constants

class TimeoutException(Exception):
    pass

class TSPSolver(ABC):
    def __init__(self, graph: Graph,open_cycle= False, timeout=10):
        self.graph = graph
        self.timeout = timeout #En segundos
        self.algorithmic_complexity ="UNDEFINED COMPLEXITY"
        self.name = "Default Name"
        self.iteration_err_msg ="Algorithmic complexity undefined"
        if open_cycle:
            self.graph.distance_matrix.to_numpy()[:,0] = 0
        self.last_execution_time = 0  
        self.last_execution_msg="Not executed"
    @abstractmethod
    def findRoute(self ):
        pass

    def timedFindRoute(self):
        print("Ejecutando algoritmo...")
        start_time = time.time()
        with ThreadingTimeout(constants.ALGORITHM_TIMEOUT) as timeout_ctx:
            try:
                result = self.findRoute()
            except:
                exc_msg = "Tiempo de espera agotado. \nMuchas iteraciones\n"
                exc_msg += self.iteration_err_msg
                exc_msg += "\nAJUSTE EL TIEMPO DE ESPERA O UTILICE OTRO ALGORITMO\n"
                self.last_execution_msg = exc_msg
                return None
            finally:
                end_time = time.time()
                execution_time = end_time - start_time
                self.last_execution_time = execution_time
                
        end_time = time.time()
        execution_time = end_time - start_time
        self.last_execution_time = execution_time
            
        return result
    

#ALGORITMOS EXACTOS

class BruteForceSolver(TSPSolver):
    def __init__(self, graph: Graph, open_cycle=False):
        super().__init__(graph, open_cycle)
        self.name = "Algoritmo de Fuerza Bruta"
        self.algorithmic_complexity = "O(n!)"
        size = graph.distance_matrix.shape[0]
        self.iteration_err_msg = f"El algoritmo necesitaria iterar: {size}! = {'%.2E' % Decimal(math.factorial(size))} veces"
    def findRoute(self):
        permutation, distance = solve_tsp_brute_force(self.graph.get_distance_matrix())
        return (permutation, distance)
    
class DynamicProgrammingSolver(TSPSolver):    
    def __init__(self, graph: Graph, open_cycle=False):
        super().__init__(graph, open_cycle)
        self.name = "Algoritmo de Programación Dinámica"
        self.algorithmic_complexity = "O(n^2 * 2^n)"
        size = graph.distance_matrix.shape[0]
        self.iteration_err_msg = f"El algoritmo necesitaria iterar: {size}^2 * 2^{size} = {'%.2E' % Decimal(size * size *(pow(2,size)) )} veces"
    def findRoute(self):
        permutation, distance = solve_tsp_dynamic_programming(self.graph.get_distance_matrix())
        return (permutation, distance)
    
class BnBSolver(TSPSolver):    
    def __init__(self, graph: Graph, open_cycle=False):
        super().__init__(graph, open_cycle)
        self.name = "Algoritmo de Ramificación y Acotamiento"
        self.algorithmic_complexity = "O(n!)"
        size = graph.distance_matrix.shape[0]
        self.iteration_err_msg = f"El algoritmo necesitaria iterar: {size}! = {'%.2E' % Decimal(math.factorial(size))} veces"
    def findRoute(self):
        permutation, distance = solve_tsp_branch_and_bound(self.graph.get_distance_matrix())
        return (permutation, distance)
    
#ALGORITMOS CON HEURISTICA (NO SIEMPRE EXACTOS NI SIEMPRE OPTIMOS)
    
class BnBSolver(TSPSolver):    
    def __init__(self, graph: Graph, open_cycle=False):
        super().__init__(graph, open_cycle)
        self.name = "Algoritmo de Ramificación y Acotamiento"
        self.algorithmic_complexity = "O(n!)"
        size = graph.distance_matrix.shape[0]
        self.iteration_err_msg = f"El algoritmo necesitaria iterar: {size}! = {'%.2E' % Decimal(math.factorial(size))} veces"
    def findRoute(self):
        permutation, distance = solve_tsp_branch_and_bound(self.graph.get_distance_matrix())
        return (permutation, distance)
    