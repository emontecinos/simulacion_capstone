from supermercat import GraphNode, Graph
#from buscar_gondola import buscar_gondola
from calcular_ruta_productos_vistos import calcular_ruta_productos_vistos
#from compra_espontanea import compra_espontanea
#from Cliente import Cliente
#import random
from simulacion import Simulacion
import time

if __name__ == "__main__":
    t1 = time.time()
    grafo = Graph()
    grafo.cargar_base("datos_nodos_new.csv")
    simulacion = Simulacion(grafo)
    simulacion.run(50, 4000)
    print("Tardó: {}".format(time.time()-t1))

    












    '''clientes = []
    for i in [5,5,6,6,7,7]:
        lista_cliente_i = random.sample(productos_totales,k=i)
        clientes.append(Cliente(lista_cliente_i))
        clientes[-1].calcular_ruta(grafo)
        clientes[-1].calcular_productos_vistos(grafo)
        for prod_visto in clientes[-1].productos_vistos:
            clientes[-1].comprar_producto(prod_visto)
        print(clientes[-1])'''


    #lista_clientes=["Melon","Mayonesa","Pollo"]

    #cliente = Cliente(lista_clientes)
    #cliente.calcular_ruta(grafo)
    #cliente.calcular_productos_vistos(grafo)
    #for prod in cliente.productos_vistos:
    #    cliente.comprar_producto(prod)
    #print(cliente.comprado)



    #  Calcular ruta minima
    #nodes = ["(2,2)","(10,1)","(3,5)","(9,3)"]
    #ruta = grafo.calcular_ruta_nodos(nodes)

    # Calcular nodo de una lista de productos

    # comprar


    # Encontrar Productos de una góndola
    # print(grafo.gondolas["13D"].espacios)
