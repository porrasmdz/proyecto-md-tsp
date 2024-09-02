from solvers import TSPSolver
from stopit import ThreadingTimeout


def print_travelling_route(algorithm: TSPSolver, open_cycle = False):
    ciudades = algorithm.graph.cities
    graph = algorithm.graph
    try:
        (permutations, distance) = algorithm.timedFindRoute()
    except:
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
    for perm_idx in range(len(permutations)):
        first_perm = permutations[0]
        perm = permutations[perm_idx]
        if perm_idx < len(permutations) -1:
            next_perm = permutations[perm_idx + 1]
            ciudad_orig =ciudades[perm]
            ciudad_destino = ciudades[next_perm]
            distance_node = graph.distance_matrix.loc[ciudad_destino, ciudad_orig]
            print(f"Paso {perm_idx+1}:",ciudad_orig ,"->" ,ciudad_destino, f" | Distancia {distance_node}")
        elif perm_idx == len(permutations) - 1 and not open_cycle:
            ciudad_orig =ciudades[perm]
            ciudad_destino = ciudades[first_perm]
            distance_node = graph.distance_matrix.loc[ciudad_destino, ciudad_orig]
            print(f"Paso {perm_idx+1}:", ciudades[perm],"->" ,ciudades[first_perm],  f" | Distancia {distance_node}")
