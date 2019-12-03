sum = lambda arg1, arg2: arg1 + arg2

print(sum(10, 20))
print(sum(40, 20))

def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)

f(10, 20, 30, d=40, e=50, f=60)
# f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
# f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式


def Foo(x):
    if (x==1):
        return 1
    else:
        return x+Foo(x-1)

print(Foo(4))


numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x , numbers))
print(newNumbers)