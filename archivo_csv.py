import csv
import os

ARCHIVO_CSV = "paises.csv"

def cargar_paises():
    """Lee el archivo CSV y retorna una lista de diccionarios con los países"""
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
