from name_function import get_formatted_name

print('Введите "q" для выхода.')

while True:
    first = input('Введите ваше имя: ')
    if first == 'q':
        break
    last = input('Введите вашу фамилию: ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print('Ваше отформатированное имя: ' + formatted_name)
    