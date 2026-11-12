from Tpintegrador import Videojuegos


def mostrar_menu():
    print("\n========== BÓVEDA DE VIDEOJUEGOS ==========")
    print("1. Buscar un videojuego")
    print("2. Recomendar por género")
    print("3. Ver Top 10")
    print("4. Comparar búsquedas")
    print("5. Recorrido Inorder")
    print("6. Recorrido Preorder")
    print("7. Recorrido Postorder")
    print("8. Pruebas de rendimiento")
    print("9. Comparar BST vs AVL")
    print("10. Explorar categorías")
    print("11. Ver Top 5 con Heap")
    print("12. Ver videojuegos relacionados")
    print("13. Salir")


def main():
    try:
        juegos = Videojuegos("games.csv")
    except (FileNotFoundError, ValueError) as error:
        print("Error al iniciar el programa:", error)
        return

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción por numero: ").strip()

        if opcion == "1":
            nombre = input("Nombre del videojuego: ").strip()
            juegos.info_juegos(nombre)
        elif opcion == "2":
            genero = input("Género: ").strip()
            juegos.recomendar(genero)
        elif opcion == "3":
            juegos.top_10()
        elif opcion == "4":
            nombre = input("Nombre del videojuego: ").strip()
            juegos.comparar_busquedas(nombre)
        elif opcion == "5":
            juegos.mostrar_recorrido("inorden")
        elif opcion == "6":
            juegos.mostrar_recorrido("preorden")
        elif opcion == "7":
            juegos.mostrar_recorrido("postorden")
        elif opcion == "8":
            juegos.pruebas_rendimiento()
        elif opcion == "9":
            juegos.comparar_bst_avl()
        elif opcion == "10":
            juegos.explorar_categorias()
        elif opcion == "11":
            juegos.top_5_heap()
        elif opcion == "12":
            nombre = input("Nombre del videojuego: ").strip()
            juegos.mostrar_relacionados(nombre)
        elif opcion == "13":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intentá nuevamente.")


if __name__ == "__main__":
    main()
