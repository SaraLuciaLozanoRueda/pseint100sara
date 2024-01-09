sumatoria=0
v=4
v1=5
v2=1
x=2
x1=0.5
ope="-"

print ("MUESTRA SERIE DE NUMEROS:")
print ("")
N=int(input("INGRESA UN VALOR PARA N: "))

for i in range(1,N+1):
    if i !=N:
        print (v,"/",x, " " ,ope, " " )
    else:
        print (v,"/",x," ",ope,"....")

    if i % 2 ==1:
        ope = "+"
        sumatoria +=(v/x)
    else:
        ope="-"
        sumatoria -=(v/x)

    v +=v1
    v1 +=v2
    v2 +=1
    x *=x1
    x1 +=x1

print ("")
print ("SUMATORIA: ",sumatoria)