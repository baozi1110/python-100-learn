"""
比较、逻辑和算身份运算符的使用
"""
flag0 = 1 == 1
flag1 = 3 > 2 #True
flag2 = 2 < 1 #False
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0) # flag0 = True
print('flag1 =', flag1) # flag1 = True
print('flag2 =', flag2) # flag2 = False
print('flag3 =', flag3) # flag3 = False
print('flag4 =', flag4) # flag4 = True
print('flag5 =', flag5) # flag5 = False
print(flag1 is True) # True
print(flag2 is not False) # False