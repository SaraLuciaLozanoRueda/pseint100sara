import math
r=float(input("RADIO: "))
h=float(input("ALTURA: "))
a=float(2*math.pi*r*(h+r))
v=float(math.pi*(r*r)*h)
print("AREA TOTAL DEL CILINDRO: ",a,"cm2")
print("VOLUMEN DEL CILINDRO:    ",v,"cm3")