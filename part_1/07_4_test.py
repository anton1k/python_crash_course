flag = True
ingr = []

while flag:
    pizza = input('Введите ингриедейты для пицы: ')
    if pizza == 'выход':
        flag = False
    else:
        ingr.append(pizza)
result =', '.join(ingr)

print('Ваша пица с ингридиентами: ' + result)


