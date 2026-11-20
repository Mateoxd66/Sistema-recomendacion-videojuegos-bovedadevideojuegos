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
- Recorridos BFS y DFS sobre el grafo para responder consultas de cercanía y exploración en profundidad.

## Tecnologías

- Python 3.
- Pandas.

## Instalación y ejecución

1. Instalar Pandas:

   ```bash
   pip install pandas
Colocar games.csv, main.py y Tpintegrador.py en la misma carpeta.

Ejecutar:

Bash
python main.py

## Estructuras de datos
ABB y AVL
Se utilizan para almacenar y buscar videojuegos por título. También permiten realizar recorridos y comparar alturas y tiempos de búsqueda.

Árbol general
Organiza categorías de videojuegos, como géneros, décadas de lanzamiento y rangos de valoración.

Heap (cola de prioridad)
Se implementó un Heap máximo manual. Cada videojuego se ordena según su valoración (Rating): cuanto mayor es la valoración, mayor es su prioridad. El Heap se construye a partir de los videojuegos que tienen una valoración numérica y permite obtener los cinco videojuegos con mayor puntuación.

Construcción del Heap: O(n), mediante el método de construcción desde abajo.

Extracción de un máximo: O(log n).

Obtención del TOP 5: hasta cinco extracciones, O(5 log n).

La consulta del TOP 5 utiliza una copia de la estructura para que se pueda volver a consultar sin vaciar el Heap original.

Grafo no dirigido (BFS y DFS - Versión 6)
Se implementó un grafo no dirigido mediante listas de adyacencia. Para evitar crear una cantidad enorme de conexiones repetidas entre videojuegos que comparten géneros muy amplios, se utiliza una representación bipartita:

Hay nodos de tipo videojuego.

Hay nodos de tipo género.

Hay nodos de tipo desarrollador.

Cada videojuego se conecta con sus nodos de género y desarrollador.

Cada conexión se guarda en ambos sentidos, por lo que el grafo es no dirigido.

Dos videojuegos están relacionados cuando comparten al menos un nodo de género o de desarrollador. Al consultar un título, el programa muestra primero los relacionados por desarrollador y después los relacionados por género, evitando repetir títulos y mostrando hasta diez de cada grupo.

Esta representación conserva las relaciones del conjunto de datos sin tener que generar todas las conexiones directas entre cada par de videojuegos de un mismo género, lo que podría consumir mucha memoria.

Recorridos BFS y DFS
Se incorporaron recorridos BFS (búsqueda en anchura) y DFS (búsqueda en profundidad) sobre el grafo bipartito:

BFS: explora el grafo nivel por nivel usando una cola. Es ideal para encontrar la conexión más cercana (menor cantidad de aristas/saltos) desde un videojuego inicial.

Caso de uso (BFS): "¿Cuál es el videojuego relacionado más cercano a un título dado?" (encuentra el camino más corto en cantidad de conexiones a través de atributos compartidos).

DFS: explora una rama lo más profundo posible antes de retroceder (usando recursión o pila). Es útil para recorrer cadenas de relaciones y explorar subcomponentes conectadas del catálogo.

Caso de uso (DFS): "Explorar en profundidad todos los videojuegos alcanzables desde un título dado a través de las relaciones del grafo."

Análisis de complejidad y diferencias (BFS vs. DFS)
Complejidad temporal: O(V + E) en ambos algoritmos, donde V es la cantidad de nodos (videojuegos, géneros y desarrolladores) y E es la cantidad de aristas en la lista de adyacencia.

Complejidad espacial: O(V) en el peor caso en ambos recorridos para almacenar los nodos visitados y la estructura auxiliar (cola en BFS; pila de llamadas o pila explícita en DFS).

## Diferencias clave:

Orden de exploración: BFS avanza por capas/distancia en aristas; DFS profundiza primero por una rama antes de abrir otras.

Cuándo conviene cada uno: conviene BFS cuando importa la cercanía o el camino mínimo en saltos; conviene DFS cuando se busca explorar exhaustivamente una rama/componente o detectar rutas profundas.

## Archivos
main.py: menú principal del programa.

Tpintegrador.py: clases, estructuras de datos y funcionalidades.

games.csv: conjunto de datos de videojuegos.

README.md: documentación del proyecto.

## Integrantes - Grupo 18
Mateo Esquef

Francisco Storino

Dylan Stellato
