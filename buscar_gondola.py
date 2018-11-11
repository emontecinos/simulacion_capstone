## Buscar góndola de acuerdo a un producto

def buscar_gondola(productos, supermercado):
    nodos = []
    i = 0
    while len(nodos) < len(productos):
        producto_i = productos[i]
        j = 0
        while j < len(supermercado):
            nodo_j = supermercado[j]
            if producto_i in nodo_j.productos:
                nodos.append(nodo_j)
                break
            j += 1
        i += 1
        
    return nodos
{'g1':[1,5],'g2':[10,20]}
class Nodo:
    def __init__(self,nombre, gondola_rango):
        self.nombre = nombre
        self.gondolas_rango = gondola_rango



productos = ['Acelga', 'Palta', 'Ajo', 'Alcachofa', 'Alcaparra', 'Almendras', 'Apio', 'Avellana', 'Betarraga',
                     'Brócoli', 'Calabaza', 'Castañas', 'Cebolla', 'Champiñón', 'Ciruela', 'Ciruela_pasa', 'Coliflor',
                     'Durazno', 'Espinacas', 'Fresa', 'Frijoles', 'Granada', 'Kiwi', 'Lechuga', 'Lima', 'Limón',
                     'Mandarina', 'Mango', 'Manzana', 'Melón', 'Naranja', 'Nuez', 'Papa', 'Papaya', 'Pasa_(Uva_pasa)',
                     'Pepino', 'Pimiento', 'Piña', 'Plátano', 'Rábano', 'Sandía', 'Tomate',
                     'Tuna', 'Uva', 'Zanahoria']

gondolas = {'g1':[],'g2':[],'g3':[],'g4':[],'g5':[],'g6':[],'g7':[],'g8':[],'g9':[]}
gond1 = 0
gond2 = 5
final = False
while not final:
    print(gond1,gond2)
    for g in range(gond1,gond2):
        gondolas['g{}'.format((gond1//5)+1)].append(productos[g])
    t = gond2
    gond2 = gond2+5
    gond1 = t
    if gond2 >= len(productos):
        gond2 = len(productos)
        for g in range(gond1,gond2):
            gondolas['g{}'.format((gond1//5)+1)].append(productos[g])
        final = True
print(gondolas)

nodos = []
for i in range(3):
    node = Nodo(str(i+1),{})
    #node = Nodo(str(i+1),{gondolas['g{}'.format(2*(i+1)-1)]:gondolas['g{}'.format(2*(i+1)-1)][:3],gondolas['g{}'.format(2*(i+1))]:gondolas['g{}'.format(2*(i+1))][:3]})
print(nodos)

productos_cliente = ['Mandarina','Zanahoria','Piña','Nuez','Acelga','Alcaparra']
nodos_a_visitar = buscar_gondola(productos_cliente,nodos)
print('Cantidad de nodos a visitar: ', len(nodos_a_visitar))
for n in nodos_a_visitar:
    print(n.nombre, n.productos)