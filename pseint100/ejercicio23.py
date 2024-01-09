suma=0
notas_totales=int(input("INGRESE LA CANTIDAD DE NOTAS: "))
for notas in range (0,notas_totales):
    nota=int(input("NOTA: "))
    suma +=nota

promedio = suma /notas_totales

print ("PROMEDIO:",promedio)