"""
Obtener el nombre mas largo de tres personas, según los siguientes requerimientos
Mediante tres miembros de la familia o amigos.
Calcular e Imprimir el nombre de la persona que tenga el nombre más largo (en cantidad de caracteres) (Imprimir sólo uno de los tres, el de más caracteres en el nombre.)
Podría usar .split(" "); del objeto str para separar nombre y apellido en un arreglo, y con el indice cero accedemos al nombre de la persona.
Restricción no usar loops en el desarrollo de la tarea.
Ejemplo del resultado: "Guillermo Doe tiene el nombre más largo."
"""

print("Ingresa el nombre completo de tres personas:")
p1 = input("Persona 1: ")
p2 = input("Persona 2: ")
p3 = input("Persona 3: ")

len1, len2, len3 = len(p1.split()[0]), len(p2.split()[0]), len(p3.split()[0])

mas_largo = p1 if len1 > len2 and len1 > len3 else (p2 if len2 > len3 else p3)

print(f"{mas_largo} tiene el nombre más largo.")