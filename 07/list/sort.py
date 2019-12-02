from filecmp import cmp

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
# sorted函数返回列表排序后的拷贝不会修改传入的列表
# 函数的设计就应该像sorted函数一样尽可能不产生副作用
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
list4 = sorted(list1, key=len)

print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)

a = [5, 7, 6, 3, 4, 1, 2]
b = sorted(a)  # 保留原列表
print(a)
# [5, 7, 6, 3, 4, 1, 2]
print(b)
# [1, 2, 3, 4, 5, 6, 7]

L = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
# sorted(L, cmp=lambda x, y: cmp(x[1], y[1]))  # 利用cmp函数
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
sorted(L, key=lambda x: x[1])  # 利用key
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print(L)

students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted(students, key=lambda s: s[2])  # 按年龄排序
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
print(students)

sorted(students, key=lambda s: s[2], reverse=True)  # 按降序
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
print(students)
