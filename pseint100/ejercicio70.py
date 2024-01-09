n1=int(input("INGRESE NOTA 1: "))
n2=int(input("INGRESE NOTA 2: "))
n3=int(input("INGRESE NOTA 3: "))

prom=int((n1+n2+n3)/3)

if prom > 10.5:
    print("APROBADO CON:",prom)
elif prom < 10.5:
    print("DESAPROBADO CON:",prom)
