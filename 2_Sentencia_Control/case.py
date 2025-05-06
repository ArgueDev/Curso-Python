number = 1

match number:
    case 1:
        print('Seleccionaste la opcion 1')
    case 2:
        print('Seleccionaste la opcion 2')
    case 3:
        print('Seleccionaste la opcion 3')
    case _:
        print('Opcion no valida!')


def option(number):
    if number == 1:
        return 'Seleccionaste la opcion 1'
    elif number == 2:
        return 'Seleccionaste la opcion 2'
    elif number == 3:
        return 'Seleccionaste la opcion 3'
    else:
        return 'Opcion no valida!'


result = option(3)
print(result)