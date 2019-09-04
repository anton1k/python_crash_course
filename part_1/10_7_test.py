print('"q" для выхода')

while True:
    first = input('Введите первое чило: ')
    if first == 'q':
        break

    last = input('Введите второе число чило: ')
    if last == 'q':
        break

    try:
        res = int(first) + int(last)
    except ValueError:
        print('что-то не число')
    else:
        print(res)

