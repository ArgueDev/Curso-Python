def bubble_sort(array):
    count = 0
    total = len(array)

    for i in range(total):
        for j in range(total - i - 1):
            if array[j + 1].__lt__(array[j]):
                array[j], array[j + 1] = array[j + 1], array[j]

            count += 1

    print(f'Contador: {count}')