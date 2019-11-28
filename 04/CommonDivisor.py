"""
输入两个正整数计算它们的最大公约数和最小公倍数
"""
x = int(input('x = '))
y = int(input('y = '))
# 交换x y的值使x为较小值
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d and %d的最大公约数是%d' % (x, y, factor))
        print('%d and %d的最小公倍数是%d' % (x, y, x*y // factor))
        break
