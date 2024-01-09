total=0
desc=0
consumo_total=0
print ("cuando le pregunten por consumo responda con numeros")
for con in range (1,11):
    consumo=float(input("CONSUMO {}:$".format(con)))
    total +=consumo

    pagoTotal=total

if total>50:
    desc=total*0.07

print ("CONSUMO TOTAL:  $.",pagoTotal)
print ("DESCUENTO:      $.",desc)
print ("PAGO TOTAL:     $.",(pagoTotal-desc))