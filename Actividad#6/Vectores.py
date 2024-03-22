#1. Lista vacia
list = []
#2. Lista con 5 elementos
vocales = ['a', 'e', 'i', 'o', 'u']
#3. Longitud de listas
length = (len(list))
print('list: ', length)
length = (len(vocales))
print('vocales:', length)
IN = True,False
#4. Obtener elemento primario, central y final de la lista
print('Lista: ' + vocales[0] + ',' + vocales[2] + ',' + vocales[4])

#5. Lista de Datos personales
Datos_personales = ['Yulian', '19', '1.81', 'Soltero', 'Olaya Herrera']
#6. Agrego datos utilizando append
Datos_personales.append('Encoder')
print(Datos_personales)

#7. Añadir lista nueva de empresas y agregar una con metodo insert
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.insert(8, 'Youtube')
print(it_companies)
#8. Comprobar si existe dicha empresa
does_exit = 'Youtube' in it_companies
print(does_exit)

#9. Ordenar lista con metodo sort
it_companies.sort()
print(it_companies)
#I10. nvertir lista
it_companies.sort(reverse=True)
print(it_companies)

#11. Eliminar usando pop
it_companies.pop(0)
print(it_companies)
#Eliminar usando delete
del it_companies[0]
print(it_companies)
#12. Eliminar todas las empresas de it_companies
it_companies.clear()
print(it_companies)