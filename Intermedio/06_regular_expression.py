# Expresiones regulares #

import re

my_string = 'Esta es la leccion 6: Leccion llamada Expresiones regulares'
my_other_string = 'Esta no es la leccion 6: Manejo de ficheros'

match = re.match('Esta es la leccion', my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

print(re.match('Esta es la leccion', my_other_string))
print(re.match('Expresiones regulares', my_string))

# -- search -- #

search = re.search('leccion', my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# -- findall -- #

findall = re.findall('leccion', my_string, re.I)
print(findall)

# -- split -- #

split = re.split(':', my_string)
print(split)

# -- sub -- #

sub = re.sub('Expresiones', 'expresiones', my_string)
sub2 = re.sub('leccion|Leccion', 'LECCION', my_string)
print(sub)
print(sub2)

# -- Patterns -- #
pattern = r'[lL]eccion'
print(re.findall(pattern, my_string))

pattern = r'[lL]eccion|Expresiones'
print(re.findall(pattern, my_string))

pattern = r'[a-z]'
pattern = r'[0-9]'
print(re.findall(pattern, my_string))

pattern =  r'\d'
print(re.findall(pattern, my_string))
pattern =  r'\D'
print(re.findall(pattern, my_string))

pattern =  r'[l].*'
print(re.findall(pattern, my_string))

# -- email validation regular expression (regex) -- #

email = 'correo@correo.com'
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
print(re.findall(pattern, email))