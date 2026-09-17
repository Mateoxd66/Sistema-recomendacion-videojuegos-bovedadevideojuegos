from Tpintegrador import Videojuegos

juegos = Videojuegos()

while True:

    print("===============================================")

    print("            BOVEDA DE VIDEOJUEGOS              ")

    print("===============================================")


    print("[1]. Buscar un videojuego")

    print("[2]. Recomendar por genero")

    print("[3]. Ver Top 10")

    print("[4]. Salir")


    opcion = input("Ingrese una opcion (1-4): ")


    if opcion == "1":
        nombre = input("Ingrese el titulo del videojuego: ")

        juegos.Info_juegos(nombre,)


    elif opcion == "2":
        genero = input("Ingresa un genero: ")

        juegos.recomendar(genero)


    elif opcion == "3":
        juegos.top_10()


    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opcion Invalida.")


    input("\nPresiona Enter para volver al menu...")