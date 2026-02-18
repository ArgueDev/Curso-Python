"""
Escribir un programa que recorra una lista y genere un histograma en base a los valores de este.

La lista debe contener 12 elementos que corresponden a números enteros de rango 1 al 6.

Un histograma es una representación gráfica (de puntos o barra) de que tanto un elemento aparece en un conjunto de datos, es decir debe mostrar la frecuencia para todos los números del 1 al 6,
incluso si no están presente en el arreglo.

Por ejemplo para el arreglo {4, 3, 4, 6, 6, 4, 1, 4, 5, 4, 1, 1} el histograma debería ser:

1: ***
2:
3: *
4: *****
5: *
6: **
Para la tarea usaremos el asterisco(*) como representación gráfica para el histograma.
"""

# Lista de ejemplo
arreglo = [4, 3, 4, 6, 6, 4, 1, 4, 5, 4, 1, 1]

# Inicializar contador para números del 1 al 6
frecuencias = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Contar frecuencias
for numero in arreglo:
    if 1 <= numero <= 6:
        frecuencias[numero] += 1

# Generar histograma
print("Histograma:")
for numero in range(1, 7):
    print(f"{numero}: {'*' * frecuencias[numero]}")