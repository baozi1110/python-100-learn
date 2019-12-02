s1 = 'hello ' * 3
print(s1)  # hello hello hello
s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('good' in s1)
str2 = 'abc123456'
print(str2)
# 从字符串中取出指定位置的字符（下标）
print(str2[2])
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])
print(str2[2:])
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 翻转 654321cba
print(str2[-3::-1])  # 4321cba
print(str2[-3:-1])  # 45

