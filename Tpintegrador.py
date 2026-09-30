import pandas as pd
import time


# =========================
# NODO DEL ÁRBOL
# =========================

class Nodo:
    def __init__(self, juego):
        self.juego = juego
        self.izquierda = None
        self.derecha = None


# =========================
# ÁRBOL BINARIO DE BÚSQUEDA
# =========================

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # Inserción ordenada por Título
    def insertar(self, juego):

        nuevo = Nodo(juego)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz

        while True:

            if juego["Title"].lower() < actual.juego["Title"].lower():

                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    return

                actual = actual.izquierda

            else:

                if actual.derecha is None:
                    actual.derecha = nuevo
                    return

                actual = actual.derecha

    # Búsqueda por título
    def buscar(self, titulo):

        actual = self.raiz
        titulo = titulo.lower()

        while actual is not None:

            titulo_actual = actual.juego["Title"].lower()

            if titulo == titulo_actual:
                return actual.juego

            elif titulo < titulo_actual:
                actual = actual.izquierda

            else:
                actual = actual.derecha

        return None

    # Recorrido Inorder
    def inorder(self, nodo):

        if nodo is not None:
            self.inorder(nodo.izquierda)
            print(nodo.juego["Title"])
            self.inorder(nodo.derecha)

    # Recorrido Preorder
    def preorder(self, nodo):

        if nodo is not None:
            print(nodo.juego["Title"])
            self.preorder(nodo.izquierda)
            self.preorder(nodo.derecha)

    # Recorrido Postorder
    def postorder(self, nodo):

        if nodo is not None:
            self.postorder(nodo.izquierda)
            self.postorder(nodo.derecha)
            print(nodo.juego["Title"])


# =========================
# CLASE VIDEOJUEGOS
# =========================

class Videojuegos:

    def __init__(self):

        self.datos = pd.read_csv("games.csv")

        # Crear árbol
        self.arbol = ArbolBinario()

        # Insertar todos los videojuegos en el árbol
        for _, juego in self.datos.iterrows():
            self.arbol.insertar(juego)

    # =========================
    # BÚSQUEDA CON ÁRBOL
    # =========================

    def Info_juegos(self, Title):

        juego = self.arbol.buscar(Title)

        if juego is not None:

            print("Titulo:", juego["Title"])
            print("Fecha de salida:", juego["Release_Date"])
            print("Rating:", juego["Rating"])
            print("Genero:", juego["Genres"])

        else:
            print("Videojuego no encontrado")

    # =========================
    # BÚSQUEDA SECUENCIAL
    # =========================

    def busqueda_secuencial(self, Title):

        juego = self.datos[self.datos["Title"].str.lower() == Title.lower()]

        if not juego.empty:
            return juego.iloc[0]

        return None

    # =========================
    # TOP 10
    # =========================

    def top_10(self):

        top = self.datos.sort_values("Rating", ascending=False).head(10)

        top = top.drop_duplicates("Title").head(10)

        for _, juego in top.iterrows():
            print(juego["Title"], "-", juego["Rating"])

    # =========================
    # RECOMENDACIONES
    # =========================

    def recomendar(self, genero):

        juegos = self.datos[
            self.datos["Genres"].str.contains(
                "'" + genero + "'",
                case=False,
                na=False
            )
        ]

        juegos = juegos.sort_values("Rating", ascending=False)

        juegos = juegos.drop_duplicates("Title").head(5)

        print("Juegos recomendados:")

        for _, juego in juegos.iterrows():
            print(juego["Title"], "-", juego["Rating"])

    # =========================
    # COMPARACIÓN DE BÚSQUEDAS
    # =========================

    def comparar_busquedas(self, Title):

        # -------------------------
        # BÚSQUEDA SECUENCIAL
        # -------------------------

        inicio = time.perf_counter()

        juego_secuencial = self.busqueda_secuencial(Title)

        fin = time.perf_counter()

        tiempo_secuencial = (fin - inicio) * 1000


        # -------------------------
        # BÚSQUEDA EN ÁRBOL
        # -------------------------

        inicio = time.perf_counter()

        juego_arbol = self.arbol.buscar(Title)

        fin = time.perf_counter()

        tiempo_arbol = (fin - inicio) * 1000


        print("\n===============================================")
        print("       COMPARACIÓN DE ESTRATEGIAS")
        print("===============================================")

        print("Videojuego buscado:", Title)

        print("\nBúsqueda secuencial:")
        print("Tiempo:", tiempo_secuencial, "ms")

        print("\nBúsqueda en árbol:")
        print("Tiempo:", tiempo_arbol, "ms")

        print("\nComplejidad teórica:")

        print("Búsqueda secuencial: O(n)")
        print("Búsqueda en árbol balanceado: O(log n)")
        print("Peor caso de un árbol no balanceado: O(n)")


    # =========================
    # RECORRIDOS DEL ÁRBOL
    # =========================

    def mostrar_inorder(self):

        print("\nRecorrido INORDER:")
        self.arbol.inorder(self.arbol.raiz)

    def mostrar_preorder(self):

        print("\nRecorrido PREORDER:")
        self.arbol.preorder(self.arbol.raiz)

    def mostrar_postorder(self):

        print("\nRecorrido POSTORDER:")
        self.arbol.postorder(self.arbol.raiz)

    
    
    
    
    
    
    
    def pruebas_rendimiento(self):

        tamaños = [100, 1000, 10000, 100000]

        print("\n===============================================")
        print("          PRUEBA DE RENDIMIENTO")
        print("===============================================")

        print("\nN elementos | Secuencial | Árbol")
        print("-----------------------------------------------")

        for tamaño in tamaños:

            datos_prueba = self.datos.head(tamaño)

            if datos_prueba.empty:
                continue

            titulo = datos_prueba.iloc[-1]["Title"]

            # Búsqueda secuencial
            inicio = time.perf_counter()

            self.busqueda_secuencial(titulo)

            fin = time.perf_counter()

            tiempo_secuencial = (fin - inicio) * 1000


            # Crear árbol para este tamaño
            arbol_prueba = ArbolBinario()

            for _, juego in datos_prueba.iterrows():
                arbol_prueba.insertar(juego)


            # Búsqueda en árbol
            inicio = time.perf_counter()

            arbol_prueba.buscar(titulo)

            fin = time.perf_counter()

            tiempo_arbol = (fin - inicio) * 1000


            print(
                tamaño,
                " | ",
                round(tiempo_secuencial, 4),
                "ms | ",
                round(tiempo_arbol, 4),
                "ms"
            )