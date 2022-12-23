import random

def seleccionar_palabra():
    palabras=['caja','avion','locomotora','pecera','ahorcado']
    palabra = random.choice(palabras)
    return palabra

def convertir_lista():
    lista=list(seleccionar_palabra())
    print(lista)
    return lista



