# Ejemplo de login con logica de operadores

user_names = ['andres', 'arguedev', 'admin', 'pepe', 'josefa']
passwords = ['1234', '5678', '9012', '3456', '7890']

user = input('Ingrese el user name: ')
password = input('Ingrese la clave: ')

authenticaded = False

for i in range(len(user_names)):
    if user_names[i] ==  user and passwords[i] == password:
        authenticaded = True
        break

if authenticaded:
    print(f'Bienvenido usuario {user}')
else:
    print('User o password incorrecto!')