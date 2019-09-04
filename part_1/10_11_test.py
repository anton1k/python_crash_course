import json

favoritenumber = input('Ваше любимое число?: ')
filname = 'favoritenumber.json'

with open(filname, 'w') as target:
    json.dump(favoritenumber, target)
    print('Мы будем помнить тебя, когда ты вернешься ' + favoritenumber)