monto=float(input("MONTO DE COMPRA: S/. "))
if monto>=350:
    desc=int(monto*0.35)
    print("DESCUENTO ES DE 35%: S/. ",desc)
else:
    desc=int(monto*0.10)
    print("DESCUENTO ES DE 10%: S/.",desc)
total=int(monto-desc)
print("MONTO A PAGAR: S/.",total)