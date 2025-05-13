from datetime import date

today = date.today()
year = date.today().year
month = date.today().month
day =  date.today().day
print(f'Hoy es {today}')
print(f'year {year}')
print(f'Mes es {month}')
print(f'Dia es {day}')

birthday = date(1997, 9, 24)
print(f'Mi nacimiento es el {birthday }')