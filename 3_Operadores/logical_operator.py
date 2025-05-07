# Operador Logico

i = 3
j = 7
k = 0.00127e-7
l = 3.1415e3
m = False

b1 = i == j and k > l
print(f'b1 =  {b1}')

b2 = i == j or k > l
print(f'b2 = {b2}')

b3 = i == j and k > l or m == False
print(f'b3 = {b3}')

print(not (5 > 3))
print(not i == j)