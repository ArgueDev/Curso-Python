numbers = [
    [1, 2, 3, 4],
    [11, 12, 13, 14],
]

print(numbers)
print('Numero de filas: ', len(numbers))
print(f'Numero de columnas: {len(numbers[0])}')
print(f'Primer elemento de la matriz: {numbers[0][0]}')
print(f'Ultimo elemento de la matriz: {numbers[len(numbers)-1][len(numbers[1])-1]}')
print(f'Ultimo elemento de la matriz: {numbers[-1][-1]}')
print(f'Penultimo elemento de la matriz: {numbers[-1][-2]}')

num1 = numbers[0][0]
num2 = numbers[0][1]
num3 = numbers[0][2]
num4 = numbers[0][3]

num5 = numbers[1][0]
num6 = numbers[1][1]
num7 = numbers[1][2]
num8 = numbers[1][3]

print(f'num1: {num1}')
print(f'num2: {num2}')
print(f'num3: {num3}')
print(f'num4: {num4}')
print(f'num5: {num5}')
print(f'num6: {num6}')
print(f'num7: {num7}')
print(f'num8: {num8}')