import numpy as np
from solvers import BnBSolver, BruteForceSolver, DynamicProgrammingSolver, LinKernSolver, LocalSearchSolver, RecordToRecordSolver, SimulatedAnnealingSolver, TSPSolver
import constants

def print_travelling_route(algorithm: TSPSolver, open_cycle = False):
    ciudades = algorithm.graph.cities
    graph = algorithm.graph
    try:
        (permutations, distance) = algorithm.timedFindRoute()
        
    except Exception as e:
        print(f"Método: {algorithm.name}")
        print(f"Complejidad algoritmica: {algorithm.algorithmic_complexity}")
        print(f"Tiempo total de ejecución: {algorithm.last_execution_time:.6f}s")
        print("No se puedo completar el algoritmo")
    
        print(algorithm.last_execution_msg)
        return    
    
    print(f"Método: {algorithm.name}")
    print(f"Complejidad algoritmica: {algorithm.algorithmic_complexity}")
    print(f"Tiempo total de ejecución: {algorithm.last_execution_time:.6f}s")
    print(f"Recorrido total: {distance} unidades")
    df = graph.distance_matrix
    ord_cities = [ciudades[i] for i in permutations]   
    route = [(ord_cities[i], ord_cities[i+1]) for i in range(len(permutations)-1)] 
    route += [(ord_cities[-1], ord_cities[0])]
    for index in range(len(route)):
        src,tgt = route[index][0],route[index][1]
        print(f"Paso {index+1}:",src ,"->" ,tgt, f" | Distancia {df.loc[src,tgt]}")
def demo_exacts(graph, g_drawing=None):
    is_open_route = constants.RTRN_OPEN_CYCLE  
    print(f"Resolviendo problema del viajero para:\n{graph}\n\n")
    brute_force_results = BruteForceSolver(graph=graph,open_cycle=is_open_route, g_drawing=g_drawing)
    dynamic_prog_solver = DynamicProgrammingSolver(graph=graph,open_cycle=is_open_route, g_drawing=g_drawing)
    bnb_solver = BnBSolver(graph=graph,open_cycle=is_open_route,g_drawing=g_drawing)
    print("################################")
    print_travelling_route(algorithm=brute_force_results, open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=dynamic_prog_solver, open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=bnb_solver, open_cycle=is_open_route)

def demo_heur(graph, g_drawing=None):
    is_open_route = constants.RTRN_OPEN_CYCLE  
    #Heuristics
    sannealing = SimulatedAnnealingSolver(graph=graph,open_cycle=is_open_route, g_drawing=g_drawing)
    localsearch = LocalSearchSolver(graph=graph,open_cycle=is_open_route, g_drawing=g_drawing)
    rtorsolver= RecordToRecordSolver(graph=graph,open_cycle=is_open_route,g_drawing=g_drawing)
    linkernsolver= LinKernSolver(graph=graph,open_cycle=is_open_route,g_drawing=g_drawing)
    print("##########HEURISTICS##############")
    print_travelling_route(algorithm=sannealing, open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=localsearch, open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=rtorsolver, open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=linkernsolver, open_cycle=is_open_route)