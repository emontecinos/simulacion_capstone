from distribucion_aleatoria import productos_esta_gondola

class Gondola:

    def __init__(self, id, espacios = [None for i in range(17)]):
        self.id = id
        self.espacios = productos_esta_gondola(id) # [None for i in range(17)]

    def solicitar_swap(self):
        pass

    def manejo_swap(self, producto_propio, largo_producto, producto_origen): #esta funcion maneja la solicitud de un swap
        largo_producto_viejo = self.espacios.count(producto_propio)
        if largo_producto_viejo > largo_producto:
            return False
        else:
            if largo_producto_viejo == largo_producto:
                self.swap([producto_propio for i in range(largo_producto_viejo)], producto_origen)
                return [producto_propio for i in range(largo_producto_viejo)]
            else:
                juntar = self.juntar_producto_adyacente(producto_propio, largo_producto)
                if juntar[0]:
                    self.swap(juntar[1], producto_origen)
                    return juntar[1] ###### ver si el swap es con la misma gondola para no swapear dos veces



    def swap(self, productos_propios, producto_origen): #se cambian los espacios de los productos propios por el producto origen
        pass

    def juntar_producto_adyacente(self, producto_propio, largo_producto): #ve si puede juntar el producto a cambiar con el del lado para poder hacer el swap
        pass #retorna bool, lista --> el bool es de si se puede juntar y que calce
                # la lista sería en caso de que se pueda donde se entrega la lista de espacios para darle a la otra gondola


    def __str__(self):
        return "{}".format(self.id)




