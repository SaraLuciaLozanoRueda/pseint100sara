decena = ""
unidad = ""

print("PASAR NÚMEROS A LETRAS")
num = int(input("Ingrese un número de hasta 2 cifras: "))

if 0 < num < 100:
    if 10 < num < 16:
        if num == 11:
            print("ONCE")
        elif num == 12:
            print("DOCE")
        elif num == 13:
            print("TRECE")
        elif num == 14:
            print("CATORCE")
        elif num == 15:
            print("QUINCE")
    else:
        dec=int(num-(num%10))/10
        uni = int(num % 10)

        if dec == 1:
            if uni == 0:
                decena = "DIEZ"
            else:
                print("DIECI" + {1: "UNO", 2: "DOS", 3: "TRES", 4: "CUATRO", 5: "CINCO", 6: "SEIS", 7: "SIETE", 8: "OCHO", 9: "NUEVE"}.get(uni))
        elif dec == 2:
            if uni == 0:
                decena = "VEINTE"
            else:
                print("VEINTI" + {1: "UNO", 2: "DOS", 3: "TRES", 4: "CUATRO", 5: "CINCO", 6: "SEIS", 7: "SIETE", 8: "OCHO", 9: "NUEVE"}.get(uni))
        elif 2 < dec < 10:
            decena = {3: "TREINTA", 4: "CUARENTA", 5: "CINCUENTA", 6: "SESENTA", 7: "SETENTA", 8: "OCHENTA", 9: "NOVENTA"}.get(dec)

            if 0 < uni < 10:
                unidad = {1: "UNO", 2: "DOS", 3: "TRES", 4: "CUATRO", 5: "CINCO", 6: "SEIS", 7: "SIETE", 8: "OCHO", 9: "NUEVE"}.get(uni)

            if 0 < uni < 10:
                print(decena + " Y " + unidad)
            else:
                print(decena)
else:
    print("Número equivocado...")