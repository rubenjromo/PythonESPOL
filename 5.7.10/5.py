#menor número de billetes
#es muy parecido al ejercicio de años, meses y dias
d=int(input("Ingrese cantidad de dolares: "))
b100=d//100  #cantidad de billetes de 100
d=d%100
b50=d//50 #cantidad de billetes de 50
d=d%50 #para este momento d ya no tiene el valor original
print("Cantidad de billetes de $100: ",b100)
print("Cantidad de billetes de $50: ",b50)
#queda para el lector seguir el mismo procedimiento para los otros billetes de 20,10, etc
