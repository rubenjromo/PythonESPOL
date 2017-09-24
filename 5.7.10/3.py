n1=int(input("Ingrese 1er número de tres cifras:"))
n2=int(input("Ingrese 2do número de tres cifras:"))
n1=n1%100 #el resultado nos deja las 2 ultimas cifras, el residuo
n1=n1//10  #esto nos deja la 1er cifra de las 2 obtenidas anteriormente, es decir, nuetro termino central
n2=n2%100 
n2=n2//10
s=n1+n2
print ("La suma de las cifras centrales es%5d"%s)
