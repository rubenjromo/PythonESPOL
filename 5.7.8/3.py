
a=float(input("Ingrese el ancho: ")) #usamos float para poder usar números con decimales 
l=float(input("Ingrese el largo: "))
h=float(input("Ingrese la altura: "))
at=(2*a*l)+(2*a*h)+(2*h*l)
v=a*l*h
print("El area total es: %8.2f"%at) #damos formato %c.pf para mostrar máximo 2 decimales
print("El volumen es: %8.2f"%v)
