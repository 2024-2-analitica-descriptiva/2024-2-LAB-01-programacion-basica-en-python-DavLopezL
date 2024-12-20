"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    data = open("files/input/data.csv","r").readlines()
    data = [z.replace('\n','') for z in data]
    data = [z.split("\t") for z in data]    
    data = [z[4].split(",") for z in data]
    lista = []
    for i in range(len(data)):
        lista += data[i]
    a = [t.split(":") for t in lista]
    dict_min={}
    dict_max={}

    for i in a:
        if i[0] not in dict_max:
            dict_max[i[0]]=int(i[1])
            
        else:
            if int(dict_max[i[0]]) <= int(i[1]):
                dict_max[i[0]]= int(i[1])

        if i[0] not in dict_min:
            dict_min[i[0]]=int(i[1])
            
        else:
            if int(dict_min[i[0]]) >= int(i[1]):
                dict_min[i[0]]=int(i[1])

    l = []
    for i in dict_max:
        new_tuple = (i,dict_min[i],dict_max[i])
        l.append(new_tuple)

    l = sorted(l, key=lambda i: i[0])

    return l

    # """
    # La columna 5 codifica un diccionario donde cada cadena de tres letras
    # corresponde a una clave y el valor despues del caracter `:` corresponde al
    # valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    # pequeño y el valor asociado mas grande computados sobre todo el archivo.

    # Rta/
    # [('aaa', 1, 9),
    #  ('bbb', 1, 9),
    #  ('ccc', 1, 10),
    #  ('ddd', 0, 9),
    #  ('eee', 1, 7),
    #  ('fff', 0, 9),
    #  ('ggg', 3, 10),
    #  ('hhh', 0, 9),
    #  ('iii', 0, 9),
    #  ('jjj', 5, 17)]

    # """
