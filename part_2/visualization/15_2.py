import matplotlib.pyplot as plt

x_int = list(range(1, 5001))
y_int = [i**3 for i in x_int]

plt.scatter(x_int, y_int, c=y_int, cmap=plt.cm.Blues, s=40)
plt.show()

