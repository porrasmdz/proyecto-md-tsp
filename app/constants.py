from enum import Enum

class Strategy(str, Enum):
    BRUTE_FORCE= 'brute_force'
    NEAREST_NEIGHBOUR= "nneighbour"
    GENETRIC_ALGORITHM="genetic"
