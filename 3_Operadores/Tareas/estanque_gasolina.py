"""
Suponiendo un estanque de gasolina (gas) con capacidad 70 litros, se requiere un programa que pida la medida actual en litros y mostrar el resultado de la forma:
Insuficiente, Suficiente, Medio...
La medida o capacidad actual del estanque puede ser en tipo float, para una mejor precisión, pero también puede ser del tipo int.
Si la capacidad actual es 70 litros: imprimir Estanque lleno
Si está entre 60 y menor a 70: imprimir Estanque casi lleno
Si está entre 40 y menor a 60: imprimir Estanque 3/4
Si está entre 35 y menor a 40: imprimir Medio Estanque
Si está entre 20 y menor a 35: imprimir Suficiente
Si está entre 1 y menor a 20: imprimir Insuficiente
"""

print('Ingrese la cantidad actual del estanque de gasolina (max 70)')
cantidad = float(input('Cantidad: '))

if cantidad < 0 or cantidad > 70:
    print('Cantidad no válida. Debe estar entre 0 y 70 litros')
elif cantidad == 70:
    print('Estanque lleno')
elif 60 <= cantidad < 70:
    print('Estanque casi lleno')
elif 40 <= cantidad < 60:
    print('Estanque 3/4')
elif 35 <= cantidad < 40:
    print('Medio Estanque')
elif 20 <= cantidad < 35:
    print('Suficiente')
elif 1 <= cantidad < 20:
    print('Insuficiente')
else:  # cantidad == 0
    print('Estanque vacío')