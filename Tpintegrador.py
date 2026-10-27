import pandas as pd
import time
import random
import math


# =========================
# FUNCIONES AUXILIARES
# =========================

def normalizar(texto):
    return str(texto).strip().strip("'\"[] ").casefold()


def buscar_columna(datos, nombres):
    for columna in datos.columns:
        for nombre in nombres:
            if columna.strip().lower().replace("_", "").replace(" ", "") == nombre.lower().replace("_", "").replace(" ", ""):
                return columna
    return None


def obtener_generos(valor):
    if pd.isna(valor):
        return []

    texto = str(valor).strip()
    generos = texto.replace(";", ",").split(",")

    return list(dict.fromkeys(
        g.strip().strip("'\"[] ")
        for g in generos if g.strip().strip("'\"[] ")
    ))


def obtener_anio(valor):
    if pd.isna(valor):
        return None

    texto = str(valor)

    for i in range(len(texto) - 3):
        posible = texto[i:i + 4]

        if posible.isdigit():
            anio = int(posible)
            if 1000 <= anio <= 2099:
                return anio

    return None


def obtener_numero(valor):
    try:
        numero = float(valor)
        if math.isfinite(numero):
            return numero
    except (ValueError, TypeError):
        pass

    return None


# =========================
# ARBOL BINARIO DE BUSQUEDA
# =========================

class Nodo:
    def __init__(self, juego):
        self.juego = juego
        self.izquierdo = None
        self.derecho = None

    def clave(self):
        return normalizar(self.juego["Title"])


class ArbolBinario:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def insertar(self, juego):
        nuevo = Nodo(juego)

        if self.raiz is None:
            self.raiz = nuevo
            self.cantidad += 1
            return

        actual = self.raiz

        while True:
            clave = normalizar(juego["Title"])
            actual_clave = normalizar(actual.juego["Title"])

            if clave < actual_clave:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo
                    self.cantidad += 1
                    return
                actual = actual.izquierdo

            elif clave > actual_clave:
                if actual.derecho is None:
                    actual.derecho = nuevo
                    self.cantidad += 1
                    return
                actual = actual.derecho

            else:
                return

    def buscar(self, titulo):
        clave = normalizar(titulo)
        actual = self.raiz

        while actual is not None:
            actual_clave = normalizar(actual.juego["Title"])

            if clave == actual_clave:
                return actual.juego
            elif clave < actual_clave:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return None

    def altura(self):
        if self.raiz is None:
            return 0

        pendientes = [(self.raiz, 1)]
        mayor = 0

        while pendientes:
            nodo, nivel = pendientes.pop()
            mayor = max(mayor, nivel)

            if nodo.izquierdo:
                pendientes.append((nodo.izquierdo, nivel + 1))
            if nodo.derecho:
                pendientes.append((nodo.derecho, nivel + 1))

        return mayor

    def recorrido(self, tipo):
        resultado = []

        def recorrer(nodo):
            if nodo is None:
                return

            if tipo == "preorden":
                resultado.append(nodo.juego["Title"])

            recorrer(nodo.izquierdo)

            if tipo == "inorden":
                resultado.append(nodo.juego["Title"])

            recorrer(nodo.derecho)

            if tipo == "postorden":
                resultado.append(nodo.juego["Title"])

        recorrer(self.raiz)
        return resultado


# =========================
# ARBOL AVL
# =========================

class NodoAVL:
    def __init__(self, juego):
        self.juego = juego
        self.izquierdo = None
        self.derecho = None
        self.altura = 1


