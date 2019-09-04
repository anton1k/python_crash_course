import json

filname = 'favoritenumber.json'

with open(filname) as target:
    favoritenumber = json.load(target)
    print('я знаю ваше любимое число ' + favoritenumber)