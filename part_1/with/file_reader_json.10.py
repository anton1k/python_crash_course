import json

username = input('Как вас зовут?: ')
filname = 'username.json'

with open(filname, 'w') as target:
    json.dump(username, target)
    print('Мы будем помнить тебя, когда ты вернешься ' + username)