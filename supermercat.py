import csv
from gondolas import Gondola

class GraphNode:
    def __init__(self, id, x, y, gondolas, posiciones_accesibles = None):
        self.conexiones = set()
        self.posiciones_accesibles = posiciones_accesibles
        self.gondolas = gondolas
        self.id = id
        self.x = x
        self.y = y
        for i in self.conexiones:
            self.conectar(i)

    def conectar(self, nodo):
        self.conexiones.add(nodo.id)

    def desconectar(self, nodo):
        self.conexiones.remove(nodo.nombre)

    @property
    def productos_accesibles(self):
        productos = set()
        for gondola in self.gondolas:
            for posicion in self.posiciones_accesibles:
                productos.add(gondola.espacios[int(posicion)])
        return productos

    def __repr__(self):
        return self.id


class Graph:
    def __init__(self):
        self.nodos = dict()
        self.gondolas = {"1I": Gondola("1I"), "2I": Gondola("2I"), "1D": Gondola("1D"), "3I": Gondola("3I")}

    def productos_visibles(self, nodo):
        nodo = self.get_node(nodo)
        productos = set()
        for conexion in nodo.conexiones:
            nodo_adyacente = self.get_node(conexion)
            productos.add(*nodo_adyacente.productos_accesibles)
        return productos


    def _crear_nodo(self, nombre):
        nodo = self.nodos.get(nombre)
        if nodo is None:
            nodo = GraphNode(nombre)
            self.nodos[nombre] = nodo
        return nodo

    def agregar_conexion(self, origen, destino):
        nodo_origen = self._crear_nodo(origen)
        nodo_destino = self._crear_nodo(destino)
        nodo_origen.conectar(nodo_destino)

    def cargar_base(self, path_base):
        with open(path_base, 'r') as file:
            datos = csv.reader(file)
            next(datos)
            list_datos = [dato for dato in datos]
            for nodo in list_datos:
                nodo, conexiones, x, y, gondolas, posiciones = nodo
                nodo = "(" + nodo.replace(";",",") + ")"
                gondolas = [self.get_gondola(i) for i in gondolas.split(";")]
                posiciones = "(" + posiciones.replace(";",",") + ")"
                self.nodos[nodo] = GraphNode(nodo, x, y, gondolas, posiciones)
            for nodo in list_datos:
                nodo, conexiones, x, y, gondolas, posiciones = nodo
                conexiones = conexiones.strip().split("-")
                for i in conexiones:
                    origen = "("+nodo.replace(";",",")+")"
                    tupla = "("+i.replace(";",",")+")"
                    self.nodos[origen].conectar(self.get_node(tupla))
                    self.nodos[tupla].conectar(self.get_node(origen))

    def get_node(self, name):
        if name in self.nodos.keys():
            return self.nodos[name]
        return None

    def get_gondola(self, id):
        if id == "None":
            return None
        return self.gondolas[id]

    def encontrar_camino(self, origen, destino):
        if origen == destino:
            return True
        origen = self.get_node(origen)
        destino = self.get_node(destino)
        if origen is None or destino is None:
            return None
        cola = [[origen]]
        visited = list()
        while len(cola):
            current_path = cola.pop(0)
            current = current_path[-1]
            if current not in visited:
                lista_vecinos = [self.get_node(x) for x in current.conexiones]
                for vecino in lista_vecinos:
                    cola.append(list(current_path) + [vecino])
                    if vecino == destino:
                        return cola[-1]
                visited.append(current)
        return None

    def distancia_camino(self, origen, destino):
        camino = self.encontrar_camino(origen, destino)
        nodo_inicial = camino[0]
        nodo_anterior = nodo_inicial
        distancia = 0
        for nodo in camino:
            distancia += abs(float(nodo_anterior.x) - float(nodo.x))
            distancia += abs(float(nodo_anterior.y) - float(nodo.y))
            nodo_anterior = nodo
        return distancia

grafo = Graph()
grafo.cargar_base("datos_nodos.csv")
grafo.gondolas = {"1I": Gondola("1I"), "2I": Gondola("2I"), "1D": Gondola("1D")}

grafo.productos_visibles("(1,1)")


#print(grafo.distancia_camino("(10,1)","(11,7)"))



#nodos = []

# for i in range(1,10):
#     tupla = f"({i},4)"
#     nodos.append(tupla)
# for i in range(1,12):
#     tupla = f"({i},10)"
#     nodos.append(tupla)
# nodos.append("(3.5,1)")
# nodos.append("(7.5,1)")
# for nodo in nodos:
#     for destino in nodos:
#         if nodo != destino:
#             distancia = grafo.distancia_camino(nodo, destino)
#         else:
#             distancia = "0"
#         print(f"{nodo} {destino} {distancia}")

