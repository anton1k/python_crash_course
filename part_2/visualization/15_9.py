import sys
sys.path.insert(0, './die/')


import pygal
from die import Die

# создание кубика D6 и D6.
die_1 = Die()
die_2 = Die()

# число подкидываний
int_pod = 100000

# моделирование серии бросков и вывод результатов в списке
results = []

for rull_num in range(int_pod):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# создает множество неповоряемых значений
values = set(results)

# создает обысчный массив и сортирует его
values_sort = list(i for i in values)
values_sort.sort()

# анализ результатов
frequencies = []

max_result = die_1.num_sides * die_2.num_sides
for value in values_sort:
    frequency = results.count(value)
    frequencies.append(frequency)

# визуализация результатов
hist = pygal.Bar()

hist.title = 'Results of rolling a D6 and a D6 {0} times.'.format(int_pod)
hist.x_labels = values_sort
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 * D6', frequencies)
hist.render_to_file('visual.svg')
