print("CLAVES DE DESTINO")
print("1.Estados Unidos - $0.13\n2.Canada - $0.11\n5.America del sur - $0.52\n6.America central - $0.99\n8.Mexico - $0.17\n9. Europa - $0.17\n10. Asia - $0.20\n15.Africa - $0.59\n20. Oceania -$0.28")
print("")
clave=input("INGRESE CLAVE DESTINO: ")
minutos=int(input("DURACION DE LA LLAMADA: "))

if clave =="1":
    print("COSTO: $.",minutos*0.13)
elif clave=="2":
    print("COSTO: $.",minutos*0.11)
elif clave=="5":
    print("COSTO: $.",minutos*0.52)
elif clave=="6":
    print("COSTO: $.",minutos*0.99)
elif clave=="8":
    print("COSTO: $.",minutos*0.17)
elif clave=="9":
    print("COSTO: $.",minutos*0.17)
elif clave=="10":
    print("COSTO: $.",minutos*0.20)
elif clave=="15":
    print("COSTO: $.",minutos*0.59)
elif clave=="20":
    print("COSTO: $.",minutos*0.28)
else:
    print("!! ERROR EN LA CLAVE !!")














