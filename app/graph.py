
import string
import numpy as np
import pandas as pd
from numpy import ndarray
'''
Utilizando matriz de distancia pq todos los algoritmos
son más fáciles de implementar con matriz de distancia

Esta matriz es como la de adyancencia pero con la distancia total
de un vértice a otro
Ej.:
  A  B  C  D  E
A 0 12  3  5  9
B 1  0  2  8  9
C 3  9  0  7  3
D 5  4  3  0  1
E 1  2  7  1  0

No es necesario que sea simétrica pero es para visualizarlo fácil
Si debe ser cuadrada 
'''
def validate_distance_matrix(matrix:ndarray=np.array([])):
    width= matrix.shape[0]
    height= matrix.shape[1]
    if width != height:
        raise ValueError(f"La matriz debe ser cuadrada # Filas == # Col pero se obtuvo matriz de {matrix.shape}", )

def validate_headers(matrix:ndarray=np.array([]), headers:ndarray=np.array([])):
    width= matrix.shape[1]
    if width != len(headers):
        raise ValueError(f"Las cabeceras no ocupan todas las columnas. Espearadas {width} recibidas {len(headers)}", )

class Graph:
    def __init__(self, distance_matrix: ndarray= np.array([]), headers = None):
        if headers is None:
            self.headers = [string.ascii_uppercase[idx] for idx in range(len(distance_matrix.transpose()))]
        else:
            validate_headers(distance_matrix, headers)
            self.headers = headers
        
        validate_distance_matrix(distance_matrix)
        self.distance_matrix  = pd.DataFrame(distance_matrix, 
                                             columns=self.headers)
        
        for idx in range(len(self.distance_matrix)):
            if headers is None:
                self.distance_matrix = self.distance_matrix.rename(index={idx: string.ascii_uppercase[idx]})
            else:
                self.distance_matrix = self.distance_matrix.rename(index={idx: headers[idx]})
    
    def get_distance_matrix(self):
        return self.distance_matrix.to_numpy()
    
    def __str__(self):
        graph = self.distance_matrix
        str =f"Grafo con Matriz de distancias {graph.shape})\n"
        str += self.distance_matrix.to_string()
        return str
            

