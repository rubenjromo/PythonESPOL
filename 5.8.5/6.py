kw=float(input("Ingrese cantidad de kw: "))
p=float(input("Precio por kw: $"))
if kw>700:
    t=(700*p)+((kw-700)*1.05*p)
else:
    t=kw*p
print("Valor total a pagar: $%3.2f"%t) #damos formato para que solo se muestren 2 decimales
