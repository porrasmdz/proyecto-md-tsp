from enum import Enum

ALGORITHM_TIMEOUT=10
RTRN_OPEN_CYCLE=False

class Strategy(str, Enum):
    BRUTE_FORCE= 'brute_force'
    NEAREST_NEIGHBOUR= "nneighbour"
    GENETRIC_ALGORITHM="genetic"
