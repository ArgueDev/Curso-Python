# 1. Solicitar la cantidad de números a comparar
n = int(input("Ingrese la cantidad de números a comparar (mínimo 10): "))

# Validación opcional para asegurar el mínimo de 10
while n < 10:
    print("Por favor, ingrese un número mayor o igual a 10.")
    n = int(input("Ingrese la cantidad de números a comparar: "))

# 2. Inicializamos la variable menor con un valor muy grande
# float('inf') representa el infinito matemático
menor_numero = float('inf')

# 3. Sentencia for para iterar n veces
for i in range(n):
    numero = int(input(f"Ingrese el número entero {i + 1}: "))

    # Comprobar si el número actual es menor al guardado
    if numero < menor_numero:
        menor_numero = numero

# 4. Imprimir el valor menor encontrado
print(f"\nEl número menor es: {menor_numero}")

# 5. Lógica de impresión según el valor del menor
if menor_numero < 10:
    print("El número menor es menor que 10!")
else:
    print("El número menor es igual o mayor que 10!")