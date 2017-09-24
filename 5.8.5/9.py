a1=float(input("Ingrese 1era calificación para estudiante: "))
a2=float(input("Ingrese 2da calificación para estudiante: "))
a3=float(input("Ingrese 3ra calificación para estudiante: "))
#verificaremos calificacion por calificacion para el estudiante
'''Mas adelante veremos que facilmente se lo puede resolver con min y max'''
if a1>a2>a3:  
    print("La mayor calificación es: ",a1)
    print("La menor calificación es: ",a3)
elif a1>a3>a2:
    print("La mayor calificación es: ",a1)
    print("La menor calificación es: ",a2)
elif a2>a3>a1:
    print("La mayor calificación es: ",a2)
    print("La menor calificación es: ",a1)
elif a2>a1>a3:
    print("La mayor calificación es: ",a2)
    print("La menor calificación es: ",a3)
elif a3>a1>a2:
    print("La mayor calificación es: ",a3)
    print("La menor calificación es: ",a2)
elif a3>a2>a1:
    print("La mayor calificación es: ",a3)
    print("La menor calificación es: ",a1)
