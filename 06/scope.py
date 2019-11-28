"""
作用域
"""


def foo():
    global a
    # nonlocal a
    a = 200
    print(a)


if __name__ == '__main__':
    a = 100
    foo()
    print(a)
