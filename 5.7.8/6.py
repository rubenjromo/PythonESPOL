e=float(input("Ingrese nota del examen sobre 100 puntos:"))
e=e*0.7
l=float(input("Ingrese nota de la lección sobre 10 puntos:"))
l=l*0.2*10
t1=float(input("Ingrese nota del primer taller sobre 10 puntos:"))
t2=float(input("Ingrese nota del segundo taller sobre 10 puntos:"))
t3=float(input("Ingrese nota del tercer taller sobre 10 puntos:"))
tt=((t1+t2+t3)/3)*0.1*10
total=(tt+e+l)
print ("Calificación total sobre 100 es: %5.2f"%total)
