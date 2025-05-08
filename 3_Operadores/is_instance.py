# Operador de instancia

num = 10
text = 'Creando un objeto de clase str'
num_decimal = 3.14

b1 = isinstance(text, str)
print(f'Text es del tipo str = {b1}')

b2 = isinstance(num, int)
print(f'Num es del tipo int = {b2}')

b3 = isinstance(num_decimal, float)
print(f'Decimal es del tipo float = {b3}')

b4 = isinstance(text, int)
print(f'Text es del tipo int = {b4}')

b5 = isinstance(num, str)
print(f'Num es del tipo str = {b5}')

b6 = isinstance(num_decimal, int)
print(f'Decimal es del tipo int = {b6}')

b7 = isinstance(b5, bool)
print(f'b5 es de tipo bool = {b7}')