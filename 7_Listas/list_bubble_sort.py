from bubble_sort import bubble_sort

# Ordenamiento con Algoritmo de burbuja


# count = 0
# total = len(products)

# for i in range(total):
#     for j in range(total):
#         if products[i] < products[j]:
#             temp = products[i]
#             products[i] = products[j]
#             products[j] = temp
#
#         count += 1


# Metodo optimizado algoritmo de burbuja
# for i in range(total):
#     for j in range(total - i - 1):
#         if products[j + 1].__lt__(products[j]):
#             products[j], products[j + 1] = products[j + 1], products[j]
#
#         count += 1
#
#
# print(f'Contador: {count}')

products = ['Memoria Kingston', 'Samsung Galaxy', 'Disco Duro SSD Samsung', 'Asus Notebook', 'Macbook Air', 'Chromecast', 'Bicicleta Oxford']
bubble_sort(products)
for i in range(len(products)):
    print(f'Indice {i} : {products[i]}')


print('-'*7)

numbers = [10, 7, 35, -4, int('6'), int('-1')]
bubble_sort(numbers)
for i in range(len(numbers)):
    print(f'Indice {i} : {numbers[i]}')