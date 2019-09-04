while True:
    age = int(input('Введите возраст: '))
    if age < 3:
        print('Для вас билет бесплтен.')
    elif 3 <= age < 12:
        print('Для вас билет стоит 10$.')
    else:
        print('Для вас билет стоит 15$.')


