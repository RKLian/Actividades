#Condicionales
print("Opciones: \n 1 = Personas \n 2 = Vehiculos \n 3 = Universidades \n 4 = Notas \n 5 = Salir")
Menu = int(input("Digite una de las opciones: "))

if Menu == 1:
    print("Usted ha seleccionado la opción Personas")
elif Menu == 2:
    print("Usted ha seleccionado la opción Vehiculos")
elif Menu == 3:
    print("Usted ha seleccionado la opción Universidades")
elif Menu == 4:
    print("Usted ha seleccionado la opción Notas")
if Menu == 5:
    print("Usted ha seleccionado la opción Salir")
    SystemExit
else:
    print("Gracias por haber utilizado el menu")