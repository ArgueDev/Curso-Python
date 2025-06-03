numbers = [0] * 5
numbers[0] = 1
numbers[1] = 2
numbers[2] = 3
numbers[3] = 4
numbers[4] = 'Christian'

i = numbers[0]
j = numbers[1]
k = numbers[2]
l = numbers[3]
m = numbers[4]

print(f'i = {i}')
print(f'j = {j}')
print(f'k = {k}')
print(f'l = {l}')
print(f'm = {m}')

# Accedemos al utlimo elemento
print(f'Ultimo Elemento: {numbers[len(numbers)-1]}')

for elemento in numbers:
    print(elemento)


for i in range(len(numbers)):
    print(f'Indice {i}: {numbers[i]}')