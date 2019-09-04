# не сработает
squa = [i for i in range(1, 100001)]
print(min(squa)) # сработает
print(max(squa)) # сработает
print(sum(squa))

# сработает
square = []
for i in range(1, 1000001):
    square.append(i)

print(min(square))
print(max(square))
print(sum(square))
