"""
    author: RealgodJJ
    function: Cast only one dice
    version: 1.0
    date: 2018/10/4
"""
import random


def roll_dice():
    """
        模拟掷骰子
    :return: 骰子点数
    """
    roll = random.randint(1, 6)
    return roll


def main():
    total_times = 10000
    dice_number_times = [0] * 6
    for i in range(total_times):
        roll = roll_dice()
        for value in range(1, 7):
            if roll == value:
                dice_number_times[value - 1] += 1

    print("=================================")
    for value, time in enumerate(dice_number_times):
        print("点数{}: {}， 频率: {}".format(value + 1, time, time / total_times))


if __name__ == '__main__':
    main()
