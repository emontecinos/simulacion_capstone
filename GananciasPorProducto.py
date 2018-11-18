import numpy as np


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
precios_prod = {}
largos_prod = {}
cant_vendida = {}
productos = []
porcentaje_ventas_prod = {}

########################################################################################################################
###########################------------PARAMETROS----------- ###########################################################
########################################################################################################################

espacio_total_supermercado = 10440
largo_slot_gondola_corta = 16
largo_slot_gondola_larga = 24


espacio_aceiteygrasas = 816 * 1
espacio_bebidas = 816 * 2
espacio_cafeyendulzantes = 816 * 1
espacio_carnes = 816 * 5
espacio_cereales = 816 * 0.8
espacio_condimentosyaderezos = 816 * 4
espacio_dulcesygolosinas = 816 * 2
espacio_legumbres = 816 * 0.8
espacio_panyderivados = 816 * 2
espacio_pescadosymariscos = 816 * 3
espacio_frutasyverduras = 816 * 6
espacio_lacteosyhuevo = 816 * 3
espacio_fiambreria = 816 * 2
espacio_cuidadopersonal = 816 * 3
espacio_limpiezahogar = 816 * 2

espacio_unid_equiv_familia = dict()

espacio_unid_equiv_familia['aceite_y_grasas'] = espacio_aceiteygrasas

espacio_unid_equiv_familia['bebidas'] = espacio_bebidas

espacio_unid_equiv_familia['cafe_y_endulzantes'] = espacio_cafeyendulzantes

espacio_unid_equiv_familia['carnes'] = espacio_carnes

espacio_unid_equiv_familia['cereales'] = espacio_cereales

espacio_unid_equiv_familia['condimentos_y_aderezos'] = espacio_condimentosyaderezos

espacio_unid_equiv_familia['dulces_y_golosinas'] = espacio_dulcesygolosinas

espacio_unid_equiv_familia['legumbres_secas'] = espacio_legumbres

espacio_unid_equiv_familia['pan_y_derivados_del_trigo'] = espacio_panyderivados

espacio_unid_equiv_familia['pescado_y_mariscos'] = espacio_pescadosymariscos

espacio_unid_equiv_familia['frutas_y_verduras'] = espacio_frutasyverduras

espacio_unid_equiv_familia['lacteos_y_huevo'] = espacio_lacteosyhuevo

espacio_unid_equiv_familia['fiambreria'] = espacio_fiambreria

espacio_unid_equiv_familia['cuidado_personal'] = espacio_cuidadopersonal

espacio_unid_equiv_familia['limpieza_hogar'] = espacio_limpiezahogar



########################################################################################################################
########################################################################################################################

for x in prod_familia.values():
    ventas_familia[x] = 0


with open('precios productos.csv', 'r', encoding='utf-8') as precios:
    c = 0
    for line in precios:
        c += 1
        if c > 1:
            x = line.strip('\n').split(',')
            precios_prod[x[0].replace(" ", "_").replace("á", "a").replace("é", "e").replace("í", "i")\
            .replace("ó", "o").replace("ú", "u").replace("/", ".")] = int(x[1])
            cant_vendida[x[0].replace(' ', '_').lower()] = 0
            largos_prod[x[0].replace(' ', '_').lower()] = float(x[2])


with open('Boletas_completas.csv', 'r', encoding='utf-8') as file:
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


print(productos)
print(precios_prod)
print(largos_prod)
print(cant_vendida)
print(ventas_familia)

ventas_totales = 0
for cant in cant_vendida.values():
    ventas_totales += cant
# with open("Porcentaje de ventas por familia segun volumen de ventas.csv", 'w', encoding='utf-8') as trololo:
#     trololo.write("Familia, Porcentaje de ventas familia \n")
#     for trolo in ventas_familia.items():
#         porcentaje = (trolo[1] / ventas_totales)
#         trololo.write("{}, {} \n".format(trolo[0], porcentaje))
#

porcentaje_ventas_prod_en_su_familia = {}
for ventas in cant_vendida.items():
    """ Esto calcula el porcentaje de volumen de ventas de un producto en su familia"""
    porcentaje_ventas_prod_en_su_familia[ventas[0]] = ventas[1] / ventas_familia[prod_familia[ventas[0]]]
print(porcentaje_ventas_prod_en_su_familia)

# with open("Ventas de un producto en su familia.csv", 'w', encoding='utf-8') as lala:
#     lala.write("Producto, Pocentaje de ventas en su familia \n")
#     for q in porcentaje_ventas_prod_en_su_familia.items():
#         lala.write("{}, {}\n".format(q[0], q[1]))

