"""
输出乘法口诀表(九九表)
"""
for i in range(1, 10):
    for j in range(1, 10):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print('\t')
