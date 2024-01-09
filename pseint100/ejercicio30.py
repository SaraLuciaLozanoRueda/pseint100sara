muj=0

empleados=int(input("CANTIDAD DE EMPLEADOS: "))

for cont in range (1,empleados+1):
    print ("EMPLEADO NRo",cont,"/",empleados)
    nombre=input("NOMBRE: ")
    genero=input("GENERO (H/M): ")
    ventas=int(input("VENTAS: "))
    
    if genero== "H" or genero=="h":
        TVH = + ventas
    elif genero == "M" or genero=="m":
        TVM = + ventas  
        muj += 1

porcentaje= (muj *100)/empleados

print ("TOTAL DE VENTAS HOMBRES: ",TVH)
print ("TOTAL DE VENTAS MUJERES: ",TVM)    

print ("PORCENTAJE DE MUJERES:   ",porcentaje,"%") 
    
    
    