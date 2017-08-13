#Enésimo término U de una progresión aritmética
# u=a+(n-1)*r 
a=float(input("Ingrese primer término: ")) #usamos float para poder usar números con decimales 
u=float(input("Ingrese enésimo término: "))
n=float(input("Ingrese cantidad de términos: "))
r=(u-a)/(n-1)
print("La razón es: %8.2f"%r) #damos formato %c.pf para mostrar máximo 2 decimales

