# BOVEDA DE VIDEOJUEGOS

## Sobre el proyecto

En esta demo presentamos un sistema de recomendación y búsqueda de videojuegos. Permite buscar juegos, consultar su información, recibir recomendaciones según el género y ver un Top 10 según el rating. Además, se incorporaron dos métodos de búsqueda para comparar sus tiempos de ejecución.

## Requisitos

* Python 3.13
* Pandas

## Como ejecutar el programa

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

## Como utilizar el programa

Al iniciar el programa aparecerá un menú con las siguientes opciones:

### 1. Buscar un videojuego (Búsqueda Secuencial)

Permite ingresar el título de un videojuego y consultar su información:

* Título
* Fecha de lanzamiento
* Rating
* Géneros

La búsqueda se realiza recorriendo los datos de forma secuencial.

### 2. Buscar un videojuego (Búsqueda en Árbol / Índice)

Permite buscar un videojuego utilizando un índice ordenado por título. También muestra su información:

* Título
* Fecha de lanzamiento
* Rating
* Géneros

Esta opción permite comparar la búsqueda mediante índice con la búsqueda secuencial.

### 3. Recomendar por género

Permite ingresar un género y muestra hasta 5 videojuegos recomendados, ordenados según su rating.

### 4. Ver Top 10

Muestra los 10 videojuegos con mayor rating dentro del dataset.

### 5. Ejecutar experimento de complejidad

Realiza mediciones de tiempo para comparar la búsqueda secuencial con la búsqueda mediante índice utilizando diferentes cantidades de elementos: 1.000, 10.000 y 100.000.

Los resultados se muestran en milisegundos para observar cómo cambia el tiempo de búsqueda según el tamaño de los datos.

### 6. Salir

Cierra el programa.

## Dataset

El programa utiliza un archivo CSV con información de videojuegos, incluyendo datos como título, fecha de lanzamiento, género y rating.

## Integrantes

* Mateo Esquef
* Francisco Storino
* Dylan Stellato
