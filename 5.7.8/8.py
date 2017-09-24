#banco
p=float(input("Valor de cada depósito mensual: "))
n=float(input("Cantidad de depositos mensuales: "))
x=float(input("Tasa de interés mensual: "))
a=p*((((1+x)**n)-1)/x)
print("Valor acumulado %5.2f"%a)
