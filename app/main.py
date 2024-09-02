import numpy as np
from strategies import NearestNeighborSolver, TSPSolver, BruteForceSolver
from graph import Graph
matrix = np.array([[0, 11, 2],
               [1, 0, 3],
               [3,3,0]])

ciudadesA=np.array(["GYE", "UIO", "CNC",])
ciudadesB=np.array(["GYE", "UIO", "CNC"])
graph = Graph(matrix, col_headers=ciudadesA, row_headers=ciudadesB)

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
            print(f"Paso {perm_idx+1}:", ciudadesA[perm],"->" ,ciudadesA[next_perm])
        elif perm_idx == len(permutations) - 1 and not open_cycle:
            print(f"Paso {perm_idx+1}:", ciudadesA[perm],"->" ,ciudadesA[first_perm])

if __name__ == "__main__":
    is_open_route = False
    brute_force_results = BruteForceSolver(graph=graph,open_cycle=is_open_route)
    nearest_neighbor = NearestNeighborSolver(graph=graph,open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=brute_force_results, open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=nearest_neighbor, open_cycle=is_open_route)