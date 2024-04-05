print("Diccionario: ")
Perro = {
    'Nombre':'Zeus',
    'Color':'Gris',
    'Raza':'Perro Lobo',
    'Patas':4,
    'Edad':'2 años',
}
print(Perro)


print("\nDiccionario Estudiantes: ")
Estudiante = {
    'Nombre':'Yulian',
    'Apellido':'Herrera',
    'Sexo':'M',
    'Edad':19,
    'Estado Civil':'Soltero',
    'Habilidades':['Programar', 'Leer', 'Ingles'],
    'Pais':'Colombia',
    'Ciudad':'Cartagena',
    'Direccion':'Olaya Herrera',
}
for key,value in Estudiante.items():
    print(f"{key} : {value}")

print("\nLongitud: ")
print(len(Estudiante))

print("\nHabilidades: ")
for Habilidades in Estudiante['Habilidades']:
    print(Habilidades)

print("\nHabilidades Actualizadas: ")
Estudiante['Habilidades'].extend(['Cantar', 'Dormir'])
print(Estudiante['Habilidades'])

print("\nClaves: ")
for key in Estudiante:
    print(key)

print("\nValores: ")
print(Estudiante.values())

print("\nCambiar diccionario a una lista de tuplas: ")
print(Estudiante.items())

print("\nDiccionario con elemento eliminado: ")
Estudiante.pop('Direccion')
print(Estudiante)

print("\nDiccionario eliminado: ")
del Perro
