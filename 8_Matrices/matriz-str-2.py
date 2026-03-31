matriz = [None] * 3

matriz[0] = [0] * 2
matriz[1] = [0] * 2
matriz[2] = [0] * 2

print('Matriz len: ', len(matriz))
print('Fila 0 len: ', len(matriz[0]))
print('Fila 1 len: ', len(matriz[1]))
print('Fila 2 len: ', len(matriz[2]))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = i * j

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end='\t')
    print()