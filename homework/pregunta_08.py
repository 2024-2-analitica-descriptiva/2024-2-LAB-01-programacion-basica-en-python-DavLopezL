"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    data = open("files/input/data.csv","r").readlines()
    data = [z.split("\t") for z in data]
    
    dictionary = {}
    for elem in data:
        if int(elem[1]) in dictionary:
            dictionary[int(elem[1])] = dictionary[int(elem[1])] + [elem[0]]
        else:
            dictionary[int(elem[1])]=[elem[0]]

    for i in dictionary:
        dictionary[i] = list(set(dictionary[i]))
        dictionary[i] = sorted(dictionary[i])

    l = list(dictionary.items())
    l = sorted(l, key=lambda i: i[0])
    
    return l


    # """
    # Genere una lista de tuplas, donde el primer elemento de cada tupla
    # contiene  el valor de la segunda columna; la segunda parte de la tupla
    # es una lista con las letras (ordenadas y sin repetir letra) de la
    # primera  columna que aparecen asociadas a dicho valor de la segunda
    # columna.

    # Rta/
    # [(0, ['C']),
    #  (1, ['B', 'E']),
    #  (2, ['A', 'E']),
    #  (3, ['A', 'B', 'D', 'E']),
    #  (4, ['B', 'E']),
    #  (5, ['B', 'C', 'D', 'E']),
    #  (6, ['A', 'B', 'C', 'E']),
    #  (7, ['A', 'C', 'D', 'E']),
    #  (8, ['A', 'B', 'D', 'E']),
    #  (9, ['A', 'B', 'C', 'E'])]

    # """
