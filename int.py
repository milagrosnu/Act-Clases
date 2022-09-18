partidos_ganados = int(input ("Ingresar cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingresar cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingresar cantidad de partidos perdidos: "))

puntos_totales = (partidos_ganados * 2 + partidos_empatados * 1 + partidos_perdidos * 0)
partidos_totales = (partidos_ganados + partidos_empatados + partidos_perdidos)

promedio_final = (puntos_totales / partidos_totales) 

print(f"Promedio final obtenido: {promedio_final}")