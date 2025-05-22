import random
import math

random_val = random.random() * 10
print('Numero aleatorio: ', random_val)

random_ceil = math.ceil(random_val)
print(f'Numero aleatorio redondeado hacia arriba: {random_ceil}')

colors = ['azul', 'blanco', 'amarillo', 'rojo', 'verde', 'negro']
num = random.random() * len(colors)
random_color = math.floor(num)
print(f'Color aleatorio: {colors[random_color]}')

random_int = random.randint(15, 25)
new_random_color = random.randint(0, len(colors)-1)
print(random_int)
print(f'Color aleatorio 2: {colors[new_random_color]}')

random_range = random.randrange(20)
print(random_range)