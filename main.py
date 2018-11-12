from supermercat import GraphNode, Graph
from buscar_gondola import buscar_gondola

grafo = Graph()
grafo.cargar_base("datos_nodos.csv")

#  Calcular ruta minima
nodes = ["(2,2)","(10,1)","(3,5)","(9,3)"]
ruta = grafo.calcular_ruta_nodos(nodes)
#print(grafo.gondolas["9I"].espacios)


