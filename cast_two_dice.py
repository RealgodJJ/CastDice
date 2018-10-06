"""
    author: RealgodJJ
    function: cast two dice
    version: 1.0
    date: 2018/10/4
"""
import matplotlib.pyplot as plt
import random


def roll_dice():
    """
        模拟掷骰子
    :return: 骰子点数
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 100
    value_list = list(range(2, 13))
    times_list = [0] * 11
    roll_dict = dict(zip(value_list, times_list))

    # 记录骰子的结果
    roll1_list = []
    roll2_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()
        roll1_list.append(roll1)
        roll2_list.append(roll2)

        for value in value_list:
            if roll1 + roll2 == value:
                roll_dict[value] += 1

    for value, time in roll_dict.items():
        print("点数{}: {}， 频率: {}".format(value, time, time / total_times))

    # 两个骰子的数据可视化

    plt.scatter(range(1, total_times + 1), roll1_list, c='red', alpha=0.5)
    plt.scatter(range(1, total_times + 1), roll2_list, c='green', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
