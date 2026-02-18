"""
Llenar un arreglo de 10 elementos. Luego debemos mostrarlos en el siguiente orden: el último, el primero, el penúltimo, el segundo, el antepenúltimo, el tercero, y así sucesivamente.
"""

print('Ingresa 10 numeros')
arreglo = []

for i in range(10):
    num  = int(input(f'Numero {i+1}: '))
    arreglo.append(num)

print('Arreglo original: ', arreglo)
print('Orden Solicitado: ', end='')

for i in range(5):
    print(arreglo[9-i], arreglo[i], end=' ')
