from distribucion_aleatoria import productos_esta_gondola

class Gondola:

    def __init__(self, id, largo, espacios = [None for i in range(17)]):
        self.id = id
        self.espacios = productos_esta_gondola(id) # [None for i in range(17)]
        self.largo = len(self.espacios) if self.espacios else 17

    def solicitar_swap(self):
        pass

    def manejo_swap(self, producto_propio, largo_producto, producto_origen): #esta funcion maneja la solicitud de un swap
        largo_producto_viejo = self.espacios.count(producto_propio) # cuento cuantos espacios de la gondola estoy usando
        if largo_producto_viejo > largo_producto:
            return False
        else:
            if largo_producto_viejo == largo_producto:
                self.swap([producto_propio for i in range(largo_producto_viejo)], producto_origen)
                return [producto_propio for i in range(largo_producto_viejo)] # retorno la lista de slots a poner en la gondola que solicito el swap
            else:
                juntar = self.juntar_producto_adyacente(producto_propio, largo_producto)
                if juntar[0]:
                    self.swap(juntar[1], producto_origen)
                    return juntar[1] ###### ver si el swap es con la misma gondola para no swapear dos veces



    def swap(self, productos_propios, producto_origen): #se cambian los espacios de los productos propios por el producto origen
        pass

    def juntar_producto_adyacente(self, producto_propio, cantidad_necesitada): #ve si puede juntar el producto a cambiar con el del lado para poder hacer el swap
        '''retorna bool, lista --> el bool es de si se puede juntar
        y que calce la lista sería en caso de que se pueda donde se entrega
        la lista de espacios para darle a la otra gondola '''
        i = 0
        for espacio in self.espacios:
            if espacio == producto_propio:
                break
            else:
                i += 1
        j = i
        for espacio in self.espacios[i:]:
            if espacio != producto_propio:
                j -= 1
                break
            else:
                j += 1
        productos = {producto_propio}
        suma = self.espacios.count(producto_propio)
        intento_izq = self.intentar_combinaciones(True, i, j, suma, cantidad_necesitada, productos)
        # print("termine con ese lado")
        # productos_d = {producto_propio}
        # intento_der = self.intentar_combinaciones(False, i, j, suma, cantidad_necesitada, productos_d)
        if intento_izq[0]:
            print("izq")
            return intento_izq[1]
        # elif intento_der[0]:
        #     print("derecha")
        #     return intento_der[1]
        print("NO SE PUEE!")



    def intentar_combinaciones(self, izquierda, i, j, suma, cantidad_necesitada, productos):
        if izquierda and i-1 >= 0:
            producto_nuevo = self.espacios[i-1]
            largo_producto_nuevo = self.espacios.count(producto_nuevo)
            suma += largo_producto_nuevo
            productos_extendidos = productos | {producto_nuevo}
            #print(productos_extendidos, suma, cantidad_necesitada)
            if suma == cantidad_necesitada:
                return True, productos_extendidos
            elif suma < cantidad_necesitada:
                i_nuevo = i - largo_producto_nuevo
                intento_der = self.intentar_combinaciones(False, i_nuevo, j,
                                                          suma,
                                                          cantidad_necesitada,
                                                          productos_extendidos)
                productos_extendidos = productos | {producto_nuevo}
                intento_izq = self.intentar_combinaciones(True, i_nuevo, j, suma, cantidad_necesitada, productos_extendidos)
                if intento_der[0]:
                    return intento_der
                elif intento_izq[0]:
                    return intento_izq
                else:
                    return False, None
            else:
                #productos.remove(producto_nuevo)
                return False, None
        elif not izquierda and j+1 <= self.largo:
            producto_nuevo = self.espacios[j + 1]
            largo_producto_nuevo = self.espacios.count(producto_nuevo)
            suma += largo_producto_nuevo
            productos_extendidos = productos | {producto_nuevo}
            #print(productos, suma)
            if suma == cantidad_necesitada:
                return True, productos_extendidos
            elif suma < cantidad_necesitada:
                j_nuevo = j + largo_producto_nuevo
                intento_izq = self.intentar_combinaciones(True, i, j_nuevo, suma, cantidad_necesitada,
                                                          productos_extendidos)
                productos_extendidos = productos | {producto_nuevo}
                intento_der = self.intentar_combinaciones(False, i, j_nuevo, suma, cantidad_necesitada,
                                                          productos_extendidos)
                if intento_izq[0]:
                    return intento_izq
                elif intento_der[0]:
                    return intento_der
                else:
                    return False, None
            else:
                #productos.remove(producto_nuevo)
                return False, None
        else:
            return False, None

    def __str__(self):
        return "{}".format(self.id)

if __name__ == "__main__":
    slots = ["leche", "cereal", "queso", "trigo","trigo", "pan", "pan", "carne","carne","carne","carne", None, None, None, None, None, None]
    gondola = Gondola(0, 17)
    gondola.espacios = slots
    print(gondola.juntar_producto_adyacente("queso", 5))