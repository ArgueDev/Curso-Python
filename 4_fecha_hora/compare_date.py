from datetime import date

today = date.today()
birthday = date(1997, 9, 24)

print(today == birthday)
print(today >  birthday)
print(today < birthday)