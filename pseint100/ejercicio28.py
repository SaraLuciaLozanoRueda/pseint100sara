divisi=0
numero=int(input("INGRESE UN VALOR: "))

for divi in range (1,numero+1):
    if numero % divi ==0:
        divisi+=1

if divisi==2:
    print ("NUMERO PRIMO")
else:
    print ("NO ES PRIMO")    

