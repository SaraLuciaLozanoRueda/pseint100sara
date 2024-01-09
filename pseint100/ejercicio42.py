
xseg=int(input("CANTIDAD DE SEGUNDOS:"))

hora=int(xseg/3600)
min=int((xseg -(hora*3600))/60 )
seg= int(xseg - ((hora *3600)+ (min*60)))

print ("HORAS:          ",hora)
print ("MINUTOS:        ",min)
print ("SEGUNDOS:       ",seg)

print ("")
print ("PORQUE ME PARECE EXTRAÑO")
print ("")
xseg=float(input("CANTIDAD DE SEGUNDOS:"))

hora=float(xseg/3600)
min=float(xseg/60)


print ("HORAS:          ",hora)
print ("MINUTOS:        ",min)
print ("SEGUNDOS:       ",xseg)
