Instrucciones de Uso y detalle de archivos
Grupo 13
Optimización en la distribución de los productos de un supermercado

Archivos:
Boletas2%.csv, Boletas5%.csv, Boletas 10%.csv, Boletas_20%.csv, Boletas_completas.csv, Boletas.csv, Boletas15.csv, Boletas20.csv:
Son archivos con la base de datos de varias boletas. De ellos se seleccionan clientes y se comparan sus resultados en el main.py.

csv_corr_familias.csv
Archivo que contiene las correlaciones entre las familias.

csv_corr_productos.csv
Archivo que contiene las correlaciones entre los productos.

datos_nodos_new.csv
Archivo que entrega una configuración de los nodos y la fracción de las góndolas a las que accede cada nodo.

distr_gondolas.csv
Archivo en el que se sobreescribe la distribución de los productos de cada góndola. Al inicial el main.py, se carga esta distribución, y al terminar la ejecución de main.py, se guarda la distribución.

distribucion_aleatoria.py
Crea una distribución basada en el modelo de optimización para los productos. Carga las góndolas con sus respectivos productos.

encontrar_correlaciones.py
Lee los archivos de correlaciones e incorpora dicha información al programa.

GananciasPorProductos.py
Analiza las boletas y determina porcentajes de las familias que le corresponden a cada producto, en función a su utilidad entregada.

gondolas.py
Contiene a la clase Gondola, contiene sus métodos, donde se destaca manejo_swap().

main.py
Es el corazón de la parte computacional. en base a algunos parámetros que indican cuantas iteraciones con cuantos clientes se van a realizar las corridas de una distribución dada del supermercado.
Si las estadísticas de la nueva corrida son mejores a las de la corrida anterior, entonces actualiza la distribución del supermercado, actualiza distr_gondola.csv e itera sobre esa.

simulacion.py
Contiene a la clase Simulacion, que maneja las estadísticas de la corrida actual, así como gestionar el proceso de compra de los clientes.

Cliente.py
Contiene a la clase Cliente. Destaca el método probabilidad_comprar y comprar, donde está implementado el proceso de compra de un cliente, basado en la cantidad de productos que lleva y la correlación del producto a revisar con los productos comprados.

ordenar_datos_nodos.py
Carga una distribución parcial de los nodos del supermercado, genera una que es válida y la almacena en datos_nodos_new.csv

supermercat.py
Contiene al grafo y a los nodos. Encuentra una gondola según un producto, guarda la distribución de las góndolas, etc.

swapity_swaps.py
Gestiona el swap entre productos de las góndolas de una familia dada. Actúa en base a la distribución del objeto Grafo entregado.



MODO USO

Ejecutar el archivo main.py. Si se desea modificar los parámetros según cuantas iteraciones hacer para una distribución del supermercado, el número de clientes usados en una iteración y/o el número de mejoras que se desean realizar hasta terminar la corrida, basta con cambiar
clientes_iniciales, iteraciones_por_cofig y veces_que_mejora.

La distribución obtenida luego de realizar los intercambios se guarda con la linea
simulacion.grafo.guardar_gondolas().
Esta es guardada en distr_gondolas, donde cada línea es una góndola.
 
Link al repositorio usado:
https://github.com/emontecinos/simulacion_capstone




