name = 'Christian'
age = 28

text = f'Me llamo {name} y tengo {age}'
print(text)

a = 5
b = 3
print(f'La suma de {a} y {b} es {a+b}')

result = f'El precio es {a*b} dolares'
print(result)

price = 50
text = f"Este producto es muy {'Caro' if price > 50 else 'Bararo'}"
print(text)