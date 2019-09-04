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

restaurant = Restaurant('оазис', 'вася')
print(restaurant.number_served)
restaurant.number_served = 2
print(restaurant.number_served)
restaurant.set_number_served(5)
print(restaurant.number_served)
restaurant.increment_number_served(10)
print(restaurant.number_served)