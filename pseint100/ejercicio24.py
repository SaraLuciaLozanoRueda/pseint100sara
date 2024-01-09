fact=1
numero=int(input("FACTORIAL A CALCULAR: "))
print ("SERIE DEL FACTORIAL:",end="")

for X in range (numero,0,-1):
    print (numero + 1 -X,end=" ")

    fact *= X

print ("")
print ("EL FACTORIAL ES: ",fact)
print ("")
