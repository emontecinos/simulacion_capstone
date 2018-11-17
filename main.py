from supermercat import GraphNode, Graph
from buscar_gondola import buscar_gondola
from calcular_ruta_productos_vistos import calcular_ruta_productos_vistos
from compra_espontanea import compra_espontanea
from Cliente import Cliente

grafo = Graph()
grafo.cargar_base("datos_nodos_new.csv")

#  Calcular ruta minima
#nodes = ["(2,2)","(10,1)","(3,5)","(9,3)"]
#ruta = grafo.calcular_ruta_nodos(nodes)

# Calcular nodo de una lista de productos

productos = ["Durazno", "Crema", "Pavo", "Champú"]
cliente = Cliente(productos)
cliente.calcular_ruta(grafo)
cliente.calcular_productos_vistos(grafo)


# comprar


# Encontrar Productos de una góndola
# print(grafo.gondolas["13D"].espacios)
