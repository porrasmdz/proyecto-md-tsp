
import networkx as nx
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from decimal import Decimal
import time
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force, solve_tsp_branch_and_bound
from python_tsp.heuristics import solve_tsp_simulated_annealing, solve_tsp_local_search, solve_tsp_record_to_record, solve_tsp_lin_kernighan
from stopit import ThreadingTimeout
import math
from graph import Graph
import constants

class TimeoutException(Exception):
    pass

class TSPSolver(ABC):
    def __init__(self, graph: Graph,open_cycle= False, timeout=10, g_drawing=None):
        self.graph = graph
        self.timeout = timeout #En segundos
        self.algorithmic_complexity ="UNDEFINED COMPLEXITY"
        self.name = "Default Name"
        self.iteration_err_msg ="Algorithmic complexity undefined"
        if open_cycle:
            self.graph.distance_matrix.to_numpy()[:,0] = 0
        self.g_drawing = g_drawing if g_drawing is not None else None
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
        self.visualize_optimal_path(optimal_path=result)
        return result
    
    def visualize_optimal_path(self, optimal_path):
        if self.g_drawing is None:
            print("Dibujo no encontrado.")
            return
        df = self.graph.distance_matrix
        cities = self.graph.cities
        G = nx.Graph()
        optimal_path = optimal_path[0]
        optimal_path_edges = list(zip(optimal_path, optimal_path[1:])) + [(optimal_path[-1], optimal_path[0])]
    
        pos = nx.spring_layout(self.g_drawing)  # Usa el layout del grafo ya existente
        
        nx.draw(self.g_drawing, pos, with_labels=True, node_color='lightblue', node_size=600, font_size=10, font_weight='bold', edge_color='gray')
        # nx.draw_networkx_edge_labels(self.g_drawing, pos, edge_labels=None)
        # print(optimal_path_edges)
        optimal_cities = [(cities[x],cities[y]) for x,y in optimal_path_edges]
        for src, tgt in optimal_cities:
            w = df.loc[src,tgt]
            G.add_edge(src,tgt, weight=w)
        weights = nx.get_edge_attributes(G, 'weight')
        
        # optimal_cities + [cities[len(cities)-1], cities[0]]
        # print(optimal_cities)
        # Resalta el camino óptimo
        nx.draw_networkx_edges(self.g_drawing, pos, edgelist=optimal_cities, edge_color='red', width=2)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
        # nx.draw_networkx_nodes(self.g_drawing, pos, nodelist=optimal_path, node_color='lightgreen', node_size=500)
        
        plt.show()
        

#ALGORITMOS EXACTOS

class BruteForceSolver(TSPSolver):
    def __init__(self, graph: Graph, open_cycle=False, timeout=10, g_drawing=None):
        super().__init__(graph, open_cycle, timeout, g_drawing)
        self.name = "Algoritmo de Fuerza Bruta"
        self.algorithmic_complexity = "O(n!)"
        size = graph.distance_matrix.shape[0]
        self.iteration_err_msg = f"El algoritmo necesitaria iterar: {size}! = {'%.2E' % Decimal(math.factorial(size))} veces"
    def findRoute(self):
        permutation, distance = solve_tsp_brute_force(self.graph.get_distance_matrix())
        return (permutation, distance)
    
class DynamicProgrammingSolver(TSPSolver):    
    def __init__(self, graph: Graph, open_cycle=False, timeout=10, g_drawing=None):
        super().__init__(graph, open_cycle, timeout, g_drawing)
        self.name = "Algoritmo de Programación Dinámica"
        self.algorithmic_complexity = "O(n^2 * 2^n)"
        size = graph.distance_matrix.shape[0]
        self.iteration_err_msg = f"El algoritmo necesitaria iterar: {size}^2 * 2^{size} = {'%.2E' % Decimal(size * size *(pow(2,size)) )} veces"
    def findRoute(self):
        permutation, distance = solve_tsp_dynamic_programming(self.graph.get_distance_matrix())
        return (permutation, distance)
    
class BnBSolver(TSPSolver):    
    def __init__(self, graph: Graph, open_cycle=False, timeout=10, g_drawing=None):
        super().__init__(graph, open_cycle, timeout, g_drawing)
        self.name = "Algoritmo de Ramificación y Acotamiento"
        self.algorithmic_complexity = "O(n!)"
        size = graph.distance_matrix.shape[0]
        self.iteration_err_msg = f"El algoritmo necesitaria iterar: {size}! = {'%.2E' % Decimal(math.factorial(size))} veces"
    def findRoute(self):
        permutation, distance = solve_tsp_branch_and_bound(self.graph.get_distance_matrix())
        return (permutation, distance)
    
#ALGORITMOS CON HEURISTICA (NO SIEMPRE EXACTOS NI SIEMPRE OPTIMOS)

class SimulatedAnnealingSolver(TSPSolver):    
    def __init__(self, graph: Graph, open_cycle=False, timeout=10, g_drawing=None):
        super().__init__(graph, open_cycle, timeout, g_drawing)
        
        size = graph.distance_matrix.shape[0]
        self.name = "Algoritmo de Recorrido Simulado"
        self.algorithmic_complexity = f"O(n^2 * m)"
        self.iteration_err_msg =  f"El algoritmo necesitaría iterar: {size}^2 veces dependiendo del número de iteraciones."
    def findRoute(self):
        permutation, distance = solve_tsp_simulated_annealing(self.graph.get_distance_matrix())
        return (permutation, distance)
    
class LocalSearchSolver(TSPSolver):    
    def __init__(self, graph: Graph, open_cycle=False, timeout=10, g_drawing=None):
        super().__init__(graph, open_cycle, timeout, g_drawing)
        self.name = "Algoritmo de Búsqueda Local"
        self.algorithmic_complexity = "O(n^2)"
        size = graph.distance_matrix.shape[0]
        self.iteration_err_msg = f"El algoritmo necesitaría iterar: {size}^2 veces."
    def findRoute(self):
        permutation, distance = solve_tsp_local_search(self.graph.get_distance_matrix())
        return (permutation, distance)
    
class RecordToRecordSolver(TSPSolver):    
    def __init__(self, graph: Graph, open_cycle=False, timeout=10, g_drawing=None):
        super().__init__(graph, open_cycle, timeout, g_drawing)
        self.name = "Algoritmo de Registro a Registro"
        self.algorithmic_complexity = "O(n^2)"
        size = graph.distance_matrix.shape[0]
        self.iteration_err_msg = f"El algoritmo necesitaría iterar: {size}^2 veces."
    def findRoute(self):
        permutation, distance = solve_tsp_record_to_record(self.graph.get_distance_matrix())
        return (permutation, distance)
    
class LinKernSolver(TSPSolver):    
    def __init__(self, graph: Graph, open_cycle=False, timeout=10, g_drawing=None):
        super().__init__(graph, open_cycle, timeout, g_drawing)
        self.name = "Algoritmo de Lin-Kernighan"
        self.algorithmic_complexity = "O(n^3)"
        size = graph.distance_matrix.shape[0]
        self.iteration_err_msg = f"El algoritmo podría necesitar iterar aproximadamente: {size}^3 veces"
    def findRoute(self):
        permutation, distance = solve_tsp_lin_kernighan(self.graph.get_distance_matrix())
        return (permutation, distance)
