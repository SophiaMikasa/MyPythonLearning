import matplotlib.pyplot as plt
from one import MyRandomWalk

while True:
    rw = MyRandomWalk(500)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    # plt.plot()返回的是一个图表对象 fig 和一个坐标轴对象 ax
    ax.plot = plt.plot(rw.x_values, rw.y_values, linewidth=1)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolor='none', s=1)
    ax.set_aspect('equal')

    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolor='none', s=20)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=20)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
