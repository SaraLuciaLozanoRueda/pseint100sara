print("04. CALCULAR BONIFICACION")
print("")
venta=int(input("INGRESE MONTO DE VENTA: S/. "))
b1=int(venta * 0.10)
b2=int(venta *0.50)
if venta>2000:
    print("BONIFICACION 10%: $",b1)
else:
    print("BONIFICACION 50%: $",b2)