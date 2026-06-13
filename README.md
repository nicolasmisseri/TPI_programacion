# Gestión de datos de países

Aplicación de consola desarrollada en Python para administrar información de países a partir de un archivo CSV. Permite consultar, filtrar, ordenar y modificar los registros de forma interactiva, guardando los cambios directamente en el archivo de datos.

Trabajo Práctico Integrador - Programación 1, Tecnicatura Universitaria en Programación, UTN.

## Qué hace

El programa carga `paises.csv` al iniciar y muestra un menú con opciones para:

- listar todos los países
- filtrar por continente, población o superficie
- ordenar por nombre, población o superficie
- ver estadísticas generales
- contar países por continente
- agregar, actualizar, buscar y eliminar países

La lógica está separada por responsabilidades en distintos módulos, lo que hace que el proyecto sea más fácil de mantener y de extender.

## Estructura del proyecto

```
TPI_programacion/
├── archivo_csv.py
├── estadisticas.py
├── filtros.py
├── main.py
├── operaciones.py
├── ordenamiento.py
├── paises.csv
├── README.md
└── utils.py
```

## Archivos principales

- `main.py`: punto de entrada del programa y menú principal.
- `archivo_csv.py`: lectura y guardado del archivo CSV.
- `filtros.py`: búsquedas por continente y rangos numéricos.
- `ordenamiento.py`: ordenamiento por nombre, población y superficie.
- `estadisticas.py`: cálculo de promedios, máximos, mínimos y conteos.
- `operaciones.py`: alta, edición, búsqueda y eliminación de países.
- `utils.py`: funciones auxiliares para normalizar texto, limpiar números y mostrar tablas.

## Requisitos

- Python 3
- El archivo `paises.csv` en la misma carpeta que `main.py`

## Cómo ejecutar

Desde la carpeta del proyecto:

```bash
python main.py
```

## Formato del CSV

El archivo debe tener estas columnas:

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

`poblacion` y `superficie` deben ser números enteros. Las filas incompletas o inválidas se informan como advertencias al cargar el archivo.

## Uso general

Al iniciar, la aplicación muestra un menú numerado. Cada opción pide los datos necesarios por consola y luego imprime los resultados en una tabla legible. Las operaciones de alta, actualización y eliminación se guardan automáticamente en el CSV.

## Validaciones implementadas

- No se permiten nombres vacíos.
- No se puede agregar un país duplicado.
- La población y la superficie deben ser valores numéricos válidos.
- Se aceptan puntos y comas como separadores de miles al ingresar números.
- Si una búsqueda o filtro no encuentra resultados, el programa muestra un mensaje informativo.

## Conceptos aplicados

- listas y diccionarios para representar los países
- funciones separadas por responsabilidad
- estructuras condicionales y repetitivas para el menú y las validaciones
- lectura y escritura de archivos CSV
- ordenamiento manual con bubble sort
- cálculo de estadísticas sobre colecciones

## Integrantes

- Camila Tosti
- Nicolas Misseri

## Recursos

- [Marco teórico del proyecto](https://drive.google.com/file/d/1NTIc3Oubpzm6VIJzzXbuSzhHPZ9SbjCq/view)
- [Video explicativo del proyecto](https://drive.google.com/file/d/1SmcOwr1XhP8_SptPo3m5c3tgD43te3Gj/view)
