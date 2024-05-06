"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""


def isAnagrama(value1, value2):
    # Primero, verifica si las palabras tienen la misma longitud y no son idénticas
    if len(value1) != len(value2) or value1.lower() == value2.lower():
        return False

    # Convierte las palabras en listas y ordénalas
    sorted_value1 = sorted(value1.lower())
    sorted_value2 = sorted(value2.lower())

    # Compara las listas ordenadas
    if sorted_value1 == sorted_value2:
        return True
    else:
        return False



print(isAnagrama('Hola', 'aloh'))
print(isAnagrama('hola', 'holo'))
print(isAnagrama('Roma', 'amor'))
print(isAnagrama('amor', 'Amor'))
print(isAnagrama('Hola', 'holas'))