"""
Leer 7 números por teclado para llenar una lista y a continuación calcular el promedio de los números positivos, el promedio de los negativos y contar el número de ceros.
"""

# Inicializar contadores y acumuladores
suma_pos = 0
suma_neg = 0
count_pos = 0
count_neg = 0
ceros = 0

# Leer y procesar los 7 números
print("Ingresa 7 números:")
for i in range(7):
    num = float(input(f"Número {i + 1}: "))

    if num > 0:
        suma_pos += num
        count_pos += 1
    elif num < 0:
        suma_neg += num
        count_neg += 1
    else:
        ceros += 1

# Calcular promedios
prom_pos = suma_pos / count_pos if count_pos > 0 else 0
prom_neg = suma_neg / count_neg if count_neg > 0 else 0

# Mostrar resultados
print("\nRESULTADOS:")
print(f"Promedio de positivos: {prom_pos:.2f}")
print(f"Promedio de negativos: {prom_neg:.2f}")
print(f"Cantidad de ceros: {ceros}")