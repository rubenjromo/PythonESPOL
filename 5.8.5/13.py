"""3 trabajadores"""
h1=int(input("Ingrese horas trabajador 1: "))
s1=float(input("Salario por hora:$ "))
d1=float(input("Descuentos:$ "))
h2=int(input("Ingrese horas trabajador 2: "))
s2=float(input("Salario por hora:$ "))
d2=float(input("Descuentos:$ "))
h3=int(input("Ingrese horas trabajador 3: "))
s3=float(input("Salario por hora:$ "))
d3=float(input("Descuentos:$ "))
t1=h1*s1-d1
t2=h2*s2-d2
t3=h3*s3-d3
if t1>t2>t3 or t1>t3>t2:
    print("El trabajador 1 recibirá el mayor pago semanal $%3.2f"%t1)
elif t2>t1>t3 or t2>t3>t1:
    print("El trabajador 2 recibirá el mayor pago semanal $%3.2f"%t2)
else :
    print("El trabajador 3 recibirá el mayor pago semanal $%3.2f"%t3)    
