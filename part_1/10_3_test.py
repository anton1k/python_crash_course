filname = 'guest.txt'

name = input('Введите свое имя: ')

with open(filname, 'w') as target:
    target.write(name)

