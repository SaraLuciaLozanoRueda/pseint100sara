altura = int(input("ALTURA DEL ROMBO: "))


while altura <= 0:
    altura = int(input("REPITE LA ALTURA DEL ROMBO:" ))


for i in range(1, altura+1, 2):
    print(" " * ((altura-i)//2) + "*" * i)


for i in range(altura-2, 0, -2):
    print(" " * ((altura-i)//2) + "*" * i)