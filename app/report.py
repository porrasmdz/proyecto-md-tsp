import numpy as np
from solvers import TSPSolver


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
    weights = [df.loc[ord_cities[x], ord_cities[x+1]] for x in range(len(ord_cities)-1)] 
    weights += [df.loc[ord_cities[-1], ord_cities[0]]]
    weights = np.array(weights)    
    route = [(ord_cities[i], ord_cities[i+1]) for i in range(len(permutations)-1)] 
    route += [(ord_cities[-1], ord_cities[0])]
    for index in range(len(route)):
        src,tgt = route[index][0],route[index][1]
        print(f"Paso {index+1}:",src ,"->" ,tgt, f" | Distancia {weights[index]}")
