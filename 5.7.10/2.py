d=int(input("Ingrese cantidad de días:"))
a=d//30 #el resultado nos da los meses
m=d%30  #el residuo lo usaremos para calcular los meses
s=m//7  #número de semanas
di=m%7 #número de dias
print (d," días equivalen a: %5d meses, %6d semanas y %7d días"%(a,s,di))
