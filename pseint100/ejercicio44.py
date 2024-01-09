print ("    PRESTAMO DEL BANCO    ")
monto=float (1000)

meses=int(input("Nro de meses: "))
intereses=float (monto*(meses*0.02))
totalp=monto + intereses

print ("INTERESES:      ",intereses)
print ("TOTAL A PAGAR:  ",totalp)