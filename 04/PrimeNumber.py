"""
输入一个正整数判断它是不是素数
素数指的是只能被1和自身整除的大于1的整数。
"""
from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d is prime number' % num)
else:
    print('%d is not prime number' % num)
