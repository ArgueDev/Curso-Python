# Manejo de Paquetes

# pip
import numpy # pip install numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 23, 44, 12, 39, 10, 2])

print(type(numpy_array))

print(numpy_array * 2)


import requests # pip install requests

respuesta = requests.get('https://pokeapi.co/api/v2/pokemon?limit=5')
print(respuesta)
print(respuesta.status_code)
print(respuesta.json())

# Paquete Aritmetico
from mypackage import arithmetics

print(arithmetics.suma(2,4 ))