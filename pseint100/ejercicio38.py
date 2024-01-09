verde = 0
rojo = 0
azul = 0

personas = int(input("CANTIDAD DE PERSONAS: "))

for i in range(1, personas + 1):
    print("PERSONA Nro", i, " ")
    c = ""

    while c not in ["rojo", "verde", "azul"]:
        c = input("ROJO - VERDE - AZUL\n COLOR: ").lower() 
        break

    if c == "rojo":
        rojo += 1
    elif c == "verde":
        verde += 1
    elif c == "azul":
        azul += 1

print("")
if rojo > verde and rojo > azul:
    Mcolor = "ROJO"
elif verde > rojo and verde > azul:
    Mcolor = "VERDE"
elif azul > verde and azul > rojo:
    Mcolor = "AZUL"
else:
    Mcolor = "NINGUNO"

print("CANTIDAD DE COLOR ROJO:    ", rojo)
print("CANTIDAD DE COLOR VERDE:   ", verde)
print("CANTIDAD DE COLOR AZUL:    ", azul)
print("EL COLOR MAS ESCOGIDO ES:  ", Mcolor)

    
