import pandas as pd

class Videojuegos:
    def __init__(self):
        self.datos = pd.read_csv("games.csv")

    def Info_juegos(self, Title):
        juego = self.datos[self.datos["Title"] == Title]

        if not juego.empty:
            juego = juego.iloc[0]

            print("Titulo:", juego["Title"])
            print("Fecha de salida:", juego["Release Date"])
            print("Rating:", juego["Rating"])
            print("Genero:", juego["Genres"])
        else:
            print("Videojuego no encontrado")





    def top_10(self):
        top = self.datos.sort_values("Rating", ascending=False).head(10)
        top = top.drop_duplicates("Title").head(10)


        for _, juego in top.iterrows():
            print(juego["Title"], "-", juego["Rating"])









    def recomendar(self, genero):
     juegos = self.datos[self.datos["Genres"].str.contains("'" + genero + "'", case=False, na=False)]

     juegos = juegos.sort_values("Rating", ascending=False)
     juegos = juegos.drop_duplicates("Title").head(5)

     print("Juegos recomendados:")

     for _, juego in juegos.head(5).iterrows():
        print(juego["Title"], "-", juego["Rating"])