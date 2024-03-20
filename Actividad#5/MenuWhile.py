#While
while (True):
    print("Menu: \n 1 = Personas \n 2 = Vehiculos \n 3 = Universidades \n 4 = Notas \n 5 = Salir")
    MenuWhile = int(input("Digite una de las opciones:"))

    if MenuWhile == 1:
        print("Usted ha seleccionado la opción Personas")
    if MenuWhile == 2:
        print("Usted ha seleccionado la opción Vehiculos")
    if MenuWhile == 3:
        print("Usted ha seleccionado la opción Universidades")
    if MenuWhile == 4:
        print("Usted ha seleccionado la opción Notas")
    if MenuWhile == 5:
        print("Usted ha seleccionado la opción Salir")
        print("Gracias por haber usando el menu chafa")
        exit()
    if MenuWhile >= 6 or MenuWhile <1:
        print("Esta opción no existe")
    SystemExit
