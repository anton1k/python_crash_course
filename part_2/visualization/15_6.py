import sys
sys.path.insert(0, './die/')


import pygal
from die import Die

# создание кубика D6 и D10.
die_1 = Die()
die_2 = Die(10)

# моделирование серии бросков и вывод результатов в списке
results = []
for rull_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# анализ результатов
frequencies = []
max_result = die_1.num_sides +die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# визуализация результатов
hist = pygal.Bar()

hist.title = 'Results of rolling a D6 and a D10 50,000 times.'
hist.x_labels = list(range(2, max_result+1))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequencies)
hist.render_to_file('visual.svg')