class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    def altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def actualizar(self, nodo):
        nodo.altura = 1 + max(
            self.altura(nodo.izquierdo),
            self.altura(nodo.derecho)
        )

    def balance(self, nodo):
        return self.altura(nodo.izquierdo) - self.altura(nodo.derecho)

    def rotar_derecha(self, nodo):
        nuevo = nodo.izquierdo
        nodo.izquierdo = nuevo.derecho
        nuevo.derecho = nodo

        self.actualizar(nodo)
        self.actualizar(nuevo)
        return nuevo

    def rotar_izquierda(self, nodo):
        nuevo = nodo.derecho
        nodo.derecho = nuevo.izquierdo
        nuevo.izquierdo = nodo

        self.actualizar(nodo)
        self.actualizar(nuevo)
        return nuevo

    def insertar(self, juego):
        if self.buscar(juego["Title"]) is not None:
            return

        self.raiz = self._insertar(self.raiz, juego)
        self.cantidad += 1

    def _insertar(self, nodo, juego):
        if nodo is None:
            return NodoAVL(juego)

        clave = normalizar(juego["Title"])
        actual = normalizar(nodo.juego["Title"])

        if clave < actual:
            nodo.izquierdo = self._insertar(nodo.izquierdo, juego)
        else:
            nodo.derecho = self._insertar(nodo.derecho, juego)

        self.actualizar(nodo)
        balance = self.balance(nodo)

        if balance > 1:
            if clave > normalizar(nodo.izquierdo.juego["Title"]):
                nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
            return self.rotar_derecha(nodo)

        if balance < -1:
            if clave < normalizar(nodo.derecho.juego["Title"]):
                nodo.derecho = self.rotar_derecha(nodo.derecho)
            return self.rotar_izquierda(nodo)

        return nodo

    def buscar(self, titulo):
        clave = normalizar(titulo)
        actual = self.raiz

        while actual is not None:
            actual_clave = normalizar(actual.juego["Title"])

            if clave == actual_clave:
                return actual.juego
            elif clave < actual_clave:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return None

    def obtener_altura(self):
        return self.altura(self.raiz)


# =========================
# ARBOL GENERAL DE CATEGORIAS
# =========================

class NodoGeneral:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []


class ArbolGeneral:
    def __init__(self):
        self.raiz = NodoGeneral("Videojuegos")

    def buscar(self, nombre):
        pendientes = [self.raiz]
        objetivo = normalizar(nombre)

        while pendientes:
            nodo = pendientes.pop()

            if normalizar(nodo.nombre) == objetivo:
                return nodo

            pendientes.extend(reversed(nodo.hijos))

        return None

    def agregar(self, padre, nombre):
        nombre = str(nombre).strip()
        nodo_padre = self.buscar(padre)

        if not nombre or nodo_padre is None:
            return

        for hijo in nodo_padre.hijos:
            if normalizar(hijo.nombre) == normalizar(nombre):
                return

        nodo_padre.hijos.append(NodoGeneral(nombre))

    def mostrar_hijos(self, nombre):
        nodo = self.buscar(nombre)

        if nodo is None:
            print("No se encontró esa categoría.")
            return

        print(f"\nCategoría: {nodo.nombre}")

        if not nodo.hijos:
            print("No tiene subcategorías.")
            return

        for hijo in nodo.hijos:
            print("-", hijo.nombre)

    def recorrido(self, tipo):
        resultado = []

        def recorrer(nodo):
            if tipo == "preorden":
                resultado.append(nodo.nombre)

            for hijo in nodo.hijos:
                recorrer(hijo)

            if tipo == "postorden":
                resultado.append(nodo.nombre)

        recorrer(self.raiz)
        return resultado


# =========================
# CLASE PRINCIPAL
# =========================

