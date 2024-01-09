numero = int(input("INGRESE UN VALOR: "))

for cont in range(2, numero + 1):
    divisible = 0
    for divi in range(1, cont + 1):
        if cont % divi == 0:
            divisible += 1
    if divisible == 2:
        print(cont, end=" ")

print("")

       


