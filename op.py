nombre = (input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))

#NOMBRE sea diferente de cuatro asteriscos “****”
#EDAD sea mayor que 5 y a su vez menor que 20
#Que la longitud de NOMBRE sea mayor o igual a 4  pero a la vez menor que 8
#EDAD multiplicada por 3 sea mayor que 35
verificar = nombre != "****" and 20 > edad > 5 and 8 >= len(nombre) >= 4 and (edad * 3) > 35
print(verificar)



