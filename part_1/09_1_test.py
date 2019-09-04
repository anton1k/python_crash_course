class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('ресторан - {0}, повар - {1}'.format(self.restaurant_name.title(), self.cuisine_type.title()))

    def open_restaurant(self):
        print('Ресторан {0} открыт'.format(self.restaurant_name.title()))

restaurant = Restaurant('оазис', 'вася')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.open_restaurant()