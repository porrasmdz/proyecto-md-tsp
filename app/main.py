import numpy as np
from solvers import NearestNeighborSolver, TSPSolver, BruteForceSolver
from graph import Graph

distance_matrix = np.array([[0, 11, 2],
               [1, 0, 3],
               [3,3,0]])
headers = np.array(["GYE", "UIO", "CNC"])
ciudades=headers


def print_travelling_route(algorithm: TSPSolver, open_cycle = False):
    (permutations, distance) = algorithm.findRoute()
    print(f"Resolviendo problema del viajero para:\n{algorithm.graph}\n\n")
    print(f"Método: {algorithm.name}")
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