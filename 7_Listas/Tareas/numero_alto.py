"""
Escriba un programa que imprima el número más alto de un arreglo de 7 elementos (de rango 11 a 99), por ejemplo {14, 33, 15, 36, 78, 21, 43}, si se repite un valor considerar uno solo.
"""

# Llenar arreglo
a = [int(input(f"Elemento {i+1}: ")) for i in range(7)]

# Encontrar máximo sin duplicados
maximo = max(set(a))
print(f"Arreglo: {a}")
print(f"Máximo (sin considerar duplicados): {maximo}")