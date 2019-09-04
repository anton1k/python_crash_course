ingr = []

while True:
    pizza = input('Введите ингриедейты для пицы: ')
    if pizza == 'выход':
        break
    else:
        ingr.append(pizza)
        
result = ', '.join(ingr)

print('Ваша пица с ингридиентами: ' + result)


