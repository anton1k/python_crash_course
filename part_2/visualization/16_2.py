import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Чтение дат, температурных максимумов и минимумов из файла
filename = 'sitka_weather_2014.csv'
filename_2 = 'death_valley_2014.csv'

def f_temp(filename):
    with open(filename) as f:
        render = csv.reader(f)
        header_row = next(render)
        res = {
            'dates': [],
            'highs': []
        }
        for row in render:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
            except ValueError:
                print(current_date, 'missing data')
            else:
                res['dates'].append(current_date)
                res['highs'].append(high)
        
    return res

t1 = f_temp(filename)
t2 = f_temp(filename_2)

# нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(t1['dates'], t1['highs'], c='red', alpha=0.5)
plt.plot(t2['dates'], t2['highs'], c='blue', alpha=0.5)
# plt.fill_between(t2['dates'], t1['highs'], t2['highs'], facecolor='blue', alpha=0.1)
# форматирование диаграммы
title = 'Сравнение температур в разных городах'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

