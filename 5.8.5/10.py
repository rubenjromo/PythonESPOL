#lados de un triangulo
x=int(input("Ingrese 1er lado del triángulo: "))
y=int(input("Ingrese 2do lado del triángulo: "))
z=int(input("Ingrese 3er lado del triángulo: "))
if x==y==z:
    print("El triángulo es equilatero")
elif x==y!=z or x!=y==z or x==z!=y:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")