# ----------------------------------------------------------------------------------------------------------------------
""" Este bloque es para multiplicar cada porcentaje por el espacio que se le deberia dar a cada familia """
espacio_unid_equiv_producto = dict()

for p in porcentaje_ventas_prod_en_su_familia.items():
    familia = prod_familia[p[0]]
    espacio_unid_equiv_producto[p[0]] = espacio_unid_equiv_familia[familia] * p[1]
print(espacio_unid_equiv_producto)
# ----------------------------------------------------------------------------------------------------------------------


""" Lo que el siguiente bloque hace es asignar la cantidad de slots que representaran a cada producto,
    Adaptandolo proporcinalmente para que cada cual tenga la longitud correspondiente en los 17 slots definidos"""


familias_con_productos_con_espacio = dict()

for familia in espacio_unid_equiv_familia.keys():
    familias_con_productos_con_espacio[familia] = []

for prod in espacio_unid_equiv_producto.items():
    familias_con_productos_con_espacio[prod_familia[prod[0]]].append(prod)


print(familias_con_productos_con_espacio)


def slots_productos(familias_con_productos):
    slots_producto = dict()
    for fam in familias_con_productos.items():
        largos_familia = [L[1] for L in fam[1]]
        percentiles = np.quantile(largos_familia, [0.25, 0.5, 0.75, 1])
        divisiones = []
        for prt in percentiles:
            divisiones.append(prt)
        slots = 0
        for producto in fam[1]:
            j = 1
            for P in divisiones:
                if producto[1] <= P:
                    if producto[0] not in slots_producto.keys():
                        slots += j
                    slots_producto[producto[0]] = j
                else:
                    j += 1
        n_gond = espacio_unid_equiv_familia[fam[0]] / 816
        if slots < n_gond * 17:
            for s in fam[1]:
                factor = n_gond * 17 / slots
                actual = slots_producto[s[0]]
                slots_producto[s[0]] = round(actual * factor)

    return slots_producto


slots = slots_productos(familias_con_productos_con_espacio)

for_nacrur = dict()
aaaaa = []
with open('Productos 20-80.csv', 'r') as file:
    for line in file:
        producto = line.strip("\n").replace(" ", "_").lower()
        aaaaa.append(producto)
        print(producto)
for w in familias_con_productos_con_espacio.keys():
    for_nacrur[w] = []

for o in aaaaa:
    q = o.replace(" ", "_").replace("á", "a").replace("é", "e").replace("í", "i")\
            .replace("ó", "o").replace("ú", "u").replace("/", ".")
    inicial = q[0].upper()
    w = inicial + q[1:]
    for_nacrur[prod_familia[o]].append(w)
print(for_nacrur)


#
# with open('Slots por producto.csv', 'w', encoding='UTF-8') as file:
#     file.write("Producto, Slots \n")
#     for i in slots.items():
#         file.write("{}, {} \n".format(i[0], i[1]))
#
#
# print(slots)
#
# slots_fam = dict()
#
#
# for familia in espacio_unid_equiv_familia.keys():
#     slots_fam[familia] = 0
#
# for y in slots.items():
#     slots_fam[prod_familia[y[0]]] += y[1]
#
#
# print(slots_fam)



# with open("Slots por producto.csv", 'w', encoding="UTF-8") as file:
#     file.write("Producto, Slots \n")
#     for x in slots.items():
#         file.write("{}, {} \n".format(x[0], x[1]))

#
# for ventas in cant_vendida.items():
#     porcentaje_ventas_prod[ventas[0]] = ventas[1] / ventas_totales
#
#
# for we in porcentaje_ventas_prod.items():
#     espacio_ponderado = we[1] * espacio_total_supermercado
#     if espacio_ponderado < largos_prod[we[0]]:
#         print(espacio_ponderado, largos_prod[we[0]])
#
#
#
# # print(cant_vendida)
# print(ventas_totales)
# # print(productos)
# # print(porcentaje_ventas_prod)
#
# print(ventas_familia)
#
#
# porcentaje_ventas_familia = {}
#
# for tupla in ventas_familia.items():
#     porcentaje_ventas_familia[tupla[0]] = (tupla[1]/ventas_totales, (tupla[1]*espacio_total_supermercado)/ventas_totales,
#                                            (tupla[1] * espacio_total_supermercado) / (ventas_totales * 816))
#
# suma_de_gondolas = 0
# for i in porcentaje_ventas_familia.items():
#     suma_de_gondolas += i[1][2]
#     print(i)
# print(suma_de_gondolas)
#
# for i in range(2,272):
#     if 272 // i == 0:
#         print(i)
