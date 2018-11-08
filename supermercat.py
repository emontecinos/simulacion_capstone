

class GraphNode:
    def __init__(self, id, conexiones, posiciones_visibles = None):
        self.conexiones = set()
        self.posiciones_visibles = posiciones_visibles
        for i in conexiones:
            self.conectar(i)

    def conectar(self, nodo):
        self.conexiones.add(nodo.nombre)

    def desconectar(self, nodo):
        self.conexiones.remove(nodo.nombre)


class Graph:
    def __init__(self):
        self.nodos = dict()

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

    def quitar_conexion(self, origen, destino):
        nodo_origen = self.nodos.get(origen)
        nodo_destino = self.nodos.get(destino)
        nodo_origen.desconectar(nodo_destino)

    def cargar_base(self, path_base):
        with open(path_base, 'r') as file:
            for line in file:
                nodo, x, y, conexiones = line.strip().split(",")
                for i in conexiones:
                    pass

    def existe_camino(self, origen, destino, visited=None):
        nodo_origen = self.nodos.get(origen)
        if origen == destino:
            return True
        if visited is None:
            visited = []
        for nodo in nodo_origen.conexiones:
            if not nodo in visited:
                visited.append(nodo)
                if self.existe_camino(nodo, destino, visited):
                    return True
        return False

    def get_node(self, name):
        if name in self.nodos.keys():
            return self.nodos[name]
        return None

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
