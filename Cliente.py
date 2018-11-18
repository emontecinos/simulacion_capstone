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
        self.ruta = grafo.calcular_ruta_nodos(lista_nodos_a_visitar)
    
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
            if self.comprado == []:
               factor_cant_productos = 1
               factor_corr_producto = encontrar_corr_producto(self.lista_compras, producto)
               factor_corr_familia = encontrar_corr_familia(self.lista_compras, producto)
            else:
                factor_cant_productos = 0.5 + 1/len(self.comprado)
                factor_corr_producto = encontrar_corr_producto(self.lista_compras + self.comprado, producto)
                factor_corr_familia = encontrar_corr_familia(self.lista_compras + self.comprado, producto)
            probabilidad = (float(factor_cant_productos) + float(factor_corr_producto) + float(factor_corr_familia))/3.5
            return probabilidad
    
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


if __name__ == "__main__":
    pass
    #cliente.ordenar_archivo('matriz_correlaciones_productos.txt')

