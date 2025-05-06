from decimal import Decimal, getcontext

# Tipos de numeros

age = 30
big_int = 1234567890987654321
decimal_number = 3.14

print(f'{age} es de tipo {type(age)}')
print(f'{big_int} es de tipo {type(big_int)}')
print(f'{decimal_number} es de tipo {type(decimal_number)}')

number_complex = 2 + 3j
print(number_complex)
print(type(number_complex))

getcontext().prec = 10
num1 = Decimal('10.123456789')
num2 = Decimal('2.1')
result = num1 * num2
print(result)