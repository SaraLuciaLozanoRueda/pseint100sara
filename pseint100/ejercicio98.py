
print("MENU DE OPCIONES DE UN TRIANGULO")
print("-------------------------------------------------")
print("1.Area de un triangulo,dada la base y la altura\n2. Base de un triangulo,dada la altura y el area\n3. Altura de un triangulo,dada la base y el area")
opc=input("Selecciona un opcion: ")
print("")

if opc =="1":
    base=float((input("BASE: ")))
    altura=float((input("ALTURA: ")))
    area=float(((base*altura)/2))
    print("")
    print("EL AREA ES: ",area)
elif opc=="2":
    altura=float(input("ALTURA: "))
    area=float(input("AREA: "))
    base=float(((area*2)/altura))
    print("")
    print("LA BASE ES: ",base)
elif opc=="3":
    base=float(input("BASE: "))
    area=float(input("AREA: "))
    altura=float(((area*2)/base))
    print("")
    print("LA ALTURA ES: ",altura)
else:
    print("Error... Opcion Incorrecta")