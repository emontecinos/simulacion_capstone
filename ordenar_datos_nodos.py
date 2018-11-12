## Ordenar datos_nodos.csv
import csv


with open('datos_nodos.csv') as file:
    datos = csv.reader(file)
    next(datos)
    informacion = [dato for dato in datos]
    string_node = "nodo,conexiones,x,y,gondolas,posiciones\n"
    for nodo in informacion:
        
        node_name = nodo[0]
        conexiones = nodo[1]
        x = nodo[2]
        y = nodo[3]
        gondolas = nodo[4]
        posiciones = nodo[5]

        # Ver las conexiones
        if int(node_name.split(";")[-1]) == 1: 
            if int(node_name.split(";")[0]) >= 2: 
                posiciones = "{};{};{}".format(3*int(node_name[0])-5, 3*int(node_name[0])-4, 3*int(node_name[0])-3)
        if node_name.split(";")[-1] in ['7','13']:
            posiciones = "None"
        elif node_name.split(";")[-1] in ['2','8']:
            posiciones = "1;2;3;4"
        elif node_name.split(";")[-1] in ['3','9']:
            posiciones = "5;6;7"
        elif node_name.split(";")[-1] in ['4','10']:
            posiciones = "8;9;10"
        elif node_name.split(";")[-1] in ['5','11']:
            posiciones = "11;12;13"
        elif node_name.split(";")[-1] in ['6','12']:
            posiciones = "14;15;16;17"
        
        # Ver las gondolas
        # mitad superior
        if int(node_name.split(";")[-1]) < 7:
            if int(node_name.split(";")[-1]) == 1: ## Gondola 19
                gondolas = "19"
            else:
                if int(node_name.split(";")[0]) == 1:
                    gondolas = "{}I".format(2*int(node_name.split(";")[0])-1)
                elif  int(node_name.split(";")[0]) == 9:
                    gondolas = "{}D".format(2*int(node_name.split(";")[0])-1)
                else:
                    gondolas = "{}D;{}I".format(2*int(node_name.split(";")[0])-3, 2*int(node_name.split(";")[0])-1)
            
        # Mitad inferior
        elif int(node_name.split(";")[-1]) >= 8 and int(node_name.split(";")[-1]) < 13:
            if int(node_name.split(";")[0]) == 1:
                gondolas = "{}I".format(2*int(node_name.split(";")[0]))
                
            elif int(node_name.split(";")[0]) == 11:
                gondolas = "{}D".format(2*int(node_name.split(";")[0])-4)
            else:
                if int(node_name.split(";")[0]) <= 9:
                    gondolas = "{}D;{}I".format(2*int(node_name.split(";")[0])-2, 2*int(node_name.split(";")[0]))
                else:
                    gondolas = "{}D;{}I".format(2*int(node_name.split(";")[0])-3, 2*int(node_name.split(";")[0])-2)
        else:
            # 7, 13
            gondolas = "None"
        string_node += "{},{},{},{},{},{}\n".format(node_name, conexiones, x,y,gondolas,posiciones)
    print(string_node)

with open('datos_nodos_new.csv','w') as file:
    file.write(string_node)

               
            
            

        