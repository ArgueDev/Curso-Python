products = []
products.append('Kingston Pendrive 64GB')
products.append('Samsung Galaxy')
products.append('Samsung External SSD Drive')
products.append('Asus Notebook')
products.append('Mackbook Pro')
products.append('Chromecast 4th Generation')
products.append('Oxford Bicycle')

products.sort()

prod_1 = products[0]
prod_2 = products[1]
prod_3 = products[2]
prod_4 = products[3]
prod_5 = products[4]
prod_6 = products[5]
prod_7 = products[6]

print(prod_1)
print(prod_2)
print(prod_3)
print(prod_4)
print(prod_5)
print(prod_6)
print(prod_7)

for e in products:
    print(f' - {e}')

print('\n--- Lista al reves ---')
for e in reversed(products):
    print(f' - {e}')