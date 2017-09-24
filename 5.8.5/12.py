x=int(input("Ingrese cantidad de artículos: "))
p=float(input("Precio unitario del producto: $"))
if x<=5:
    p=p
elif 5<x<10:
    p=p*0.95
else x>=10:
    p=p*0.92
t=x*p
print("Valor total a pagar: $%3.2f"%t)
