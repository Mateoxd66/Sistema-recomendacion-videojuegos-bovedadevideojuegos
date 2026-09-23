from Tpintegrador import Videojuegos

juegos = Videojuegos()

while True:
    print("===============================================")
    print("            BOVEDA DE VIDEOJUEGOS              ")
    print("===============================================")

    print("[1]. Buscar un videojuego (Búsqueda Secuencial)")
    print("[2]. Buscar un videojuego (Búsqueda en Árbol / Índice)")
    print("[3]. Recomendar por genero")
    print("[4]. Ver Top 10")
    print("[5]. Ejecutar experimento de complejidad (Tiempos)")
    print("[6]. Salir")

    opcion = input("Ingrese una opcion (1-6): ")

    if opcion == "1":
        nombre = input("Ingrese el titulo del videojuego: ")
        juegos.Info_juegos(nombre)

    elif opcion == "2":
        nombre = input("Ingrese el titulo del videojuego: ")
        encontrado, juego = juegos.Info_juegos_arbol(nombre)
        if encontrado:
            print("Titulo:", nombre)
            print("Fecha de salida:", juego["Release Date"])
            print("Rating:", juego["Rating"])
            print("Genero:", juego["Genres"])
        else:
            print("Videojuego no encontrado")

    elif opcion == "3":
        genero = input("Ingresa un genero: ")
        juegos.recomendar(genero)

    elif opcion == "4":
        juegos.top_10()

    elif opcion == "5":
        print("\nEjecutando mediciones de complejidad...")
        juegos.experimento_tiempos()

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opcion Invalida.")

    input("\nPresiona Enter para volver al menu..")
