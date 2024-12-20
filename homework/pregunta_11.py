"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():

    data = open("files/input/data.csv","r").readlines()
    data = [z.split("\t") for z in data]
    dictionary = {}

    for elem in data:
        col_4 = elem[3].split(",")
        for letra in col_4:
            if letra in dictionary:
                dictionary[letra] += int(elem[1])
            else:
                dictionary[letra] = int(elem[1])

    dictionary_ord = dict(sorted(dictionary.items()))

    return dictionary_ord
   
    # """
    # Retorne un diccionario que contengan la suma de la columna 2 para cada
    # letra de la columna 4, ordenadas alfabeticamente.

    # Rta/
    # {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    # """
