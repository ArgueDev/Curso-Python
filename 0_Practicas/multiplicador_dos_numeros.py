"""
Se pide dos números enteros positivos o negativos, pero sin usar el símbolo de multiplicación (*).

Puede utilizar una sentencia for para realizar la multiplicación y tener en cuenta los unarios, donde menos por menos es positivo.
"""

print('Ingrese dos numeros enteros positivos o negativos')
num1 = int(input('Numero 1: '))
num2 = int(input('Numero 2: '))
resultado = 0

for _ in range(abs(num2)):
    resultado += num1

if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
    resultado = -resultado

print(f'El resultado de la multiplicacion es: {resultado}')