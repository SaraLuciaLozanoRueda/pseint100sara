print("CALCUALR EL SUELDO FINAL DE UN EMPLEADO")
sueldobase=int(input("INGRESE SU SUELDO BASE: "))
numHijos=int(input("INGRESE NUMERO DE HIJOS:"))
diasNoLaborales=int((input("INGRESE DIAS NO LABORALES TRABAJADOS: ")))

sueldoFinal=int(sueldobase+(numHijos*100)+(diasNoLaborales*25))
print("")
print("SUELDO FINAL: $ ",sueldoFinal)