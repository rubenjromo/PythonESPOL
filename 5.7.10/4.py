#cifras en orden opuesto
#más adelante veremos que esto se puede hacer más fácil con listas
n=int(input("Ingrese número de tres cifras:"))
n1=n//100 #el resultado nos deja la 1era cifra
n2=n%100  #esto nos deja las dos últimas cifras
n3=n2//10 #obtenemos número central
n4=n2%10  #obtenemos número final
print ("El número invertido es:",n4,n3,n1)
