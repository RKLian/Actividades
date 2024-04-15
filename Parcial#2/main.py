from MenuPrincipal import MenuPrincipal
if __name__ == "__main__":
    menu_principal = MenuPrincipal()
    while True:
        menu_principal.mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            menu_principal.seleccionar_opcion(opcion)
