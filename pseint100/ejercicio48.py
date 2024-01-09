numero=int(input("INGRESE UN NUMERO DE 3 CIFRAS: "))

cen=int((numero-(numero%100))/100)
res=int(numero%100)
dec=int((res-(res%10))/10)
uni=int(res%10)

print ("")
print("CENTENA: ",cen)
print("DECENA:  ",dec)
print("UNIDAD:  ",uni)