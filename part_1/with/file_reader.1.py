with open('pi_digits.txt') as target:
    content = target.read()
    print(content.rstrip()) # чтобы убрать пустую стороку в конце