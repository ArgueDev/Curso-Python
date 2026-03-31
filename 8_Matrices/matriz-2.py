rows = 2
cols = 4
numbers = [[0 for j in range(4)] for i in range(2)]

for i in range(rows):
    for j in range(cols):
        numbers[i][j] = j + 1
        if i == 1:
            numbers[i][j]  += 10

print(numbers)