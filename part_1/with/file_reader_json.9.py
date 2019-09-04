import json

filname = 'nambers.json'

with open(filname) as target:
    numbers = json.load(target)

print(numbers)