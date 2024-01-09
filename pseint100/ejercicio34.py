tarifa =0
bus=0
van =0
micro=0
man=0
noc=0

print ("GANANCIAS DE UNA GARITA DE CONTROL")
print ("----------------------------------")
cantidad=int(input("CANTIDAD DE VEHICIULOS:"))
print ("")
 
for cont in range (1,cantidad+1):
    print ("TIPO DE VEHICULO Nro",cont,"/",cantidad)
    opcion=input("1.Omnibus\n2.Minivan\n3.Micro\nOPCION:")
    if opcion == "1":
        tarifa=13
        bus +=tarifa
    elif opcion == "2":
        tarifa=10
        van +=tarifa
    elif opcion == "3":
        tarifa=8
        micro +=tarifa 
    turno=input("TURNO (M/N): ")
    if turno =="M" or turno =="m":
        man +=tarifa
    elif turno == "N" or turno =="n":
        noc +=tarifa   
    else:
        pass
    print ("")

print ("")
print ("IMPORTE DE TURNO MAÑANA:  ",man)
print ("IMPORTE DE TURNO NOCHE:   ",noc)
print ("")
print ("IMPORTE DE OMNIBUS:       ",bus)
print ("IMPORTE DE MINIVAN:       ",van)
print ("IMPORTE DE MICRO:         ",micro)
