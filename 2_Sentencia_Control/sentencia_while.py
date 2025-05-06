count = 0
while count <= 5:
    print(f'Count: {count}')
    count += 1


count2 = 0
names = ['Andres', 'Pepe', 'Jhon', 'Juan', 'Maria']
while count2 < len(names):
    print(f'Nombre en posicion {count2}: {names[count2]}')
    count2 += 1

print('--Do While--')
i = 0
while True:
    print(i)
    i += 1
    if i >= 10:
        break;


print('--Do While Ejemplo Practico--')
correct_number = 7
while True:
    attempt = int(input('Adivina el numero: '))
    if attempt == correct_number:
        print('Correcto! has adivinado el numero')
        break
    else:
        print('Incorrecto, intenta de nuevo!')