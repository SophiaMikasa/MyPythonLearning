import matplotlib.pyplot as plt

input_values = range(1, 1001)
squares = [x**2 for x in input_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# c根据squares的值来决定颜色的深浅,cmap使用蓝色调色板(Blues)来表示颜色的深浅
ax.scatter(input_values, squares, c=squares, cmap=plt.cm.Blues, s=3)
# ax.plot(input_values, squares, linewidth=3)

ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

# 设置图表中刻度标签的大小
ax.tick_params(labelsize=14)
# 设置每个坐标轴的取值范围
ax.axis([0, 1100, 0, 1_100_100])
# ax.ticklabel_format(style='plain')

plt.show()
# 可用path保存在其他地方
# plt.savefig('/path/to/save/squares.png', bbox_inches='tight')
# plt.savefig('squares.png', bbox_inches='tight')
