"""
    author: RealgodJJ
    function: Scientific with numpy
    version: 1.0
    date: 2018/10/6
"""
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


def main():
    total_times = 10000
    # 记录骰子的结果
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr

    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)

    plt.hist(result_arr, bins=list(range(2, 14)), edgecolor="black", color='grey', density=1, linewidth=0.5, rwidth=0.8)

    # 设置轴坐标点的显示
    tick_labels = [0] * 11
    for num in range(2, 13):
        tick_labels[num - 2] = str(num) + "点"
    tick_position = np.arange(2, 13) + 0.5
    plt.xticks(tick_position, tick_labels)

    plt.title("骰子点数概率统计")
    plt.xlabel("骰子点数")
    plt.ylabel("骰子点数概率")
    plt.show()


if __name__ == '__main__':
    main()
