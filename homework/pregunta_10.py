"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    data = open("files/input/data.csv","r").readlines()
    data = [z.split("\t") for z in data]

    col_1 = []
    col_4 = []
    col_5 = []

    for elem in data:
        col_1.append(elem[0])
        col_4.append(len(elem[3].split(",")))
        col_5.append(len(elem[4].split(",")))

    lista = list(zip(col_1,col_4,col_5))


    return lista

    # """
    # Retorne una lista de tuplas contengan por cada tupla, la letra de la
    # columna 1 y la cantidad de elementos de las columnas 4 y 5.

    # Rta/
    # [('E', 3, 5),
    #  ('A', 3, 4),
    #  ...
    #  ('E', 2, 3),
    #  ('E', 3, 3)]


    # """
