import csv

class Simulation:
    def __init__(self):
        #self.supermerado = Graph()
        self.total_distancias = 0
        self.total_compras = 0
        self.total_vistos = 0
        self.cliente = None
        self.productos = [Aceite,Aceite_de_oliva,Grasa_comestible,Manteca,Manteca_de_cerdo,Margarina,Margarina_Light,Agua_con_gas,Agua_sin_gas,Bebida_hidratante,Jugo_de_fruta,Refresco,Cerveza,Jerez,Rompope,Sidra,Vino_de_mesa,Azucar,Cafe_soluble,Cafe_tostado_y_molido,Jarabe_p.preparar_bebidas,Miel_de_abeja,Bebida_energetica,Polvo_p.preparar_bebidas,Te,Bistec_de_diezmillo_de_res,Bistec_de_espaldilla_de_res,Chuleta_de_res,Falda_de_res,Filete_de_res,Higado_de_res,Milanesa_de_res,Panza_de_res,Res,Retazo_hueso_de_res,Ternera,Cabeza_de_cerdo,Carnes_molida_de_cerdo,Carnes_molida_de_res,Cerdo,Chuleta_ahumada_de_cerdo,Espinazo_de_cerdo,Lomo_de_cerdo,Milanesa_de_cerdo,Pata_de_cerdo,Pernil,Pavo,Pechuga_de_pollo,Pierna_de_pollo,Pollo,Pollo_entero,Arroz,Avena,Cereal_mixto,Harina_de_arroz,Ajonjoli,Canela,Chilorio,Clavo,Cochinita_pibil,Concentrado_de_pollo,Condimento_de_achiote,Hojas_de_perejil,Mayonesa,Mole_rojo_en_pasta,Mostaza,Pimienta,Polvo_p.hornear,Sal,Sal_molida_de_mesa,Salsa,Salsa_catsup,Salsa_de_chile,Salsa_de_soya,Salsa_inglesa,Salsa_mexicana,Salsa_picante,Sopa_y_crema,Vainilla,Vinagre,Chocolate_en_tablillas,Colacion,Flan,Gelatina_en_polvo,Manjarate,Polvo_bebida_sabor_chocolate,Chandell,Postre_estilo_flan,Praline,Torta_Imperial,Turron,Poroto,Garbanzo,Haba,Lenteja,Galletas,Galletas_dulces,Galletas_populares,Harina_de_trigo,Harina_hot_cakes,Pan_de_caja,Pan_tostado,Pasta_para_sopa,Pastelillos,Tortilla_de_harina_de_trigo,Almeja,Atun,Bacalao,Blanco_Nilo,Boqueron,Calamar,Callo_de_hacha,Camaron,Carpa,Cazon,Charal,Cintilla,Curvina,Gurrubata,Huachinango,Jaiba,Langosta,Acelga,Palta,Ajo,Alcachofa,Alcaparra,Almendras,Apio,Avellana,Betarraga,Brocoli,Calabaza,Castanas,Cebolla,Champinon,Ciruela,Ciruela_pasa,Coliflor,Durazno,Espinacas,Fresa,Frijoles,Granada,Kiwi,Lechuga,Lima,Limon,Mandarina,Mango,Manzana,Melon,Naranja,Nuez,Papa,Papaya,Pasa_.Uva_pasa.,Pepino,Pera,Pimiento,Pina,Platano,Rabano,Sandia,Tomate,Tuna,Uva,Zanahoria,Huevo,Crema,Crema_batida,Mantequilla,Queso_mantecosi,Queso_gauda,Queso_blanco,Yoghurt,Leche_condensada,Leche_en_polvo,Leche_evaporada,Leche_pasteurizada,Leche_ultrapasteurizada,Chorizo,Jamon,jamon_de_pavo,Longaniza,Mortadela,Pastel_pimiento,Pate,Queso_de_puerco,Salami,Salchicha,Tocino,Acondicionador_._enjuague,Champu,Champu_para_bebes,Crema_dental,Crema_liquida,Crema_solida,Desodorante,Jabon_de_tocador,Panales_desechables,Papel_higienico,Rastrillos_desechables,Repuestos_de_navajas,Tinte_para_el_cabello,Toalla_femenina,Toallita_humeda_limpiadora,Acondicionador_de_telas,Barra_limpiadora,Blanqueador,Detergente_ropa,Detergente_ropa_liquido,Detergente_ropa_polvo,Detergente_trastes,Insecticida_aerosol,Jabon_de_pasta,Jabon_limpiador,Limpiador_liquido,Limpiador_liquido_piso,Servilletas_de_papel,Suavizante_ropa,Toalla_de_papel]


    def cargar_cliente(self, numero_de_boleta):
        with open('Boletas.csv', 'r') as Boletas:
            next(Boletas)

            producto_en_lista = []
            numerodeboleta = 1
            productoactual = 0

            for row in Boletas:
                if numero_de_boleta == numerodeboleta: # cuando es la que queremos
                    lista = row.split(";")
                    for indice in range(2, len(lista)):
                        if "1" in lista[indice]:
                            producto_en_lista.append(int(indice)-2)  ## el primer producto va a ser el 0
                    
                numerodeboleta += 1
            print(producto_en_lista)

    def swap(self, nodo):
        pass

if __name__ == "__main__":
    mysimulation = Simulation()
    mysimulation.cargar_cliente(2)


