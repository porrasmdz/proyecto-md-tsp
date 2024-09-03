
import constants
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from generators import alphabetic_generator, generate_random_square_matrix
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

class Graph:
    def __init__(self, size=10, cities = None, random_values=True):
        matrix_size = size
        if random_values:
            distance_matrix = generate_random_square_matrix(size=matrix_size)
        else:
            distance_matrix = generate_random_square_matrix(size=matrix_size, seed=constants.OPTIONAL_SEED)
        if cities is None:
            alph_gen = alphabetic_generator()
            self.cities = [next(alph_gen) for _ in range(len(distance_matrix.transpose()))]
        else:
            self.cities = list(set(cities))
            matrix_size = len(cities)
            if random_values:
                distance_matrix = generate_random_square_matrix(size=matrix_size)
            else:
                distance_matrix = generate_random_square_matrix(size=matrix_size, seed=constants.OPTIONAL_SEED)
        
        self.distance_matrix  = pd.DataFrame(distance_matrix, 
                                             columns=self.cities)
        
        alph_gen = alphabetic_generator()
        for idx in range(len(self.distance_matrix)):
            if cities is None:
                self.distance_matrix = self.distance_matrix.rename(index={idx: next(alph_gen)})
            else:
                self.distance_matrix = self.distance_matrix.rename(index={idx: cities[idx]})
    
    def get_distance_matrix(self):
        return self.distance_matrix.to_numpy()
    
    def show_graph(self):
        print("Una vez termine de trabajar con la imagen del grafo. Ciérrela para continuar.")
        df = self.distance_matrix
        G = nx.Graph()
        for i in df.index:
            for j in df.columns:
                weight = df.loc[i, j]
                if i != j and weight > constants.MIN_EDGES_VALUES:  # Evitar los lazos
                    G.add_edge(i, j, weight=weight)
        pos = nx.spring_layout(G)  # Layout para la disposición de los nodos
        weights = nx.get_edge_attributes(G, 'weight')

        nx.draw(G, pos, with_labels=True, node_color='lightblue', font_size=10, font_weight='bold', edge_color='gray')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

        plt.show()
        return G


    
    def __str__(self):
        graph = self.distance_matrix
        str =f"Grafo con Matriz de distancias {graph.shape})\n"
        if self.distance_matrix.shape[0] > 10:
            
            # str+=f"Indices: {self.distance_matrix.index}\n"
            # str+=f"Columnas: {self.distance_matrix.columns}\n"
            str+=f"Mostrando primeras {constants.DEFAULT_SHOW_COLS} columnas y {constants.DEFAULT_SHOW_ROWS} filas\n"
            subset_columns = self.distance_matrix.iloc[:, :constants.DEFAULT_SHOW_COLS]
            subset = subset_columns.head(constants.DEFAULT_SHOW_ROWS)
            str += subset.to_string()
        else:
            str += self.distance_matrix.to_string()
        return str
            

