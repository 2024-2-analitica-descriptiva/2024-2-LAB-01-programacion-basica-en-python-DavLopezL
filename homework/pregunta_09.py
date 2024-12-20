"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    data = open("files/input/data.csv","r").readlines()
    data = [z.replace('\n','') for z in data]
    data = [z.split("\t") for z in data]    
    data = [z[4].split(",") for z in data]
    dictionary = {}

    for elem in data:
        lista = []
        for i in elem:
            keys = i.split(":")[0]
            lista.append(keys)
        for k in lista:
            if k in dictionary:
                dictionary[k] += 1
            else:
                dictionary[k] = 1

    dictionary_ord = dict(sorted(dictionary.items()))

    return dictionary_ord

    # """
    # Retorne un diccionario que contenga la cantidad de registros en que
    # aparece cada clave de la columna 5.

    # Rta/
    # {'aaa': 13,
    #  'bbb': 16,
    #  'ccc': 23,
    #  'ddd': 23,
    #  'eee': 15,
    #  'fff': 20,
    #  'ggg': 13,
    #  'hhh': 16,
    #  'iii': 18,
    #  'jjj': 18}}

    # """
