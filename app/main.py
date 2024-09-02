from graph import Graph
from utils import print_travelling_route
from solvers import NearestNeighborSolver, BruteForceSolver
from generators import generate_random_square_matrix
import constants

cities = [
    "GYE", "UIO", "CUE", "SDO", "DUR", "MCH", "MTA", "PTV", "LOJ", "QVD", 
    "AMB", "RIO", "DLE", "MIL", "IBR", "ESM", "LLI", "BAB", "SGQ", "LTC", 
    "SBO", "MNT", "PAS", "STR", "TUL", "HUA", "NLO", "CHN", "SLE", "CAR", 
    "COC", "GVM", "BFE", "JIP", "CAY", "VIB", "OTA", "VEN", "TRF", "LTC", 
    "NRJ", "AZG", "LCD", "SAL", "VIN", "NRJ", "PUY", "BLZ", "LMA", "RZT", 
    "GRA", "TEN", "SLO", "JRM", "PED", "CAT", "GBO", "ATU", "PCB", "MCH", 
    "VAL", "YGC", "MCS", "BDC", "ORN", "CCA", "ATC", "PNS", "SHF", "MLV", 
    "PJL", "LJS", "SGA", "BNS", "GLO", "SLT", "YNT", "CRM", "CAN", "TBM", 
    "BLA", "PAY", "PLO", "MCR", "SNT", "RFT", "CMD", "PLL", "SLU", "SUC", 
    "CTC", "SVT", "PAL", "CMA", "PVM", "ECH", "BBA", "BCY", "SUC"
]
matrix_size = len(cities) # 200, 400, 10000
distance_matrix = generate_random_square_matrix(size=matrix_size)
graph = Graph(distance_matrix)#, headers=cities)
  
if __name__ == "__main__":
    is_open_route = constants.RTRN_OPEN_CYCLE  
    print(f"Resolviendo problema del viajero para:\n{graph}\n\n")
    brute_force_results = BruteForceSolver(graph=graph,open_cycle=is_open_route)
    nearest_neighbor = NearestNeighborSolver(graph=graph,open_cycle=is_open_route)
    print("################################")
    if brute_force_results is not None:
       print_travelling_route(algorithm=brute_force_results, open_cycle=is_open_route)
    print("################################")
    if nearest_neighbor is not None:
        print_travelling_route(algorithm=nearest_neighbor, open_cycle=is_open_route)
