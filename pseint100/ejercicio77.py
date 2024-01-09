print("09.CALCULAR EL SUELDO FINAL")
nom=input("INGRESE NOMBRE: ")
sueldoB=float(input("SUELDO BASICO: S/. "))
hijos=int(input("Nro. DE HIJOS: "))

if hijos>0:
    boni=sueldoB*0.7

sueldoF=float( sueldoB +boni)
print("")
print(f"BONIFICACION: {boni:.1f}")
print(f"SUELDO FINAL: {sueldoF:.1f}")