import matplotlib.pyplot as plt
import math

input_values = range(1, 5001)
cube = [math.pow(x, 3) for x in input_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(input_values, cube, c=cube, s=3)

ax.set_xlabel('input_values', fontsize=14)
ax.set_ylabel('cube', fontsize=14)
ax.set_title('Cube of Value', fontsize=14)

ax.tick_params(labelsize=14)
ax.axis([0, 5100, 0, 1500_1000_1000])

plt.show()
