from math import* #importamos libreria math para usar PI
v=float(input("Ingrese volumen en litros: ")) #usamos float para poder usar números con decimales 
h=float(input("Ingrese altura: "))
r=sqrt((v)/pi*h)  #despejando radio
d=2*r #diametro
print("El diametro de la base es: %8.2f"%d) #damos formato %c.pf para mostrar máximo 2 decimales
