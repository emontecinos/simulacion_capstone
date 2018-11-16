from supermercat import GraphNode, Graph
from buscar_gondola import buscar_gondola

grafo = Graph()
grafo.cargar_base("datos_nodos_new.csv")

#  Calcular ruta minima
#nodes = ["(2,2)","(10,1)","(3,5)","(9,3)"]
#ruta = grafo.calcular_ruta_nodos(nodes)

# Calcular nodo de una lista de productos
productos = ["Durazno", "Crema", "Pavo", "Champú"]
dict_nodos_a_visitar = grafo.buscar_gondola(productos)
lista_nodos_a_visitar = []
for i in dict_nodos_a_visitar:
    if dict_nodos_a_visitar[i] not in lista_nodos_a_visitar:
        lista_nodos_a_visitar.append(dict_nodos_a_visitar[i])
#print(dict_nodos_a_visitar)
#print(lista_nodos_a_visitar)
ruta = grafo.calcular_ruta_nodos(lista_nodos_a_visitar)
#print(ruta)
dict_productos_vistos = []
productos_vistos = []
for n in ruta:
       dict_productos_vistos.append(grafo.productos_visibles(n))
for i in dict_productos_vistos:
        for j in i:
                if j not in productos_vistos:
                        productos_vistos.append(j)
print(productos_vistos, len(productos_vistos))

# Encontrar Productos de una góndola
# print(grafo.gondolas["13D"].espacios)
