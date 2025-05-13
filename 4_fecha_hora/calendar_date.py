import calendar
from datetime import datetime

current_date = datetime.now()
print(f'Fecha Actual: {current_date}')

days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
day_index = current_date.weekday()
week_day = days[day_index]
print(f'Hoy es {week_day}')

if  calendar.isleap(current_date.year):
    print(f'{current_date.year} es un año bisiesto')
else:
    print(f'{current_date} no es biciesto')

print('Calendario del mes actual')
print(calendar.month(current_date.year, current_date.month))

first_weekday, day_in_month = calendar.monthrange(current_date.year, current_date.month)
print(first_weekday)
print(day_in_month)