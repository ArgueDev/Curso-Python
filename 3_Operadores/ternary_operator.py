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