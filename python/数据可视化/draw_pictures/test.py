import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

# 生成一些示例数据
x = np.linspace(0, 10, 100)
y = x ** 3

# 创建颜色数组，使用彩虹色的渐变
colors = plt.cm.rainbow(np.linspace(0, 1, len(x)))

# 创建线段集合
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)
lc = LineCollection(segments, colors=colors)

# 创建图表
fig, ax = plt.subplots()

# 添加线段集合到图表
ax.add_collection(lc)

# 设置坐标轴范围
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min(), y.max())

# 显示图表（可选）
plt.show()