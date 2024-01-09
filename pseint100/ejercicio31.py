C = 0
S=0
D=0
L=0
R=0
M=0
consonantes=0

refran=input("INGRESE UN REFRAN O UNA FRASE: ")

for letra in refran:
        if letra == "C" or letra == "c":
            C += 1
        elif letra == "S" or letra == "s":
            S += 1
        elif letra == "D" or letra == "d":
            D += 1
        elif letra == "L" or letra == "l":
            L += 1
        elif letra == "R" or letra == "r":
            R += 1
        elif letra == "M" or letra == "m":
            M += 1
        elif letra not in ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]:
            consonantes += 1

print ("CANTIDAD DE C: ",C)
print ("CANTIDAD DE S: ",S)
print ("CANTIDAD DE D: ",D)
print ("CANTIDAD DE L: ",L)
print ("CANTIDAD DE R: ",R)
print ("CANTIDAD DE M: ",M)
print ("CANTIDAD DE CONSONANTES: ",consonantes)






