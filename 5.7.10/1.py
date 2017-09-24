d=int(input("Ingrese cantidad de días:"))
a=d//365 #el resultado nos da los años
m=d%365  #el residuo lo usaremos para calcular los meses
s=m//30  #número de meses
di=m%30 #número de dias
print (d," días equivalen a: %5d años, %6d meses y %7d días"%(a,s,di))
