import time
import pandas as pd


class Videojuegos:

    def __init__(self, ruta_csv="games.csv"):
        self.datos = pd.read_csv(ruta_csv)
        self.datos_indexados = (
            self.datos.drop_duplicates("Title")
            .sort_values("Title")
            .set_index("Title")
        )

    def Info_juegos_secuencial(self, Title):
        juego = self.datos[self.datos["Title"] == Title]
        if not juego.empty:
            juego = juego.iloc[0]
            return True, juego
        else:
            return False, None

    def Info_juegos(self, Title):
        encontrado, juego = self.Info_juegos_secuencial(Title)
        if encontrado:
            print("Titulo:", juego["Title"])
            print("Fecha de salida:", juego["Release Date"])
            print("Rating:", juego["Rating"])
            print("Genero:", juego["Genres"])
        else:
            print("Videojuego no encontrado")

    def Info_juegos_arbol(self, Title):
        try:
            juego = self.datos_indexados.loc[Title]
            return True, juego
        except KeyError:
            return False, None

    def top_10(self):
        top = self.datos.sort_values("Rating", ascending=False).head(10)
        top = top.drop_duplicates("Title").head(10)

        for _, juego in top.iterrows():
            print(juego["Title"], "-", juego["Rating"])

    def recomendar(self, genero):
        juegos = self.datos[
            self.datos["Genres"].str.contains(
                "'" + genero + "'", case=False, na=False
            )
        ]
        juegos = juegos.sort_values("Rating", ascending=False)
        juegos = juegos.drop_duplicates("Title").head(5)

        print("Juegos recomendados:")
        for _, juego in juegos.head(5).iterrows():
            print(juego["Title"], "-", juego["Rating"])

    def experimento_tiempos(self):
        tamanos = [1_000, 10_000, 100_000]
        repeticiones = 50
        juego_inexistente = "ZZZ_Juego_Inexistente_9999"

        print(f"\n{'='*65}")
        print(f"{'N Elementos':<12} | {'Búsqueda Secuencial':<22} | {'Búsqueda en Árbol':<20}")
        print(f"{'='*65}")

        for n in tamanos:
            df_escalado = self.datos.sample(
                n=n, replace=True, random_state=42
            ).copy()
            df_escalado["Title"] = [f"Game_{i}" for i in range(n)]

            df_secuencial = df_escalado
            df_arbol = df_escalado.sort_values("Title").set_index("Title")

            t_inicio = time.perf_counter()
            for _ in range(repeticiones):
                _ = df_secuencial[
                    df_secuencial["Title"] == juego_inexistente
                ]
            t_fin = time.perf_counter()
            tiempo_secuencial = ((t_fin - t_inicio) / repeticiones) * 1000

            t_inicio = time.perf_counter()
            for _ in range(repeticiones):
                try:
                    _ = df_arbol.loc[juego_inexistente]
                except KeyError:
                    pass
            t_fin = time.perf_counter()
            tiempo_arbol = ((t_fin - t_inicio) / repeticiones) * 1000

            print(
                f"{n:<12,d} | {tiempo_secuencial:>18.4f} ms | {tiempo_arbol:>17.4f} ms"
            )

        print(f"{'='*65}\n")
