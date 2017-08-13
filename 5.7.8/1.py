from math import* #importamos libreria math para usar PI
r=float(input("Ingrese radio:")) #usamos float para poder usar números con decimales 
h=float(input("Ingrese altura:"))
al=2*pi*r*h #area lateral del cilindro
at=2*pi*r*(h+r) #area total 
v=pi*(r**2)*h #volumen
print("El area lateral es: %8.2f"%al) #damos formato %c.pf para mostrar máximo 2 decimales
print("El area total es: %8.2f"%at)
print("El volumen es: %8.2f"%v)
