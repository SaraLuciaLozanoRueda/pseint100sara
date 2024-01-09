val = int
contador = int
espa = str
num = 0
val = 1

print("MUESTRA GRAFICA DE NUMEROS COMO TRIANGULO.")
while (num<3):
	print("INGRESE NUMERO : ", end="")
	num = int(input())
print("")

for x in range(1,num+1):
	espa = ""
	for z in range(1,(num-x)+1):
		espa = espa+" "
	print(espa, end="")
	contador = 1
	for f in range(1,val+1):
		print(contador, end="")
		if (contador==9):
			contador = 0
		else:
			contador = contador+1
	val = val+2
	print("")