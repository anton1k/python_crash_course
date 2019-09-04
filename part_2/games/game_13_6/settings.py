class Settings():
    '''Класс для хранения всех настороек игры'''

    def __init__(self):
        '''Инициализация настроек игры'''

        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # насторйки корабля
        self.ship_speed_factor = 1.5
        self.ship_width = 200
        self.ship_height = 15
        self.ship_color = (0, 100, 50)
        self.ship_limit = 3

        # настроекйки пули
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (255, 100, 200)
        self.bullet_allowed = 10




    