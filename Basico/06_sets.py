# sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un dict

my_other_set = {'Christian', 'Arguello', 26}
print(my_other_set)
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('ArgueDev')
print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("ArgueDev")
print(my_other_set)  # Un set no admite repetidos

print('ArgueDev' in my_other_set)
print('ArguelDev' in my_other_set)

my_other_set.remove('ArgueDev')
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

del my_other_set
# print(my_other_set)

my_set = {'Arguello', 'Christian', 26}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'Python', 'JavaScript', 'PHP'}
my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))
