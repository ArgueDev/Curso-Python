from functools import reduce

# Funciones orden de superior #

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(value1, value2, f_sum):
    return f_sum(value1 + value2)


print(sum_two_values_and_add_value(5, 4, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

# Closures #
def sum_ten(original):
    def add(value):
        return value + 10 + original
    return add


add_closure = sum_ten(1)
print(add_closure(5))
print(sum_ten(5)(1))

# Built-in Funciones orden de superior #
numbers = [2, 5, 10, 21, 3, 30]

# Map
def multiply_two(number):
    return number * 2


print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filters
def filter_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_ten, numbers)))
print(list(filter(lambda number: number > 5, numbers)))

# Reduce
def sum_values(value1, value2):
    return value1 + value2

print(reduce(sum_values, numbers))