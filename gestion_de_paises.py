# Se importa el módulo csv y os
import csv
import os

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

# Main con menú de opciones
def main():
    paises = cargar_paises()
    print(f"Operación realizada con éxito. Se cargaron {len(paises)} países desde el CSV.")

    while True:
        print("----- MENÚ DE OPCIONES -----")
        print("1. Salir")

        opcion = input("Ingrese opción: ").strip()

        if opcion == "1":
            break

# Inicio de la ejecución
main()
