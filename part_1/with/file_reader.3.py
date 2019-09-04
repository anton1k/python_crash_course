filname = 'pi_digits.txt'
with open(filname) as target:
    lines = target.readlines()
    
print(lines)
for line in lines:
    print(line)
    # print(line.rstrip())