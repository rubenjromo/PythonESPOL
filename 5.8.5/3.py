#mayor diagonal de un bloque
from math import *
x=float(input("Ingrese largo del bloque rectangular: "))
y=float(input("Ingrese ancho del bloque rectangular: "))
z=float(input("Ingrese altura del bloque rectangular: "))
#ahora calcularemos las diagonales
d1=sqrt((x**2)+(y**2))
d2=sqrt((x**2)+(z**2))
d3=sqrt((z**2)+(y**2))
'''
print (d1) PARA COMPROBAR PODEMOS IMPRIMIR LOS
print (d2) RESULTADOS DE LAS DIAGONALES Y VERIFICAR  
print (d3) QUE EFECTIVAMENTE NOS MUESTRA EL VALOR DE LA DIAGONAL MAYOR
'''
#conditional if para clasificar e imprimir la diagonal mayor
if d1>d2>d3 or d1>d3>d2:  #nos aseguramos que d1 sea mayor a todas
    print("La diagonal mayor es: %5.2f"%d1)
elif d2>d1>d3 or d2>d3>d1: #nos aseguramos que d2 sea mayor a todas
    print("La diagonal mayor es: %5.2f"%d2)
else:  #por descarte solo nos queda d3
    print("La diagonal mayor es: %5.2f"%d3)
