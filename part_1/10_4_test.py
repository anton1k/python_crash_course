filname = 'guest_book.txt'

while True:
    name = input('Введите свое имя: ')
    if name == 'выход':
        break
    name += '\n'
    with open(filname, 'a') as target:
        target.write(name)

