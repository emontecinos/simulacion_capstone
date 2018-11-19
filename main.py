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
    grafo.cargar_gondolas("distr_gondolas.csv")
    ######################## PARAMETROS DE LA SIMULACION ###########################
    clientes_iniciales = 5
    limite_boletas = 50
    iteraciones_por_config = 3
    veces_que_busca_mejora = 3
    #################################################################################
    simulacion = Simulacion(grafo)
    estadisticas_prom = dict()
    swaps_hechos = []
    estadisticas_prom["utilidad_supermercado"] = 0
    estadisticas_prom["probabilidad_total"] = 0
    estadisticas_prom["utilidad_espontanea"] = 0
    estadisticas_prom["numero_medio_compras_espontaneas"] = 0
    estadisticas_prom["top_productos_espontaneos"] = 0
    estadisticas_prom["distancia_media_recorrida"] = 0




    for i in range(iteraciones_por_config):
        estadisticas_iniciales = simulacion.run(clientes_iniciales, limite_boletas)
        print("_______________________")
        for estadistica in estadisticas_iniciales.items():
            if type(estadistica[1]) is not list:

                estadisticas_prom[estadistica[0]] += estadistica[1] / iteraciones_por_config
    print("Estadistica inicial {}".format(estadisticas_prom["probabilidad_total"]))
    print("Tardó: {}".format(time.time()-t1))

    for i in range(veces_que_busca_mejora):
        # lista_swaps = grafo.calcular_lista_swaps()
        gondola = grafo.gondolas["1I"]
        gondola_2 = grafo.gondolas["10I"]
        # print(gondola)
        # print(gondola_2)
        print("_______________________")


        lista_swaps = [(gondola.manejo_swap, 'Falda_de_res', 'Pollo', gondola_2)]

        for swap in lista_swaps:
            swap[0](swap[1], swap[2], swap[3])
            estadisticas_nuevas = dict()
            estadisticas_nuevas["probabilidad_total"] = 0
            estadisticas_nuevas["utilidad_supermercado"] = 0
            estadisticas_nuevas["utilidad_espontanea"] = 0
            estadisticas_nuevas["numero_medio_compras_espontaneas"] = 0
            estadisticas_nuevas["top_productos_espontaneos"] = 0
            estadisticas_nuevas["distancia_media_recorrida"] = 0
            for i in range(iteraciones_por_config):
                estadisticas_iteracion = simulacion.run(5, 50)
                print("_______________________")
                for estadistica in estadisticas_iteracion.items():
                    if type(estadistica[1]) is not list:
                        estadisticas_nuevas[estadistica[0]] += estadistica[1] / iteraciones_por_config
            mejor = False
            if estadisticas_prom["probabilidad_total"] < estadisticas_nuevas["probabilidad_total"]:
                mejor = True
            if mejor:
                print("Estadistica swap numero X {}".format(estadisticas_nuevas["probabilidad_total"]))
                print('MEJOROOOOOOO')
                grafo.guardar_gondolas()
                break

            print("_______________________")


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
