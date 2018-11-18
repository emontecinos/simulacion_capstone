## define un orden aleatorio del supermercado

def productos_esta_gondola(nombre):  ## Esta devuelve los slots de una gondola en particular

    Aceites_y_grasas = ['Aceite', 'Aceite_de_oliva', 'Grasa_comestible', 'Manteca',
                   'Manteca_de_cerdo', 'Margarina', 'Margarina_light']

    Bebidas = ['Agua_con_gas', 'Agua_sin_gas', 'Bebida_hidratante', 'Jugo_de_fruta',
            'Refresco', 'Cerveza', 'Jerez', 'Rompope', 'Sidra', 'Vino_de_mesa']

    Cafe_endulzantes_y_saborizantes = ['Azucar', 'Cafe_soluble', 'Cafe_tostado_y_molido', 'Jarabe_p/preparar_bebidas',
                        'Miel_de_abeja', 'Bebida_energetica', 'Polvo_p/preparar_bebidas', 'Te']

    Carnes = ['Bistec_de_diezmillo_de_res', 'Bistec_de_espaldilla_de_res', 'Chuleta_de_res', 'Falda_de_res',
            'Filete_de_res', 'Higado_de_res', 'Milanesa_de_res', 'Panza_de_res', 'Res', 'Retazo_hueso_de_res',
            'Ternera', 'Cabeza_de_cerdo', 'Carnes_molida_de_cerdo', 'Carnes_molida_de_res', 'Cerdo',
            'Chuleta_ahumada_de_cerdo', 'Espinazo_de_cerdo', 'Lomo_de_cerdo', 'Milanesa_de_cerdo', 'Pata_de_cerdo',
            'Pernil', 'Pavo', 'Pechuga_de_pollo', 'Pierna_de_pollo', 'Pollo', 'Pollo_entero']

    Cereales = ['Arroz', 'Avena', 'Cereal_mixto', 'Harina_de_arroz']

    Condimentos_y_aderezos = ['Ajonjoli', 'Canela', 'Chilorio', 'Clavo', 'Cochinita_pibil', 'Concentrado_de_pollo',
                            'Condimento_de_achiote', 'Hojas_de_perejil', 'Mayonesa', 'Mole_rojo_en_pasta',
                            'Mostaza', 'Pimienta', 'Polvo_p/hornear', 'Sal', 'Sal_molida_de_mesa', 'Salsa',
                            'Salsa_catsup', 'Salsa_de_chile', 'Salsa_de_soya', 'Salsa_inglesa', 'Salsa_mexicana',
                            'Salsa_picante', 'Sopa_y_crema', 'Vainilla', 'Vinagre']

    Dulces_y_golosinas = ['Chocolate_en_tablillas', 'Colacion', 'Flan', 'Gelatina_en_polvo',
                        'Manjarate', 'Polvo_bebida_sabor_chocolate', 'Chandell', 'Postre_estilo_flan',
                        'Praline', 'Torta_Imperial', 'Turron']

    Legumbres_secas = ['Poroto', 'Garbanzo', 'Haba', 'Lenteja']

    Pan_y_derivados_del_trigo = ['Galletas', 'Galletas_dulces', 'Galletas_populares', 'Harina_de_trigo',
                                'Harina_hot_cakes', 'Pan_de_caja', 'Pan_tostado', 'Pasta_para_sopa',
                                'Pastelillos', 'Tortilla_de_harina_de_trigo']

    Pescados_y_mariscos = ['Almeja', 'Atun', 'Bacalao', 'Blanco_Nilo', 'Boqueron', 'Calamar', 'Callo_de_hacha',
                        'Camaron', 'Carpa', 'Cazon', 'Charal', 'Cintilla', 'Curvina', 'Gurrubata',
                        'Huachinango', 'Jaiba', 'Langosta']

    Frutas_y_verduras = ['Acelga', 'Palta', 'Ajo', 'Alcachofa', 'Alcaparra', 'Almendras', 'Apio', 'Avellana', 'Betarraga',
                        'Brocoli', 'Calabaza', 'Castañas', 'Cebolla', 'Champiñón', 'Ciruela', 'Ciruela_pasa', 'Coliflor',
                        'Durazno', 'Espinacas', 'Fresa', 'Frijoles', 'Granada', 'Kiwi', 'Lechuga', 'Lima', 'Limon',
                        'Mandarina', 'Mango', 'Manzana', 'Melón', 'Naranja', 'Nuez', 'Papa', 'Papaya', 'Pasa_(Uva_pasa)',
                        'Pepino', 'Pera', 'Pimiento', 'Piña', 'Platano', 'Rabano', 'Sandia', 'Tomate',
                        'Tuna', 'Uva', 'Zanahoria']

    Lacteos_y_huevo = ['Huevo', 'Crema', 'Crema_batida', 'Mantequilla', 'Queso_mantecosi', 'Queso_gauda',
                    'Queso_blanco', 'Yoghurt', 'Leche_condensada', 'Leche_en_polvo', 'Leche_evaporada',
                    'Leche_pasteurizada', 'Leche_ultrapasteurizada']

    Fiambreria = ['Chorizo', 'Jamon', 'jamon_de_pavo', 'Longaniza', 'Mortadela', 'Pastel_pimiento',
                'Pate', 'Queso_de_puerco', 'Salami', 'Salchicha', 'Tocino']

    Cuidado_personal = ['Acondicionador_._enjuague', 'Champu', 'Champu_para_bebes', 'Crema_dental',
                        'Crema_liquida', 'Crema_solida', 'Desodorante', 'Jabon_de_tocador', 'Panales_desechables',
                        'Papel_higienico', 'Rastrillos_desechables', 'Repuestos_de_navajas', 'Tinte_para_el_cabello',
                        'Toalla_femenina', 'Toallita_humeda_limpiadora']

    Limpieza_del_hogar = ['Acondicionador_de_telas', 'Barra_limpiadora', 'Blanqueador', 'Detergente_ropa',
                    'Detergente_ropa_liquido', 'Detergente_ropa_polvo', 'Detergente_trastes',
                    'Insecticida_aerosol', 'Jabon_de_pasta', 'Jabon_limpiador', 'Limpiador_liquido',
                    'Limpiador_lìquido_piso', 'Servilletas_de_papel', 'Suavizante_ropa', 'Toalla_de_papel']



    slots = []

    if nombre == "1I":  ##lacteos

        for producto in Lacteos_y_huevo:
            slots.append(producto)
        while len(slots)<17:
            slots.append(None)

        
    elif nombre == "1D":
        contador = 1
        for producto in Condimentos_y_aderezos:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots)<17:
            slots.append(None)


    elif nombre == "3I":
        contador = 1
        for producto in Condimentos_y_aderezos:
            if contador > 17:
                slots.append(producto)
            contador += 1
        while len(slots)<17:
            slots.append(None)

    elif nombre == "2D":
        while len(slots)<17: ## todos los codimentos caben en un pasillo
            slots.append(None)

    elif nombre == "4I":
        while len(slots)<17: ## todos los codimentos caben en un pasillo
            slots.append(None)

    
    elif nombre == "3D":
        contador = 1
        for producto in Bebidas:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots)<17:
            slots.append(None)


    elif nombre == "5I":
        while len(slots)<17:  ## todas las bebidas caben en una gondola
            slots.append(None)


    elif nombre == "4D":
        while len(slots)<17: ## todas las bebidas caben en una gondola
            slots.append(None)



    elif nombre == "6I":
        while len(slots)<17: ## todas las bebidas caben en una gondola
            slots.append(None)


    elif nombre == "5D":
        contador = 1
        for producto in Pescados_y_mariscos:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots)<17:
            slots.append(None)


    elif nombre == "7I":
        while len(slots)<17: ## todos los pescados caben en una gondola
            slots.append(None)


    elif nombre == "7D":
        contador = 1
        for producto in Carnes:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots)<17:
            slots.append(None)


    elif nombre == "9I":
        contador = 1
        for producto in Carnes:
            if contador > 17:
                slots.append(producto)
            contador += 1
        while len(slots)<17:
            slots.append(None)


    elif nombre == "9D":
        while len(slots)<17: ## todas las carnes caben en un pasillo
            slots.append(None)


    elif nombre == "11I":
        while len(slots)<17: ## todas las carnes caben en un pasillo
            slots.append(None)


    elif nombre == "11D":
        contador = 1
        for producto in Frutas_y_verduras:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots) < 17:
            slots.append(None)


    elif nombre == "13I":
        contador = 1
        for producto in Frutas_y_verduras:
            if contador > 17:
                slots.append(producto)
            contador += 1
        while len(slots) < 17:
            slots.append(None)


    elif nombre == "10D":
        contador = 1
        for producto in Frutas_y_verduras:
            if contador > 34:
                slots.append(producto)
            contador += 1
        while len(slots) < 17:
            slots.append(None)


    elif nombre == "12I":
        while len(slots)<17: ## todas las frutas caben en un pasillo y medio
            slots.append(None)


    elif nombre == "12D":
        while len(slots)<17: ## todas las frutas caben en un pasillo y medio
            slots.append(None)


    elif nombre == "14I":
        while len(slots)<17: ## todas las frutas caben en un pasillo y medio
            slots.append(None)


    elif nombre == "13D":
        contador = 1
        for producto in Cuidado_personal:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots) < 17:
            slots.append(None)


    elif nombre == "15I":
        while len(slots)<17: ## todas las cosas de higiene caben en una gondola
            slots.append(None)


    elif nombre == "15D":
        while len(slots)<17: ## todas las cosas de higiene caben en una gondola
            slots.append(None)


    elif nombre == "2I":
        contador = 1
        for producto in Aceites_y_grasas:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots) < 17:
            slots.append(None)


    elif nombre == "6D":
        contador = 1
        for producto in Pan_y_derivados_del_trigo:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots) < 17:
            slots.append(None)


    elif nombre == "8I":
        while len(slots)<17:
            slots.append(None)


    elif nombre == "8D":
        contador = 1
        for producto in Cafe_endulzantes_y_saborizantes:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots) < 17:
            slots.append(None)


    elif nombre == "10I":
        while len(slots)<17:
            slots.append(None)


    elif nombre == "14D":
        contador = 1
        for producto in Limpieza_del_hogar:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots) < 17:
            slots.append(None)


    elif nombre == "16I":
        while len(slots)<17:
            slots.append(None)


    elif nombre == "16D":
        contador = 1
        for producto in Fiambreria:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots) < 17:
            slots.append(None)


    elif nombre == "17I":
        while len(slots)<17:
            slots.append(None)


    elif nombre == "17D":
        contador = 1
        for producto in Cereales:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots) < 17:
            slots.append(None)


    elif nombre == "18I":
        while len(slots)<17:
            slots.append(None)

    elif nombre == "18D":
        contador = 1
        for producto in Dulces_y_golosinas:
            if contador < 18:
                slots.append(producto)
            contador += 1
        while len(slots) < 17:
            slots.append(None)


    elif nombre == "19":
        while len(slots)<27:
            slots.append(None)


    return slots 


if __name__ == "__main__":
    #distribucion_inicial()
    a = productos_esta_gondola("1I")
    print(a)