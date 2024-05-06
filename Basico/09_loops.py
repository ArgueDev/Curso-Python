# Loops #

# While
condition = 0

while condition < 10:
    print(condition)
    condition += 2
else:  # Es Opcional
    print('Mi condicion es mayor o igual que 10')


print('La ejecucion continua')

condition2 = 0

while condition2 < 20:
    condition2 += 1

    if condition2 == 15:
        print("Se detiene la ejecucion")
        break

    print(condition2)


# For

lista = [35, 24, 62, 52, 30, 30, 17]

for element in lista:
    print(element)

tupla = (35, 1.77, "Brais", "Moure", "Brais")
print('-- Tupla --')
for e in tupla:
    print(e)

sets = {"Brais", "Moure", 35}
print("-- Set --")
for e in sets:
    print(e)

dicts = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}
print('-- Dict --')
for e in dicts.values():
    print(e)

for e in range(1, 11):
    print(e)

personas = [("JUAN", 25), ("MARÍA", 30), ("PEDRO", 20)]

for nombre, edad in personas:
    print("NOMBRE:", nombre)
    print("EDAD:", edad)
