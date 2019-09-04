first = input('Введите первое чило: ')
last = input('Введите второе число чило: ')

try:
    res = int(first) + int(last)
except ValueError:
    print('что-то не число')
else:
    print(res)

