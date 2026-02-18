"""
El desafío es un programa que pida dos números y los muestre ordenados de mayor a menor.

Podría ser utilizando operador ternario.
"""
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 == num2:
    print(f"Los números son iguales: {num1}")
else:
    mayor = num1 if num1 > num2 else num2
    menor = num2 if num1 > num2 else num1
    print(f"Los números ordenados de mayor a menor son: {mayor}, {menor}")