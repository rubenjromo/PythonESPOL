#suma de dos cifras y determinar si es par o impar
'''En este ejercicio podemos usar divmod(x,y) que nos entrega el par
(x//y,x%y)'''
x=int(input("Ingrese número de 2 cifras: "))
[a,b]=divmod (x,10) #al usar esto nos queda en a el valor de la 1era cifra y en b la 2da cifra
s=a+b #sumamos la 2 cifras
#ahora verificaremos si la suma es par
if s%2==0:
    print("La suma de ambas cifras es un número par: ",s)
else:
    print("La suma de ambas cifras es un número impar: ",s)
