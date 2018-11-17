def calcular_ruta_productos_vistos(grafo, productos):
    dict_nodos_a_visitar = grafo.buscar_gondola(productos)
    lista_nodos_a_visitar = []
    for i in dict_nodos_a_visitar:
        if dict_nodos_a_visitar[i] not in lista_nodos_a_visitar:
            lista_nodos_a_visitar.append(dict_nodos_a_visitar[i])
    ruta = grafo.calcular_ruta_nodos(lista_nodos_a_visitar)
    dict_productos_vistos = []
    productos_vistos = []
    for n in ruta:
        dict_productos_vistos.append(grafo.productos_visibles(n))
    for i in dict_productos_vistos:
            for j in i:
                    if j not in productos_vistos:
                            productos_vistos.append(j)
    print(productos_vistos, len(productos_vistos))
    print(ruta)
    return ruta, productos_vistos