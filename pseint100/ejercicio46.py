H=int(input("HORAS:    "))
M=int(input("MINUTOS:  "))
S=int(input("SEGUNDOS: "))

costo=((H*3600)+(M*60)+S)*0.25 #VALOR SEGUNDO

print("")
print("COSTO TOTAL:",costo)