from utils import normalizar_texto, limpiar_numero, mostrar_paises
from archivo_csv import guardar_paises


def agregar_pais(paises):
    """Solicita los datos de un nuevo país, valida que no haya campos vacíos
    y lo agrega a la lista y al archivo CSV."""
    print("\n----- AGREGAR PAÍS -----")

    # Nombre: no puede estar vacío ni repetido
    while True:
        nombre = input("Nombre del país: ").strip()
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
            continue

        encontrado = False
        for p in paises:
            if normalizar_texto(p["nombre"]) == normalizar_texto(nombre):
                encontrado = True
                break
        if encontrado:
            print(f"Error: ya existe un país con el nombre '{nombre}'.")
            continue

        break

    # Población: número entero positivo
    while True:
        try:
            poblacion = limpiar_numero(input("Población: "))
            if poblacion < 0:
                print("Error: la población no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Error: ingrese un número entero válido para la población.")

    # Superficie: número entero positivo
    while True:
        try:
            superficie = limpiar_numero(input("Superficie (km²): "))
            if superficie < 0:
                print("Error: la superficie no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Error: ingrese un número entero válido para la superficie.")

    # Continente: no puede estar vacío
    while True:
        continente = input("Continente: ").strip()
        if continente == "":
            print("Error: el continente no puede estar vacío.")
            continue
        break

    nuevo_pais = {
        "nombre":     nombre,
        "poblacion":  poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    guardar_paises(paises)
    print(f"País '{nombre}' agregado exitosamente.")


def actualizar_pais(paises):
    """Busca un país por nombre y permite actualizar
    su población y/o superficie. Guarda los cambios en el CSV."""
    print("\n----- ACTUALIZAR PAÍS -----")

    nombre_busqueda = input("Ingrese el nombre del país a actualizar: ").strip()
    if nombre_busqueda == "":
        print("Error: debe ingresar un nombre.")
        return

    indice = -1
    for i in range(len(paises)):
        if normalizar_texto(paises[i]["nombre"]) == normalizar_texto(nombre_busqueda):
            indice = i
            break

    if indice == -1:
        print(f"No se encontró ningún país con el nombre '{nombre_busqueda}'.")
        return

    pais = paises[indice]
    print(f"\nPaís encontrado: {pais['nombre']} | Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km²")

    # Actualizar población
    while True:
        nueva_poblacion = input(f"Nueva población (actual: {pais['poblacion']:,}) — dejar vacío para no cambiar: ").strip()
        if nueva_poblacion == "":
            break
        try:
            valor = limpiar_numero(nueva_poblacion)
            if valor < 0:
                print("Error: la población no puede ser negativa.")
                continue
            paises[indice]["poblacion"] = valor
            break
        except ValueError:
            print("Error: ingrese un número entero válido.")

    # Actualizar superficie
    while True:
        nueva_superficie = input(f"Nueva superficie (actual: {pais['superficie']:,} km²) — dejar vacío para no cambiar: ").strip()
        if nueva_superficie == "":
            break
        try:
            valor = limpiar_numero(nueva_superficie)
            if valor < 0:
                print("Error: la superficie no puede ser negativa.")
                continue
            paises[indice]["superficie"] = valor
            break
        except ValueError:
            print("Error: ingrese un número entero válido.")

    guardar_paises(paises)
    print(f"Datos de '{paises[indice]['nombre']}' actualizados correctamente.")


def buscar_por_nombre(paises):
    """Busca países cuyo nombre contenga el texto ingresado
    (coincidencia parcial, insensible a mayúsculas)."""
    print("\n----- BUSCAR PAÍS POR NOMBRE -----")

    termino = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip()
    if termino == "":
        print("Error: debe ingresar un término de búsqueda.")
        return

    termino_normalizado = normalizar_texto(termino)
    resultados = []
    for p in paises:
        if termino_normalizado in normalizar_texto(p["nombre"]):
            resultados.append(p)

    if not resultados:
        print(f"No se encontraron países con '{termino}' en el nombre.")
    else:
        print(f"\nSe encontraron {len(resultados)} resultado(s):")
        mostrar_paises(resultados)


def eliminar_pais(paises):
    """Busca un país por nombre y lo elimina de la lista y del CSV
    después de solicitar confirmación."""
    print("\n----- ELIMINAR PAÍS -----")

    nombre_busqueda = input("Ingrese el nombre del país a eliminar: ").strip()
    if nombre_busqueda == "":
        print("Error: debe ingresar un nombre.")
        return

    indice = -1
    for i in range(len(paises)):
        if normalizar_texto(paises[i]["nombre"]) == normalizar_texto(nombre_busqueda):
            indice = i
            break

    if indice == -1:
        print(f"No se encontró ningún país con el nombre '{nombre_busqueda}'.")
        return

    pais = paises[indice]
    print(f"\nPaís a eliminar: {pais['nombre']} | Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km²")

    confirmacion = input("¿Está seguro de que desea eliminar este país? (s/n): ").strip().lower()
    if confirmacion != "s":
        print("Eliminación cancelada.")
        return

    nombre_eliminado = paises[indice]["nombre"]
    paises.pop(indice)
    guardar_paises(paises)
    print(f"País '{nombre_eliminado}' eliminado correctamente.")
