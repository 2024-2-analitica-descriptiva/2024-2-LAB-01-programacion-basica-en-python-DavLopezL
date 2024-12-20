"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    data = open("files/input/data.csv","r").readlines()
    data = [z.split("\t") for z in data]
    letras = []
    x = []

    for i in data:
        letras.append(i[0])
    letras = list(set(letras))
    
    for i in letras:
        val = []
        for r in data:
            if i == r[0]:
                val.append(r[1])
        new_tuple = (i,int(max(val)),int(min(val)))
        x.append(new_tuple)

    x = sorted(x, key=lambda i: i[0])

    return x

    # """
    # Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    # por cada letra de la columa 1.

    # Rta/
    # [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    # """
