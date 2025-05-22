import math

# 1. Pedir un numero y muestre la raiz cuadrada y su cuadrado
# 2. Pedir el radio y usar math.pi para calcular el area del ciruclo

print('--- Ejercicio 1 ---')
num1 = int(input('Ingrese un numero: '))
raiz = math.sqrt(num1)
cuadrado = math.pow(num1, 2)
print(f'La raiz cuadrada de {num1} es: {raiz}')
print(f'Su cuadrado es: {cuadrado}')

print('--- Ejercicio 2 ---')
radio = float(input('Ingrese el radio del circulo: '))
area =  math.pi * math.pow(radio, 2)
print(f'El area del ciruclo es: {area}')