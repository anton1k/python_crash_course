class Car():
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("Эта машина имеет " + str(self.odometer_reading) + " миль на это.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Вы не можете откатить одометр!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    """Простая модель аккумулятора электромобиля."""
    def __init__(self, battery_size=70):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print("Этот автомобиль имеет аккумулятор " + str(self.battery_size) + "-кВтч.") 

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "Эта машина может ехать примерно " + str(range)
        message += " миль на полном заряде."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank():
        """У электромобилей нет бензобака."""
        print("Этому автомобилю не нужен бензобак!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()