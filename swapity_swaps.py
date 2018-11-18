from supermercat import Graph

super = Graph()


def buscar_gondola(producto, super):
    nodos = []
    for gondola in super.gondolas.values():
        if producto in gondola.espacios:
            return gondola


dict_20_80 = {'aceite_y_grasas': ['Margarina', 'Margarina_light'], 'bebidas': ['Agua_con_gas', 'Agua_sin_gas', 'Sidra'], 'cafe_y_endulzantes': ['Azucar', 'Jarabe_p.preparar_bebidas', 'Miel_de_abeja'], 'carnes': ['Bistec_de_diezmillo_de_res', 'Falda_de_res', 'Pavo', 'Pollo'], 'cereales': [], 'condimentos_y_aderezos': ['Canela', 'Condimento_de_achiote', 'Mayonesa', 'Mole_rojo_en_pasta', 'Mostaza', 'Salsa_de_chile', 'Salsa_inglesa'], 'dulces_y_golosinas': ['Flan', 'Chandell', 'Praline'], 'legumbres_secas': [], 'pan_y_derivados_del_trigo': ['Galletas_dulces', 'Pan_de_caja'], 'pescado_y_mariscos': ['Bacalao', 'Carpa'], 'frutas_y_verduras': ['Ciruela', 'Coliflor', 'Granada', 'Pasa_.Uva_pasa.', 'Pera', 'Tuna'], 'lacteos_y_huevo': ['Huevo', 'Crema_batida', 'Mantequilla', 'Queso_blanco', 'Leche_condensada', 'Leche_en_polvo'], 'fiambreria': ['jamon_de_pavo', 'Queso_de_puerco'], 'cuidado_personal': ['Rastrillos_desechables', 'Tinte_para_el_cabello', 'Toalla_femenina'], 'limpieza_hogar': ['Barra_limpiadora', 'Suavizante_ropa']}

dict_swaps = dict()

for familia in dict_20_80:
    dict_swaps[familia] = []
    lista_productos = dict_20_80[familia]
    for i in range(len(lista_productos)):
        producto_solicitante = lista_productos[i]  # solicitante de swap
        for j in range(i+ 1,len(lista_productos)):
            producto_solicitado = lista_productos[j]
            tupla = (buscar_gondola(producto_solicitado, super), producto_solicitado
                , producto_solicitante, buscar_gondola(producto_solicitante, super))
            dict_swaps[familia].append(tupla)
            j += 1
        i += 1

print(dict_swaps)





