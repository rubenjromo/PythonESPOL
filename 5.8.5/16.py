g=str(input("Ingrese F para femenino o M para masculino: "))
g=g.lower()
e=int(input("Ingrese edad: "))
if g=="f": #verificamos que ingrese f y lo ponemos entre comillas porque es un string y no una variable
    p=(220-e)/10 #Número de pulsaciones
    print("Número de pulsaciones: %3.2f"%p) #damos formato 2 decimales 
elif g=="m":
    p=(210-e)/10
    print("Número de pulsaciones: %3.2f"%p) 
else:
    print("No ingresó F o M")
    

