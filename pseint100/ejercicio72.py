usuario=input("INGRESE USUARIO: ")
clave=int(input("INGRESE CLAVE: "))
if usuario=="ADMIN" and clave == 12345:
    print ("ACCESO PERMITIDO")
else:
    print("ACCESO DENEGADO")