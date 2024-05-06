# Variables

my_string_variable = 'My String Variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de Variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print(type(print(my_string_variable, my_int_to_str_variable, my_bool_variable)))
print('Este es mi valor de:', my_bool_variable)

# Funciones del sistema
print(len(my_int_to_str_variable))
print(len(my_string_variable))

# Variables en una sola linea, no abusar de esta sintaxis
name, surname, alias, age = 'Christian', 'Arguello', 'ArgueDev', 26
print(name, surname, alias, age)
print('Me llamo,', name, surname, 'mi edad es de', age, 'y mi alias es', alias)

# Inputs
'''
first_name = input('What is your name? ')
age = input('How old are you? ')
print(first_name)
print(age)
'''

# Cambiamos su tipo
name = 26
age = 'Christian'
print(name)
print(age)

# Forzamos el tipo
address: str = 'Mi Direccion'
address = 32
print(address)
print(type(address))