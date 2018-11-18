import random
from encontrar_correlaciones import encontrar_corr_familia, encontrar_corr_producto


class Cliente:
    def __init__(self, lista_compras):
        self.lista_compras = lista_compras
        self.comprado = []
        self.distancia_recorida = 0
        self.compras_espontaneas = []
        self.productos_vistos = []
        self.ruta = None
    
    def calcular_ruta(self, grafo):
        dict_nodos_a_visitar = grafo.buscar_gondola(self.lista_compras)
        lista_nodos_a_visitar = []
        for i in dict_nodos_a_visitar:
            if dict_nodos_a_visitar[i] not in lista_nodos_a_visitar:
                lista_nodos_a_visitar.append(dict_nodos_a_visitar[i])
        self.ruta = grafo.calcular_ruta_nodos(lista_nodos_a_visitar,[])
        for nodo in self.ruta:
            node = grafo.get_node(nodo)
            node.veces_visitado += 1
    
    def calcular_productos_vistos(self,grafo):
        dict_productos_vistos = []
        for nodo in self.ruta:
            dict_productos_vistos.append(grafo.productos_visibles(nodo))
        for i in dict_productos_vistos:
            for j in i:
                    if j not in self.productos_vistos and j != None:
                            self.productos_vistos.append(j)
    
    def probabilidad_comprar(self, producto):

        if producto in self.lista_compras:
            return 1
        elif producto not in self.productos_vistos:
            return 0
        else:
            a = 0.15
            b = 0.513
            c = 0.0
            if self.comprado == []:
               factor_cant_productos = 1
               factor_corr_producto = encontrar_corr_producto(self.lista_compras, producto)
               factor_corr_familia = encontrar_corr_familia(self.lista_compras, producto)
            else:
                factor_cant_productos =  1/len(self.comprado)
                factor_corr_producto = encontrar_corr_producto(list(set(self.lista_compras + self.comprado)), producto)
                factor_corr_familia = encontrar_corr_familia(list(set(self.lista_compras + self.comprado)), producto)

            probabilidad = 1*(a*float(factor_cant_productos) + b*float(factor_corr_producto) + c*float(factor_corr_familia))/2
            return probabilidad
    
    def comprar_producto(self, producto):
        if producto not in self.comprado:
            probabilidad_comprar_prod = self.probabilidad_comprar(producto)
            prob_random = random.random()
            #print('Probabilidad: {}, comparador: {}'.format(probabilidad_comprar_prod, prob_random))
            if probabilidad_comprar_prod >= prob_random:
                self.comprado.append(producto)
                if producto not in self.lista_compras:
                    self.compras_espontaneas.append(producto)
                #print("El cliente ha comprado {}".format(producto))
    
    # Ordena el txt en un csv
    def ordenar_archivo(self, archivo):
        with open (archivo) as file:
            string = ""
            lineas = file.readlines()
            for linea in lineas:
                lista_linea = linea.strip().split("\t")
                for elem in lista_linea:
                    string += elem + ','
                string=string[:-1]
                string += "\n"
        with open ("csv_corr_productos.csv",'w') as file:
            file.write(string)

    def __repr__(self):
        return "Lista_compras: {}, Comprados: {}".format(self.lista_compras, self.comprado)


if __name__ == "__main__":
    pass
    #cliente.ordenar_archivo('matriz_correlaciones_productos.txt')

