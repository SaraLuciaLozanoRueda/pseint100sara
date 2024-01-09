suma=1

numero=int(input("VALOR DE N: "))
d=3

if (numero > 1):
    print (suma, " + " ,end="" )
    
    for i in range (2,numero +1):
        if (i == numero):
            print (i,"/",d)
        else:
            print (i,"/",d, " + ",end="") 
        suma  +=(i/d) 
        d +=2

print ("LA SUMA ES: ",suma)

