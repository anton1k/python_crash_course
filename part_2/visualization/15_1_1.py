import matplotlib.pyplot as plt

x_int = list(range(1, 5001))
y_int = [x**3 for x in x_int]
print(x_int)
plt.scatter(x_int, y_int, s=40)
plt.show()

