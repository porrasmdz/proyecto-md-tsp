import string
import constants 
import numpy as np
def alphabetic_generator(alphabet=string.ascii_uppercase):
    assert len(alphabet) == len(set(alphabet))  # make sure every letter is unique
    s = [alphabet[0]]
    while 1:
        yield ''.join(s)
        l = len(s)
        for i in range(l-1, -1, -1):
            if s[i] != alphabet[-1]:
                s[i] = alphabet[alphabet.index(s[i])+1]
                s[i+1:] = [alphabet[0]] * (l-i-1)
                break
        else:
            s = [alphabet[0]] * (l+1)

def generate_random_square_matrix(size=10, seed=None):    
    if seed is not None:
        np.random.seed(seed)
    distance_matrix = np.random.randint(0, constants.MAX_EDGES_VALUES, size=(size, size))
    np.fill_diagonal(distance_matrix, 0)
    return distance_matrix