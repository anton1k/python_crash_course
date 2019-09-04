per = int(input('Введите число: '))

if per % 10 == 0:
    print('{0} число кратно 10'.format(per))
else:
    print('{0} число не кратно 10'.format(per))