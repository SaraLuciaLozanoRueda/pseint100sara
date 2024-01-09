cantidad=int(input("INGRESE CANTIDAD A COMPRAR: "))
if cantidad==1 or cantidad==2 or cantidad==3:
    costo=int(15)
elif cantidad==4 or cantidad==5 or cantidad==6 or cantidad==7 or cantidad==8:
    costo=int(11)
else:
    costo=int(10)
total=int(costo*cantidad)
print("Costo por teclado: S/",costo)
print("Total a pagar: S/",total)