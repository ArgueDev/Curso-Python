import platform, os
from os import mkdir

# 1. Muestra el sistema operativo, version de python, nombre del usuario
# 2. Crear carpeta desde python

print('--- Ejercicio 1 ---')
name_system = platform.system()
python_version = platform.python_version()
user_name = os.getlogin()
print(f'El sistema operativo es: {name_system}')
print(f'La version de python es: {python_version}')
print(f'Nombre del usuario: {user_name}')

print('--- Ejercicio 2 ---')
mkdir('Nueva Carpeta')
