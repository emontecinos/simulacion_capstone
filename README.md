# simulacion_capstone
simula el super del capstone

## Funciones:

## Clase simulacion
Atributos:
estadisticas_globales: hagamoslo primero para un cliente y despues implementamos esto.

Metodos:
* cargar_cliente: crea un objeto cliente y le da una lista de compras.
* swap: hace un cambio en el supermercado.

## Clase Gondola
Atributos:
* repisa= lista[pos_vacia, pos_vacia,...,pos_vacia] en unidades equivalentes, llena el largo de la repisa.
Así, repisas = [repisa,repisa,repisa]

## Clase Cliente
Atributos:

ruta: lista ordenada de nodos por los que pasara
nodo_actual: tupla con el nombre del nodo.
Lista de compras: list
Distancia: int
Productos_vistos: list
Compras_espontaneas: list. Tuplas producto,probabilidad

metodos:

* proximo: Recibe el nodo actual y retorna el proximo nodo (lo ve en su ruta)
* avanzar: cambia de nodo, actualiza sus propios stats.


## Clase supermercado
Se utiliza para calcular las distancias entre dos puntos y los productos que se pueden ver desde cada nodo

atributos: 
grafo_supermercado = (v,e)
 
metodos:
* ruta: Recibe un cliente y cambia el atributo ruta.
* inicial: distribucion inicial del supermercado aleatoria
* visibles (grafosuper): recibe el nodo actual y retorna una lista con los productos que ve desde esa poscicion.
de pos i a j de las góndolas
