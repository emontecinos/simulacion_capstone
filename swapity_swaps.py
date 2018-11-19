from supermercat import Graph

super = Graph()
super.cargar_gondolas("distr_gondolas.csv")


def buscar_gondola(producto, super):
    nodos = []
    for gondola in super.gondolas.values():
        if producto in gondola.espacios:
            return gondola

def swapity_swap(grafo):
    dict_20_80 = {'aceite_y_grasas': ['Margarina', 'Margarina_light'], 'bebidas': ['Agua_con_gas', 'Agua_sin_gas', 'Sidra'], 'cafe_y_endulzantes': ['Azucar', 'Jarabe_p.preparar_bebidas', 'Miel_de_abeja'], 'carnes': ['Bistec_de_diezmillo_de_res', 'Falda_de_res', 'Pavo', 'Pollo'], 'cereales': [], 'condimentos_y_aderezos': ['Canela', 'Condimento_de_achiote', 'Mayonesa', 'Mole_rojo_en_pasta', 'Mostaza', 'Salsa_de_chile', 'Salsa_inglesa'], 'dulces_y_golosinas': ['Flan', 'Chandell', 'Praline'], 'legumbres_secas': [], 'pan_y_derivados_del_trigo': ['Galletas_dulces', 'Pan_de_caja'], 'pescado_y_mariscos': ['Bacalao', 'Carpa'], 'frutas_y_verduras': ['Ciruela', 'Coliflor', 'Granada', 'Pasa_.Uva_pasa.', 'Pera', 'Tuna'], 'lacteos_y_huevo': ['Huevo', 'Crema_batida', 'Mantequilla', 'Queso_blanco', 'Leche_condensada', 'Leche_en_polvo'], 'fiambreria': ['jamon_de_pavo', 'Queso_de_puerco'], 'cuidado_personal': ['Rastrillos_desechables', 'Tinte_para_el_cabello', 'Toalla_femenina'], 'limpieza_hogar': ['Barra_limpiadora', 'Suavizante_ropa']}

    Aceites_y_grasas = ['Aceite', 'Aceite_de_oliva', 'Grasa_comestible', 'Manteca',
                        'Manteca_de_cerdo', 'Margarina', 'Margarina_light']

    Bebidas = ['Agua_con_gas', 'Agua_sin_gas', 'Bebida_hidratante', 'Jugo_de_fruta',
               'Refresco', 'Cerveza', 'Jerez', 'Rompope', 'Sidra', 'Vino_de_mesa']

    Cafe_endulzantes_y_saborizantes = ['Azucar', 'Cafe_soluble',
                                       'Cafe_tostado_y_molido',
                                       'Jarabe_p.preparar_bebidas',
                                       'Miel_de_abeja', 'Bebida_energetica',
                                       'Polvo_p.preparar_bebidas', 'Te']

    Carnes = ['Bistec_de_diezmillo_de_res', 'Bistec_de_espaldilla_de_res',
              'Chuleta_de_res', 'Falda_de_res',
              'Filete_de_res', 'Higado_de_res', 'Milanesa_de_res', 'Panza_de_res',
              'Res', 'Retazo_hueso_de_res',
              'Ternera', 'Cabeza_de_cerdo', 'Carnes_molida_de_cerdo',
              'Carnes_molida_de_res', 'Cerdo',
              'Chuleta_ahumada_de_cerdo', 'Espinazo_de_cerdo', 'Lomo_de_cerdo',
              'Milanesa_de_cerdo', 'Pata_de_cerdo',
              'Pernil', 'Pavo', 'Pechuga_de_pollo', 'Pierna_de_pollo', 'Pollo',
              'Pollo_entero']

    Cereales = ['Arroz', 'Avena', 'Cereal_mixto', 'Harina_de_arroz']

    Condimentos_y_aderezos = ['Ajonjoli', 'Canela', 'Chilorio', 'Clavo',
                              'Cochinita_pibil', 'Concentrado_de_pollo',
                              'Condimento_de_achiote', 'Hojas_de_perejil',
                              'Mayonesa', 'Mole_rojo_en_pasta',
                              'Mostaza', 'Pimienta', 'Polvo_p.hornear', 'Sal',
                              'Sal_molida_de_mesa', 'Salsa',
                              'Salsa_catsup', 'Salsa_de_chile', 'Salsa_de_soya',
                              'Salsa_inglesa', 'Salsa_mexicana',
                              'Salsa_picante', 'Sopa_y_crema', 'Vainilla',
                              'Vinagre']

    Dulces_y_golosinas = ['Chocolate_en_tablillas', 'Colacion', 'Flan',
                          'Gelatina_en_polvo',
                          'Manjarate', 'Polvo_bebida_sabor_chocolate', 'Chandell',
                          'Postre_estilo_flan',
                          'Praline', 'Torta_Imperial', 'Turron']

    Legumbres_secas = ['Poroto', 'Garbanzo', 'Haba', 'Lenteja']

    Pan_y_derivados_del_trigo = ['Galletas', 'Galletas_dulces',
                                 'Galletas_populares', 'Harina_de_trigo',
                                 'Harina_hot_cakes', 'Pan_de_caja', 'Pan_tostado',
                                 'Pasta_para_sopa',
                                 'Pastelillos', 'Tortilla_de_harina_de_trigo']

    Pescados_y_mariscos = ['Almeja', 'Atun', 'Bacalao', 'Blanco_Nilo', 'Boqueron',
                           'Calamar', 'Callo_de_hacha',
                           'Camaron', 'Carpa', 'Cazon', 'Charal', 'Cintilla',
                           'Curvina', 'Gurrubata',
                           'Huachinango', 'Jaiba', 'Langosta']

    Frutas_y_verduras = ['Acelga', 'Palta', 'Ajo', 'Alcachofa', 'Alcaparra',
                         'Almendras', 'Apio', 'Avellana', 'Betarraga',
                         'Brocoli', 'Calabaza', 'Castanas', 'Cebolla', 'Champinon',
                         'Ciruela', 'Ciruela_pasa', 'Coliflor',
                         'Durazno', 'Espinacas', 'Fresa', 'Frijoles', 'Granada',
                         'Kiwi', 'Lechuga', 'Lima', 'Limon',
                         'Mandarina', 'Mango', 'Manzana', 'Melon', 'Naranja',
                         'Nuez', 'Papa', 'Papaya', 'Pasa_.Uva_pasa.',
                         'Pepino', 'Pera', 'Pimiento', 'Pina', 'Platano', 'Rabano',
                         'Sandia', 'Tomate',
                         'Tuna', 'Uva', 'Zanahoria']

    Lacteos_y_huevo = ['Huevo', 'Crema', 'Crema_batida', 'Mantequilla',
                       'Queso_mantecosi', 'Queso_gauda',
                       'Queso_blanco', 'Yoghurt', 'Leche_condensada',
                       'Leche_en_polvo', 'Leche_evaporada',
                       'Leche_pasteurizada', 'Leche_ultrapasteurizada']

    Fiambreria = ['Chorizo', 'Jamon', 'jamon_de_pavo', 'Longaniza', 'Mortadela',
                  'Pastel_pimiento',
                  'Pate', 'Queso_de_puerco', 'Salami', 'Salchicha', 'Tocino']

    Cuidado_personal = ['Acondicionador_._enjuague', 'Champu', 'Champu_para_bebes',
                        'Crema_dental',
                        'Crema_liquida', 'Crema_solida', 'Desodorante',
                        'Jabon_de_tocador', 'Panales_desechables',
                        'Papel_higienico', 'Rastrillos_desechables',
                        'Repuestos_de_navajas', 'Tinte_para_el_cabello',
                        'Toalla_femenina', 'Toallita_humeda_limpiadora']

    Limpieza_del_hogar = ['Acondicionador_de_telas', 'Barra_limpiadora',
                          'Blanqueador', 'Detergente_ropa',
                          'Detergente_ropa_liquido', 'Detergente_ropa_polvo',
                          'Detergente_trastes',
                          'Insecticida_aerosol', 'Jabon_de_pasta',
                          'Jabon_limpiador', 'Limpiador_liquido',
                          'Limpiador_liquido_piso', 'Servilletas_de_papel',
                          'Suavizante_ropa', 'Toalla_de_papel']
    familias = [Aceites_y_grasas, Bebidas, Cafe_endulzantes_y_saborizantes, Carnes,
                Cereales, Condimentos_y_aderezos, Dulces_y_golosinas,
                Legumbres_secas, Pan_y_derivados_del_trigo, Pescados_y_mariscos,
                Frutas_y_verduras, Lacteos_y_huevo, Fiambreria, Cuidado_personal,
                Limpieza_del_hogar]
    dict_completo = {"Aceites_y_grasas": Aceites_y_grasas , "Bebidas": Bebidas,
                     "Cafe_endulzantes_y_saborizantes": Cafe_endulzantes_y_saborizantes , "Carnes": Carnes,
                "Cereales": Cereales, "Condimentos_y_aderezos": Condimentos_y_aderezos, "Dulces_y_golosinas": Dulces_y_golosinas,
                "Legumbres_secas": Legumbres_secas, "Pan_y_derivados_del_trigo": Pan_y_derivados_del_trigo,
                     "Pescados_y_mariscos": Pescados_y_mariscos, "Frutas_y_verduras": Frutas_y_verduras,
                     "Lacteos_y_huevo": Lacteos_y_huevo, "Fiambreria": Fiambreria, "Cuidado_personal": Cuidado_personal,
                "Limpieza_del_hogar": Limpieza_del_hogar}

    dict_swaps = dict()

    dicto = dict_completo
    t= 0
    for familia in dicto:
        dict_swaps[familia] = []
        lista_productos = dicto[familia]
        for i in range(len(lista_productos)):
            producto_solicitante = lista_productos[i]  # solicitante de swap
            for j in range(i+ 1,len(lista_productos)):
                producto_solicitado = lista_productos[j]
                t += 1
                tupla = (buscar_gondola(producto_solicitado, super).manejo_swap, producto_solicitado
                    , producto_solicitante, buscar_gondola(producto_solicitante, super))
                dict_swaps[familia].append(tupla)
                j += 1
            i += 1
    return dict_swaps

print(swapity_swap(super)["Cereales"])





