import json

# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.
filname = 'username.json'

try:
    with open(filname) as target:
        username = json.load(target)
except FileNotFoundError:
    username = input('Как вас зовут?: ')
    with open(filname, 'w') as target:
        json.dump(username, target)
        print('Мы будем помнить тебя, когда ты вернешься ' + username)
else:
    print('С возвращением ' + username)