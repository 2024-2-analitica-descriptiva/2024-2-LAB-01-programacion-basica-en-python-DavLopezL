"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    data = open("files/input/data.csv","r").readlines()
    data = [z.split("\t") for z in data]
    fechas = [z[2] for z in data]
    meses = [t.split("-")[1] for t in fechas]
    lista = []

    for key in meses:
        tupla = (key,1)
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
    # La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    # cantidad de registros por cada mes, tal como se muestra a continuación.

    # Rta/
    # [('01', 3),
    #  ('02', 4),
    #  ('03', 2),
    #  ('04', 4),
    #  ('05', 3),
    #  ('06', 3),
    #  ('07', 5),
    #  ('08', 6),
    #  ('09', 3),
    #  ('10', 2),
    #  ('11', 2),
    #  ('12', 3)]

    # """
