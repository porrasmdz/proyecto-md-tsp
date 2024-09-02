import numpy as np
from solvers import NearestNeighborSolver, TSPSolver, BruteForceSolver
from graph import Graph
distance_matrix = np.array([
    [0, 93, 15, 72, 61, 21, 83, 87, 75, 75],
    [88, 0, 24, 3, 22, 53, 2, 88, 30, 38],
    [2, 64, 0, 21, 33, 76, 58, 22, 89, 49],
    [91, 59, 42, 0, 60, 80, 15, 62, 62, 47],
    [62, 51, 55, 64, 0, 51, 7, 21, 73, 39],
    [18, 4, 89, 60, 14, 0, 90, 53, 2, 84],
    [92, 60, 71, 44, 8, 47, 0, 78, 81, 36],
    [50, 4, 2, 6, 54, 4, 54, 0, 63, 18],
    [90, 44, 34, 74, 62, 100, 14, 95, 0, 15],
    [72, 78, 87, 62, 40, 85, 80, 82, 53, 0]
])
headers = np.array(["UIO", "GYE", "CUE", "MEC", "LOH", "ESM", "MCH", "TUL", "SNC", "IBR"])
ciudades=headers



def print_travelling_route(algorithm: TSPSolver, open_cycle = False):
    (permutations, distance) = algorithm.timedFindRoute()
    print(f"Resolviendo problema del viajero para:\n{algorithm.graph}\n\n")
    print(f"Método: {algorithm.name}")
    
    print(f"Tiempo total de ejecución: {algorithm.last_execution_time:.6f}s")
    print(f"Recorrido total: {distance} unidades")
    for perm_idx in range(len(permutations)):
        first_perm = permutations[0]
        perm = permutations[perm_idx]
        if perm_idx < len(permutations) -1:
            next_perm = permutations[perm_idx + 1]
            ciudad_orig =ciudades[perm]
            ciudad_destino = ciudades[next_perm]
            print(f"Paso {perm_idx+1}:",ciudad_orig ,"->" ,ciudad_destino, f" | Distancia {graph.distance_matrix[ciudad_destino][ciudad_orig]}")
        elif perm_idx == len(permutations) - 1 and not open_cycle:
            ciudad_orig =ciudades[perm]
            ciudad_destino = ciudades[first_perm]
            print(f"Paso {perm_idx+1}:", ciudades[perm],"->" ,ciudades[first_perm],  f" | Distancia {graph.distance_matrix[ciudad_destino][ciudad_orig]}")

if __name__ == "__main__":
    is_open_route = False
    try:
        graph = Graph(distance_matrix, headers=ciudades)
        brute_force_results = BruteForceSolver(graph=graph,open_cycle=is_open_route)
        nearest_neighbor = NearestNeighborSolver(graph=graph,open_cycle=is_open_route)
        print("################################")
        print_travelling_route(algorithm=brute_force_results, open_cycle=is_open_route)
        print("################################")
        print_travelling_route(algorithm=nearest_neighbor, open_cycle=is_open_route)
    except Exception as e:
        print("Se encontró un error, cancelando operación")
        print("Error", str(e))