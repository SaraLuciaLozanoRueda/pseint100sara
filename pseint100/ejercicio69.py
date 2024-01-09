print("MOSTRAR EL PROCENTAJE DE LOS ALUMNOS APROBADOS Y DESAPROBADOS")
print("")
apro=float(input("INGRESE LA CANTIDAD DE ALUMNOS APROBADOS: "))
desa=float(input("INGRESE CANTIDAD DE ALUMNOS DESAPROBADOS: "))

porA=float(apro*100)/(apro + desa)
porD=float(desa*100)/(apro + desa)
totalA=float((porA*100)/100)
totalD=float((porD*100)/100)

print(f"APROBADOS:    {totalA:.2f}""%")
print(f"DESAPROBADOS: {totalD:.2f}""%")







