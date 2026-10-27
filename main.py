
from Tpintegrador import Videojuegos

juegos = Videojuegos()

while True:
    print("\n===============================================")
    print("           BOVEDA DE VIDEOJUEGOS")
    print("===============================================")
    print("[1] Buscar videojuego")
    print("[2] Recomendar por genero")
    print("[3] Ver Top 10")
    print("[4] Comparar busquedas")
    print("[5] Recorrido Inorder")
    print("[6] Recorrido Preorder")
    print("[7] Recorrido Postorder")
    print("[8] Pruebas de rendimiento")
    print("[9] Comparar BST vs AVL")
    print("[10] Explorar categorias")
    print("[11] Salir")

    opcion = input("Ingrese una opcion (1-11): ").strip()

    if opcion == "1":
        nombre = input("Titulo del videojuego: ")
        juegos.Info_juegos(nombre)

    elif opcion == "2":
        genero = input("Genero: ")
        juegos.recomendar(genero)

    elif opcion == "3":
        juegos.top_10()

    elif opcion == "4":
        nombre = input("Titulo del videojuego: ")
        juegos.comparar_busquedas(nombre)

    elif opcion == "5":
        juegos.mostrar_inorder()

    elif opcion == "6":
        juegos.mostrar_preorder()

    elif opcion == "7":
        juegos.mostrar_postorder()

    elif opcion == "8":
        juegos.pruebas_rendimiento()

    elif opcion == "9":
        juegos.comparar_bst_avl()

    elif opcion == "10":
        juegos.explorar_categorias()

    elif opcion == "11":
        print("Hasta luego!")
        break

    else:
        print("Opcion invalida.")
