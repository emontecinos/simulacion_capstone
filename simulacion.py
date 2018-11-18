import csv
from Cliente import Cliente
from supermercat import GraphNode, Graph

import random

class Simulacion:
    def __init__(self, grafo):
        #self.supermerado = Graph()
        self.total_distancias = 0
        self.total_compras = 0
        self.total_vistos = 0
        self.clientes = []
        self.grafo = grafo
        self.estadisticas = {"utilidad_supermercado":0,"utilidad_espontanea":0,"probabilidad_total":0,"numero_medio_compras_espontaneas":0,"distancia_media_recorrida":0,"top_productos_espontaneos":[]}
        self.valor_productos = {'Aceite': 6455, 'Aceite_de_oliva': 7574, 'Grasa_comestible': 600, 'Manteca': 5755, 'Manteca_de_cerdo': 6419, 'Margarina': 8789, 'Margarina_light': 6286, 'Agua_con_gas': 8073, 'Agua_sin_gas': 7715, 'Bebida_hidratante': 5949, 'Jugo_de_fruta': 8212, 'Refresco': 573, 'Cerveza': 8628, 'Jerez': 5708, 'Rompope': 4014, 'Sidra': 7816, 'Vino_de_mesa': 5725, 'Azucar': 7856, 'Cafe_soluble': 8436, 'Cafe_tostado_y_molido': 1014, 'Jarabe_p.preparar_bebidas': 7311, 'Miel_de_abeja': 4953, 'Bebida_energetica': 5195, 'Polvo_p.preparar_bebidas': 2799, 'Te': 4686, 'Bistec_de_diezmillo_de_res': 7622, 'Bistec_de_espaldilla_de_res': 6396, 'Chuleta_de_res': 6391, 'Falda_de_res': 6898, 'Filete_de_res': 4260, 'Higado_de_res': 5351, 'Milanesa_de_res': 2375, 'Panza_de_res': 1706, 'Res': 5613, 'Retazo_hueso_de_res': 3497, 'Ternera': 3679, 'Cabeza_de_cerdo': 7698, 'Carnes_molida_de_cerdo': 7571, 'Carnes_molida_de_res': 3649, 'Cerdo': 2547, 'Chuleta_ahumada_de_cerdo': 6481, 'Espinazo_de_cerdo': 550, 'Lomo_de_cerdo': 5900, 'Milanesa_de_cerdo': 4110, 'Pata_de_cerdo': 1401, 'Pernil': 1432, 'Pavo': 8221, 'Pechuga_de_pollo': 2586, 'Pierna_de_pollo': 286, 'Pollo': 8653, 'Pollo_entero': 4767, 'Arroz': 7878, 'Avena': 5380, 'Cereal_mixto': 7486, 'Harina_de_arroz': 2668, 'Ajonjoli': 4150, 'Canela': 5483, 'Chilorio': 1912, 'Clavo': 1131, 'Cochinita_pibil': 3581, 'Concentrado_de_pollo': 3638, 'Condimento_de_achiote': 8455, 'Hojas_de_perejil': 7139, 'Mayonesa': 6479, 'Mole_rojo_en_pasta': 8764, 'Mostaza': 8212, 'Pimienta': 7040, 'Polvo_p.hornear': 3945, 'Sal': 3370, 'Sal_molida_de_mesa': 6160, 'Salsa': 5906, 'Salsa_catsup': 4191, 'Salsa_de_chile': 8817, 'Salsa_de_soya': 2539, 'Salsa_inglesa': 5032, 'Salsa_mexicana': 942, 'Salsa_picante': 1328, 'Sopa_y_crema': 6538, 'Vainilla': 3903, 'Vinagre': 305, 'Chocolate_en_tablillas': 5266, 'Colacion': 859, 'Flan': 8609, 'Gelatina_en_polvo': 5957, 'Manjarate': 3299, 'Polvo_bebida_sabor_chocolate': 7590, 'Chandell': 8762, 'Postre_estilo_flan': 4472, 'Praline': 5368, 'Torta_Imperial': 744, 'Turron': 1315, 'Poroto': 7046, 'Garbanzo': 2166, 'Haba': 323, 'Lenteja': 8652, 'Galletas': 5453, 'Galletas_dulces': 7783, 'Galletas_populares': 7894, 'Harina_de_trigo': 1341, 'Harina_hot_cakes': 3567, 'Pan_de_caja': 8420, 'Pan_tostado': 2070, 'Pasta_para_sopa': 4111, 'Pastelillos': 3699, 'Tortilla_de_harina_de_trigo': 347, 'Almeja': 4459, 'Atun': 6742, 'Bacalao': 7993, 'Blanco_Nilo': 2162, 'Boqueron': 5084, 'Calamar': 6676, 'Callo_de_hacha': 7745, 'Camaron': 2563, 'Carpa': 7440, 'Cazon': 2929, 'Charal': 7913, 'Cintilla': 418, 'Curvina': 491, 'Gurrubata': 1344, 'Huachinango': 4261, 'Jaiba': 2060, 'Langosta': 2541, 'Acelga': 2122, 'Palta': 1062, 'Ajo': 2445, 'Alcachofa': 3472, 'Alcaparra': 3597, 'Almendras': 4934, 'Apio': 1347, 'Avellana': 6178, 'Betarraga': 4552, 'Brocoli': 3191, 'Calabaza': 923, 'Castanas': 6676, 'Cebolla': 8601, 'Champinon': 6000, 'Ciruela': 5527, 'Ciruela_pasa': 1762, 'Coliflor': 7888, 'Durazno': 4893, 'Espinacas': 2485, 'Fresa': 6592, 'Frijoles': 629, 'Granada': 7777, 'Kiwi': 6892, 'Lechuga': 5081, 'Lima': 3158, 'Limon': 5738, 'Mandarina': 3537, 'Mango': 7136, 'Manzana': 1169, 'Melon': 2591, 'Naranja': 4041, 'Nuez': 7501, 'Papa': 4408, 'Papaya': 8679, 'Pasa_.Uva_pasa.': 8305, 'Pepino': 4463, 'Pera': 8182, 'Pimiento': 6762, 'Pina': 4933, 'Platano': 6312, 'Rabano': 8620, 'Sandia': 6223, 'Tomate': 3150, 'Tuna': 8326, 'Uva': 8595, 'Zanahoria': 698, 'Huevo': 4946, 'Crema': 2791, 'Crema_batida': 7709, 'Mantequilla': 7886, 'Queso_mantecosi': 2549, 'Queso_gauda': 2328, 'Queso_blanco': 8257, 'Yoghurt': 7506, 'Leche_condensada': 7285, 'Leche_en_polvo': 6142, 'Leche_evaporada': 2565, 'Leche_pasteurizada': 1620, 'Leche_ultrapasteurizada': 2504, 'Chorizo': 2455, 'Jamon': 3784, 'jamon_de_pavo': 8376, 'Longaniza': 5372, 'Mortadela': 5013, 'Pastel_pimiento': 3157, 'Pate': 3131, 'Queso_de_puerco': 8161, 'Salami': 7243, 'Salchicha': 6175, 'Tocino': 826, 'Acondicionador_._enjuague': 3156, 'Champu': 4356, 'Champu_para_bebes': 1581, 'Crema_dental': 1682, 'Crema_liquida': 7620, 'Crema_solida': 5459, 'Desodorante': 6648, 'Jabon_de_tocador': 5677, 'Panales_desechables': 1185, 'Papel_higienico': 7739, 'Rastrillos_desechables': 6548, 'Repuestos_de_navajas': 2948, 'Tinte_para_el_cabello': 7408, 'Toalla_femenina': 5226, 'Toallita_humeda_limpiadora': 6392, 'Acondicionador_de_telas': 8785, 'Barra_limpiadora': 5834, 'Blanqueador': 1975, 'Detergente_ropa': 374, 'Detergente_ropa_liquido': 645, 'Detergente_ropa_polvo': 7464, 'Detergente_trastes': 1246, 'Insecticida_aerosol': 8752, 'Jabon_de_pasta': 4757, 'Jabon_limpiador': 4546, 'Limpiador_liquido': 5309, 'Limpiador_lìquido_piso': 4534, 'Servilletas_de_papel': 4951, 'Suavizante_ropa': 7260, 'Toalla_de_papel': 1277}
        self.productos = []
        self.cargar_productos()

    def cargar_productos(self):
        listas_fam_prods = [['Aceite', 'Aceite_de_oliva', 'Grasa_comestible', 'Manteca',
                    'Manteca_de_cerdo', 'Margarina', 'Margarina_Light'],['Agua_con_gas', 'Agua_sin_gas', 'Bebida_hidratante', 'Jugo_de_fruta',
            'Refresco', 'Cerveza', 'Jerez', 'Rompope', 'Sidra', 'Vino_de_mesa'],['Azucar', 'Cafe_soluble', 'Cafe_tostado_y_molido', 'Jarabe_p.preparar_bebidas',
                        'Miel_de_abeja', 'Bebida_energetica', 'Polvo_p.preparar_bebidas', 'Te'],['Bistec_de_diezmillo_de_res', 'Bistec_de_espaldilla_de_res', 'Chuleta_de_res', 'Falda_de_res',
            'Filete_de_res', 'Higado_de_res', 'Milanesa_de_res', 'Panza_de_res', 'Res', 'Retazo_hueso_de_res',
            'Ternera', 'Cabeza_de_cerdo', 'Carnes_molida_de_cerdo', 'Carnes_molida_de_res', 'Cerdo',
            'Chuleta_ahumada_de_cerdo', 'Espinazo_de_cerdo', 'Lomo_de_cerdo', 'Milanesa_de_cerdo', 'Pata_de_cerdo',
            'Pernil', 'Pavo', 'Pechuga_de_pollo', 'Pierna_de_pollo', 'Pollo', 'Pollo_entero'],['Arroz', 'Avena', 'Cereal_mixto', 'Harina_de_arroz'],['Ajonjoli', 'Canela', 'Chilorio', 'Clavo', 'Cochinita_pibil', 'Concentrado_de_pollo',
                            'Condimento_de_achiote', 'Hojas_de_perejil', 'Mayonesa', 'Mole_rojo_en_pasta',
                            'Mostaza', 'Pimienta', 'Polvo_p.hornear', 'Sal', 'Sal_molida_de_mesa', 'Salsa',
                            'Salsa_catsup', 'Salsa_de_chile', 'Salsa_de_soya', 'Salsa_inglesa', 'Salsa_mexicana',
                            'Salsa_picante', 'Sopa_y_crema', 'Vainilla', 'Vinagre'],['Chocolate_en_tablillas', 'Colacion', 'Flan', 'Gelatina_en_polvo',
                        'Manjarate', 'Polvo_bebida_sabor_chocolate', 'Chandell', 'Postre_estilo_flan',
                        'Praline', 'Torta_Imperial', 'Turron'],['Poroto', 'Garbanzo', 'Haba', 'Lenteja'],['Galletas', 'Galletas_dulces', 'Galletas_populares', 'Harina_de_trigo',
                                'Harina_hot_cakes', 'Pan_de_caja', 'Pan_tostado', 'Pasta_para_sopa',
                                'Pastelillos', 'Tortilla_de_harina_de_trigo'],['Almeja', 'Atun', 'Bacalao', 'Blanco_Nilo', 'Boqueron', 'Calamar', 'Callo_de_hacha',
                        'Camaron', 'Carpa', 'Cazon', 'Charal', 'Cintilla', 'Curvina', 'Gurrubata',
                        'Huachinango', 'Jaiba', 'Langosta'],['Acelga', 'Palta', 'Ajo', 'Alcachofa', 'Alcaparra', 'Almendras', 'Apio', 'Avellana', 'Betarraga',
                        'Brocoli', 'Calabaza', 'Castanas', 'Cebolla', 'Champinon', 'Ciruela', 'Ciruela_pasa', 'Coliflor',
                        'Durazno', 'Espinacas', 'Fresa', 'Frijoles', 'Granada', 'Kiwi', 'Lechuga', 'Lima', 'Limon',
                        'Mandarina', 'Mango', 'Manzana', 'Melon', 'Naranja', 'Nuez', 'Papa', 'Papaya', 'Pasa_.Uva_pasa.',
                        'Pepino', 'Pera', 'Pimiento', 'Pina', 'Platano', 'Rabano', 'Sandia', 'Tomate',
                        'Tuna', 'Uva', 'Zanahoria'],['Huevo', 'Crema', 'Crema_batida', 'Mantequilla', 'Queso_mantecosi', 'Queso_gauda',
                    'Queso_blanco', 'Yoghurt', 'Leche_condensada', 'Leche_en_polvo', 'Leche_evaporada',
                    'Leche_pasteurizada', 'Leche_ultrapasteurizada'],['Chorizo', 'Jamon', 'jamon_de_pavo', 'Longaniza', 'Mortadela', 'Pastel_pimiento',
                'Pate', 'Queso_de_puerco', 'Salami', 'Salchicha', 'Tocino'],['Acondicionador_._enjuague', 'Champu', 'Champu_para_bebes', 'Crema_dental',
                        'Crema_liquida', 'Crema_solida', 'Desodorante', 'Jabon_de_tocador', 'Panales_desechables',
                        'Papel_higienico', 'Rastrillos_desechables', 'Repuestos_de_navajas', 'Tinte_para_el_cabello',
                        'Toalla_femenina', 'Toallita_humeda_limpiadora'],['Acondicionador_de_telas', 'Barra_limpiadora', 'Blanqueador', 'Detergente_ropa',
                    'Detergente_ropa_liquido', 'Detergente_ropa_polvo', 'Detergente_trastes',
                    'Insecticida_aerosol', 'Jabon_de_pasta', 'Jabon_limpiador', 'Limpiador_liquido',
                    'Limpiador_liquido_piso', 'Servilletas_de_papel', 'Suavizante_ropa', 'Toalla_de_papel']]

        for i in listas_fam_prods:
            for j in i:
               self.productos.append(j)


    def cargar_clientes(self, num_clientes, tope_boleta):
        with open('Boletas.csv', 'r') as Boletas:
            datos = csv.reader(Boletas)
            informacion = [dato for dato in datos]
            for i in range(num_clientes):
                numero_de_boleta = str(i+1)
                #numero_de_boleta = str(random.randint(1,int(tope_boleta)))
                producto_en_lista = []
                productoactual = 0
                for row in informacion:
                    #print('row',row)
                    lista = row[0].split(";")
                    
                    if numero_de_boleta == lista[1]: # cuando es la que queremos
                        for indice in range(2, len(lista)):
                            if "1" in lista[indice]:
                                producto_en_lista.append(self.productos[int(indice)-2])  ## el primer producto va a ser el 0   
                self.clientes.append(Cliente(producto_en_lista))

    def calcular_rutas_productos_clientes(self):
        for cliente in self.clientes:
            cliente.calcular_ruta(self.grafo)
            cliente.calcular_productos_vistos(self.grafo)
    
    def comprar_clientes(self):
        for cliente in self.clientes:
            for prod in cliente.productos_vistos:
                cliente.comprar_producto(prod)
    
    def actualizar_stats(self):
        # utiidad supermercado
        for cliente in self.clientes:
            for producto in cliente.comprado:
                self.estadisticas["utilidad_supermercado"] += self.valor_productos[producto]
        
        # utilidad espontanea
        for cliente in self.clientes:
            for producto in cliente.compras_espontaneas:
                self.estadisticas["utilidad_espontanea"] += self.valor_productos[producto]
        
        # probabilidad total
        for cliente in self.clientes:
            self.estadisticas["probabilidad_total"] += cliente.probabilidad_total
        
        #numero medio compras espontaneas
        numero = 0
        for cliente in self.clientes:
            for prod_espontaneo in cliente.compras_espontaneas:
                numero+= 1
        self.estadisticas["numero_medio_compras_espontaneas"] = numero/len(self.clientes)

        # top productos comprados espontaneamente
        total_prods_espontaneos = []
        for cliente in self.clientes:
            for prod_espontaneo in cliente.compras_espontaneas:
                total_prods_espontaneos.append(prod_espontaneo)
        dict_prods = {}
        for prod in total_prods_espontaneos:
            if prod not in dict_prods.keys():
                dict_prods[prod]=total_prods_espontaneos.count(prod)
        max_prod = max(dict_prods.keys(), key=(lambda k:dict_prods[k]))
        self.estadisticas["top_productos_espontaneos"]=[max_prod,dict_prods[max_prod]]

        # calcular_distnacia_recorrida
        for cliente in self.clientes:
            cliente.calcular_distancia_recorrida()

        
        for k in self.estadisticas:
            print(k, self.estadisticas[k])
        
    def run(self, num_clientes, tope_boleta):
        self.cargar_clientes(num_clientes, tope_boleta)
        self.calcular_rutas_productos_clientes()
        self.comprar_clientes()
        self.actualizar_stats()

                

    def swap(self, nodo):
        pass

if __name__ == "__main__":
    grafo = Graph()
    grafo.cargar_base("datos_nodos_new.csv")
    simulacion = Simulacion(grafo)
    simulacion.run(10, 40)
    # for grafo in simulacion.grafo.nodos:
    #   print(simulacion.grafo.get_node(grafo).veces_visitado)
    gondola = grafo.gondolas["1I"]
    gondola_2 = grafo.gondolas["10I"]
    print(gondola)
    print(gondola_2)
    gondola.manejo_swap('Falda_de_res', 'Pollo', gondola_2)
    print(gondola)
    print(gondola_2)
    simulacion.run(10, 40)



