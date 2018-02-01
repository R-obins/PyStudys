# 条件语句

'''
if 判断条件:
    执行语句
else:
    执行语句

判断条件可为>   <   ==    >=    <=
'''
a = 8
b = 6
c = 9
if a<b:
    print(a)
else:
    print(b)
a = 2
b = 6
c = 9
if a>b:
    print(a)
elif a<c:
    print(b)
else:
    print(c)

# python不支持switch语句，多个条件判断，用elif实现，
# 如果判断需要多个条件需同时判断时，可以使用 or （或），表示两个条件有一个成立时判断条件成功；
# 使用 and （与）时，表示只有两个条件同时成立的情况下，判断条件才成功
n=4
if n>=0 and n<5:
    print('sssssss')
if n<0 or n>2:
    print('qqqqqq')
if(n>=0 and n<5) or (n<0 or n>2):
    print('aaaaaaaa')