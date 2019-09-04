filname = 'learning_python.txt'
with open(filname) as target:
    lines = target.readlines()

print(lines)
for line in lines:
    messeg = line.replace('Питон', 'JavaScript')
    print(messeg.strip())
