# Listas #

my_list = list()
my_other_list = []

print(len(my_list))
# print(type(my_list)) # class 'list'
# print(type(my_other_list)) # class 'list'

my_list = [26, 24, 62, 52, 30, 30, 17]
print(my_list)
print(len(my_list))

my_other_list = [26, 1.69, "Christian", "Arguello"]
print(my_other_list)

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list.count("Christian"))
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)

print(my_other_list + my_list)

my_other_list.append('ArgueDev')
print(my_other_list)

my_other_list.insert(1, 'Azul')
print(my_other_list)

my_other_list.remove('Azul')
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_list = "Hola Python"
print(my_list)
print(type(my_list))
