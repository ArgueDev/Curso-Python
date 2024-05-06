# Dictionary

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Christian", "Apellido": "Arguello", 'Edad': 35, 1: 'Python'}

my_dict = {
    "Nombre": "Christian",
    "Apellido": "Arguello",
    'Edad': 35,
    'Lenguajes': {
        'Python',
        'Swift',
        'Kotlin'
    },
    1: 1.69
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print((len(my_other_dict)))

print(my_dict['Nombre'])

my_dict['Nombre'] = 'Pedro'
print(my_dict['Nombre'])

print(my_dict[1])

my_dict['Calle'] = 'Av. Jose Maria Velasco Ibarra'
print(my_dict)

my_dict.pop('Calle')
print(my_dict)

print('Arguello' in my_dict)
print('Apellido' in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = my_other_dict.fromkeys(('Nombre', 1))
print(my_new_dict)

my_new_dict['Nombre'] = 'Christian'
my_new_dict[1] = 1.89
print(my_new_dict)

my_list = ['Nombre', 1, 'Piso']
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
