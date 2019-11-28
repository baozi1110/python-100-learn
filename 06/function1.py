"""
函数的定义和使用 - 计算组合数C(7,3)
"""


# 将阶乘封装成函数
def factorial(num):
    # 求阶乘
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))
