t=float(input("Ingrese temperatura: "))
p=int(input("Ingrese código 1 o 2: "))
if p==1:
    print("-----Conversión de grados farenheit a celsius-----")
    c=float((5/9)*(t-32))
elif p==2:
    print("-----Conversión de grados celsius a farenheit-----")
    c=float(32+(9*t/5))
else:
    print ("Error al ingresar codigo")
print (c)
