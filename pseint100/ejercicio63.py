costo=float(input("COSTO DE LA CASA: S/ "))
iva=float(input("VALOR DEL IVA: % "  ))
print("")
totPagar=(int(costo+(costo*(iva/100))))
costo2=int(costo*(iva/100))
print("IVA DE ",iva,"%: S/",costo2)
print("TOTAL A PAGAR: S/",totPagar)