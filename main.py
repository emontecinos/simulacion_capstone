from supermercat import GraphNode, Graph
from buscar_gondola import buscar_gondola
from calcular_ruta_productos_vistos import calcular_ruta_productos_vistos
#from compra_espontanea import compra_espontanea
from Cliente import Cliente

grafo = Graph()
grafo.cargar_base("datos_nodos_new.csv")

#  Calcular ruta minima
#nodes = ["(2,2)","(10,1)","(3,5)","(9,3)"]
#ruta = grafo.calcular_ruta_nodos(nodes)

# Calcular nodo de una lista de productos

lista_clientes = ["Durazno", "Crema", "Pavo", "Champu"]
clientes = []
for i in range(10):  
    clientes.append(Cliente(lista_clientes))
    print(clientes[-1])
    clientes[-1].calcular_ruta(grafo)
    clientes[-1].calcular_productos_vistos(grafo)
    for prod_visto in clientes[-1].productos_vistos:
        clientes[-1].comprar_producto(prod_visto)
    print(clientes[-1].comprado)





# comprar


# Encontrar Productos de una góndola
# print(grafo.gondolas["13D"].espacios)
