class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('ресторан - {0}, повар - {1}'.format(self.restaurant_name.title(), self.cuisine_type.title()))

    def open_restaurant(self):
        print('Ресторан {0} открыт'.format(self.restaurant_name.title()))

    def set_number_served(self, new_current):
        self.number_served =  new_current
        print('число посетителей изменено')
        
    def increment_number_served(self, next_current):
        self.number_served += next_current
        print('число посетителей изменено на ' + str(next_current))

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Морожка3', 'Морожка2', 'Морожка1']

    def r_flavors(self):
        print(', '.join(self.flavors))


ics = IceCreamStand('оазис', 'вася')
ics.r_flavors()