'''
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
'''

def string_reverse(text):
    text_len = len(text)
    text_reversed = ''

    for i in range(text_len):
        text_reversed += text[text_len - i - 1]

    return text_reversed

print(string_reverse('Hola Mundo'))