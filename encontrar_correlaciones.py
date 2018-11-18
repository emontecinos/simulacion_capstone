import csv
def encontrar_familia(producto):
    Aceites_y_grasas = ['Aceite', 'Aceite_de_oliva', 'Grasa_comestible', 'Manteca',
                   'Manteca_de_cerdo', 'Margarina', 'Margarina_light','Aceites_y_grasas']

    Bebidas = ['Agua_con_gas', 'Agua_sin_gas', 'Bebida_hidratante', 'Jugo_de_fruta',
            'Refresco', 'Cerveza', 'Jerez', 'Rompope', 'Sidra', 'Vino_de_mesa','Bebidas']

    Cafe_endulzantes_y_saborizantes = ['Azucar', 'Cafe_soluble', 'Cafe_tostado_y_molido', 'Jarabe_p.preparar_bebidas',
                        'Miel_de_abeja', 'Bebida_energetica', 'Polvo_p.preparar_bebidas', 'Te','Cafe_endulzantes_y_saborizantes']

    Carnes = ['Bistec_de_diezmillo_de_res', 'Bistec_de_espaldilla_de_res', 'Chuleta_de_res', 'Falda_de_res',
            'Filete_de_res', 'Higado_de_res', 'Milanesa_de_res', 'Panza_de_res', 'Res', 'Retazo_hueso_de_res',
            'Ternera', 'Cabeza_de_cerdo', 'Carnes_molida_de_cerdo', 'Carnes_molida_de_res', 'Cerdo',
            'Chuleta_ahumada_de_cerdo', 'Espinazo_de_cerdo', 'Lomo_de_cerdo', 'Milanesa_de_cerdo', 'Pata_de_cerdo',
            'Pernil', 'Pavo', 'Pechuga_de_pollo', 'Pierna_de_pollo', 'Pollo', 'Pollo_entero','Carnes']

    Cereales = ['Arroz', 'Avena', 'Cereal_mixto', 'Harina_de_arroz','Cereales']

    Condimentos_y_aderezos = ['Ajonjoli', 'Canela', 'Chilorio', 'Clavo', 'Cochinita_pibil', 'Concentrado_de_pollo',
                            'Condimento_de_achiote', 'Hojas_de_perejil', 'Mayonesa', 'Mole_rojo_en_pasta',
                            'Mostaza', 'Pimienta', 'Polvo_p.hornear', 'Sal', 'Sal_molida_de_mesa', 'Salsa',
                            'Salsa_catsup', 'Salsa_de_chile', 'Salsa_de_soya', 'Salsa_inglesa', 'Salsa_mexicana',
                            'Salsa_picante', 'Sopa_y_crema', 'Vainilla', 'Vinagre','Condimentos_y_aderezos']

    Dulces_y_golosinas = ['Chocolate_en_tablillas', 'Colacion', 'Flan', 'Gelatina_en_polvo',
                        'Manjarate', 'Polvo_bebida_sabor_chocolate', 'Chandell', 'Postre_estilo_flan',
                        'Praline', 'Torta_Imperial', 'Turron','Dulces_y_golosinas']

    Legumbres_secas = ['Poroto', 'Garbanzo', 'Haba', 'Lenteja','Legumbres_secas']

    Pan_y_derivados_del_trigo = ['Galletas', 'Galletas_dulces', 'Galletas_populares', 'Harina_de_trigo',
                                'Harina_hot_cakes', 'Pan_de_caja', 'Pan_tostado', 'Pasta_para_sopa',
                                'Pastelillos', 'Tortilla_de_harina_de_trigo','Pan_y_derivados_del_trigo']

    Pescados_y_mariscos = ['Almeja', 'Atun', 'Bacalao', 'Blanco_Nilo', 'Boqueron', 'Calamar', 'Callo_de_hacha',
                        'Camaron', 'Carpa', 'Cazon', 'Charal', 'Cintilla', 'Curvina', 'Gurrubata',
                        'Huachinango', 'Jaiba', 'Langosta','Pescados_y_mariscos']

    Frutas_y_verduras = ['Acelga', 'Palta', 'Ajo', 'Alcachofa', 'Alcaparra', 'Almendras', 'Apio', 'Avellana', 'Betarraga',
                        'Brocoli', 'Calabaza', 'Castañas', 'Cebolla', 'Champinon', 'Ciruela', 'Ciruela_pasa', 'Coliflor',
                        'Durazno', 'Espinacas', 'Fresa', 'Frijoles', 'Granada', 'Kiwi', 'Lechuga', 'Lima', 'Limon',
                        'Mandarina', 'Mango', 'Manzana', 'Melon', 'Naranja', 'Nuez', 'Papa', 'Papaya', 'Pasa_.Uva_pasa.',
                        'Pepino', 'Pera', 'Pimiento', 'Pina', 'Platano', 'Rabano', 'Sandia', 'Tomate',
                        'Tuna', 'Uva', 'Zanahoria','Frutas_y_verduras']

    Lacteos_y_huevo = ['Huevo', 'Crema', 'Crema_batida', 'Mantequilla', 'Queso_mantecosi', 'Queso_gauda',
                    'Queso_blanco', 'Yoghurt', 'Leche_condensada', 'Leche_en_polvo', 'Leche_evaporada',
                    'Leche_pasteurizada', 'Leche_ultrapasteurizada','Lacteos_y_huevo']

    Fiambreria = ['Chorizo', 'Jamon', 'jamon_de_pavo', 'Longaniza', 'Mortadela', 'Pastel_pimiento',
                'Pate', 'Queso_de_puerco', 'Salami', 'Salchicha', 'Tocino','Fiambreria']

    Cuidado_personal = ['Acondicionador_._enjuague', 'Champu', 'Champu_para_bebes', 'Crema_dental',
                        'Crema_liquida', 'Crema_solida', 'Desodorante', 'Jabon_de_tocador', 'Panales_desechables',
                        'Papel_higienico', 'Rastrillos_desechables', 'Repuestos_de_navajas', 'Tinte_para_el_cabello',
                        'Toalla_femenina', 'Toallita_humeda_limpiadora','Cuidado_personal']

    Limpieza_del_hogar = ['Acondicionador_de_telas', 'Barra_limpiadora', 'Blanqueador', 'Detergente_ropa',
                    'Detergente_ropa_liquido', 'Detergente_ropa_polvo', 'Detergente_trastes',
                    'Insecticida_aerosol', 'Jabon_de_pasta', 'Jabon_limpiador', 'Limpiador_liquido',
                    'Limpiador_liquido_piso', 'Servilletas_de_papel', 'Suavizante_ropa', 'Toalla_de_papel','Limpieza_del_hogar']
    familias = [Aceites_y_grasas,Bebidas,Cafe_endulzantes_y_saborizantes,Carnes,Cereales,Condimentos_y_aderezos,Dulces_y_golosinas,Legumbres_secas,Pan_y_derivados_del_trigo,Pescados_y_mariscos,Frutas_y_verduras,Lacteos_y_huevo,Fiambreria,Cuidado_personal,Limpieza_del_hogar]
    for familia in familias:
        if producto in familia:
            return familia[-1]

