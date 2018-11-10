

precios_prod = {}
largos_prod = {}
cant_vendida = {}
productos = []

porcentaje_ventas_prod = {}


####################### FAMILIAS #########################

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

familias = [aceite_y_grasas, bebidas, cafe_y_endulzantes, carnes, cereales, condimentos_y_aderezos, dulces_y_golosinas,
            legumbres_secas, pan_y_derivados_del_trigo, pescado_y_mariscos, frutas_y_verduras, lacteos_y_huevo,
            fiambreria, cuidado_personal, limpieza_hogar]

prod_familia = {}

for prod in aceite_y_grasas:
    prod_familia[prod.lower()] = 'aceite_y_grasas'
for prod in bebidas:
    prod_familia[prod.lower()] = 'bebidas'
for prod in cafe_y_endulzantes:
    prod_familia[prod.lower()] = 'cafe_y_endulzantes'
for prod in carnes:
    prod_familia[prod.lower()] = 'carnes'
for prod in cereales:
    prod_familia[prod.lower()] = 'cereales'
for prod in condimentos_y_aderezos:
    prod_familia[prod.lower()] = 'condimentos_y_aderezos'
for prod in dulces_y_golosinas:
    prod_familia[prod.lower()] = 'dulces_y_golosinas'
for p in legumbres_secas:
    prod_familia[p.lower()] = 'legumbres_secas'
for p in pan_y_derivados_del_trigo:
    prod_familia[p.lower()] = 'pan_y_derivados_del_trigo'
for p in pescado_y_mariscos:
    prod_familia[p.lower()] = 'pescado_y_mariscos'
for p in frutas_y_verduras:
    prod_familia[p.lower()] = 'frutas_y_verduras'
for p in lacteos_y_huevo:
    prod_familia[p.lower()] = 'lacteos_y_huevo'
for p in fiambreria:
    prod_familia[p.lower()] = 'fiambreria'
for p in cuidado_personal:
    prod_familia[p.lower()] = 'cuidado_personal'
for p in limpieza_hogar:
    prod_familia[p.lower()] = 'limpieza_hogar'

ventas_familia = {}

########################################################################################################################


espacio_total_supermercado = 30654.4

for x in prod_familia.values():
    ventas_familia[x] = 0


with open('precios productos.csv', 'r', encoding='utf-8') as precios:
    c = 0
    for line in precios:
        c += 1
        if c > 1:
            x = line.strip('\n').split(',')
            precios_prod[x[0].replace(' ', '_').lower()] = int(x[1])
            cant_vendida[x[0].replace(' ', '_').lower()] = 0
            largos_prod[x[0].replace(' ', '_').lower()] = float(x[2])


with open('Boletas.csv', 'r', encoding='utf-8') as file:
    cont = 0
    for i in file:
        if cont == 0:
            productos = i.split(',')[1:-1]
            cont += 1

        else:
            fila = i.split(',')[1:-1]
            a = list(zip(productos, fila))
            for compra in a:
                if compra[1] != '0':
                    cant_vendida[compra[0].lower()] += 1
                    ventas_familia[prod_familia[compra[0].lower()]] += 1

ventas_totales = 0
for cant in cant_vendida.values():
    ventas_totales += cant

for ventas in cant_vendida.items():
    porcentaje_ventas_prod[ventas[0]] = ventas[1] / ventas_totales


for we in porcentaje_ventas_prod.items():
    espacio_ponderado = we[1] * espacio_total_supermercado
    if espacio_ponderado < largos_prod[we[0]]:
        print(espacio_ponderado, largos_prod[we[0]])



# print(cant_vendida)
print(ventas_totales)
# print(productos)
# print(porcentaje_ventas_prod)

print(ventas_familia)


porcentaje_ventas_familia = {}

for tupla in ventas_familia.items():
    porcentaje_ventas_familia[tupla[0]] = (tupla[1]/ventas_totales, (tupla[1]*espacio_total_supermercado)/ventas_totales,
                                           (tupla[1] * espacio_total_supermercado) / (ventas_totales * 816))

suma_de_gondolas = 0
for i in porcentaje_ventas_familia.items():
    suma_de_gondolas += i[1][2]
    print(i)
print(suma_de_gondolas)