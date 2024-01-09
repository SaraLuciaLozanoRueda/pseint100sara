import random
i=1
sw=0
numA= random.randrange(1, 20) 

for i in range (4):
    numero=int(input("ENCUENTRE EL NUMERO [1 - 20] :" ))
    if (numero ==numA):
        print ("NUMERO ENCONTRADO")
        sw=1
        i=3
        break
    else:
        if (numero > numA):
            print ("INGRESE UN NUMERO MENOR")    
        elif (numero < numA):
            print ("INGRESE UN NUMERO MAYOR")
    print ("")

if (sw==0):
    print ("EL NUMERO ENCONTRADO ERA: ",numA)    

if (numero ==numA):
        print ("NUMERO ENCONTRADO")
        sw=1
        i=3
