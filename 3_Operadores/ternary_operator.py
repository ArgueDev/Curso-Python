# Operadores Ternario

age = 17
message = 'Mayor de edad' if age >= 18 else 'Menor de edad'
print(message)

math = float(input('Ingrese la nota de matematicas entre 2 y 7: '))
sciences = float(input('Ingrese la nota de ciencias entre 2 y 7: '))
history = float(input('Ingrese la nota de historia entre 2 y 7: '))

grade = (math + sciences + history)/3

state = 'Aprobado' if grade >= 4.99 else 'Reprobado'
print(f'\n{state} con {grade}')

# Calcular el numero mayor
number1 = int(input('Ingrese un numero: '))
number2 = int(input('Ingrese un numero: '))
number3 = int(input('Ingrese un numero: '))

numbers = [number1, number2, number3]
max = 0

for number in numbers:
    max = max if max > number else number

# max = number1 if number1 > number2 else number2
# max = max if max > number3 else number3

print(f'El numero mayor es: {max}')