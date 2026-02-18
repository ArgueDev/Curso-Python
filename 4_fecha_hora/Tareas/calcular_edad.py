"""
Para esta tarea se pide ingresar una fecha de nacimiento en formato string, convertirla a una fecha date y calcular la edad de la persona de acuerdo a la fecha actual.
"""

from datetime import date

fecha_str = input("Ingresa tu fecha de nacimiento (DD/MM/AAAA): ")
d, m, a = map(int, fecha_str.split("/"))
nacimiento = date(a, m, d)
hoy = date.today()

edad = hoy.year - a - ((hoy.month, hoy.day) < (m, d))
print(f"Edad: {edad} años")