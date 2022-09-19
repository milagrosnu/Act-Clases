#Dadas dos listas LISTA1 y LISTA2 debes realizar las siguientes tareas:

lista1=[]
lista2=[]

#Añade a la LISTA1 el int 456789 y luego el string “Hola Mundo”
lista1.append(456789) 
lista1.insert(1,"Hola Mundo")
print(lista1)
#Luego añade a la LISTA2 el string “Hola y Adios” y luego el int 5555
lista2.append("Hola y Adios")
lista2.extend(lista1)
print(lista2)
#Genera una LISTA3 con todos los elementos de la LISTA1 sin considerar el último elemento
lista3 = lista1.pop(0)
print(lista3)
#Finalmente, genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3
lista5= lista2,lista1
print(lista5)
