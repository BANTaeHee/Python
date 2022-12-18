# ezen06-2
# 시간의 표현 방법 : datetime, now, today, strftime, strptime

from datetime import datetime 

print(datetime.now())
print(datetime.today())
print(datetime.now().date())

print()

print(datetime.now().strftime('%Y년 %m월'))

print(type(datetime.now()))
print(type(datetime.now().strftime('%Y년 %m월')))

print()

dt = '14/12/2022'
print(dt)

print(datetime.strptime(dt, '%d/%m/%Y'))
print(datetime.strptime(dt, '%d/%m/%Y'), type(datetime.strptime(dt, '%d/%m/%Y')))

print(datetime.strptime(dt, '%d/%m/%Y').strftime('%Y년 %m월 %d일'))

import pandas as pd

start_date = '2023-01-01'
date_list = pd.date_range(start_date, periods=13, freq='MS')
print(date_list)
print(date_list[1])