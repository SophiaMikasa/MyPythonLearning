from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [15, 32, 42, 52, 4, 24, 53, 6, 46, 27, 42, 23]
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)
plt.xticks(x)

plt.show()