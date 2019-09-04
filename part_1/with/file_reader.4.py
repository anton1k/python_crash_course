filname = 'pi_digits.txt'
with open(filname) as target:
    lines = target.readlines()
    
pi_string = ''
for line in lines:
    # pi_string += line.rstrip() #
    pi_string += line.strip()  # убирает все пропуски и пробелы

print(pi_string)
print(len(pi_string))