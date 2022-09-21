cadena = "acitametaM ,5.8 ,otipeP ordeP"

#dar vuelta cadena, cadena_volteada
cadena_volteada = cadena[::-1]
#print(cadena_volteada)

#sacar nombre y apellido
nombre = cadena_volteada[0:5]
apellido = cadena_volteada[6:12]
#print(nombre,apellido)

#extraer nota
nota = cadena_volteada [14:17]
#print(nota)
#extraer materia
materia = cadena_volteada[19::]
#print(materia)
#Mostrar nombre, apellido ha sacado nota en materia
print(f"{nombre} {apellido} obtuvo un {nota} en {materia}")