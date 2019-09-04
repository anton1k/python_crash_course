import sys
sys.path.insert(0, './random/')
import matplotlib.pyplot as plt 
from random_walk_2 import RandomWalk


# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
    # построение случайного блуждания и нанеснеие точек на диаграмму
    rw = RandomWalk(5000)
    rw.fill_walk()
    # Назначение размера области просмотра.
    plt.figure(figsize=(10, 6))
    point_number = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1)
    # выделение первой и последней точек
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    # удаление осей
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Продолжить? (y/n): ')
    if keep_running == 'n':
        break
