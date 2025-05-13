from datetime import datetime

now = datetime.now()
print(f'La fecha actual es {now}')

date_time = datetime(2020, 9, 8, 17, 33, 32)
print(date_time)
print(date_time.year)
print(date_time.month)
print(date_time.day)
print(date_time.hour)
print(date_time.minute)
print(date_time.second)
print(date_time.microsecond)

date_format = date_time.strftime('%d/%m/%Y')
print(date_format)

