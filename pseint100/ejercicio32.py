diax=21
mesx=10
añox=2023
edad=int

for x in range (0,10,1):
    DNI=int(input("DNI: "))
    diaNacimiento=int(input("DIA DE NACIEMIENTO: "))
    mesNacieminto=int(input("MES DE NACIMIENTO: "))
    añoNacimiento=int(input("AÑO DE NACIEMIENTO: "))
    genero=input("GENERO (H/M): ")
    print ("FECHA ACTUAL",diax,"/",mesx,"/",añox)
    edad=añox-añoNacimiento
    
    if mesNacieminto > mesx:
        edad -=1
    elif(mesNacieminto == mesx and  diaNacimiento > diax):
            edad -=1
    else:            
        pass
    print("EDAD:",edad, "años")
    if edad >= 8:
        print ("RECIBE TABLET")
    elif edad <=8:
        if genero == "H":
            print ("RECIBE CARRITO")
        else:
            print ("RECIBE MUÑECA") 
    else:
        pass

print ("int(")