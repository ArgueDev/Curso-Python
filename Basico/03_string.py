# Strings
my_string = "Mi String"
my_other_string = 'Mi Other String'

print(len(my_other_string))
print(len(my_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n escapado"
print(my_scape_string)

# Formateo
name = 'Christian'
lastname = 'Arguello'
age = 26

print("Mi Nombre es {} {} y mi edad es {}".format(name, lastname, age))
print("Mi Nombre es %s %s y mi edad es %d" %(name, lastname, age))
print(f'Mi Nombre es {name} {lastname} y mi edad es {age}')

# Desempaqueado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# Division
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# Reverse
reverse_language = language[::-1]
print(reverse_language)

# Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.lower())
print(language.isnumeric())
print(language.startswith("Py"))
