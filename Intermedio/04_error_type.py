# Error Types #

# --- Syntax Error --- #
# print 'Hola Comunidad' # Error
print('Hola Comunidad')

# --- NameError --- #
# print(name) # Error
nombre = 'Christian'
print(nombre)

# --- IndexError --- #
lista = ['Python', 'Dart', 'JavaScript', 'Java']
print(lista[0])
# print(lista[4]) # Error

# --- ModuleNotFoundError --- #
# import maths # Error
import math

# --- AttributeError --- #
# print(math.PI) # Error
print(math.pi)

# --- KeyError --- #
dictionario = {'nombre': 'Christian', 'apellido': 'Arguello', 'edad': 25}
print(dictionario['edad'])
# print(dictionario['apelido']) # Error

# --- TypeError --- #
# print(lista['0']) # Error
print(lista[0])

# --- ImportError --- #
# from math import PI # Error
from math import  pi
print(pi)

# --- ValueError --- #
my_int = int('10')
# my_int = int('10 luces') # Error
print(my_int)

# --- ZeroDivisonError --- #
print( 4 / 2 )
# print( 4 / 0 ) # Error

