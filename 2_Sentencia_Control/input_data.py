# Ingreso de datos por consola

try:
    name = input('Introduce tu nombre: ')
    print(f'Hola, {name}')

    price = int(input('Introduce el precio del producto en dolares: '))
    print(f'El valor final ${price} dolares')

    weight = float(input('Introduce el peso en gramos: '))
    print(f'Pesa: {weight} gramos')
except ValueError:
    print('Error: debe introducir bien los datos, decimal es con punto!')