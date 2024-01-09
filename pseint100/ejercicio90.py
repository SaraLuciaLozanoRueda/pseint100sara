num1 = int(input("NUMERO 1: "))
num2 = int(input("NUMERO 2: "))
print("OPERADOR: ")
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
operador = input("[1 +] [2 -] [3 *] [4 /]: ")

if operador == "1":
    print("SUMA :", suma)
elif operador == "2":
    print("RESTA :", resta)
elif operador == "3":
    print("MULTIPLICACION :", multiplicacion)
elif operador == "4":
    print("DIVISION :", division)
else:
    print("OPERADOR INCORRECTO.... número del 1 al 4 en OPERADOR")