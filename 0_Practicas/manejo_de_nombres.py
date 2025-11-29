# Varibles de nombres
nombre1 = 'Christian'
nombre2 = 'Mario'
nombre3 = 'Samuel'

# Nuevos nombres modificados
nuevo_nombre1 = nombre1[1].upper() + '.' + nombre1[-2::]
nuevo_nombre2 = nombre2[1].upper() + '.'  + nombre2[-2::]
nuevo_nombre3 = nombre3[1].upper() + '.' + nombre3[-2::]
lista_nombres = [nuevo_nombre1, nuevo_nombre2, nuevo_nombre3]

print('_'.join(lista_nombres))