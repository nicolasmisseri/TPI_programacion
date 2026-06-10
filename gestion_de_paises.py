# Se importa el módulo csv, os y unicodedata
import csv
import os
import unicodedata

# Definición de constante para referirse al archivo csv sin repetir el str

ARCHIVO_CSV = "paises.csv"

# DEFINICIÓN DE FUNCIONES

# Lectura del archivo CSV
def cargar_paises():

    paises = []

    if not os.path.exists(ARCHIVO_CSV):
        print(f"Error: No se encontró el archivo '{ARCHIVO_CSV}'.")
        return paises
    
    try:
        with open(ARCHIVO_CSV, newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                
                if not fila.get("nombre") or not fila.get("poblacion") \
                or not fila.get("superficie") or not fila.get("continente"):
                    print(f"Advertencia: fila incompleta ignorada: {fila}")
                    continue

                try:
                    paises.append({
                        "nombre":     fila["nombre"].strip(),
                        "poblacion":  int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip()
                    })
                except ValueError:
                    print(f"Advertencia: datos inválidos en la fila: {fila}")

    except Exception as e:
        print(f"Error: no se pudo abrir el archivo: {e}")

    return paises

# Escritura/guardado de la lista de países en el CSV
def guardar_paises(paises):
    """Guarda la lista de países en el archivo CSV"""
    try:
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for p in paises:
                escritor.writerow(p)
        print("Cambios guardados correctamente en el CSV.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# FUNCIÓN DE NORMALIZACIÓN

def normalizar_texto(texto):
    """Normaliza texto removiendo acentos y convirtiendo a minúscula"""
    texto_sin_acentos = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto_sin_acentos.lower()

def limpiar_numero(numero_texto):
    """Limpia y convierte números removiendo puntos y comas"""
    # Remover espacios en blanco
    numero_texto = numero_texto.strip()
    # Remover puntos y comas (separadores de miles)
    numero_texto = numero_texto.replace(".", "").replace(",", "")
    return int(numero_texto)

# FUNCIONES DE FILTRADO

def filtrar_por_continente(paises, continente):
    """Filtra países por continente (insensible a mayúsculas, minúsculas y acentos)"""
    continente_normalizado = normalizar_texto(continente)
    return [p for p in paises if normalizar_texto(p["continente"]) == continente_normalizado]

def filtrar_por_poblacion(paises, poblacion_min, poblacion_max):
    """Filtra países por rango de población"""
    return [p for p in paises if poblacion_min <= p["poblacion"] <= poblacion_max]

def filtrar_por_superficie(paises, superficie_min, superficie_max):
    """Filtra países por rango de superficie"""
    return [p for p in paises if superficie_min <= p["superficie"] <= superficie_max]

# FUNCIONES DE ORDENAMIENTO

def ordenar_por_nombre(paises, descendente=False):
    """Ordena países por nombre"""
    return sorted(paises, key=lambda p: p["nombre"], reverse=descendente)

def ordenar_por_poblacion(paises, descendente=False):
    """Ordena países por población"""
    return sorted(paises, key=lambda p: p["poblacion"], reverse=descendente)

def ordenar_por_superficie(paises, descendente=False):
    """Ordena países por superficie"""
    return sorted(paises, key=lambda p: p["superficie"], reverse=descendente)

# FUNCIONES DE ESTADÍSTICAS

def obtener_estadisticas(paises):
    """Obtiene estadísticas generales de los países"""
    if not paises:
        print("No hay países para mostrar estadísticas.")
        return
    
    poblaciones = [p["poblacion"] for p in paises]
    superficies = [p["superficie"] for p in paises]
    
    pais_mayor_poblacion = max(paises, key=lambda p: p["poblacion"])
    pais_menor_poblacion = min(paises, key=lambda p: p["poblacion"])
    
    promedio_poblacion = sum(poblaciones) / len(poblaciones)
    promedio_superficie = sum(superficies) / len(superficies)
    
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
        continentes[continente] = continentes.get(continente, 0) + 1
    
    print("\n----- PAÍSES POR CONTINENTE -----")
    for continente in sorted(continentes.keys()):
        print(f"{continente}: {continentes[continente]} país/es")

def mostrar_paises(paises):
    """Muestra una lista de países de forma formateada"""
    if not paises:
        print("No hay países para mostrar.")
        return
    
    print(f"\n{'Nombre':<25} {'Población':>15} {'Superficie':>15} {'Continente':<20}")
    print("-" * 75)
    for p in paises:
        print(f"{p['nombre']:<25} {p['poblacion']:>15,} {p['superficie']:>15,} {p['continente']:<20}")

# ── NUEVAS FUNCIONALIDADES ──────────────────────────────────────────────────

# 1. AGREGAR UN PAÍS
def agregar_pais(paises):
    """Solicita los datos de un nuevo país, valida que no haya campos vacíos
    y lo agrega a la lista y al archivo CSV."""
    print("\n----- AGREGAR PAÍS -----")

    # Nombre: no puede estar vacío ni repetido
    while True:
        nombre = input("Nombre del país: ").strip()
        if not nombre:
            print("Error: el nombre no puede estar vacío.")
            continue
        # Verificar que no exista ya un país con ese nombre
        if any(normalizar_texto(p["nombre"]) == normalizar_texto(nombre) for p in paises):
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
        if not continente:
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


# 2. ACTUALIZAR DATOS DE UN PAÍS
def actualizar_pais(paises):
    """Busca un país por nombre exacto y permite actualizar
    su población y/o superficie. Guarda los cambios en el CSV."""
    print("\n----- ACTUALIZAR PAÍS -----")

    nombre_busqueda = input("Ingrese el nombre exacto del país a actualizar: ").strip()
    if not nombre_busqueda:
        print("Error: debe ingresar un nombre.")
        return

    # Buscar el país en la lista
    indice = None
    for i, p in enumerate(paises):
        if normalizar_texto(p["nombre"]) == normalizar_texto(nombre_busqueda):
            indice = i
            break

    if indice is None:
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


# 3. BUSCAR PAÍS POR NOMBRE
def buscar_por_nombre(paises):
    """Busca países cuyo nombre contenga el texto ingresado
    (coincidencia parcial, insensible a mayúsculas y acentos)."""
    print("\n----- BUSCAR PAÍS POR NOMBRE -----")

    termino = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip()
    if not termino:
        print("Error: debe ingresar un término de búsqueda.")
        return

    termino_normalizado = normalizar_texto(termino)
    resultados = [p for p in paises if termino_normalizado in normalizar_texto(p["nombre"])]

    if not resultados:
        print(f"No se encontraron países con '{termino}' en el nombre.")
    else:
        print(f"\nSe encontraron {len(resultados)} resultado(s):")
        mostrar_paises(resultados)


# 4. ELIMINAR UN PAÍS
def eliminar_pais(paises):
    """Busca un país por nombre y lo elimina de la lista y del CSV
    después de solicitar confirmación."""
    print("\n----- ELIMINAR PAÍS -----")

    nombre_busqueda = input("Ingrese el nombre exacto del país a eliminar: ").strip()
    if not nombre_busqueda:
        print("Error: debe ingresar un nombre.")
        return

    # Buscar el país en la lista
    indice = None
    for i, p in enumerate(paises):
        if normalizar_texto(p["nombre"]) == normalizar_texto(nombre_busqueda):
            indice = i
            break

    if indice is None:
        print(f"No se encontró ningún país con el nombre '{nombre_busqueda}'.")
        return

    pais = paises[indice]
    print(f"\nPaís a eliminar: {pais['nombre']} | Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km²")
    
    # Confirmar eliminación
    confirmacion = input("¿Está seguro de que desea eliminar este país? (s/n): ").lower()
    if confirmacion != "s":
        print("Eliminación cancelada.")
        return

    nombre_eliminado = paises[indice]["nombre"]
    paises.pop(indice)
    guardar_paises(paises)
    print(f"País '{nombre_eliminado}' eliminado correctamente.")

# ───────────────────────────────────────────────────────────────────────────

# Main con menú de opciones
def main():
    paises = cargar_paises()
    print(f"Operación realizada con éxito. Se cargaron {len(paises)} países desde el CSV.")

    while True:
        print("\n----- MENÚ DE OPCIONES -----")
        print("1.  Mostrar todos los países")
        print("2.  Filtrar por continente")
        print("3.  Filtrar por rango de población")
        print("4.  Filtrar por rango de superficie")
        print("5.  Ordenar por nombre")
        print("6.  Ordenar por población")
        print("7.  Ordenar por superficie")
        print("8.  Ver estadísticas generales")
        print("9.  Contar países por continente")
        print("10. Agregar un país")
        print("11. Actualizar datos de un país")
        print("12. Buscar país por nombre")
        print("13. Eliminar un país")
        print("0.  Salir")

        opcion = input("\nIngrese opción: ").strip()

        if opcion == "0":
            print("¡Hasta luego!")
            break
        
        elif opcion == "1":
            mostrar_paises(paises)
        
        elif opcion == "2":
            continente = input("Ingrese el continente: ").strip()
            resultado = filtrar_por_continente(paises, continente)
            mostrar_paises(resultado)
        
        elif opcion == "3":
            try:
                pop_min = limpiar_numero(input("Ingrese población mínima: "))
                pop_max = limpiar_numero(input("Ingrese población máxima: "))
                resultado = filtrar_por_poblacion(paises, pop_min, pop_max)
                mostrar_paises(resultado)
            except ValueError:
                print("Error: Ingrese números válidos.")
        
        elif opcion == "4":
            try:
                sup_min = limpiar_numero(input("Ingrese superficie mínima (km²): "))
                sup_max = limpiar_numero(input("Ingrese superficie máxima (km²): "))
                resultado = filtrar_por_superficie(paises, sup_min, sup_max)
                mostrar_paises(resultado)
            except ValueError:
                print("Error: Ingrese números válidos.")
        
        elif opcion == "5":
            descendente = input("¿Orden descendente? (s/n): ").lower() == "s"
            resultado = ordenar_por_nombre(paises, descendente)
            mostrar_paises(resultado)
        
        elif opcion == "6":
            descendente = input("¿Orden descendente? (s/n): ").lower() == "s"
            resultado = ordenar_por_poblacion(paises, descendente)
            mostrar_paises(resultado)
        
        elif opcion == "7":
            descendente = input("¿Orden descendente? (s/n): ").lower() == "s"
            resultado = ordenar_por_superficie(paises, descendente)
            mostrar_paises(resultado)
        
        elif opcion == "8":
            obtener_estadisticas(paises)
        
        elif opcion == "9":
            contar_paises_por_continente(paises)

        elif opcion == "10":
            agregar_pais(paises)

        elif opcion == "11":
            actualizar_pais(paises)

        elif opcion == "12":
            buscar_por_nombre(paises)

        elif opcion == "13":
            eliminar_pais(paises)
        
        else:
            print("Opción no válida. Intente de nuevo.")

# Inicio de la ejecución
main()
