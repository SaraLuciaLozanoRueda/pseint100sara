sueldo=float(input("SUELDO BASE: S/\n  "))
categoria=input("CATEGORIA\n1. A\n2. B\n3. C\n4. D\n digita el numero de su categoria: ")
if categoria=="1":
    bonificacion=int(sueldo*0.1)
elif categoria=="2":
    bonificacion=int(sueldo*0.2)
elif categoria=="3":
    bonificacion=int(sueldo*0.3)
elif categoria=="4":
    bonificacion=int(sueldo*0.5)
else:
    print("SOLO DEL 1 AL 4")
total=int(sueldo+bonificacion)
print("")
print("BONIFICACION: S/.",bonificacion)
print("SUELDO NETO:  S/.",total)