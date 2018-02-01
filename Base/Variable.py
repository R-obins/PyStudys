#####变量#######
'''
五个标准数据类型
Numeber(数字)
String(字符串)
List(列表)
Tuple（元组）
Dictionary(字典)
四种不同数字类型
int（有符号整型）
long（长整型，八进制十六进制）
float（浮点型）
complex（复数）
'''
a="sadfasdasdasd"
print(a[1:6])#输出第一到第六个之间的字符串
print(a[4:])#输出从第四个开始的字符串
print(a*2)#输出两次字符串

list=['a',123,3.45,'ss']
list1=[123,'ssss']
print (list)
print(list[1:3])#输出列表第一至第三之间的元素
print(list1*2)#输出list1列表两次
print(list+list1)#拼接list和list1列表

tuple=('aaaa',123,2.44444,'ddsas')
print(tuple[2:5])#输出元组内第二个至第五个之间的元素

#tuple[2]=1111111    元组是不允许更新的
list[2]=1111111
#print(tuple)
print(list) #列表中则是可以更新的

#Dictionary(字典) 无序的集合,取值是通过键来取得
dict={}
dict['aaaa']="ssassssdaadsdsdsd"
dict[2]="wwwwwwwwwwwwwwwwwwwq"

dictttt={'name':'qwe','age':22222,'sal':'000'}
print(dict[2]) #输出键为2的值
print(dictttt) #输出字典dictttt
print(dictttt.keys()) #输出字典的所有键
print(dictttt.values()) #输出字典的所有值
