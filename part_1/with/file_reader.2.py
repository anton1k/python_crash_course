filname = 'pi_digits.txt'
with open(filname) as target:
    for line in target:
        print(line)
        # print(line.rstrip())