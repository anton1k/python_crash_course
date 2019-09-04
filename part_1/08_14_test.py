
def make_car(first, last, **info):
   """Строит словарь с информацией о пользователе."""
   profile = {}
   profile['name'] = first
   profile['model_name'] = last

   for key, value in info.items():
      profile[key] = value

   return profile

car = make_car('Лада', 'Веста',
               color ='Белый',
               complect = 'lux',
               test = 'тест'
               )
print(car)
