import csv

class Simulation:
    def __init__(self):
        #self.supermerado = Graph()
        self.total_distancias = 0
        self.total_compras = 0
        self.total_vistos = 0
        self.cliente = None

    def cargar_cliente(self, numero_de_boleta):
        with open('Boletas.csv', 'r') as Boletas:
            next(Boletas)

            producto_en_lista = []
            numerodeboleta = 1
            productoactual = 0

            for row in Boletas:
                if numero_de_boleta == numerodeboleta: # cuando es la que queremos
                    lista = row.split(";")
                    for indice in range(2, len(lista)):
                        if "1" in lista[indice]:
                            producto_en_lista.append(int(indice)-2)  ## el primer producto va a ser el 0
                    
                numerodeboleta += 1
            print(producto_en_lista)

    def swap(self, nodo):
        pass

if __name__ == "__main__":
    mysimulation = Simulation()
    mysimulation.cargar_cliente(15)


