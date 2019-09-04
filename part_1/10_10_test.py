with open('text.txt') as target:
    string = ''

    for line in target:
        string += line.strip()

    print(string.count('json'))


