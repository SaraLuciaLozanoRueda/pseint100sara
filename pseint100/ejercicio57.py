dias=int(input("INGRESE LA CANTIDAD DE DIAS: "))
A=int(dias/365)
M=int((dias-(A*365))/30)
D=int(dias-((A*365)+(M*30)))
print("AÑO:  ",A)
print("MES:  ",M)
print("DIA:  ",D)  

print("PORQUE ME ES EXTRAÑA LA LOGICA DE ARRIBA")
dias=int(input("INGRESE LA CANTIDAD DE DIAS: "))
A=int(dias/365)
M=int(dias/30)
print("AÑO:  ",A)
print("MES:  ",M)
print("DIA:  ",dias)  