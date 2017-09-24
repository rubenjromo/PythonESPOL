from math import *
x=float(input("Ingrese largo del bloque: "))
y=float(input("Ingrese ancho del bloque: "))
z=float(input("Ingrese altura del bloque: "))
w=float(input("Ingrese diametro del agujero: "))
#ahora calcularemos las diagonales
d1=sqrt(x**2+y**2)
d2=sqrt(x**2+z**2)
d3=sqrt(z**2+y**2)
#verificamos si alguna diagonal es menor al diametro del agujero
if w<d1 or w<d2 or w<d3:
    print("El bloque no pasa por el agujero")
else :
    print("Si pasa por el agujero")
