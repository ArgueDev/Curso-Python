"""
Pedir 20 notas finales de alumnos en una escala de 1 a 7, manejar decimales en las notas (float). Mostrar el promedio de las notas mayores a 5,
promedio de notas inferiores a 4 y la cantidad de notas 1, ademas mostrar el promedio total.

Ayuda: usar un bucle for que itere hasta 20 (notas) y dentro del ciclo pedir las notas una a una para realizar los cálculos (contadores, sumas).

Opcional: si una de las notas ingresadas es 0 debe salirse del ciclo for y mostrar un mensaje de error finalizando el programa.
"""

# Inicializamos las variables necesarias
suma_mayores_5 = 0
cant_mayores_5 = 0

suma_inferiores_4 = 0
cant_inferiores_4 = 0

cant_notas_1 = 0
suma_total = 0

print('Ingrese las notas de los alumnos en una escala del 1.0 al 7.0')

for i in range(20):
    while True:
        try:
            nota = float(input(f'Alumno No {i + 1}: '))

            # Opcional: Salida por nota 0
            if nota == 0:
                print('Error: No se pueden ingresar notas 0. Finalizando programa...')
                exit()  # Detiene la ejecución completa

            if 1 <= nota <= 7:
                break  # Nota válida, salimos del while
            else:
                print('La nota debe estar entre 1.0 y 7.0')
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # --- Procesamiento de datos ---
    suma_total += nota

    # 1. Notas mayores a 5
    if nota > 5:
        suma_mayores_5 += nota
        cant_mayores_5 += 1

    # 2. Notas inferiores a 4
    if nota < 4:
        suma_inferiores_4 += nota
        cant_inferiores_4 += 1

    # 3. Cantidad de notas 1
    if nota == 1:
        cant_notas_1 += 1

# --- Cálculos Finales ---
# Usamos una validación simple para evitar dividir por cero si no hay notas en una categoría
prom_mayores_5 = suma_mayores_5 / cant_mayores_5 if cant_mayores_5 > 0 else 0
prom_inferiores_4 = suma_inferiores_4 / cant_inferiores_4 if cant_inferiores_4 > 0 else 0
promedio_total = suma_total / 20

# --- Resultados ---
print("-" * 30)
print(f"Promedio total del curso: {promedio_total:.2f}")
print(f"Promedio de notas > 5: {prom_mayores_5:.2f} (Total: {cant_mayores_5})")
print(f"Promedio de notas < 4: {prom_inferiores_4:.2f} (Total: {cant_inferiores_4})")
print(f"Cantidad de alumnos con nota 1.0: {cant_notas_1}")
print("-" * 30)

