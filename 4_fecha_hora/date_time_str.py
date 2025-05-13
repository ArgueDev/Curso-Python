import locale
from datetime import datetime

text = '17/04/2025 18:30'
date_time = datetime.strptime(text, '%d/%m/%Y %H:%M')
print(date_time)
print(date_time.year)
print(date_time.month)
print(date_time.day)

locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')

date_str = '9 mayo, 2025'
format = '%d %B, %Y'

date_obj = datetime.strptime(date_str, format)
print(date_obj)