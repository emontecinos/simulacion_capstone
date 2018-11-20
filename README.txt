Instrucciones de Uso y detalle de archivos
Grupo 13
Optimizaci�n en la distribuci�n de los productos de un supermercado

Archivos:
Boletas2%.csv, Boletas5%.csv, Boletas 10%.csv, Boletas_20%.csv, Boletas_completas.csv, Boletas.csv, Boletas15.csv, Boletas20.csv:
Son archivos con la base de datos de varias boletas. De ellos se seleccionan clientes y se comparan sus resultados en el main.py.

csv_corr_familias.csv
Archivo que contiene las correlaciones entre las familias.

csv_corr_productos.csv
Archivo que contiene las correlaciones entre los productos.

datos_nodos_new.csv
Archivo que entrega una configuraci�n de los nodos y la fracci�n de las g�ndolas a las que accede cada nodo.

distr_gondolas.csv
Archivo en el que se sobreescribe la distribuci�n de los productos de cada g�ndola. Al inicial el main.py, se carga esta distribuci�n, y al terminar la ejecuci�n de main.py, se guarda la distribuci�n.

distribucion_aleatoria.py
Crea una distribuci�n basada en el modelo de optimizaci�n para los productos. Carga las g�ndolas con sus respectivos productos.

encontrar_correlaciones.py
Lee los archivos de correlaciones e incorpora dicha informaci�n al programa.

GananciasPorProductos.py
Analiza las boletas y determina porcentajes de las familias que le corresponden a cada producto, en funci�n a su utilidad entregada.

gondolas.py
Contiene a la clase Gondola, contiene sus m�todos, donde se destaca manejo_swap().

main.py
Es el coraz�n de la parte computacional. en base a algunos par�metros que indican cuantas iteraciones con cuantos clientes se van a realizar las corridas de una distribuci�n dada del supermercado.
Si las estad�sticas de la nueva corrida son mejores a las de la corrida anterior, entonces actualiza la distribuci�n del supermercado, actualiza distr_gondola.csv e itera sobre esa.

simulacion.py
Contiene a la clase Simulacion, que maneja las estad�sticas de la corrida actual, as� como gestionar el proceso de compra de los clientes.

Cliente.py
Contiene a la clase Cliente. Destaca el m�todo probabilidad_comprar y comprar, donde est� implementado el proceso de compra de un cliente, basado en la cantidad de productos que lleva y la correlaci�n del producto a revisar con los productos comprados.

ordenar_datos_nodos.py
Carga una distribuci�n parcial de los nodos del supermercado, genera una que es v�lida y la almacena en datos_nodos_new.csv

supermercat.py
Contiene al grafo y a los nodos. Encuentra una gondola seg�n un producto, guarda la distribuci�n de las g�ndolas, etc.

swapity_swaps.py
Gestiona el swap entre productos de las g�ndolas de una familia dada. Act�a en base a la distribuci�n del objeto Grafo entregado.



MODO USO

Ejecutar el archivo main.py. Si se desea modificar los par�metros seg�n cuantas iteraciones hacer para una distribuci�n del supermercado, el n�mero de clientes usados en una iteraci�n y/o el n�mero de mejoras que se desean realizar hasta terminar la corrida, basta con cambiar
clientes_iniciales, iteraciones_por_cofig y veces_que_mejora.

La distribuci�n obtenida luego de realizar los intercambios se guarda con la linea
simulacion.grafo.guardar_gondolas().
Esta es guardada en distr_gondolas, donde cada l�nea es una g�ndola.
 
Link al repositorio usado:
https://github.com/emontecinos/simulacion_capstone




