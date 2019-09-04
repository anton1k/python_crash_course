import json

filname = 'nambers.json'
numbers = [2, 3, 5, 7, 11, 13]

with open(filname, 'w') as target:
    json.dump(numbers, target)
