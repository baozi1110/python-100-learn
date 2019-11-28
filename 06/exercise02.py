"""
实现判断一个数是不是回文数的函数
"""


def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp = temp // 10
    return total == num


print(is_palindrome(12321))

"""
实现判断一个数是不是素数的函数。
"""


def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


print(is_prime(21))

if __name__ == '__main__':
    num = int(input('请输入正整数： '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
