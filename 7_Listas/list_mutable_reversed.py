products = ['Memoria Kingston', 'Samsung Galaxy', 'Disco Duro SSD Samsung', 'Asus Notebook', 'Macbook Air', 'Chromecast', 'Bicicleta Oxford']

total = len(products)
print(f'Total de productos: {total}')

for i in range(total // 2):
    current = products[i]
    reversed = products[total -1 -i]
    products[i] = reversed
    products[total -1 -i] = current


for i in range(total):
    print(f'Indice {i}: {products[i]}')