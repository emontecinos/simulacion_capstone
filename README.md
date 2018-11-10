﻿# Simulacion_capstone
simula el super del capstone

## Funciones:

## Clase simulacion
Atributos:
estadisticas_globales: hagamoslo primero para un cliente y despues implementamos esto.
Medir utilidades del supermercado y probabilidades acumuladas de posibilidad de compra

Metodos:
* cargar_cliente: obtiene un cliente en base a las boletas
* swap: hace un cambio en el supermercado. Los swaps se haran de un objeto mas largo a uno mas corto, si se puede se hace el cambio, si no se puede el objeto corto revisa si tiene un objeto adyacente cuyo largo sumado al de si mismo sea igual al del producto con el cual se desea hacer el swap.



## Clase Gondola
Atributos:
Cada gondola estara dividida por secciones, por lo que solo tendra una dimension
* productos: [lista de 17 slots de 16 unidades equivalentes cada uno]

## Clase Cliente
Atributos:

ruta: lista ordenada de nodos por los que pasara
nodo_actual: tupla con el nombre del nodo.
Lista de compras: list
Distancia: int
Productos_vistos: set
Compras_espontaneas: list. Tuplas producto,probabilidad

metodos:

* proximo: Recibe el nodo actual y retorna el proximo nodo (lo ve en su ruta)
* avanzar: cambia de nodo, actualiza sus propios stats.
* calcular la probabilidad de compra cuando vea un producto


## Clase supermercado
Se utiliza para calcular las distancias entre dos puntos y los productos que se pueden ver desde cada nodo

atributos: 
grafo_supermercado = (v,e)
 
metodos:
* ruta: Recibe un cliente y cambia el atributo ruta.
* inicial: distribucion inicial del supermercado aleatoria
* visibles (grafosuper): recibe el nodo actual y retorna una lista con los productos que ve desde esa poscicion.
de pos i a j de las góndolas


## Update

Las gondolas se van a dividir en 17 slots de 16 unidades equivalentes cada una, por lo que cada producto tendrá asignado un espacio fijo en slots ,de 1 a 4 segun la categoria en que caiga.
(corto, medio corto, medio latgo, largo)


La dinamica de la simulacion va a ser:  
Poblar el supermercado con todos los productos  
para cada cliente actualizar los stats en cada nodo