class Videojuegos:
    def __init__(self, archivo="games.csv"):
        try:
            self.datos = pd.read_csv(archivo, low_memory=False)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo {archivo}.")

        if self.datos.empty:
            raise ValueError("El archivo CSV está vacío.")

        self.col_titulo = buscar_columna(
            self.datos, ["title", "name", "titulo", "título"]
        )
        self.col_generos = buscar_columna(
            self.datos, ["genres", "genre", "generos", "géneros", "genero"]
        )
        self.col_rating = buscar_columna(
            self.datos, ["rating", "score", "valoracion", "valoración"]
        )
        self.col_fecha = buscar_columna(
            self.datos, ["release_date", "release date", "fecha de lanzamiento", "fecha"]
        )

        if self.col_titulo is None:
            raise ValueError("No se encontró la columna de títulos.")

        if self.col_titulo != "Title":
            self.datos.rename(columns={self.col_titulo: "Title"}, inplace=True)

        self.arbol = ArbolBinario()
        self.avl = ArbolAVL()
        self.arbol_general = ArbolGeneral()

        print("Cargando los árboles...")

        for _, fila in self.datos.iterrows():
            if pd.isna(fila["Title"]) or not str(fila["Title"]).strip():
                continue

            juego = fila.to_dict()
            self.arbol.insertar(juego)
            self.avl.insertar(juego)

        self.construir_categorias()

        print("Datos cargados correctamente.")
        print("Registros:", len(self.datos))
        print("Títulos ABB:", self.arbol.cantidad)
        print("Títulos AVL:", self.avl.cantidad)

    # =========================
    # CATEGORIAS
    # =========================

    def construir_categorias(self):
        arbol = self.arbol_general

        for categoria in ["Géneros", "Lanzamiento", "Valoraciones"]:
            arbol.agregar("Videojuegos", categoria)

        if self.col_generos is not None:
            for valor in self.datos[self.col_generos].dropna():
                for genero in obtener_generos(valor):
                    arbol.agregar("Géneros", genero)

        if self.col_fecha is not None:
            for valor in self.datos[self.col_fecha].dropna():
                anio = obtener_anio(valor)

                if anio is not None:
                    decada = (anio // 10) * 10
                    arbol.agregar("Lanzamiento", f"Década de {decada}")

        if self.col_rating is not None:
            for valor in self.datos[self.col_rating].dropna():
                numero = obtener_numero(valor)

                if numero is None:
                    continue
                elif numero < 0:
                    rango = "Menor que 0"
                elif numero < 2:
                    rango = "De 0 a menos de 2"
                elif numero < 4:
                    rango = "De 2 a menos de 4"
                elif numero < 6:
                    rango = "De 4 a menos de 6"
                elif numero < 8:
                    rango = "De 6 a menos de 8"
                elif numero <= 10:
                    rango = "De 8 a 10"
                else:
                    rango = "Mayor que 10"

                arbol.agregar("Valoraciones", rango)

    def explorar_categorias(self):
        print("\n--- ÁRBOL GENERAL ---")

        for hijo in self.arbol_general.raiz.hijos:
            print("-", hijo.nombre)

        nombre = input("\nEscribí una categoría: ").strip()
        self.arbol_general.mostrar_hijos(nombre)

    # =========================
    # INFORMACION Y BUSQUEDAS
    # =========================

    def info_juegos(self, titulo):
        coincidencias = self.datos[
            self.datos["Title"].astype(str).str.casefold()
            == str(titulo).strip().casefold()
        ]

        if coincidencias.empty:
            print("No se encontró el videojuego.")
            return

        for columna, valor in coincidencias.iloc[0].items():
            print(f"{columna}: {valor}")

    def busqueda_secuencial(self, titulo):
        objetivo = normalizar(titulo)

        for _, fila in self.datos.iterrows():
            if normalizar(fila["Title"]) == objetivo:
                return fila.to_dict()

        return None

    def buscar_en_arboles(self, titulo):
        for nombre, arbol in [("ABB", self.arbol), ("AVL", self.avl)]:
            inicio = time.perf_counter()
            resultado = arbol.buscar(titulo)
            tiempo = time.perf_counter() - inicio

            print(f"{nombre}:", resultado["Title"] if resultado else "No encontrado")
            print(f"Tiempo: {tiempo:.8f} segundos")

    # =========================
    # TOP 10 Y RECOMENDACIONES
    # =========================

    def top_10(self):
        if self.col_rating is None:
            print("No hay columna de valoraciones.")
            return

        datos = self.datos.copy()
        datos["_rating"] = pd.to_numeric(datos[self.col_rating], errors="coerce")
        datos = datos.dropna(subset=["_rating"]).sort_values(
            "_rating", ascending=False
        ).head(10)

        if datos.empty:
            print("No hay valoraciones numéricas.")
            return

        print("\n--- TOP 10 ---")

        for i, (_, fila) in enumerate(datos.iterrows(), 1):
            print(f"{i}. {fila['Title']} - Valoración: {fila['_rating']}")

    def recomendar(self, genero):
        if self.col_generos is None:
            print("No hay columna de géneros.")
            return

        resultados = []

        for _, fila in self.datos.iterrows():
            generos = obtener_generos(fila[self.col_generos])

            if any(normalizar(g) == normalizar(genero) for g in generos):
                resultados.append(fila["Title"])

        if not resultados:
            print("No se encontraron juegos de ese género.")
            return

        print(f"\n--- VIDEOJUEGOS DE {genero} ---")

        for titulo in resultados[:10]:
            print("-", titulo)

        if len(resultados) > 10:
            print(f"Se muestran 10 de {len(resultados)} resultados.")

    # =========================
    # RECORRIDOS DEL ABB
    # =========================

    def mostrar_recorrido(self, tipo):
        if tipo not in ["inorden", "preorden", "postorden"]:
            print("Recorrido no válido.")
            return

        titulos = self.arbol.recorrido(tipo)

        print(f"\n--- RECORRIDO {tipo.upper()} ---")

        for titulo in titulos[:50]:
            print("-", titulo)

        if len(titulos) > 50:
            print(f"Se muestran 50 de {len(titulos)} títulos.")

    # =========================
    # COMPARAR BUSQUEDAS
    # =========================

    def comparar_busquedas(self, titulo):
        print("\n--- COMPARACIÓN DE BÚSQUEDAS ---")

        inicio = time.perf_counter()
        secuencial = self.busqueda_secuencial(titulo)
        tiempo_sec = time.perf_counter() - inicio

        inicio = time.perf_counter()
        abb = self.arbol.buscar(titulo)
        tiempo_abb = time.perf_counter() - inicio

        inicio = time.perf_counter()
        avl = self.avl.buscar(titulo)
        tiempo_avl = time.perf_counter() - inicio

        print("Secuencial:", "Encontrado" if secuencial else "No encontrado")
        print("ABB:", "Encontrado" if abb else "No encontrado")
        print("AVL:", "Encontrado" if avl else "No encontrado")

        print(f"Secuencial: {tiempo_sec:.8f} segundos")
        print(f"ABB: {tiempo_abb:.8f} segundos")
        print(f"AVL: {tiempo_avl:.8f} segundos")

    # =========================
    # ALTURAS
    # =========================

    def altura_bst(self):
        altura = self.arbol.altura()
        print("Altura del ABB:", altura)
        return altura

    def comparar_bst_avl(self):
        print("\n--- COMPARACIÓN DE ALTURAS ---")
        print("Títulos ABB:", self.arbol.cantidad)
        print("Títulos AVL:", self.avl.cantidad)
        print("Altura ABB:", self.arbol.altura())
        print("Altura AVL:", self.avl.obtener_altura())

    # =========================
    # PRUEBAS DE RENDIMIENTO
    # =========================

    def pruebas_rendimiento(self):
        titulos = [
            str(t) for t in self.datos["Title"].dropna().unique()
            if str(t).strip()
        ]

        if not titulos:
            print("No hay títulos para probar.")
            return

        random.Random(42).shuffle(titulos)

        tamanos = [n for n in [100, 1000, 10000, 100000] if n <= len(titulos)]

        if not tamanos:
            tamanos = [len(titulos)]

        print("\n--- PRUEBAS DE RENDIMIENTO ---")

        for cantidad in tamanos:
            muestra = titulos[:cantidad]
            datos = self.datos[
                self.datos["Title"].astype(str).isin(muestra)
            ].drop_duplicates(subset=["Title"])

            abb = ArbolBinario()
            avl = ArbolAVL()

            inicio = time.perf_counter()
            for _, fila in datos.iterrows():
                abb.insertar(fila.to_dict())
            tiempo_abb = time.perf_counter() - inicio

            inicio = time.perf_counter()
            for _, fila in datos.iterrows():
                avl.insertar(fila.to_dict())
            tiempo_avl = time.perf_counter() - inicio

            objetivo = muestra[-1]

            inicio = time.perf_counter()
            abb.buscar(objetivo)
            busqueda_abb = time.perf_counter() - inicio

            inicio = time.perf_counter()
            avl.buscar(objetivo)
            busqueda_avl = time.perf_counter() - inicio

            print(f"\nCantidad solicitada: {cantidad}")
            print("Títulos insertados:", abb.cantidad)
            print("Altura ABB:", abb.altura())
            print("Altura AVL:", avl.obtener_altura())
            print(f"Construcción ABB: {tiempo_abb:.6f} s")
            print(f"Construcción AVL: {tiempo_avl:.6f} s")
            print(f"Búsqueda ABB: {busqueda_abb:.8f} s")
            print(f"Búsqueda AVL: {busqueda_avl:.8f} s")