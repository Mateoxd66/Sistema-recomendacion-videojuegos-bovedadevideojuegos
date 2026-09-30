from Tpintegrador import Videojuegos


juegos = Videojuegos()


while True:

    print("===============================================")
    print("            BOVEDA DE VIDEOJUEGOS")
    print("===============================================")

    print("[1]. Buscar un videojuego")
    print("[2]. Recomendar por genero")
    print("[3]. Ver Top 10")
    print("[4]. Comparar busquedas")
    print("[5]. Recorrido Inorder")
    print("[6]. Recorrido Preorder")
    print("[7]. Recorrido Postorder")
    print("[8]. Pruebas de rendimiento")
    print("[9]. Salir")

    opcion = input("Ingrese una opcion (1-9): ")


    # =================================
    # BUSCAR VIDEOJUEGO
    # =================================

    if opcion == "1":

        nombre = input("Ingrese el titulo del videojuego: ")

        juegos.Info_juegos(nombre)


    # =================================
    # RECOMENDAR
    # =================================

    elif opcion == "2":

        genero = input("Ingresa un genero: ")

        juegos.recomendar(genero)


    # =================================
    # TOP 10
    # =================================

    elif opcion == "3":

        juegos.top_10()


    # =================================
    # COMPARAR BÚSQUEDAS
    # =================================

    elif opcion == "4":

        nombre = input("Ingrese el titulo del videojuego: ")

        juegos.comparar_busquedas(nombre)


    # =================================
    # INORDER
    # =================================

    elif opcion == "5":

        juegos.mostrar_inorder()


    # =================================
    # PREORDER
    # =================================

    elif opcion == "6":

        juegos.mostrar_preorder()


    # =================================
    # POSTORDER
    # =================================

    elif opcion == "7":

        juegos.mostrar_postorder()


    elif opcion == "8":

       juegos.pruebas_rendimiento()


    elif opcion == "9":

      print("¡Hasta luego!")
      break
   
     