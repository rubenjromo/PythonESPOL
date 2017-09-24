from math import * #importamos math para usar pi
r=float(input("Radio del cilindro: "))
h=float(input("Altura del cilindro:"))
if h>r:
    v=pi*(r**2)*h
    print("El volumen es: %5.2f"%v)
else:
    a=2*pi*r*h
    print("Área lateral del cilindro: %5.2f"%a)
