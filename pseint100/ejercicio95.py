n1=int(input("INGRESE NOTA 1: "))
n2=int(input("INGRESE NOTA 2: "))
n3=int(input("INGRESE NOTA 3: "))
prom=int((n1+n2+n3)/3)
if prom==0 or prom==1 or prom==2 or prom==3 or prom==4 or prom==5 or prom==6 or prom==7 or prom==8 or prom==9 or prom==10:
    print("NIVEL MALO")
elif  prom==11 or prom==12 or prom==13:
    print("NIVEL REGULAR")
elif prom==14 or prom==15 or prom==16:
    print("NIVEL BUENO")
elif prom==17 or prom==18 or prom==19 or prom==20:
    print("NIVEL MUY BUENO")