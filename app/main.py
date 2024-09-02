from graph import Graph
from utils import print_travelling_route
from solvers import BnBSolver, DynamicProgrammingSolver, BruteForceSolver
from generators import generate_random_square_matrix
import constants

cities = list({
    "GYE", "UIO", "CUE", "SDO", "DUR", "MCH", "MTA", "PTV", "LOJ", "QVD",}) 
#     "AMB", "RIO", "DLE", "MIL", "IBR", "ESM", "LLI", "BAB", "SGQ", "LTC", 
#     "SBO", "MNT", "PAS", "STR", "TUL", "HUA", "NLO", "CHN", "SLE", "CAR", 
#     "COC", "GVM", "BFE", "JIP", "CAY", "VIB", "OTA", "VEN", "TRF", "LTC", 
#     "NRJ", "AZG", "LCD", "SAL", "VIN", "NRJ", "PUY", "BLZ", "LMA", "RZT", 
#     "GRA", "TEN", "SLO", "JRM", "PED", "CAT", "GBO", "ATU", "PCB", "MCH", 
#     "VAL", "YGC", "MCS", "BDC", "ORN", "CCA", "ATC", "PNS", "SHF", "MLV", 
#     "PJL", "LJS", "SGA", "BNS", "GLO", "SLT", "YNT", "CRM", "CAN", "TBM", 
#     "BLA", "PAY", "PLO", "MCR", "SNT", "RFT", "CMD", "PLL", "SLU", "SUC", 
#     "CTC", "SVT", "PAL", "CMA", "PVM", "ECH", "BBA", "BCY", "SUC"
# })

graph = Graph(size=10) 
# graph = Graph(cities=cities)
graph.show_graph() #<- Funcion para ver el grafo

if __name__ == "__main__":
    is_open_route = constants.RTRN_OPEN_CYCLE  
    print(f"Resolviendo problema del viajero para:\n{graph}\n\n")
    brute_force_results = BruteForceSolver(graph=graph,open_cycle=is_open_route)
    dynamic_prog_solver = DynamicProgrammingSolver(graph=graph,open_cycle=is_open_route)
    bnb_solver = BnBSolver(graph=graph,open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=brute_force_results, open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=dynamic_prog_solver, open_cycle=is_open_route)
    print("################################")
    print_travelling_route(algorithm=bnb_solver, open_cycle=is_open_route)