def encontrar_corr_familia_un_producto(producto1, producto2):
    familia_movil = encontrar_familia(producto1)
    familia_revisar = encontrar_familia(producto2)
    with open ("csv_corr_familias.csv") as file:
        datos = csv.reader(file)
        informacion = [dato for dato in datos]
        #print(informacion[0], familia_revisar, producto2)
        pos_revisar = informacion[0].index(familia_revisar)
        for dato in informacion[1:]:
            if dato[0] == familia_movil:
                return dato[pos_revisar+1]


def encontrar_corr_familia(lista_productos, producto):
    correlaciones = []
    for prod_movil in lista_productos:
        correlaciones.append(encontrar_corr_familia_un_producto(prod_movil, producto))
    return max(correlaciones)       



def encontrar_corr_producto(lista_productos, producto):
    correlaciones = []
    with open ("csv_corr_productos.csv") as file:
        datos = csv.reader(file)
        informacion = [dato for dato in datos]
        #print('encontrar_correlaciones', producto, informacion)
        pos_revisar = informacion[0].index(producto)
        for prod_movil in lista_productos:
            for dato in informacion[1:]:
                if dato[0] == prod_movil:
                    correlaciones.append(dato[pos_revisar+1])
    return max(correlaciones)


if __name__ == "__main__":
    productos_lista = ["Durazno", "Crema", "Pavo", "Champu"]
    productos_vistos = ["Tuna","Manteca","Canela","Ajonjoli","Poroto"]
    for prod_ver in productos_vistos:
        m = encontrar_corr_familia(productos_lista,prod_ver)
        n = encontrar_corr_producto(productos_lista,prod_ver)
        print("Producto: {}, Corr_familia: {}, Corr_prod: {}".format(prod_ver, m, n))

    
