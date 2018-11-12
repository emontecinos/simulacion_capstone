## define un orden aleatorio del supermercado
from gondolas import Gondola 


def distribucion_inicial():

    aceite_y_grasas = ['Aceite', 'Aceite_de_oliva', 'Grasa_comestible', 'Manteca',
                   'Manteca_de_cerdo', 'Margarina', 'Margarina_light']

    bebidas = ['Agua_con_gas', 'Agua_sin_gas', 'Bebida_hidratante', 'Jugo_de_fruta',
            'Refresco', 'Cerveza', 'Jerez', 'Rompope', 'Sidra', 'Vino_de_mesa']

    cafe_y_endulzantes = ['Azúcar', 'Café_soluble', 'Café_tostado_y_molido', 'Jarabe_p/preparar_bebidas',
                        'Miel_de_abeja', 'Bebida_energética', 'Polvo_p/preparar_bebidas', 'Té']

    carnes = ['Bistec_de_diezmillo_de_res', 'Bistec_de_espaldilla_de_res', 'Chuleta_de_res', 'Falda_de_res',
            'Filete_de_res', 'Hígado_de_res', 'Milanesa_de_res', 'Panza_de_res', 'Res', 'Retazo_hueso_de_res',
            'Ternera', 'Cabeza_de_cerdo', 'Carnes_molida_de_cerdo', 'Carnes_molida_de_res', 'Cerdo',
            'Chuleta_ahumada_de_cerdo', 'Espinazo_de_cerdo', 'Lomo_de_cerdo', 'Milanesa_de_cerdo', 'Pata_de_cerdo',
            'Pernil', 'Pavo', 'Pechuga_de_pollo', 'Pierna_de_pollo', 'Pollo', 'Pollo_entero']

    cereales = ['Arroz', 'Avena', 'Cereal_mixto', 'Harina_de_arroz']

    condimentos_y_aderezos = ['Ajonjolí', 'Canela', 'Chilorio', 'Clavo', 'Cochinita_pibil', 'Concentrado_de_pollo',
                            'Condimento_de_achiote', 'Hojas_de_perejil', 'Mayonesa', 'Mole_rojo_en_pasta',
                            'Mostaza', 'Pimienta', 'Polvo_p/hornear', 'Sal', 'Sal_molida_de_mesa', 'Salsa',
                            'Salsa_catsup', 'Salsa_de_chile', 'Salsa_de_soya', 'Salsa_inglesa', 'Salsa_mexicana',
                            'Salsa_picante', 'Sopa_y_crema', 'Vainilla', 'Vinagre']

    dulces_y_golosinas = ['Chocolate_en_tablillas', 'Colación', 'Flan', 'Gelatina_en_polvo',
                        'Manjarate', 'Polvo_bebida_sabor_chocolate', 'Chandell', 'Postre_estilo_flan',
                        'Praline', 'Torta_Imperial', 'Turrón']

    legumbres_secas = ['Poroto', 'Garbanzo', 'Haba', 'Lenteja']

    pan_y_derivados_del_trigo = ['Galletas', 'Galletas_dulces', 'Galletas_populares', 'Harina_de_trigo',
                                'Harina_hot_cakes', 'Pan_de_caja', 'Pan_tostado', 'Pasta_para_sopa',
                                'Pastelillos', 'Tortilla_de_harina_de_trigo']

    pescado_y_mariscos = ['Almeja', 'Atún', 'Bacalao', 'Blanco_Nilo', 'Boquerón', 'Calamar', 'Callo_de_hacha',
                        'Camarón', 'Carpa', 'Cazón', 'Charal', 'Cintilla', 'Curvina', 'Gurrubata',
                        'Huachinango', 'Jaiba', 'Langosta']

    frutas_y_verduras = ['Acelga', 'Palta', 'Ajo', 'Alcachofa', 'Alcaparra', 'Almendras', 'Apio', 'Avellana', 'Betarraga',
                        'Brócoli', 'Calabaza', 'Castañas', 'Cebolla', 'Champiñón', 'Ciruela', 'Ciruela_pasa', 'Coliflor',
                        'Durazno', 'Espinacas', 'Fresa', 'Frijoles', 'Granada', 'Kiwi', 'Lechuga', 'Lima', 'Limón',
                        'Mandarina', 'Mango', 'Manzana', 'Melón', 'Naranja', 'Nuez', 'Papa', 'Papaya', 'Pasa_(Uva_pasa)',
                        'Pepino', 'Pera', 'Pimiento', 'Piña', 'Plátano', 'Rábano', 'Sandía', 'Tomate',
                        'Tuna', 'Uva', 'Zanahoria']

    lacteos_y_huevo = ['Huevo', 'Crema', 'Crema_batida', 'Mantequilla', 'Queso_mantecosi', 'Queso_gauda',
                    'Queso_blanco', 'Yoghurt', 'Leche_condensada', 'Leche_en_polvo', 'Leche_evaporada',
                    'Leche_pasteurizada', 'Leche_ultrapasteurizada']

    fiambreria = ['Chorizo', 'Jamón', 'jamon_de_pavo', 'Longaniza', 'Mortadela', 'Pastel_pimiento',
                'Paté', 'Queso_de_puerco', 'Salami', 'Salchicha', 'Tocino']

    cuidado_personal = ['Acondicionador_/_enjuague', 'Champú', 'Champú_para_bebés', 'Crema_dental',
                        'Crema_líquida', 'Crema_sólida', 'Desodorante', 'Jabon_de_tocador', 'Pañales_desechables',
                        'Papel_higiénico', 'Rastrillos_desechables', 'Repuestos_de_navajas', 'Tinte_para_el_cabello',
                        'Toalla_femenina', 'Toallita_húmeda_limpiadora']

    limpieza_hogar = ['Acondicionador_de_telas', 'Barra_limpiadora', 'Blanqueador', 'Detergente_ropa',
                    'Detergente_ropa_líquido', 'Detergente_ropa_polvo', 'Detergente_trastes',
                    'Insecticida_aerosol', 'Jabón_de_pasta', 'Jabón_limpiador', 'Limpiador_líquido',
                    'Limpiador_lìquido_piso', 'Servilletas_de_papel', 'Suavizante_ropa', 'Toalla_de_papel']


    gondolas = []
    slots = []
    nombres_gondolas = ["1I", "1D", "2I", "2D", "3I", "3D", "4I", "4D", "5I", "5D", "6I", "6D", "7I", "7D", "8I", "8D", "9I", "9D", "10I", "10D", "11I", "11D", "12I", "12D", "13I", "13D", "14I", "14D", "15I", "15D", "16I", "16D", "17I", "17D", "18I", "18D", "19"]
    for nombre in nombres_gondolas:

        if nombre == "1I":  ##lacteos

            for producto in lacteos_y_huevo:
                slots.append(producto)
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)
            
        elif nombre == "1D":
            contador = 1
            for producto in condimentos_y_aderezos:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "3I":
            contador = 1
            for producto in condimentos_y_aderezos:
                if contador > 17:
                    slots.append(producto)
                contador += 1
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "2D":
            while len(slots)<17: ## todos los codimentos caben en un pasillo
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "4I":
            while len(slots)<17: ## todos los codimentos caben en un pasillo
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)
        
        elif nombre == "3D":
            contador = 1
            for producto in bebidas:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "5I":
            while len(slots)<17:  ## todas las bebidas caben en una gondola
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "4D":
            while len(slots)<17: ## todas las bebidas caben en una gondola
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)


        elif nombre == "6I":
            while len(slots)<17: ## todas las bebidas caben en una gondola
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "5D":
            contador = 1
            for producto in pescado_y_mariscos:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "7I":
            while len(slots)<17: ## todos los pescados caben en una gondola
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "7D":
            contador = 1
            for producto in carnes:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "9I":
            contador = 1
            for producto in carnes:
                if contador > 17:
                    slots.append(producto)
                contador += 1
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "9D":
            while len(slots)<17: ## todas las carnes caben en un pasillo
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "11I":
            while len(slots)<17: ## todas las carnes caben en un pasillo
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "11D":
            contador = 1
            for producto in frutas_y_verduras:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots) < 17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "13I":
            contador = 1
            for producto in frutas_y_verduras:
                if contador > 17:
                    slots.append(producto)
                contador += 1
            while len(slots) < 17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "10D":
            contador = 1
            for producto in frutas_y_verduras:
                if contador > 34:
                    slots.append(producto)
                contador += 1
            while len(slots) < 17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "12I":
            while len(slots)<17: ## todas las frutas caben en un pasillo y medio
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "12D":
            while len(slots)<17: ## todas las frutas caben en un pasillo y medio
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "14I":
            while len(slots)<17: ## todas las frutas caben en un pasillo y medio
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "13D":
            contador = 1
            for producto in cuidado_personal:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots) < 17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "15I":
            while len(slots)<17: ## todas las cosas de higiene caben en una gondola
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "15D":
            while len(slots)<17: ## todas las cosas de higiene caben en una gondola
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "2I":
            contador = 1
            for producto in aceite_y_grasas:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots) < 17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "6D":
            contador = 1
            for producto in pan_y_derivados_del_trigo:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots) < 17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "8I":
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "8D":
            contador = 1
            for producto in cafe_y_endulzantes:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots) < 17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "10I":
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "14D":
            contador = 1
            for producto in limpieza_hogar:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots) < 17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "16I":
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "16D":
            contador = 1
            for producto in fiambreria:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots) < 17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "17I":
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "17D":
            contador = 1
            for producto in cereales:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots) < 17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "18I":
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "18D":
            contador = 1
            for producto in dulces_y_golosinas:
                if contador < 18:
                    slots.append(producto)
                contador += 1
            while len(slots) < 17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)

        elif nombre == "19":
            while len(slots)<17:
                slots.append(None)
            esta_gondola = Gondola(nombre, slots)
            gondolas.append(esta_gondola)



        print(nombre)
        print(slots)
        slots = []

        

        


        
    return gondolas 

if __name__ == "__main__":
    distribucion_inicial()