# Módulo principal: punto de entrada del programa
# Importaciones de cada módulo según su responsabilidad
from archivo_csv import cargar_paises
from utils import mostrar_paises, limpiar_numero
from filtros import filtrar_por_continente, filtrar_por_poblacion, filtrar_por_superficie
from ordenamiento import ordenar_por_nombre, ordenar_por_poblacion, ordenar_por_superficie
from estadisticas import obtener_estadisticas, contar_paises_por_continente
from operaciones import agregar_pais, actualizar_pais, buscar_por_nombre, eliminar_pais


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
            descendente = input("¿Orden descendente? (s/n): ").strip().lower() == "s"
            resultado = ordenar_por_nombre(paises, descendente)
            mostrar_paises(resultado)

        elif opcion == "6":
            descendente = input("¿Orden descendente? (s/n): ").strip().lower() == "s"
            resultado = ordenar_por_poblacion(paises, descendente)
            mostrar_paises(resultado)

        elif opcion == "7":
            descendente = input("¿Orden descendente? (s/n): ").strip().lower() == "s"
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
