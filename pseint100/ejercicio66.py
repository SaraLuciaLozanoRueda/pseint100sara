alt = int(input("ALTURA DEL TRIANGULO: "))
caract = input("INGRESE UN CARACTER: ")

for i in range(alt+1):
    for j in range(0, alt - i):
        print(" ", end=" ")

    for j in range(0, (i * 2) - 1):
        print(caract, end=" ")

    print("")