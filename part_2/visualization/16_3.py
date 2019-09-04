import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Чтение осадков и дат из файла.
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    render = csv.reader(f)
    header_row = next(render)

    dates, highs =[], []
    for row in render:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = float(row[19])
        highs.append(high)

    # нанесение данных на диаграмму
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c='red')

    # форматирование диаграммы
    plt.title('Осадки - 2014"', fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()