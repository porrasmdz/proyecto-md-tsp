from graph import Graph
from report import demo_exacts, demo_heur, print_travelling_route


cities = list({
    "GYE", "UIO", "CUE", "SDO", "DUR", "MCH", "MTA", "PTV", "LOJ", "QVD",}) 

graph = Graph(cities=cities, random_values=False) 
# graph = Graph(cities=cities)
# graph = Graph(size=10, random_values=False) #<-Para q se repita siempre
g_drawing = graph.show_graph() #<- Funcion para ver el grafo #None para no verlo

if __name__ == "__main__":
    demo_exacts(graph, g_drawing)
    # input("FOR HEURISTICS PRESS ENTER")
    # demo_heur(graph, g_drawing)
    
    
    
    
    
    
    
    
    
    
    
    
