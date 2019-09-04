filname = 'learning_python.txt'
with open(filname) as target:
    lines = target.readlines()

print(lines)
for line in lines:
    for i in range(3):
        print(line.strip())
