from utils import normalizar_texto

def filtrar_por_continente(paises, continente):
    """Filtra países por continente (insensible a mayúsculas)"""
    continente_normalizado = normalizar_texto(continente)
    resultado = []
    for p in paises:
        if normalizar_texto(p["continente"]) == continente_normalizado:
            resultado.append(p)
    return resultado


def filtrar_por_poblacion(paises, poblacion_min, poblacion_max):
    """Filtra países por rango de población"""
    resultado = []
    for p in paises:
        if poblacion_min <= p["poblacion"] <= poblacion_max:
            resultado.append(p)
    return resultado


def filtrar_por_superficie(paises, superficie_min, superficie_max):
    """Filtra países por rango de superficie"""
    resultado = []
    for p in paises:
        if superficie_min <= p["superficie"] <= superficie_max:
            resultado.append(p)
    return resultado
