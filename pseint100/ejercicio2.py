con =0
cantidadpar=0
cantidadimpar=0


for con in range (1,10):
    print ("numero",con,":",con )
    if con % 2 == 0:
        cantidadpar +=1
    else:
        cantidadimpar +=1    

print ("El total de pares      :", cantidadpar)
print ("El total de impares   :",cantidadimpar) 