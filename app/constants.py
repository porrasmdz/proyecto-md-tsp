from enum import Enum

ALGORITHM_TIMEOUT=12
RTRN_OPEN_CYCLE=False

DEFAULT_SHOW_COLS=20
DEFAULT_SHOW_ROWS=20

RANDOM_CAP=100

class Strategy(str, Enum):
    BRUTE_FORCE= 'brute_force'
    NEAREST_NEIGHBOUR= "nneighbour"
    GENETRIC_ALGORITHM="genetic"
