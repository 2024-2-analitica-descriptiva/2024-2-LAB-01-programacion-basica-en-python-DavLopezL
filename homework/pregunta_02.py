"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    data = open("files/input/data.csv","r").readlines()
    data = [z.split("\t") for z in data]
    lista = []
    for key in data:
        tupla = (key[0],1)
        lista.append(tupla)
    diccionario = {}
    for key, value in lista:
        if key in diccionario:
            diccionario[key] += value
        else:
            diccionario[key] = value
    x = list(diccionario.items())
    x = sorted(x, key=lambda i: i[0])
    return x

    # """
    # Retorne la cantidad de registros por cada letra de la primera columna como
    # la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    # Rta/
    # [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    # """
