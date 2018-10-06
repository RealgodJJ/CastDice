"""
    author: RealgodJJ
    function: cast two dice
    version: 1.0
    date: 2018/10/4
"""
import matplotlib.pyplot as plt
import random

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False


def roll_dice():
    """
        模拟掷骰子
    :return: 骰子点数
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 10000
    value_list = list(range(2, 13))
    times_list = [0] * 11
    roll_dict = dict(zip(value_list, times_list))

    # 记录骰子的结果
    roll1_list = []
    roll2_list = []
    roll_sum_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll1_list.append(roll1)
        roll2_list.append(roll2)
        roll_sum_list.append(roll1 + roll2)

        for value in value_list:
            if roll1 + roll2 == value:
                roll_dict[value] += 1

    for value, time in roll_dict.items():
        print("点数{}: {}， 频率: {}".format(value, time, time / total_times))

    # # 两个骰子的数据可视化
    # plt.scatter(range(1, total_times + 1), roll1_list,s=8, c='red', alpha=0.5)
    # plt.scatter(range(1, total_times + 1), roll2_list, s=8, c='green', alpha=0.5)
    # 点数频率统计
    plt.hist(roll_sum_list, list(range(2, 14)), edgecolor="black", color='grey', normed=1, linewidth=0.5)
    plt.title("骰子点数概率统计")
    plt.xlabel("骰子点数")
    plt.ylabel("骰子点数概率")
    plt.show()


if __name__ == '__main__':
    main()
