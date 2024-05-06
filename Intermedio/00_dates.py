# Dates #

from datetime import datetime as dt
from datetime import time
from datetime import date

now = dt.now()

timestamp = now.timestamp()
print(timestamp)

year_2023 = dt(2023, 1, 1)

def print_date(date):
    print(date)
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)
print_date(year_2023)

current_time = time(12, 42, 22)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time)

current_date = date(2024, 11, 25)
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date.today()
print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)
