N = 0
pro= 1

N=int(input("VALOR DE N: ".format(N)))
f=1
for f in range (1,N +1):
    print (f," ")
    pro =pro * f

print ("PRODUCTO DE ",N," ES: ",pro)