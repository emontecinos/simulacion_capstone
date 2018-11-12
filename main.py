from supermercat import GraphNode, Graph
from buscar_gondola import buscar_gondola

grafo = Graph()
grafo.cargar_base("datos_nodos_new.csv")

#  Calcular ruta minima
#nodes = ["(2,2)","(10,1)","(3,5)","(9,3)"]
#ruta = grafo.calcular_ruta_nodos(nodes)

# Calcular nodo de una lista de productos
productos = ["Durazno", "Crema", "Pavo", "Champú"]
print(grafo.buscar_gondola(productos))

# Encontrar Productos de una góndola
print(grafo.gondolas["13D"].espacios)
