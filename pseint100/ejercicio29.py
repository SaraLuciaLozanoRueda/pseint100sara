sumaP=0
sumaI=0

numero=int(input("INGRESE UN NUMERO: "))
for x in range (1,numero+1):
    if x % 2==0:
        sumaP +=x
    else:    
        sumaI +=x

print ("SUMA DE PARES      :",sumaP)
print ("SUMA DE IMPARES    :",sumaI)