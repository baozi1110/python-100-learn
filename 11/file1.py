# 创建文件
# f = open('foo.txt','w')
# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# f.close()

# 读取文件 f.read()
# f = open('foo.txt', 'r')
# str = f.read()
# print(str)
# f.close()

# f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
# f = open('foo.txt', 'r')
# str = f.readline()
# print(str)
# f.close()

# f.readlines() 将返回该文件中包含的所有行。
# 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
# f = open('foo.txt', 'r')
# str = f.readlines()
# print(str)

# 通过迭代一个文件对象读取每行
# for line in f:
#     print(line,end='')

# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
# f = open("foo.txt", "w")
# num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# print(num)

# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:
# f = open("foo1.txt", "w")
# value = ('www.runoob.txt.com', 14)
# s = str(value)
# f.write(s)
# f.close()

# tell() 方法返回文件的当前位置，即文件指针当前位置。
# 打开文件
# fo = open("runoob.txt", "r+")
# print("文件名为: ", fo.name)
# line = fo.readline()
# print("读取的数据为: %s" % (line))
# 获取当前文件位置
# pos = fo.tell()
# print("当前位置: %d" % (pos))
# fo.close()

# f = open('foo2.txt','rb+')
# print(f.write(b'0123456789abcdef'))
# print(f.seek(5))  # 移动到文件第五个字节
# print(f.read(1))
# print(f.seek(-3, 2))  # 移动到文件倒数第三个字节
# print(f.read(1))

# 使用with关键字自动关闭文件
with open('foo.txt', 'r') as f:
    read_data = f.read()
print(f.closed)


