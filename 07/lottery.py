from random import randrange, randint, sample

"""
双色球随机选号程序
"""


def display(balls):
    """
    输出列表中的双色球号码
    :param balls:
    :return:
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    """
    随机选择一组号码
    :return:
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    # sample 从序列a中随机抽取n个元素，并将n个元素生以list形式返回。
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注：'))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
