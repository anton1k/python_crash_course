class Settings():
    '''Класс для хранения всех настороек игры'''

    def __init__(self):
        '''Инициализация настроек игры'''

        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 33, 55)

        # размер корабля
        self.size_ship = 50

        # насторйки корабля
        self.ship_speed_factor = 1.5



    