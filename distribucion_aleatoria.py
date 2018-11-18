## define un orden aleatorio del supermercado

def productos_esta_gondola(nombre):  ## Esta devuelve los slots de una gondola en particular
    slots = []

    if nombre == "1I":  #Carnes
        slots.append('Bistec_de_diezmillo_de_res')   #1
        slots.append('Bistec_de_diezmillo_de_res')   #2
        slots.append('Bistec_de_diezmillo_de_res')   #3
        slots.append('Bistec_de_diezmillo_de_res')   #4
        slots.append('Bistec_de_espaldilla_de_res')   #5
        slots.append('Bistec_de_espaldilla_de_res')   #6
        slots.append('Bistec_de_espaldilla_de_res')   #7
        slots.append('Chuleta_de_res')   #8
        slots.append('Falda_de_res')   #9
        slots.append('Falda_de_res')   #10
        slots.append('Falda_de_res')   #11
        slots.append('Falda_de_res')   #12
        slots.append('Filete_de_res')   #13
        slots.append('Filete_de_res')   #14
        slots.append('Filete_de_res')   #15
        slots.append('Higado_de_res')   #16
        slots.append('Milanesa_de_res')   #17

        
    elif nombre == "1D": #Carnes
        slots.append('Milanesa_de_res')   #1
        slots.append('Milanesa_de_res')   #2
        slots.append('Milanesa_de_res')   #3
        slots.append('Milanesa_de_res')   #4
        slots.append('Panza_de_res')   #5
        slots.append('Panza_de_res')   #6
        slots.append('Panza_de_res')   #7
        slots.append('Panza_de_res')   #8
        slots.append('Panza_de_res')   #9
        slots.append('Res')   #10
        slots.append('Res')   #11
        slots.append('Res')   #12
        slots.append('Retazo_hueso_de_res')   #13
        slots.append('Retazo_hueso_de_res')   #14
        slots.append('Retazo_hueso_de_res')   #15
        slots.append('Retazo_hueso_de_res')   #16
        slots.append('Ternera')   #17

    elif nombre == "2I": #Cafe
        slots.append('Azucar')   #1
        slots.append('Azucar')   #2
        slots.append('Azucar')   #3
        slots.append('Azucar')   #4
        slots.append('Cafe_soluble')   #5
        slots.append('Cafe_tostado_y_molido')   #6
        slots.append('Jarabe_p.preparar_bebidas')   #7
        slots.append('Jarabe_p.preparar_bebidas')   #8
        slots.append('Miel_de_abeja')   #9
        slots.append('Miel_de_abeja')   #10
        slots.append('Miel_de_abeja')   #11
        slots.append('Miel_de_abeja')   #12
        slots.append('Bebida_energetica')   #13
        slots.append('Bebida_energetica')   #14
        slots.append('Polvo_p.preparar_bebidas')   #15
        slots.append('Polvo_p.preparar_bebidas')   #16
        slots.append('Te')   #17

    elif nombre == "2D": #Pan
        slots.append('Galletas')   #1
        slots.append('Galletas')   #2
        slots.append('Galletas_dulces')   #3
        slots.append('Galletas_dulces')   #4
        slots.append('Galletas_dulces')   #5
        slots.append('Galletas_dulces')   #6
        slots.append('Galletas_populares')   #7
        slots.append('Harina_de_trigo')   #8
        slots.append('Harina_de_trigo')   #9
        slots.append('Harina_de_trigo')   #10
        slots.append('Harina_de_trigo')   #11
        slots.append('Harina_de_trigo')   #12
        slots.append('Harina_hot_cakes')   #13
        slots.append('Harina_hot_cakes')   #14
        slots.append('Harina_hot_cakes')   #15
        slots.append('Harina_hot_cakes')   #16
        slots.append('Pan_de_caja')   #17

    elif nombre == "3I": #Pan
        slots.append('Pan_de_caja')   #1
        slots.append('Pan_de_caja')   #2
        slots.append('Pan_de_caja')   #3
        slots.append('Pan_de_caja')   #4
        slots.append('Pan_tostado')   #5
        slots.append('Pan_tostado')   #6
        slots.append('Pan_tostado')   #7
        slots.append('Pan_tostado')   #8
        slots.append('Pan_tostado')   #9
        slots.append('Pasta_para_sopa')   #10
        slots.append('Pasta_para_sopa')   #11
        slots.append('Pastelillos')   #12
        slots.append('Pastelillos')   #13
        slots.append('Pastelillos')   #14
        slots.append('Tortilla_de_harina_de_trigo')   #15
        slots.append('Tortilla_de_harina_de_trigo')   #16
        slots.append('Tortilla_de_harina_de_trigo')   #17
    
    elif nombre == "3D": #Pescado
        slots.append('Almeja')   #1
        slots.append('Atun')   #2
        slots.append('Atun')   #3
        slots.append('Bacalao')   #4
        slots.append('Bacalao')   #5
        slots.append('Bacalao')   #6
        slots.append('Bacalao')   #7
        slots.append('Blanco_Nilo')   #8
        slots.append('Boqueron')   #9
        slots.append('Boqueron')   #10
        slots.append('Boqueron')   #11
        slots.append('Boqueron')   #12
        slots.append('Calamar')   #13
        slots.append('Calamar')   #14
        slots.append('Callo_de_hacha')   #15
        slots.append('Callo_de_hacha')   #16
        slots.append('Callo_de_hacha')   #17

    elif nombre == "4I": #Cuidado personal
        slots.append('Acondicionador_._enjuague')   #1
        slots.append('Acondicionador_._enjuague')   #2
        slots.append('Acondicionador_._enjuague')   #3
        slots.append('Champu')   #4
        slots.append('Champu')   #5
        slots.append('Champu')   #6
        slots.append('Champu')   #7
        slots.append('Champu_para_bebes')   #8
        slots.append('Champu_para_bebes')   #9
        slots.append('Champu_para_bebes')   #10
        slots.append('Champu_para_bebes')   #11
        slots.append('Crema_dental')   #12
        slots.append('Crema_dental')   #13
        slots.append('Crema_dental')   #14
        slots.append('Crema_dental')   #15
        slots.append('Crema_liquida')   #16
        slots.append('Crema_solida')   #17

    elif nombre == "4D": #Cuidado personal
        slots.append('Crema_solida')   #1
        slots.append('Crema_solida')   #2
        slots.append('Desodorante')   #3
        slots.append('Desodorante')   #4
        slots.append('Desodorante')   #5
        slots.append('Jabon_de_tocador')   #6
        slots.append('Jabon_de_tocador')   #7
        slots.append('Panales_desechables')   #8
        slots.append('Panales_desechables')   #9
        slots.append('Panales_desechables')   #10
        slots.append('Papel_higienico')   #11
        slots.append('Papel_higienico')   #12
        slots.append('Rastrillos_desechables')   #13
        slots.append('Rastrillos_desechables')   #14
        slots.append('Rastrillos_desechables')   #15
        slots.append('Rastrillos_desechables')   #16
        slots.append('Rastrillos_desechables')   #17

    elif nombre == "5I": #Frutas
        slots.append('Acelga')   #1
        slots.append('Acelga')   #2
        slots.append('Acelga')   #3
        slots.append('Palta')   #4
        slots.append('Palta')   #5
        slots.append('Palta')   #6
        slots.append('Palta')   #7
        slots.append('Ajo')   #8
        slots.append('Alcachofa')   #9
        slots.append('Alcachofa')   #10
        slots.append('Alcachofa')   #11
        slots.append('Alcaparra')   #12
        slots.append('Alcaparra')   #13
        slots.append('Almendras')   #14
        slots.append('Almendras')   #15
        slots.append('Almendras')   #16
        slots.append('Apio')   #17

    elif nombre == "5D": #Frutas
        slots.append('Avellana')   #1
        slots.append('Avellana')   #2
        slots.append('Avellana')   #3
        slots.append('Betarraga')   #4
        slots.append('Betarraga')   #5
        slots.append('Betarraga')   #6
        slots.append('Brocoli')   #7
        slots.append('Calabaza')   #8
        slots.append('Calabaza')   #9
        slots.append('Castanas')   #10
        slots.append('Cebolla')   #11
        slots.append('Cebolla')   #12
        slots.append('Champinon')   #13
        slots.append('Champinon')   #14
        slots.append('Ciruela')   #15
        slots.append('Ciruela')   #16
        slots.append('Ciruela')   #17


    elif nombre == "6I": #Fruta
        slots.append('Ciruela')   #1
        slots.append('Ciruela_pasa')   #2
        slots.append('Ciruela_pasa')   #3
        slots.append('Ciruela_pasa')   #4
        slots.append('Coliflor')   #5
        slots.append('Coliflor')   #6
        slots.append('Coliflor')   #7
        slots.append('Coliflor')   #8
        slots.append('Durazno')   #9
        slots.append('Durazno')   #10
        slots.append('Durazno')   #11
        slots.append('Espinacas')   #12
        slots.append('Espinacas')   #13
        slots.append('Espinacas')   #14
        slots.append('Fresa')   #15
        slots.append('Frijoles')   #16
        slots.append('Frijoles')   #17

    elif nombre == "6D": #Fruta
        slots.append('Granada')   #1
        slots.append('Granada')   #2
        slots.append('Granada')   #3
        slots.append('Granada')   #4
        slots.append('Kiwi')   #5
        slots.append('Lechuga')   #6
        slots.append('Lima')   #7
        slots.append('Limon')   #8
        slots.append('Limon')   #9
        slots.append('Mandarina')   #10
        slots.append('Mandarina')   #11
        slots.append('Mandarina')   #12
        slots.append('Mango')   #13
        slots.append('Mango')   #14
        slots.append('Manzana')   #15
        slots.append('Manzana')   #16
        slots.append('Manzana')   #17

    elif nombre == "7I": #Fruta
        slots.append('Melon')   #1
        slots.append('Melon')   #2
        slots.append('Naranja')   #3
        slots.append('Naranja')   #4
        slots.append('Nuez')   #5
        slots.append('Papa')   #6
        slots.append('Papaya')   #7
        slots.append('Pasa_(Uva_pasa)')   #8
        slots.append('Pasa_(Uva_pasa)')   #9
        slots.append('Pasa_(Uva_pasa)')   #10
        slots.append('Pepino')   #11
        slots.append('Pepino')   #12
        slots.append('Pera')   #13
        slots.append('Pera')   #14
        slots.append('Pera')   #15
        slots.append('Pimiento')   #16
        slots.append('Pina')   #17

    elif nombre == "7D": #Aceites
        slots.append('Aceite')   #1
        slots.append('Aceite_de_oliva')   #2
        slots.append('Grasa_comestible')   #3
        slots.append('Grasa_comestible')   #4
        slots.append('Grasa_comestible')   #5
        slots.append('Manteca')   #6
        slots.append('Manteca')   #7
        slots.append('Manteca_de_cerdo')   #8
        slots.append('Manteca_de_cerdo')   #9
        slots.append('Margarina')   #10
        slots.append('Margarina')   #11
        slots.append('Margarina')   #12
        slots.append('Margarina')   #13
        slots.append('Margarina_light')   #14
        slots.append('Margarina_light')   #15
        slots.append('Margarina_light')   #16
        slots.append('Margarina_light')   #17

    elif nombre == "8I": #Condimentos
        slots.append('Ajonjoli')   #1
        slots.append('Ajonjoli')   #2
        slots.append('Canela')   #3
        slots.append('Canela')   #4
        slots.append('Canela')   #5
        slots.append('Canela')   #6
        slots.append('Canela')   #7
        slots.append('Chilorio')   #8
        slots.append('Chilorio')   #9
        slots.append('Chilorio')   #10
        slots.append('Chilorio')   #11
        slots.append('Chilorio')   #12
        slots.append('Clavo')   #13
        slots.append('Cochinita_pibil')   #14
        slots.append('Concentrado_de_pollo')   #15
        slots.append('Concentrado_de_pollo')   #16
        slots.append('Concentrado_de_pollo')   #17

    elif nombre == "8D": #Condimentos
        slots.append('Concentrado_de_pollo')   #1
        slots.append('Condimento_de_achiote')   #2
        slots.append('Condimento_de_achiote')   #3
        slots.append('Condimento_de_achiote')   #4
        slots.append('Hojas_de_perejil')   #5
        slots.append('Hojas_de_perejil')   #6
        slots.append('Mayonesa')   #7
        slots.append('Mayonesa')   #8
        slots.append('Mayonesa')   #9
        slots.append('Mayonesa')   #10
        slots.append('Mayonesa')   #11
        slots.append('Mole_rojo_en_pasta')   #12
        slots.append('Mole_rojo_en_pasta')   #13
        slots.append('Mole_rojo_en_pasta')   #14
        slots.append('Mole_rojo_en_pasta')   #15
        slots.append('Mostaza')   #16
        slots.append('Mostaza')   #17

    elif nombre == "9I": #Carnes
        slots.append('Cabeza_de_cerdo')   #1
        slots.append('Cabeza_de_cerdo')   #2
        slots.append('Cabeza_de_cerdo')   #3
        slots.append('Carnes_molida_de_cerdo')   #4
        slots.append('Carnes_molida_de_res')   #5
        slots.append('Carnes_molida_de_res')   #6
        slots.append('Carnes_molida_de_res')   #7
        slots.append('Carnes_molida_de_res')   #8
        slots.append('Carnes_molida_de_res')   #9
        slots.append('Cerdo')   #10
        slots.append('Cerdo')   #11
        slots.append('Cerdo')   #12
        slots.append('Cerdo')   #13
        slots.append('Chuleta_ahumada_de_cerdo')   #14
        slots.append('Chuleta_ahumada_de_cerdo')   #15
        slots.append('Chuleta_ahumada_de_cerdo')   #16
        slots.append('Chuleta_ahumada_de_cerdo')   #17

    elif nombre == "9D": #Carnes
        slots.append('Espinazo_de_cerdo')   #1
        slots.append('Lomo_de_cerdo')   #2
        slots.append('Milanesa_de_cerdo')   #3
        slots.append('Milanesa_de_cerdo')   #4
        slots.append('Milanesa_de_cerdo')   #5
        slots.append('Pata_de_cerdo')   #6
        slots.append('Pata_de_cerdo')   #7
        slots.append('Pata_de_cerdo')   #8
        slots.append('Pata_de_cerdo')   #9
        slots.append('Pernil')   #10
        slots.append('Pernil')   #11
        slots.append('Pernil')   #12
        slots.append('Pernil')   #13
        slots.append('Pernil')   #14
        slots.append('Pavo')   #15
        slots.append('Pavo')   #16
        slots.append('Pavo')   #17


    elif nombre == "10I": #Carnes
        slots.append('Pavo')   #1
        slots.append('Pavo')   #2
        slots.append('Pechuga_de_pollo')   #3
        slots.append('Pierna_de_pollo')   #4
        slots.append('Pierna_de_pollo')   #5
        slots.append('Pierna_de_pollo')   #6
        slots.append('Pierna_de_pollo')   #7
        slots.append('Pierna_de_pollo')   #8
        slots.append('Pollo')   #9
        slots.append('Pollo')   #10
        slots.append('Pollo')   #11
        slots.append('Pollo')   #12
        slots.append('Pollo')   #13
        slots.append('Pollo_entero')   #14
        slots.append('Pollo_entero')   #15
        slots.append('Pollo_entero')   #16
        slots.append('Pollo_entero')   #17

    elif nombre == "10D": #Fiambreria
        slots.append('Chorizo')   #1
        slots.append('Chorizo')   #2
        slots.append('Chorizo')   #3
        slots.append('Chorizo')   #4
        slots.append('Jamon')   #5
        slots.append('Jamon')   #6
        slots.append('Jamon')   #7
        slots.append('jamon_de_pavo')   #8
        slots.append('jamon_de_pavo')   #9
        slots.append('jamon_de_pavo')   #10
        slots.append('jamon_de_pavo')   #11
        slots.append('jamon_de_pavo')   #12
        slots.append('Longaniza')   #13
        slots.append('Longaniza')   #14
        slots.append('Longaniza')   #15
        slots.append('Mortadela')   #16
        slots.append('Pastel_pimiento')   #17


    elif nombre == "11I": #Fiambreria
        slots.append('Pastel_pimiento')   #1
        slots.append('Pate')   #2
        slots.append('Queso_de_puerco')   #3
        slots.append('Queso_de_puerco')   #4
        slots.append('Queso_de_puerco')   #5
        slots.append('Queso_de_puerco')   #6
        slots.append('Queso_de_puerco')   #7
        slots.append('Salami')   #8
        slots.append('Salchicha')   #9
        slots.append('Salchicha')   #10
        slots.append('Salchicha')   #11
        slots.append('Salchicha')   #12
        slots.append('Salchicha')   #13
        slots.append('Tocino')   #14
        slots.append('Tocino')   #15
        slots.append('Tocino')   #16
        slots.append('Tocino')   #17

    elif nombre == "11D": # Pescado
        slots.append('Camaron')   #1
        slots.append('Camaron')   #2
        slots.append('Carpa')   #3
        slots.append('Carpa')   #4
        slots.append('Carpa')   #5
        slots.append('Carpa')   #6
        slots.append('Carpa')   #7
        slots.append('Cazon')   #8
        slots.append('Cazon')   #9
        slots.append('Cazon')   #10
        slots.append('Cazon')   #11
        slots.append('Charal')   #12
        slots.append('Charal')   #13
        slots.append('Cintilla')   #14
        slots.append('Curvina')   #15
        slots.append('Curvina')   #16
        slots.append('Curvina')   #17


    elif nombre == "12I": # Pescados
        slots.append('Curvina')   #1
        slots.append('Curvina')   #2
        slots.append('Gurrubata')   #3
        slots.append('Gurrubata')   #4
        slots.append('Gurrubata')   #5
        slots.append('Gurrubata')   #6
        slots.append('Gurrubata')   #7
        slots.append('Huachinango')   #8
        slots.append('Huachinango')   #9
        slots.append('Huachinango')   #10
        slots.append('Huachinango')   #11
        slots.append('Huachinango')   #12
        slots.append('Jaiba')   #13
        slots.append('Jaiba')   #14
        slots.append('Jaiba')   #15
        slots.append('Jaiba')   #16
        slots.append('Langosta')   #17

    elif nombre == "12D": #Cuidado personal
        slots.append('Repuestos_de_navajas')   #1
        slots.append('Repuestos_de_navajas')   #2
        slots.append('Repuestos_de_navajas')   #3
        slots.append('Repuestos_de_navajas')   #4
        slots.append('Repuestos_de_navajas')   #5
        slots.append('Tinte_para_el_cabello')   #6
        slots.append('Tinte_para_el_cabello')   #7
        slots.append('Tinte_para_el_cabello')   #8
        slots.append('Tinte_para_el_cabello')   #9
        slots.append('Tinte_para_el_cabello')   #10
        slots.append('Toalla_femenina')   #11
        slots.append('Toalla_femenina')   #12
        slots.append('Toalla_femenina')   #13
        slots.append('Toalla_femenina')   #14
        slots.append('Toalla_femenina')   #15
        slots.append('Toallita_humeda_limpiadora')   #16
        slots.append('Toallita_humeda_limpiadora')   #17

    elif nombre == "13I": # Limpieza
        slots.append('Acondicionador_de_telas')   #1
        slots.append('Barra_limpiadora')   #2
        slots.append('Barra_limpiadora')   #3
        slots.append('Barra_limpiadora')   #4
        slots.append('Blanqueador')   #5
        slots.append('Blanqueador')   #6
        slots.append('Blanqueador')   #7
        slots.append('Detergente_ropa')   #8
        slots.append('Detergente_ropa_liquido')   #9
        slots.append('Detergente_ropa_liquido')   #10
        slots.append('Detergente_ropa_liquido')   #11
        slots.append('Detergente_ropa_liquido')   #12
        slots.append('Detergente_ropa_polvo')   #13
        slots.append('Detergente_ropa_polvo')   #14
        slots.append('Detergente_trastes')   #15
        slots.append('Insecticida_aerosol')   #16
        slots.append('Insecticida_aerosol')   #17


    elif nombre == "13D": #Limpieza
        slots.append('Jabon_de_pasta')   #1
        slots.append('Jabon_limpiador')   #2
        slots.append('Jabon_limpiador')   #3
        slots.append('Limpiador_liquido')   #4
        slots.append('Limpiador_liquido')   #5
        slots.append('Limpiador_liquido_piso')   #6
        slots.append('Servilletas_de_papel')   #7
        slots.append('Servilletas_de_papel')   #8
        slots.append('Servilletas_de_papel')   #9
        slots.append('Servilletas_de_papel')   #10
        slots.append('Suavizante_ropa')   #11
        slots.append('Suavizante_ropa')   #12
        slots.append('Suavizante_ropa')   #13
        slots.append('Suavizante_ropa')   #14
        slots.append('Toalla_de_papel')   #15
        slots.append('Toalla_de_papel')   #16
        slots.append('Toalla_de_papel')   #17

    elif nombre == "14I": #Fruta
        slots.append('Pina')   #1
        slots.append('Pina')   #2
        slots.append('Platano')   #3
        slots.append('Platano')   #4
        slots.append('Platano')   #5
        slots.append('Platano')   #6
        slots.append('Rabano')   #7
        slots.append('Rabano')   #8
        slots.append('Rabano')   #9
        slots.append('Sandia')   #10
        slots.append('Sandia')   #11
        slots.append('Sandia')   #12
        slots.append('Sandia')   #13
        slots.append('Sandia')   #14
        slots.append('Tomate')   #15
        slots.append('Tomate')   #16
        slots.append('Tomate')   #17

    elif nombre == "14D": #Fruta
        slots.append('Tomate')   #1
        slots.append('Tomate')   #2
        slots.append('Tuna')   #3
        slots.append('Tuna')   #4
        slots.append('Tuna')   #5
        slots.append('Tuna')   #6
        slots.append('Tuna')   #7
        slots.append('Uva')   #8
        slots.append('Uva')   #9
        slots.append('Uva')   #10
        slots.append('Uva')   #11
        slots.append('Uva')   #12
        slots.append('Zanahoria')   #13
        slots.append('Zanahoria')   #14
        slots.append('Zanahoria')   #15
        slots.append('Zanahoria')   #16
        slots.append('Zanahoria')   #17

    elif nombre == "15I": #Bebidas
        slots.append('Agua_con_gas')   #1
        slots.append('Agua_con_gas')   #2
        slots.append('Agua_con_gas')   #3
        slots.append('Agua_con_gas')   #4
        slots.append('Agua_con_gas')   #5
        slots.append('Agua_sin_gas')   #6
        slots.append('Agua_sin_gas')   #7
        slots.append('Agua_sin_gas')   #8
        slots.append('Agua_sin_gas')   #9
        slots.append('Agua_sin_gas')   #10
        slots.append('Bebida_hidratante')   #11
        slots.append('Bebida_hidratante')   #12
        slots.append('Bebida_hidratante')   #13
        slots.append('Bebida_hidratante')   #14
        slots.append('Bebida_hidratante')   #15
        slots.append('Jugo_de_fruta')   #16
        slots.append('Jugo_de_fruta')   #17

    elif nombre == "15D": #Bebidas
        slots.append('Refresco')   #1
        slots.append('Cerveza')   #2
        slots.append('Jerez')   #3
        slots.append('Jerez')   #4
        slots.append('Jerez')   #5
        slots.append('Rompope')   #6
        slots.append('Rompope')   #7
        slots.append('Rompope')   #8
        slots.append('Sidra')   #9
        slots.append('Sidra')   #10
        slots.append('Sidra')   #11
        slots.append('Sidra')   #12
        slots.append('Sidra')   #13
        slots.append('Vino_de_mesa')   #14
        slots.append('Vino_de_mesa')   #15
        slots.append('Vino_de_mesa')   #16
        slots.append('Vino_de_mesa')   #17

    elif nombre == "16I": #Condimentos
        slots.append('Pimienta')   #1
        slots.append('Polvo_p.hornear')   #2
        slots.append('Polvo_p.hornear')   #3
        slots.append('Sal')   #4
        slots.append('Sal')   #5
        slots.append('Sal')   #6
        slots.append('Sal')   #7
        slots.append('Sal')   #8
        slots.append('Sal_molida_de_mesa')   #9
        slots.append('Sal_molida_de_mesa')   #10
        slots.append('Salsa')   #11
        slots.append('Salsa')   #12
        slots.append('Salsa_catsup')   #13
        slots.append('Salsa_catsup')   #14
        slots.append('Salsa_de_chile')   #15
        slots.append('Salsa_de_chile')   #16
        slots.append('Salsa_de_chile')   #17

    elif nombre == "16D": #Condimentos
        slots.append('Salsa_de_soya')   #1
        slots.append('Salsa_de_soya')   #2
        slots.append('Salsa_de_soya')   #3
        slots.append('Salsa_inglesa')   #4
        slots.append('Salsa_inglesa')   #5
        slots.append('Salsa_inglesa')   #6
        slots.append('Salsa_inglesa')   #7
        slots.append('Salsa_inglesa')   #8
        slots.append('Salsa_mexicana')   #9
        slots.append('Salsa_picante')   #10
        slots.append('Sopa_y_crema')   #11
        slots.append('Vainilla')   #12
        slots.append('Vainilla')   #13
        slots.append('Vainilla')   #14
        slots.append('Vinagre')   #15
        slots.append('Vinagre')   #16
        slots.append('Vinagre')   #17

    elif nombre == "17I": #Lacteos
        slots.append('Huevo')   #1
        slots.append('Huevo')   #2
        slots.append('Huevo')   #3
        slots.append('Huevo')   #4
        slots.append('Huevo')   #5
        slots.append('Crema')   #6
        slots.append('Crema')   #7
        slots.append('Crema')   #8
        slots.append('Crema_batida')   #9
        slots.append('Crema_batida')   #10
        slots.append('Crema_batida')   #11
        slots.append('Crema_batida')   #12
        slots.append('Crema_batida')   #13
        slots.append('Mantequilla')   #14
        slots.append('Mantequilla')   #15
        slots.append('Mantequilla')   #16
        slots.append('Mantequilla')   #17

    elif nombre == "17D": #Lacteos
        slots.append('Mantequilla')   #1
        slots.append('Queso_mantecosi')   #2
        slots.append('Queso_mantecosi')   #3
        slots.append('Queso_mantecosi')   #4
        slots.append('Queso_gauda')   #5
        slots.append('Queso_gauda')   #6
        slots.append('Queso_gauda')   #7
        slots.append('Queso_gauda')   #8
        slots.append('Queso_gauda')   #9
        slots.append('Queso_blanco')   #10
        slots.append('Queso_blanco')   #11
        slots.append('Queso_blanco')   #12
        slots.append('Queso_blanco')   #13
        slots.append('Queso_blanco')   #14
        slots.append('Yoghurt')   #15
        slots.append('Yoghurt')   #16
        slots.append('Yoghurt')   #17

    elif nombre == "18I": #Lacteos
        slots.append('Leche_condensada')   #1
        slots.append('Leche_condensada')   #2
        slots.append('Leche_condensada')   #3
        slots.append('Leche_en_polvo')   #4
        slots.append('Leche_en_polvo')   #5
        slots.append('Leche_en_polvo')   #6
        slots.append('Leche_en_polvo')   #7
        slots.append('Leche_en_polvo')   #8
        slots.append('Leche_evaporada')   #9
        slots.append('Leche_evaporada')   #10
        slots.append('Leche_pasteurizada')   #11
        slots.append('Leche_pasteurizada')   #12
        slots.append('Leche_pasteurizada')   #13
        slots.append('Leche_pasteurizada')   #14
        slots.append('Leche_ultrapasteurizada')   #15
        slots.append('Leche_ultrapasteurizada')   #16
        slots.append('Leche_ultrapasteurizada')   #17

    elif nombre == "18D": #Dulces
        slots.append('Chocolate_en_tablillas')   #1
        slots.append('Colacion')   #2
        slots.append('Flan')   #3
        slots.append('Flan')   #4
        slots.append('Gelatina_en_polvo')   #5
        slots.append('Gelatina_en_polvo')   #6
        slots.append('Manjarate')   #7
        slots.append('Polvo_bebida_sabor_chocolate')   #8
        slots.append('Chandell')   #9
        slots.append('Chandell')   #10
        slots.append('Postre_estilo_flan')   #11
        slots.append('Praline')   #12
        slots.append('Praline')   #13
        slots.append('Praline')   #14
        slots.append('Torta_Imperial')   #15
        slots.append('Turron')   #16
        slots.append('Turron')   #17

    elif nombre == "19I": #Legumbres
        slots.append('Poroto')   #1
        slots.append('Garbanzo')   #2
        slots.append('Garbanzo')   #3
        slots.append('Garbanzo')   #4
        slots.append('Garbanzo')   #5
        slots.append('Haba')   #6
        slots.append('Haba')   #7
        slots.append('Haba')   #8
        slots.append('Haba')   #9
        slots.append('Lenteja')   #10
        slots.append('Lenteja')   #11
        slots.append('Lenteja')   #12
        slots.append('Lenteja')   #13
        slots.append('Lenteja')   #14

    elif nombre == "19D": #Cereales
        slots.append('Arroz')   #1
        slots.append('Avena')   #2
        slots.append('Avena')   #3
        slots.append('Avena')   #4
        slots.append('Avena')   #5
        slots.append('Cereal_mixto')   #6
        slots.append('Cereal_mixto')   #7
        slots.append('Cereal_mixto')   #8
        slots.append('Harina_de_arroz')   #9
        slots.append('Harina_de_arroz')   #10
        slots.append('Harina_de_arroz')   #11
        slots.append('Harina_de_arroz')   #12
        slots.append('Harina_de_arroz')   #13

    return slots 

if __name__ == "__main__":

    a = productos_esta_gondola("6I")
    print(a)