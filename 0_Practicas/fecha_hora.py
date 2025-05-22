from datetime import datetime

# 1. Muestra la fecha y hora actual con datetime
# 2. Pide al usuario su año de nacimiento y calcula su edad

print('--- Ejercicio 1 ---')
today = datetime.today()
print(today)

print('--- Ejercicio 2 ---')
year_birthday = int(input('Ingrese su año de nacimiento: '))
age = datetime.today().year - year_birthday
print(f'Tu edad es: {age}')