import json

filname = 'username.json'

with open(filname) as target:
    username = json.load(target)
    print('С возвращением ' + username)