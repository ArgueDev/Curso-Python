# Tuples #

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (26, 1.77, 'Christian', 'Arguello', 'Christian')
my_other_tuple = (30, 60, 20)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('Christian'))
print(my_tuple.count('ArgueDev'))

print(my_tuple.index('Arguello'))

# my_tuple[1] = 1.80
# print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = 'ArgueDev'
my_tuple.insert(1, "Blanco")
print(my_tuple)

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
