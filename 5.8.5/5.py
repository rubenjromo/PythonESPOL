#multiplo de 7
x=input("Ingrese un número: ")
x=int(x)
s=x%7  #calculamos el residuo, si da 0 es múltiplo de 7
#isinstance nos sirve para verificar si una variable de cierto tipo
if isinstance(x,int) and s==0: 
    print (x,"es un número entero y múltiplo de 7")
else:
    print("No es entero")
    
