# Agregar un elemento en una posicion adecuada de manera que se mantenga ordenada

numbers = [0] * 10

for i in range(len(numbers)):
    numbers[i] = int(input('Ingrese un numero: '))


element = int(input('Nuevo elemento: '))
position = next((i for i in range(len(numbers) - 1) if element <= numbers[i]), len(numbers) - 1)

for i in range(len(numbers) -2, position -1, -1):
    numbers[i + 1] = numbers[i]


numbers[position] = element
print(numbers)