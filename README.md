# BÓVEDA DE VIDEOJUEGOS

## Sobre el proyecto

En esta demo presentamos las funciones principales de nuestro sistema de consulta e información de videojuegos:
- Buscar juegos y consultar su información detallada.
- Recibir recomendaciones según géneros.
- Ver un Top 10 según rating.
- **Análisis de Complejidad y Medición de Tiempos:** Módulo experimental que compara el rendimiento de la búsqueda secuencial frente a la búsqueda indexada/en árbol con distintos volúmenes de datos ($1.000$, $10.000$ y $100.000$ elementos).

El objetivo es ayudar a los jugadores a encontrar nuevos títulos y demostrar la eficiencia algorítmica al escalar la base de datos.

---

## Requisitos

- Python 3.10+ (probado en Python 3.13)
- Pandas

---

## Cómo ejecutar el programa

1. Descargar o clonar este repositorio desde GitHub.
2. Abrir la carpeta del proyecto en la terminal o IDE.
3. Instalar Pandas:
   ```bash
   pip install pandas
Ejecutar el archivo principal:

Bash
python main.py
Cómo utilizar el programa
Al iniciar el programa aparecerá un menú interactivo con las siguientes opciones:

Buscar un videojuego (Búsqueda Secuencial): Consulta un juego recorriendo el dataset elemento por elemento (O(n)).

Buscar un videojuego (Búsqueda en Árbol / Índice): Consulta un juego mediante un índice ordenado que descarta mitades en cada paso (O(logn)).

Recomendar por género: Ingresa un género y muestra hasta 5 videojuegos recomendados ordenados por rating.

Ver Top 10: Muestra los 10 videojuegos con mayor rating dentro del dataset.

Ejecutar experimento de complejidad (Tiempos): Corre las pruebas de rendimiento comparando ambas estrategias sobre 1.000, 10.000 y 100.000 registros e imprime la tabla de tiempos en milisegundos.

Salir: Cierra el programa.

Dataset
El programa utiliza un archivo CSV (games.csv) que contiene información sobre videojuegos con los siguientes campos principales:

Title (Título)

Release Date (Fecha de lanzamiento)

Rating (Puntuación)

Genres (Géneros)

Developers, Platforms, entre otros.

Análisis de Complejidad
Estrategia	Notación Peor Caso	Descripción
Búsqueda Secuencial	O(n)/Θ(n)	Filtrado directo por fila. Su tiempo crece de forma estrictamente lineal a medida que aumenta el volumen de datos.
Búsqueda en Árbol / Índice	O(logn)/Θ(logn)	Búsqueda logarítmica sobre el índice ordenado. Mantiene un tiempo de respuesta casi constante sin importar el tamaño del dataset.
Integrantes - GRUPO 18
Mateo Esquef

Francisco Storino

Dylan Stellato
