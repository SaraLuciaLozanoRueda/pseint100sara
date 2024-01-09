numeroInvertido=""
numero=int(input("INGRESE UN NUMERO: "))
numeroInvertido = str(numero)[::-1]
numeroInvertidoN = int(numeroInvertido)
print ("NUMERO INGRESADO: ",numero)
print ("NUMERO INVERTIDO: ",numeroInvertidoN)

if numero==numeroInvertidoN:
    print ("si es un numero capicua")
elif numero!=numeroInvertidoN:
    print ("no es un numero capicua")  