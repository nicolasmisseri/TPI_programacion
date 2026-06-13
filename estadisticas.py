def obtener_estadisticas(paises):
    """Obtiene estadísticas generales de los países"""
    if not paises:
        print("No hay países para mostrar estadísticas.")
        return

    pais_mayor_poblacion = paises[0]
    pais_menor_poblacion = paises[0]
    suma_poblacion = 0
    suma_superficie = 0

    for p in paises:
        suma_poblacion += p["poblacion"]
        suma_superficie += p["superficie"]
        if p["poblacion"] > pais_mayor_poblacion["poblacion"]:
            pais_mayor_poblacion = p
        if p["poblacion"] < pais_menor_poblacion["poblacion"]:
            pais_menor_poblacion = p

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print("\n----- ESTADÍSTICAS GENERALES -----")
    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']:,})")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']:,})")
    print(f"Promedio de población: {promedio_poblacion:,.0f}")
    print(f"Promedio de superficie: {promedio_superficie:,.0f} km²")


def contar_paises_por_continente(paises):
    """Cuenta la cantidad de países por continente"""
    if not paises:
        print("No hay países para contar.")
        return

    continentes = {}
    for p in paises:
        continente = p["continente"]
        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\n----- PAÍSES POR CONTINENTE -----")
    for continente in continentes:
        print(f"{continente}: {continentes[continente]} país/es")
