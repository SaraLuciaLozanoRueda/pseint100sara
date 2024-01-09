A =0
E =0
I =0
O =0
U =0


frase=input("INGRESE UNA FRASE QUE TE MOTIVE: ")

for letra in frase:
    if letra == "a" or letra=="A" or letra=="á" or letra =="Á":
        A +=1    
        
    if letra == "e" or letra=="E" or letra=="é" or letra =="É":
        E +=1
        
    if letra == "i" or letra=="I" or letra=="í" or letra =="Í ":
        I +=1
        
    if letra == "o" or letra=="O" or letra=="ó" or letra =="Ó":
        O +=1
        
    if letra == "u" or letra=="U" or letra=="ú" or letra =="Ú":
        U +=1
        

print ("CANTIDAD DE VOCALES: ")   
print ("A:   ",A) 
print ("E:   ",E)
print ("I:   ",I) 
print ("O:   ",O) 
print ("U:   ",U)  