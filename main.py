from supermercat import GraphNode, Graph
#from buscar_gondola import buscar_gondola
from calcular_ruta_productos_vistos import calcular_ruta_productos_vistos
#from compra_espontanea import compra_espontanea
#from Cliente import Cliente
#import random
from copy import deepcopy
from simulacion import Simulacion
from swapity_swaps import swapity_swap
import time
from random import shuffle

if __name__ == "__main__":
    t1 = time.time()
    grafo = Graph()
    grafo.cargar_base("datos_nodos_new.csv")
    grafo.cargar_gondolas("distr_gondolas.csv")
    ######################## PARAMETROS DE LA SIMULACION ###########################
    clientes_iniciales = 30
    limite_boletas = 200
    iteraciones_por_config = 2
    veces_que_busca_mejora = 20
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

########################################################################################################################
    # print("ESTADISTICAS INICIALES")
    for i in range(1):
        estadisticas_iniciales = simulacion.run(clientes_iniciales, limite_boletas)
        for estadistica in estadisticas_iniciales.items():
            if type(estadistica[1]) is not list:
                if estadistica[0] == "probabilidad_total":
                    estadisticas_prom[estadistica[0]] += estadistica[1] / (50 * clientes_iniciales)
                else:
                    estadisticas_prom[estadistica[0]] += estadistica[1] / 50
    with open("Swaps_hechos.csv", 'w') as file:
        for x in estadisticas_prom.items():
            file.write("{}:, {} \n".format(x[0], x[1]))
    with open('Swaps_hechos.csv', 'a') as file:
        file.write("Prod1, Prod2 \n")
    # print("Tardó: {}".format(time.time()-t1))
    # print("_______________________")
    lista_swaps = swapity_swap(simulacion.grafo)
    lista = []
    for lista_fam in lista_swaps.values():
        lista += lista_fam
    lista_swaps = lista
    # for x in lista_swaps:
    #     print(x[1:3])
    for i in range(veces_que_busca_mejora):
        # if matar:
        #     print("-----------------------NO SE ENCONTRO MEJORA-----------------------------------")
        #     break
        grafo_iteracion_actual = deepcopy(grafo)
        # print("ESTASITICAS A SUPERAR")
        # print("prob total : {}".format(estadisticas_prom["probabilidad_total"]))
        # print("utilidad_espontanea: {}".format(estadisticas_prom["utilidad_espontanea"]))
        # print("numero medio de compras: {}".format(estadisticas_prom["numero_medio_compras_espontaneas"]))
        # print("______________________________________________________")
        #
        # print("############# LOS SWAGPS ################")
        for _ in range(len(lista_swaps)):
            swap = lista_swaps.pop(0)
            nro_swap = 1
            factible = swap[0](swap[1], swap[2], swap[3])
            buen_candidato = True

            if factible:
                estadisticas_nuevas = dict()
                estadisticas_nuevas["probabilidad_total"] = 0
                estadisticas_nuevas["utilidad_supermercado"] = 0
                estadisticas_nuevas["utilidad_espontanea"] = 0
                estadisticas_nuevas["numero_medio_compras_espontaneas"] = 0
                estadisticas_nuevas["top_productos_espontaneos"] = 0
                estadisticas_nuevas["distancia_media_recorrida"] = 0
                revision_mitad = True
                for nro_iter in range(iteraciones_por_config):
                    estadisticas_iteracion = simulacion.run(clientes_iniciales, limite_boletas)
                    for estadistica in estadisticas_iteracion.items():
                        if type(estadistica[1]) is not list:
                            if estadistica[0] == "probabilidad_total":
                                estadisticas_nuevas[estadistica[0]] += estadistica[1] / (
                                            iteraciones_por_config * clientes_iniciales)
                            else:
                                estadisticas_nuevas[estadistica[0]] += estadistica[1] / iteraciones_por_config
                    if ((nro_iter + 1) >= iteraciones_por_config / 2) and revision_mitad:
                        revision_mitad = False
                        if estadisticas_prom["utilidad_espontanea"] * 1.05/2 < estadisticas_nuevas["utilidad_espontanea"] \
                                and estadisticas_prom["numero_medio_compras_espontaneas"] * 1.05/2 < estadisticas_nuevas[
                                     "numero_medio_compras_espontaneas"]:
                            pass
                            # print("Estadisticas a la mitad:")
                            # print("p total {}".format(estadisticas_nuevas["probabilidad_total"]))
                            # print("ut espontanea {}".format(estadisticas_nuevas["utilidad_espontanea"]))
                            # print("nume medio {}".format(estadisticas_nuevas["numero_medio_compras_espontaneas"]))
                        else:
                            # print("-----No es un buen candidato----- ")
                            # print("_______________________")
                            buen_candidato = False
                            break
                mejor = False
                if buen_candidato:
                    # print("Es un buen candidato")
                    # print("Se probo un swap de {} por {}".format(swap[1], swap[2]))
                    # print("prob total : {}".format(estadisticas_nuevas["probabilidad_total"]))
                    print("utilidad_espontanea: {}".format(estadisticas_nuevas["utilidad_espontanea"]))
                    print("numero medio de compras: {}".format(estadisticas_nuevas["numero_medio_compras_espontaneas"]))
                    if estadisticas_prom["utilidad_espontanea"] < estadisticas_nuevas["utilidad_espontanea"] and estadisticas_prom["numero_medio_compras_espontaneas"] < estadisticas_nuevas["numero_medio_compras_espontaneas"]:
                            mejor = True
                    if mejor:
                        swaps_hechos.append((swap[1], swap[2]))
                        estadisticas_prom = estadisticas_nuevas
                        print('La ESTADISTICA ANTERIOR MEJORO')
                        print("_______________________")
                        simulacion.grafo.guardar_gondolas()
                        with open('Swaps_hechos.csv', 'a') as file:
                            file.write("{}, {} \n".format(swap[1], swap[2]))
                        break
                    else:
                        pass
                        # print("Era un buen candidato pero no lo suficiente")
                        # print("_______________________")

                else:
                    pass
                    # print("Mal candidato")
                    # print("_______________________")
        grafo = grafo_iteracion_actual
    with open('Swaps_hechos.csv', 'a') as file:
        file.write("ESTADISTICAS FINALES \n")
        for i in estadisticas_prom.items():
            file.write("{} : {} \n".format(i[0], i[1]))


