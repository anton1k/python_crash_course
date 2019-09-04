filname = 'pi_4_million_digits.txt'
with open(filname) as target:
    lines = target.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()  # убирает все пропуски и пробелы

bitthday = input('Введите свой день рождения в виде mmddyy: ')
if bitthday in pi_string:
    print('Ваш день рождения появляется в первых 4х миллионах цифр числа пи!')
else:
    print('Ваш день рождения не появляется в первых 4х миллионах цифр числа пи!')