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
        print(self)
        productos = set()
        for gondola in self.gondolas:
            for posicion in self.posiciones_accesibles:
                productos.add(gondola.espacios[int(posicion)])
                print(gondola.espacios[int(posicion)])
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
            for producto in nodo_adyacente.productos_accesibles:
                productos.add(producto)
        if nodo.productos_accesibles:
            productos.add(*nodo.productos_accesibles)
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
                _posiciones = []
                for posicion in posiciones.split(";"):
                    if not posicion == "None":
                        _posiciones.append(int(posicion))
                self.nodos[nodo] = GraphNode(nodo, x, y, gondolas, _posiciones)
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
        return distancia, camino
    
    def calcular_ruta_nodos(self, nodos, ruta = []):
        if ruta == []:
            inicial = "(11,13)"
            ruta.append(inicial)
        else:
            inicial = ruta[-1]
        # Cargar rutas entre todos los nodos a visitar
        dict_nodos = {}
        for nodo_i in nodos:
            if nodo_i not in ruta:
                distancia, camino = self.distancia_camino(inicial, nodo_i)
                dict_nodos[(inicial,nodo_i)] = [camino, distancia]
                if inicial == nodo_i:
                    dict_nodos[(inicial,nodo_i)] = inicial
        par_minimo = min(dict_nodos.keys(), key=(lambda k: dict_nodos[k][-1]))
        for t in dict_nodos[par_minimo][0]:
            if str(t) not in ruta:
                ruta.append(str(t))
        for nodoe in nodos:
            if nodoe not in ruta:
                self.calcular_ruta_nodos(nodos,ruta)
        # Los retorna como un string [...,'(1,2)','(4,5)',...]
        return ruta


grafo = Graph()
grafo.cargar_base("datos_nodos.csv")

#  Calcular ruta minima
nodes = ["(2,2)","(10,1)","(3,5)","(9,3)"]
ruta = grafo.calcular_ruta_nodos(nodes)
print('ruta')
print(ruta)

#grafo.productos_visibles("(2,2)")

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

