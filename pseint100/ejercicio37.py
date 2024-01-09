m = int
e = int
izq = int
der = int
val = int
espacios = str
dimension = [20, 20]

print("MOSTRAR EL TRIÁNGULO DE PASCAL")
n = int(input("INGRESE DIMENSIÓN [MENOS O IGUAL A 20]: "))

if n > 0 and n <= 20:
    izq = 1
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        m = izq
        for k in range(i + 1):
            print(f"{m:2}", end="")
            m = m * (i - k) // (k + 1)
        print()
else:
    print("La dimensión debe estar entre 1 y 20.")