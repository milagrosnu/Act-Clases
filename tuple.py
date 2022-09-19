tupla = (8, 15, 4, 39, 5, 89, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

#ultimo item
show1=tupla[-1]
print(show1)
#El número de ítems de tupla
show2 = len(tupla)
print(show2)
#La posición donde se encuentra el ítem 87 de tupla
show3 = tupla.index(88)
print(show3)
#Una lista con los últimos tres ítems de tupla
list = list(tupla[-3::])
print(list)
#Un ítem que haya en la posición 8 de tupla
item8 = tupla[8]
print(item8)
#El número de veces que el ítem 7 aparece en tupla
