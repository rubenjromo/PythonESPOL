a1=float(input("Ingrese 1era calificación para estudiante #1: "))
a2=float(input("Ingrese 2da calificación para estudiante #1: "))
a3=float(input("Ingrese 3ra calificación para estudiante #1: "))
b1=float(input("Ingrese 1era calificación para estudiante #2: "))
b2=float(input("Ingrese 2da calificación para estudiante #2: "))
b3=float(input("Ingrese 3ra calificación para estudiante #2: "))
#verificaremos calificacion por calificacion para el estudiante #1
'''Yo lo vi mas conveniente de esta manera aunque se haga un poco largo'''
if a1>a2>a3:  
    s1=a1+a2
elif a1>a3>a2:
    s1=a1+a3
elif a2>a3>a1:
    s1=a2+a3
elif a2>a1>a3:
    s1=a2+a1
elif a3>a1>a2:
    s1=a3+a1
elif a3>a2>a1:
    s1=a3+a2
#ahora verificaremos calificacion por calificacion para el estudiante #2
if b1>b2>b3:  
    s2=b1+b2
elif b1>b3>b2:
    s2=b1+b3
elif b2>b3>b1:
    s2=b2+b3
elif b2>b1>b3:
    s2=b2+b1
elif b3>b1>b2:
    s2=b3+b1
elif b3>b2>b1:
    s2=b3+b2
#ahora mostraremos cual estudiante tiene mayor calificacion final
if s1>s2:
    print("El estudiante #1 tiene mayor calificación final: %3.2f"%s1)
else:
    print("El estudiante #2 tiene mayor calificación final: %3.2f"%s2)

