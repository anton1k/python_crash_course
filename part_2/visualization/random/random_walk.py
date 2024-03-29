from random import choice

class RandomWalk():
    '''Класс для гененрации случайных блужданий'''

    def __init__(self, num_points=5000):
        '''Инициализирует атрибуты блуждания'''
        self.num_points = num_points

        # все блуждания начинаются с точки (0,0)
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        '''Вычесляет все точки блуждания'''

        # шаги генерируются до достижения нужной длинны
        while len(self.x_values) < self.num_points:
            # определяет направления и длины перемещения
            x_direction = choice([1, -1])
            x_distsnce = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distsnce

            y_direction = choice([1, -1])
            y_distsnce = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distsnce

            # отколнение нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            # вычесление следующих значений х и у
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)