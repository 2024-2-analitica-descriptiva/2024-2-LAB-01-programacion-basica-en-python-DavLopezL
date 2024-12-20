"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    data = open("files/input/data.csv","r").readlines()
    data = [z.replace('\n','') for z in data]
    data = [z.split("\t") for z in data]
    
    dictionary = {}
    col_1 = []

    for elem in data:
        col_1.append(elem[0])
        valores_col_5 = []
        for i in elem[4].split(","):
            vals = i.split(":")[1]
            valores_col_5.append(int(vals))
        if elem[0] in dictionary:
            dictionary[elem[0]] += sum(valores_col_5)
        else:
            dictionary[elem[0]] = sum(valores_col_5)

    dictionary_ord = dict(sorted(dictionary.items()))

    return dictionary_ord

    # """
    # Genere un diccionario que contengan como clave la columna 1 y como valor
    # la suma de los valores de la columna 5 sobre todo el archivo.

    # Rta/
    # {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    # """
