from collections import namedtuple

with open("Book1.csv", encoding="latin-1") as archivo:
    gen = (linea for linea in archivo)
    lista = next(gen).strip().split(",")
    productos = namedtuple("Productos", lista)
    for linea in gen:
        pass


