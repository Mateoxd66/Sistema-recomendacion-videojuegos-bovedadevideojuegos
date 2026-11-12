# Bóveda de Videojuegos

Sistema de búsqueda, organización y recomendación de videojuegos desarrollado en Python.

## Funcionalidades

- Búsqueda de videojuegos por título.
- Consulta de información de cada videojuego.
- Recomendaciones por género.
- TOP 10 según valoración.
- TOP 5 mediante una cola de prioridad implementada con Heap.
- Búsqueda y organización mediante ABB y AVL.
- Recorridos Inorder, Preorder y Postorder.
- Organización de categorías mediante un árbol general.
- Comparación de búsquedas y alturas entre ABB y AVL.
- Pruebas de rendimiento con diferentes cantidades de elementos.
- Exploración de videojuegos relacionados mediante un grafo no dirigido.

## Tecnologías

- Python 3.
- Pandas.

## Instalación y ejecución

1. Instalar Pandas:

   ```bash
   pip install pandas
   ```

2. Colocar `games.csv`, `main.py` y `Tpintegrador.py` en la misma carpeta.
3. Ejecutar:

   ```bash
   python main.py
   ```

## Estructuras de datos

### ABB y AVL

Se utilizan para almacenar y buscar videojuegos por título. También permiten realizar recorridos y comparar alturas y tiempos de búsqueda.

### Árbol general

Organiza categorías de videojuegos, como géneros, décadas de lanzamiento y rangos de valoración.

### TP6 - Heap (cola de prioridad)

Se implementó un Heap máximo manual. Cada videojuego se ordena según su valoración (`Rating`): cuanto mayor es la valoración, mayor es su prioridad. El Heap se construye a partir de los videojuegos que tienen una valoración numérica y permite obtener los cinco videojuegos con mayor puntuación.

- Construcción del Heap: O(n), mediante el método de construcción desde abajo.
- Extracción de un máximo: O(log n).
- Obtención del TOP 5: hasta cinco extracciones, O(5 log n).

La consulta del TOP 5 utiliza una copia de la estructura para que se pueda volver a consultar sin vaciar el Heap original.

### TP7 - Grafo no dirigido

Se implementó un grafo no dirigido mediante listas de adyacencia. Para evitar crear una cantidad enorme de conexiones repetidas entre videojuegos que comparten géneros muy amplios, se utiliza una representación bipartita:

- Hay nodos de tipo videojuego.
- Hay nodos de tipo género.
- Hay nodos de tipo desarrollador.
- Cada videojuego se conecta con sus nodos de género y desarrollador.
- Cada conexión se guarda en ambos sentidos, por lo que el grafo es no dirigido.

Dos videojuegos están relacionados cuando comparten al menos un nodo de género o de desarrollador. Al consultar un título, el programa muestra primero los relacionados por desarrollador y después los relacionados por género, evitando repetir títulos y mostrando hasta diez de cada grupo.

Esta representación conserva las relaciones del conjunto de datos sin tener que generar todas las conexiones directas entre cada par de videojuegos de un mismo género, lo que podría consumir mucha memoria.

## Archivos

- `main.py`: menú principal del programa.
- `Tpintegrador.py`: clases, estructuras de datos y funcionalidades.
- `games.csv`: conjunto de datos de videojuegos.
- `README.md`: documentación del proyecto.

## Integrantes - Grupo 18

- Mateo Esquef
- Francisco Storino
- Dylan Stellato
