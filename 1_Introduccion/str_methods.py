# Metodos para un String

name = 'Christian Arguello'
course = 'Curso de Python'

print(name.upper())
print(course.lower())

words = 'curso de python'
print(words.capitalize())
print(words.title())

words = '   hola Christian   '
print(words)
print(words.strip())
print(words.lstrip())
print(words.rstrip())

text = 'Hola Java'
print(text.replace('Java', 'Python'))

text = 'Christian,Arguello,Python,Java,Angular'
data_list = text.split(',')
print(data_list[2])
print(data_list[len(data_list)-1])
print(data_list)

data = ['Christian', 'Arguello', 'Python', 'Java', 'Angular']
text = ' - '.join(data)
print(text)

text = 'Hola, Christian que tal como estas?'
print(text.find('Christian'))
print(text.find('tal'))
print(text.index('como'))
print(text.startswith('Christian'))
print(text.startswith('Hola'))
print(text.endswith('estas'))
print(text.endswith('?'))

number = '1234'
decimal = '1234.5'
text = 'Python'
mix = 'Python3'
print(number.isnumeric())
print(decimal.isdecimal())
print(text.isalpha())
print(mix.isalnum())