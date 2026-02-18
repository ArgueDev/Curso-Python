"""
programa que imprima el número que tiene más ocurrencias en la lista y también imprimir la cantidad de veces que aparece en el arreglo.

Por ejemplo, para el arreglo: {1, 2, 3, 3, 4, 5, 5, 5, 6, 7}

Como resultado debería imprimir lo siguiente:

La mayor ocurrencias es: 3 El elemento que mas se repite es: 5
En el ejemplo, el elemento que más se repite en el arreglo es el número 5 con una ocurrencia de 3 veces.
"""

# Lista de ejemplo (puedes modificarla o pedirla al usuario)
arreglo = [1, 2, 3, 3, 4, 5, 5, 5, 6, 7]

# Crear un diccionario para contar ocurrencias
contador = {}

for numero in arreglo:
    if numero in contador:
        contador[numero] += 1
    else:
        contador[numero] = 1

# Encontrar el número con más ocurrencias
max_ocurrencias = 0
elemento_mas_repetido = None

for numero, ocurrencias in contador.items():
    if ocurrencias > max_ocurrencias:
        max_ocurrencias = ocurrencias
        elemento_mas_repetido = numero

# Mostrar resultado
print(f"La mayor ocurrencias es: {max_ocurrencias} El elemento que mas se repite es: {elemento_mas_repetido}")
