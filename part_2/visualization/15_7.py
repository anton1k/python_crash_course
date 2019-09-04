import sys
sys.path.insert(0, './die/')


import pygal
from die import Die

# создание кубика D8 и D18.
die_1 = Die(8)
die_2 = Die(8)

# число подкидываний
int_pod = 1000000

# моделирование серии бросков и вывод результатов в списке
results = []
for rull_num in range(int_pod):
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

hist.title = 'Results of rolling a D8 and a D8 {0} times.'.format(int_pod)
hist.x_labels = list(range(2, max_result+1))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D8 + D8', frequencies)
hist.render_to_file('visual.svg')
