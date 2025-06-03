# Imprimiendo el i-esimo numero por el principio y el i-esimo por el final

numbers = [0] * 10
result = [0] * 10

for i in range(len(numbers)):
    numbers[i] = i + 1

for i in range(len(numbers)):
    print(f'{numbers[i]}: {numbers[len(numbers)-1-i]}')

index = 0
for i in range(len(numbers) // 2):
    result[index] = numbers[i]
    index += 1
    result[index] = numbers[len(numbers)-1-i]
    index += 1

for i in range(len(result)):
    print(f'i = {i} value: {result[i]}')