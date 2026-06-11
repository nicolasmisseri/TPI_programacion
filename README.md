# 🌍 Gestión de Datos de Países

Sistema de consola desarrollado en Python para gestionar información de países del mundo. Permite cargar datos desde un archivo CSV y realizar búsquedas, filtros, ordenamientos y estadísticas.

Trabajo Práctico Integrador — Programación 1 | Tecnicatura Universitaria en Programación — UTN

---

## 📋 Descripción

La aplicación lee un archivo `paises.csv` con información de países (nombre, población, superficie y continente) y ofrece un menú interactivo con 13 opciones para consultar y administrar los datos. Todos los cambios (agregar, actualizar o eliminar países) se guardan automáticamente en el CSV.

---

## 🗂️ Estructura del proyecto

```
📁 proyecto/
├── paises.py       # Código fuente principal
├── paises.csv      # Dataset de países
└── README.md       # Este archivo
```

---

## 📄 Formato del CSV

El archivo `paises.csv` debe tener el siguiente encabezado y formato:

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Brasil,213993437,8515767,América
Alemania,83149300,357022,Europa
```

> Los campos `poblacion` y `superficie` deben ser números enteros. No se permiten campos vacíos.

---

## ▶️ Cómo ejecutar

1. Asegurarse de tener **Python 3** instalado.
2. Colocar el archivo `paises.csv` en la misma carpeta que `paises.py`.
3. Ejecutar desde la terminal:

```bash
python paises.py
```

---

## 🧭 Menú de opciones

Al iniciar el programa se mostrará el siguiente menú:

```
----- MENÚ DE OPCIONES -----
1.  Mostrar todos los países
2.  Filtrar por continente
3.  Filtrar por rango de población
4.  Filtrar por rango de superficie
5.  Ordenar por nombre
6.  Ordenar por población
7.  Ordenar por superficie
8.  Ver estadísticas generales
9.  Contar países por continente
10. Agregar un país
11. Actualizar datos de un país
12. Buscar país por nombre
13. Eliminar un país
0.  Salir
```

---

## 💡 Ejemplos de uso

### Filtrar por continente
```
Ingrese opción: 2
Ingrese el continente: América

Nombre                     Población       Superficie  Continente
---------------------------------------------------------------------------
Argentina                 45,376,763        2,780,400  América
Brasil                   213,993,437        8,515,767  América
```

### Buscar país por nombre (coincidencia parcial)
```
Ingrese opción: 12
Ingrese el nombre (o parte del nombre) a buscar: al

Se encontraron 1 resultado(s):
Nombre                     Población       Superficie  Continente
---------------------------------------------------------------------------
Alemania                  83,149,300          357,022  Europa
```

### Agregar un país
```
Ingrese opción: 10
Nombre del país: Chile
Población: 19500000
Superficie (km²): 756102
Continente: América
Cambios guardados correctamente en el CSV.
País 'Chile' agregado exitosamente.
```

### Estadísticas generales
```
Ingrese opción: 8

----- ESTADÍSTICAS GENERALES -----
País con mayor población: Brasil (213,993,437)
País con menor población: Alemania (83,149,300)
Promedio de población: 116,879,875
Promedio de superficie: 3,007,791 km²
```

---

## ✅ Validaciones

- No se permiten campos vacíos al agregar un país.
- No se puede agregar un país con un nombre ya existente.
- Los valores de población y superficie deben ser números enteros positivos.
- Los números pueden ingresarse con puntos o comas como separadores de miles (ej: `1.000.000` o `1,000,000`).
- Si un filtro no encuentra resultados, se muestra un mensaje informativo.
- Los errores de formato en el CSV son reportados como advertencias sin interrumpir la ejecución.

---

## 🧩 Conceptos aplicados

| Concepto | Uso en el proyecto |
|---|---|
| Listas | Almacenamiento de los países en memoria |
| Diccionarios | Representación de cada país con sus atributos |
| Funciones | Una función por cada responsabilidad del sistema |
| Condicionales | Validaciones de entrada y selección del menú |
| Estructuras repetitivas | Recorrido de listas, menú principal, validaciones en bucle |
| Archivos CSV | Lectura y escritura persistente de datos |
| Ordenamiento | Bubble sort implementado manualmente (nombre, población, superficie) |
| Estadísticas | Cálculo de promedios, máximos y mínimos recorriendo la lista |

---

## 👥 Integrantes

| Nombre |
|---|
| Camila Tosti | 00000 |
| Nicolas Misseri | 00000 |

---

## 🔗 Enlaces

- 📁 Repositorio: [https://github.com/nicolasmisseri/TPI_programacion](#)
- 🎥 Video demostración: [[Ver Video](https://drive.google.com/file/d/1cPKmf1jJZrA5rpEl8F0_VurNqiZWerNs/view)]
- 📄 Documentación PDF: [[Ver documento](https://drive.google.com/file/d/1NTIc3Oubpzm6VIJzzXbuSzhHPZ9SbjCq/view?usp=sharing)]
