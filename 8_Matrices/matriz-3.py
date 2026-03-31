rows = 4
cols = 3
matriz = []
counter = 0

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j + 1)
    matriz.append(row)

for i in range(rows):
    for j in range(cols):
        print(matriz[i][j], end=' ')
    print()


print(matriz)