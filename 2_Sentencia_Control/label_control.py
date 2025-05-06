# Break
for number in range(10):
    if number == 5:
        break

    print(number)

# Pass
print('--------')
for number in range(10):
    if number == 5:
        pass

    print(number)

# Continue
print('--------')
users = ['Andrea', 'Pedro', 'Anonimo', 'Marta', 'Diego']

for user in users:
    if user == 'Anonimo':
        print('Usuario restringido')
        continue

    print(f'Bienvenido: {user}')