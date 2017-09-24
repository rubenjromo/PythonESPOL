#crecimiento poblacional
from math import * #importamos libreria math para poder usar e
t5=5  
t10=10
t20=20
n5=(5*t5)+(2*(e**(0.1*t5)))
n10=(5*t10)+(2*(e**(0.1*t10)))
n20=(5*t20)+(2*(e**(0.1*t20)))
print("En 5 años el número de habitantes será: %5d"%n5) #damos formato para que solo salgan números enteros
print("En 10 años el número de habitantes será: %5d"%n10)
print("En 20 años el número de habitantes será: %5d"%n20)

