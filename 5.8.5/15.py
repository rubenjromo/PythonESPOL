a=int(input("Ingrese código de 3 cifras: "))
b=a//10 #con esto obtenemos las 2 primeras cifras
c=a%10 #obtenemos la última cifra (3era)
d=b//10 #nos queda solo la 1era cifra
e=b%10 #nos queda solo la 2da cifra
f=d*e #multiplicamos la 1era con la 2da cifra
#ahora verificaremos si la multiplicación es el módulo de la 3era cifra
if f%10==c:
    print(a, "Es un código válido pues el módulo de %d x %d en 10 es igual a %d"%(d,e,c))
else :
    print("No es un código válido")
