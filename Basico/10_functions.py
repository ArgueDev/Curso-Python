# Functions #

def my_function():
    print('Desde la funcion')

my_function()
my_function()
my_function()

def sumar(a: int, b: int):
    return a + b

resultado = sumar(5, 6)
print(resultado)

def sumar2(a: int, b: int):
    print(a + b)

def print_name(name, surname):
        print(f'Hola {name} {surname}')

print_name('Christian', 'Arguello')

def print_name_with_default(name = 'Sin Nombre', surname = 'Sin Apellido'):
    result = f'Hola {name} {surname}'
    return result

saludo = print_name_with_default()
print(saludo)
saludo2 = print_name_with_default('Christian', 'Mera')
print((saludo2))

def print_text(*texts):
    # print(text)
    for text in texts:
        print(text.upper())

print_text('Hola', 'Python', 'ArgueDev')