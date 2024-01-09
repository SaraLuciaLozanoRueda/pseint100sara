cantidades=0
mejor_alumno=0
mejor_prom=0

for cantidades in range (1,6):
    nombre=(input("NOMBRE: "))
    promedio=(float(input("PROMEDIO: ")))
    if promedio > mejor_prom:
        mejor_prom=promedio
        mejor_alumno=nombre

print ("ALUMNO CON MAYOR NOTA:",mejor_alumno)
print ("PROMEDIO:            :",mejor_prom)