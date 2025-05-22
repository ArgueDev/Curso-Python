# 1. Pedir dos numeros al usuario e imprimir cual es el mayor, menor o si son iguales
# 2. Pedir un numero y determinar si es positivo, negativo o cero
# 3. Menu de opciones

print('--- Ejecicio 1 ---')
num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

if num1 == num2:
    print('Son Iguales')
elif num1 > num2:
    print(f'{num1} es el mayor')
else:
    print(f'{num2} es el mayor')

print('--- Ejercicio 2 ---')
num3 = int(input('Ingrese un numero: '))

if num3 == 0:
    print('Es 0')
elif num3 < 0:
    print('Es negativo')
else:
    print('Es positivo')

print('--- Ejericio 3 ---')
print('''
1. Saludar
2. Despedir
3. Salir
''')

option = int(input('Elige una opcion: '))

match option:
    case 1:
        print('Hola, Bienvenido')
    case 2:
        print('Adios, gracias por usar mi programa')
    case 3:
        exit(0)
    case _:
        print('Opcion no valida')