#abscisas y ordenadas
from math import *
x=int(input("Ingrese valor abscisa punto 1: "))
y=int(input("Ingrese valor ordenada punto 1: "))
z=int(input("Ingrese valor abscisa punto 2 "))
w=int(input("Ingrese valor ordenada punto 2: "))
p1=sqrt(x**2+y**2)
p2=sqrt(z**2+w**2)
if p1<p2:
    print("El punto 1 es el más cercano al origen")
else:
    print("El punto 2 es el más cercano al origen")
