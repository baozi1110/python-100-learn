"""
实现计算求最大公约数和最小公倍数的函数。
"""


# 最大公约数
def gcd(x, y):
    if x > y:
        x, y = y, x
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1

def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(15, 27))
print(lcm(15, 27))