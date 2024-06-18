# manejos de archivos

# ---- .txt file ---- #
'''
# txt_file = open('../intermedio/my_file.txt', 'r+') # Leer y Escribir
txt_file = open('../intermedio/my_file.txt', 'w+')
txt_file.write('Mi Nombre es Christian\nMi Apellido es Arguello\nMi Edad es 25 Años\nMi lenguaje Favorito es Python\nNueva Línea')

# print(txt_file.read())
# print(txt_file.readline())

# txt_file.write('\nNueva Linea')
# print(txt_file.read())
'''

# ---- .json file ---- #
# import json
#
# json_file = open('../intermedio/my_file_json.json', 'w+')
# json_test = {
#     'Nombre': 'Christian',
#     'Apellido': 'Arguello',
#     'Edad': 25,
#     'Lenguajes': ['Python', 'Kotlin', 'Swift'],
#     'Web': 'https://google.com/'
# }
#
# json.dump(json_test, fp=json_file, indent=4)

# ---- .csv ---- #
import csv
csv_file = open('../Intermedio/my_file.csv', 'w+')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['name', 'surname', 'age', 'language', 'website'])
csv_writer.writerow(['Christian', 'Arguello', 26, 'Python', 'arguedev.com'])

csv_file.close()