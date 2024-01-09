import os
import random

compra = float(input("VALOR DE COMPRA: "))
os.system("pause")

colores = [1, 2, 3, 4, 5]
random.shuffle(colores)

color = colores[0]  

if color == 1:
    print("COLOR: BLANCO")
    desc = 1.0
elif color == 2:
    print("COLOR: VERDE")
    desc = 0.5
elif color == 3:
    print("COLOR: NEGRO")
    desc = 0.4
elif color == 4:
    print("COLOR: CELESTE")
    desc = 0.05
elif color == 5:
    print("COLOR: ROJO")
    desc = 0.0

importe_desc = int(compra * desc)
total = int(compra - (compra * desc))

print("DESCUENTO: S/.", desc)
print("IMPORTE DESCT: S/.", importe_desc)
print("PAGO FINAL: S/. ", total)