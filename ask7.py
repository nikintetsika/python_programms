import datetime
from datetime import datetime

monday8 = 0
months = range(1,13)

now_year = datetime.now().year
ten_years_later = now_year + 10

for year in range(now_year, ten_years_later):
    for month in months:
        if datetime(year, month, 8).weekday() == 0:
            monday8 += 1
print(monday8)
