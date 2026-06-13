def ordenar_por_nombre(paises, descendente=False):
    """Ordena países por nombre usando bubble sort"""
    lista = paises[:]
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if not descendente:
                condicion = lista[j]["nombre"].lower() > lista[j + 1]["nombre"].lower()
            else:
                condicion = lista[j]["nombre"].lower() < lista[j + 1]["nombre"].lower()
            if condicion:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def ordenar_por_poblacion(paises, descendente=False):
    """Ordena países por población usando bubble sort"""
    lista = paises[:]
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if not descendente:
                condicion = lista[j]["poblacion"] > lista[j + 1]["poblacion"]
            else:
                condicion = lista[j]["poblacion"] < lista[j + 1]["poblacion"]
            if condicion:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def ordenar_por_superficie(paises, descendente=False):
    """Ordena países por superficie usando bubble sort"""
    lista = paises[:]
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if not descendente:
                condicion = lista[j]["superficie"] > lista[j + 1]["superficie"]
            else:
                condicion = lista[j]["superficie"] < lista[j + 1]["superficie"]
            if condicion:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
