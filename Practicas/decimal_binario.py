'''
/*
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
'''

# def decimal_binario(numero):
#     cociente = int(numero / 2)
#     residuo = numero % 2
#
#     if cociente == 0:
#         pass
#
#     return f'Cociente: {cociente} - Residuo: {residuo}'


def decimal_binario(numero):
    binario = []
    nuevo_cociente = 0

    while nuevo_cociente == 0:
        cociente = int(numero / 2)
        nuevo_cociente = int(cociente / 2)
        residuo = cociente % 2
        binario.append(residuo)
        cociente = nuevo_cociente

    return binario


resultado = decimal_binario(13)
print(resultado)