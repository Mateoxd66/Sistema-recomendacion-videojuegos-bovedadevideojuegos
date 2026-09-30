# BOVEDA DE VIDEOJUEGOS

## Sobre el proyecto

En esta versión del proyecto presentamos un sistema de búsqueda y recomendación de videojuegos.

El sistema permite:

* Buscar videojuegos por título.
* Consultar información de los videojuegos.
* Recibir recomendaciones según el género.
* Ver un Top 10 según el rating.
* Realizar búsquedas utilizando un árbol binario de búsqueda.
* Comparar la búsqueda en árbol con la búsqueda secuencial.
* Realizar recorridos Inorder, Preorder y Postorder.
* Ejecutar pruebas de rendimiento con diferentes cantidades de elementos.

En esta versión se incorporó un **árbol binario de búsqueda (ABB)** como nueva estructura de datos para mejorar la búsqueda de videojuegos por título.

## Requisitos

* Python 3.13
* Pandas

## Cómo ejecutar el programa

1. Descargar o clonar el proyecto.
2. Abrir la carpeta del proyecto.
3. Instalar Pandas:

```bash
pip install pandas
```

4. Ejecutar el archivo principal:

```bash
python main.py
```

## Cómo utilizar el programa

Al iniciar el programa aparecerá un menú con las siguientes opciones:

### 1. Buscar un videojuego

Permite ingresar el título de un videojuego y consultar su información:

* Título
* Fecha de lanzamiento
* Rating
* Géneros

La búsqueda se realiza utilizando el **árbol binario de búsqueda**.

El árbol utiliza como clave de ordenamiento el **título del videojuego**. Los títulos menores al nodo actual se almacenan en el subárbol izquierdo y los mayores o iguales en el subárbol derecho.

### 2. Recomendar por género

Permite ingresar un género y muestra hasta 5 videojuegos recomendados, ordenados según su rating.

### 3. Ver Top 10

Muestra los 10 videojuegos con mayor rating dentro del dataset.

### 4. Comparar búsquedas

Permite comparar dos estrategias para buscar un videojuego por título:

* Búsqueda secuencial.
* Búsqueda mediante árbol binario.

Se muestra el tiempo de ejecución de cada estrategia en milisegundos.

La búsqueda secuencial tiene una complejidad temporal de **Θ(n)**.

En un árbol binario balanceado, la búsqueda tiene una complejidad de **Θ(log n)**. Sin embargo, en el peor caso un árbol binario puede quedar desbalanceado y alcanzar una complejidad de **Θ(n)**.

### 5. Recorrido Inorder

Realiza un recorrido **Inorder** del árbol.

El recorrido visita:

1. Subárbol izquierdo.
2. Nodo actual.
3. Subárbol derecho.

Como el árbol está ordenado por título, este recorrido permite visualizar los videojuegos en orden alfabético.

### 6. Recorrido Preorder

Realiza un recorrido **Preorder** del árbol.

El recorrido visita:

1. Nodo actual.
2. Subárbol izquierdo.
3. Subárbol derecho.

### 7. Recorrido Postorder

Realiza un recorrido **Postorder** del árbol.

El recorrido visita:

1. Subárbol izquierdo.
2. Subárbol derecho.
3. Nodo actual.

### 8. Pruebas de rendimiento

Realiza pruebas para comparar el comportamiento de la búsqueda secuencial y la búsqueda mediante árbol utilizando diferentes cantidades de elementos.

Las pruebas se realizan con:

* 100 elementos.
* 1.000 elementos.
* 10.000 elementos.
* 100.000 elementos.

Los resultados se muestran en milisegundos para observar cómo varía el tiempo de búsqueda a medida que aumenta la cantidad de datos.

### 9. Salir

Cierra el programa.

## Árbol Binario de Búsqueda

El árbol binario se implementó utilizando el título del videojuego como clave de ordenamiento.

La estructura general es:

```text
                 Título
                /      \
        títulos menores  títulos mayores
```

Cada nodo contiene la información completa de un videojuego y referencias a sus hijos izquierdo y derecho.

El árbol cuenta con las siguientes operaciones:

* Inserción.
* Búsqueda.
* Recorrido Inorder.
* Recorrido Preorder.
* Recorrido Postorder.

El árbol no funciona como una estructura aislada, sino que está integrado a la funcionalidad principal de búsqueda de videojuegos.

## Comparación de estrategias

Para evaluar las estrategias de búsqueda se comparan:

### Búsqueda secuencial

Recorre los elementos del dataset hasta encontrar el videojuego buscado.

Complejidad:

```text
Θ(n)
```

### Búsqueda en árbol

Compara el título buscado con el nodo actual y continúa por el subárbol izquierdo o derecho según corresponda.

Complejidad en un árbol balanceado:

```text
Θ(log n)
```

Peor caso de un árbol desbalanceado:

```text
Θ(n)
```

Las pruebas de rendimiento permiten observar experimentalmente cómo se comportan ambas estrategias frente a diferentes tamaños de entrada.

## Dataset

El programa utiliza un archivo CSV llamado `games.csv` con información de videojuegos.

Entre los datos utilizados se encuentran:

* Título.
* Fecha de lanzamiento.
* Géneros.
* Rating.

## Archivos principales

```text
main.py
Tpintegrador.py
games.csv
README.md
```

### main.py

Contiene el menú principal y permite al usuario interactuar con las diferentes funcionalidades del sistema.

### Tpintegrador.py

Contiene:

* La clase `Videojuegos`.
* La clase `Nodo`.
* La clase `ArbolBinario`.
* Las operaciones del árbol.
* Las búsquedas.
* Las recomendaciones.
* El Top 10.
* Las pruebas de rendimiento.

### games.csv

Contiene el dataset utilizado por el programa.

Complejidad
Operación	Complejidad
Búsqueda secuencial	Θ(n)
Búsqueda en árbol balanceado	Θ(log n)
Búsqueda en árbol desbalanceado, peor caso	Θ(n)
Inserción en árbol balanceado	Θ(log n)
Inserción en árbol desbalanceado, peor caso	Θ(n)
Recorridos del árbol	Θ(n)
Integrantes
Mateo Esquef
Francisco Storino
Dylan Stellato
