#Enésimo término U de una progresión aritmética
# u=a+(n-1)*r 
a=float(input("Ingrese primer término: ")) #usamos float para poder usar números con decimales 
u=float(input("Ingrese enésimo término: "))
r=float(input("Ingrese razón entre 2 términos consecutivos: "))
n=((u-a)/(r))+1
print("La cantidad de términos es: %8.2f"%n) #damos formato %c.pf para mostrar máximo 2 decimales

