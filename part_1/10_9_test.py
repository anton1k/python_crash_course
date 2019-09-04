fills = ['cat.txt', 'dogs.txt']

for fill in fills:
    try:
        with open(fill) as target:
            for line in target:
                print(line.strip())
    except FileNotFoundError:
        pass



