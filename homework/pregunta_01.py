"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    data = open("files/input/data.csv","r").readlines()
    data = [z.split("\t") for z in data]
    suma = sum(list(map(lambda i: int(i[1]), data)))
    return suma

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
