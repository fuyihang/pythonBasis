
###########################################################
########  Python内置的六种数据类型

# 1、数字number: int, bool, float, complex
# 2、字符串str:  "charlist"
# 3、列表list:  [val1, val2, ...]
# 4、元组tuple: (val1, val2, ...)
# 5、字典dict:  {'key1':val1; 'key2':val2}
# 6、集合set:    {va1, val2, val3}

# 请参考中文文档：
# https://docs.python.org/zh-cn/3.8/library/stdtypes.html
###########################################################

######################################################################
##基本概念： 对象四要素=======================================
######################################################################

##======Python对象=======================================
# 特别注意：在python中一切皆对象
# 对象，是内存中的一个真实存在的数据块，是有内存指针的
# Python对象四要素：
# 1、对象标识id
#   是对象的唯一标志(相当于内存指针)，在对象创建后从不会改变
#   可以用id(obj)函数来查看对象的ID（相当于内存指针编号）
#   可以用is来判断两个对象是否是同一个（即id是否相等）
# 2、对象类型type
#   表示对象的数据类型，这决定了对象能够进行哪些操作和运算
#   可以用type(obj)函数来查看对象的数据类型
#   可以用isinstance(obj, 类型名)函数来判断对象是否是某个类型（或父类）
# 3、对象取值value
#   表示对象的具体的取值
#   可以用print(obj)来查看对象的值
# 4、对象别名alias（可选要素）
#   对象的引用名称，即变量名。
#   一个对象可以有不同的别名

#1.python中的变量是没有类型的，可以为其赋值为任何类型的值
#变量在赋值（即实例化）后，在内存中才有类型
n = 2           #赋值为整数
n = 'first'     #赋值为字符串

#2.变量类型识别
a,b,c,d,e = 10, 2.5, True, "你好！", 5+3j

#查看变量保存的是什么类型的值
print(type(a), type(b), type(c), type(d), type(e))

print(type([1,2]), type((1,2)))     #复杂数据类型

#判断变量的类型
if isinstance(a, int) :
    pass                #占位，什么也不干

ret = isinstance(b, str)

######################################################################
##======数字Number=======================================
######################################################################

#数字类型有四种：int,bool,float,complex型
n = 31
n = 0x1F    #十六进制
n = 0o37    #八进制

flt = 2.1   #浮点数
cp = 1+2j   #复数

#1.数值运算
#1.1 算术运算符+,-,*,/,%（取余）,**（幂）,//（向下取整）,-x(相反数)
print(0.2+0.1)  #小数位数是不确定的
print(3*0.1)
print(3/2)  #除法1.5
print(5%3)  #求余=2, -21%10=9, 21%-10=-9
print(3**2) #乘方指数=9，相当于函数pow(x,y)
print(-21//10)  #-3

#1.2 位运算符:&按位与，|按位或，^按位异或，~按位取反，<<左移，>>右移
a = 60      #0011 1100
b = 13      #0000 1101

print(a&b)  #0000 1100  =12
print(a|b)  #0011 1101  =61
print(a^b)  #0011 0001  =49
print(~a)   #1100 0011  =-61
print(a<<2) #1111 0000  =240
print(a>>2) #0000 1111  =15


#2.数值的格式化输出
msg = "int:{0:d}, hex:{0:x},oct:{0:o},bin:{0:b},float:{0:f},Exponent:{0:e},char:{0:c}".format(42)
msg2 = "str:{0:s}".format('OK')
print(msg,msg2)

# 常用的格式化符号

# d 整数
# x,X 十六进制
# o 八进制
# b 二进制
# e,E 科学计数法
# f,F 浮点数（十进制）

# c 字符
# s 字符串（用str()转换）
# r 字符串（用repr()转换）,这个好像不支持了？？

# 常用格式化辅助符号

# m 任何数字，表示输出的宽度
# m.n m表示输出的宽度, n表示小数位数
# % 表示输出百分数
# + 在正数前面显示加号（+）
# - ：左对齐
# 0 数字前面用0填充，而不是默认的空格
# # 分别在二/八/十六进制的数字前面显示0b, 0o, 0x字符

msg = "[{0:+10d}]".format(42)      #数字默认右对齐
print(msg)
msg = "[{0:+#b}]".format(42)
print(msg)
msg = "[{0:10.2%}]".format(0.1523)
print(msg)
msg = "[percentage:{0:.2%}]".format(0.152)
print(msg)

#3.数值类型强制转换
x = '25'    #字符串
y = '3'
int(x)                  #转换为整数
float(x)                #转换为浮点数
complex(x)              #转换为复数
complex(int(x), int(y)) #转换为复数

import math
complex(math.pi, math.e)

#其余数值及数学函数常用的库有：
# numbers       #数值基类
# math          #数学函数
# cmath         #数学函数+复数
# decimal       #浮点数
# fractions     #有理数
# random        #随机数
# statistics    #统计


######################################################################
##======字符串=======================================
######################################################################

##1.字符串表示
str1 = 'hello'                  #使用单引号括起来
str2 = "Hello"                  #也可以使用双引号
str3 = '他的名字叫"姚明"'         #单引号和双引号可以混用
str4 = "He isn't a chinese"     #混用

#多行字符串(三个单引号或三个双引号), 注意：这不是注释行哟
str5 = """Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""

#两个字符串会隐性进行连接，只要中间没有除空格外的其它字符
str6 = 'Put several strings within parentheses ' 'to have them joined together.'

#字符串过长，一行表示不下，注意有括号
str7 = ('Put several strings within parentheses '
            'to have them joined together.')
#也可以用反斜杠
str8 = 'Put several strings within parentheses '\
            'to have them joined together.'

#字符串可以使用+进行连接运算
str9 = 'Put several strings within parentheses ' + 'to have them joined together.'

#可以使用*进行重复
str10 = '=='*20

##2.转义字符
##字符串中可以包含转义字符
str7 = 'He isn\'t a chinese'    #使用转义字符，\后的任何字符原样输出
str8 = '打印反斜杠\\字符'          #转义字符
str9 = 'hello\nworld'            #特殊的转义字符

##3.字符串前缀
str10 = r'hello\nworld'          #字符前缀，r表示使用原始字符串，不会发生转义

year = 2016
name = 'John'
msg = f'他叫{name},于{year}年出生。'  #f或F表示其中有参数

##4.字符串访问
str='Runoob'
#遍历
for c in str:
    print(c)
#下标访问
c = str[1]  #u

# 字符索引下标对应
# +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1


##4.字符串切片
s='Runoob'

print(s[0:-1])           # 输出第一个到倒数第二个的所有字符
print(s[0])              # 输出字符串第一个字符
print(s[2:5])            # 输出从第三个开始到第五个的字符
print(s[2:])             # 输出从第三个开始的后的所有字符

##5.字符串操作函数
##注：字符串是不可变序列，只能返回值，不能修改原有字符串
s = ' hello World! '
print('字符串的长度 =\t',len(s))

##字符串修整
str2 = s.title()  #首字母大写
str2 = s.upper()  #全部字母大写
str2 = s.lower()  #全部字母小写

str2 = s.lstrip() #去除左边空格
str2 = s.rstrip() #去除右边空格
str2 = s.strip()  #去除首尾空格
print(str2)

##字符串查找、替换
s = 'hello World'
#count(sub[,start[,end]]) 计算子串sub出现的次数
print(s.count('Wo') ) #返回1
#find(sub[,start[,end]]) 查找子串最早出现的位置,位置从0开始
#rfind(sub[,start[,end]]) 查找子串最后一次出现的位置
print(s.find('Wo'))   #返回6
#index(sub[,start[,end]]) #和find一样，但找不到子串时会抛出错误，类似还有函数rindex
print(s.replace('o','dd')) #替换所有子串，返回helldd Wddrld

##字符串分割
#split(sep=None,maxsplit=-1)以分隔符分隔字符串成列表，sep为分隔字符，maxsplit表示最大分隔次数
print(s.split())  #默认以空格分隔字符串，返回列表元素['hello', 'World']
print(s.split('l'))   #以字符l分隔，返回4个列表元素['he', '', 'o Wor', 'd']
print(s.split('ll'))  #以字符ll分隔，['he', 'o World']
print(s.split('l', 2)) #仅分隔前两次，返回3个列表元素['he', '', 'o World']
#s.splitlines()返回行列表

##字符串判断
# isalnum()
# isalpha()
# isdigit()
# isnumeric()
# islower()
# isupper()
# isspace()
# istitle()

######################################################################
##======列表类型list=======================================
######################################################################


# 1.列表是用[]来表示，用逗号分隔开元素
# 2.列表中的元素的类型可以不相同
# 3.列表中也可嵌套更复杂的数据类型

##列表定义
lt = ['ab', 12, 2.34, (5,67)]   #1.直接定义列表
print(lt)
print('列表长度=', len(lt))

lt = []                         #2.空列表
lt = [0]*5                      #3.带5个元素且元素全为0的列表
LNUM = 5
lt = [i for i in range(LNUM)]   #4.序列列表

lt = list()                     #5.空列表
lt = list(range(1,5))           #6.序列转化为列表
lt = list('abc')                #7.字符串转化为列表
lt = list((1,2,3))              #8.元组转化为列表

lt = [['a', 'b', 'c'], [1, 2, 3]]  #9.列表嵌套

##列表访问
# 列表访问有两种方式：
# 1.采用索引访问。索引从左往右以0开始，从右往左以-1开始
# 2.采用for来遍历列表

#索引访问
lt = ['a', 'b', 'c']
val = lt[0]    #第一个元素
val = lt[-1]   #最后一个元素

#遍历元素
for itm in lt:
    print(itm)

#同时遍历索引和元素
for index, val in enumerate(lt):
    print('索引=', index, '元素值=', val)

# 列表基本属性：长度
print('列表长度=',len(lt))

#按值来寻找索引位置
index = lt.index('b')     #查看值在列表中的索引位置
# index = lt.index('d')     # 如果值不在，则抛出ValueError异常
num = lt.count(8)         #查看值在列表中出现的次数

##列表切片
#所谓的切片，指的是部分列表的元素
# 切片形如:变量[i:j:k],表示返回的列表从下标i开始，到尾下标j，步长为k
# 即选择的元素的下标x满足如下条件：
# 1.i <= x < j
# 2.x = i +n *k ,其中n为整数，且n>=0
# 列表切片不会修改原列表元素，只返回指定的元素列表

lt = list('abcde')
newlt = lt[:]           #复制整个列表
newlt = lt[0:2]         #返回['a','b']
newlt = lt[2:]          #返回['c','d','e'],默认尾下标到结尾
newlt = lt[:-2]         #返回['a','b','c']，默认起始下标从0开始
newlt = lt[4:2]         #返回空列表，当j<=i时都是空列表

lt = list(range(10))
newlt = lt[1:9:2]       #返回[1, 3, 5, 7],位置间隔-步长为2

##修改元素
lt = list('abcde')
lt[0] = 'e'             #将第一个元素修改为'e'

##增加元素
lt.append(2)            #末尾添加一个元素
lt.extend(['g','h'])    #添加多个元素，相当于添加一个新列表
lt.insert(0, 'OK')      #指定位置插入新元素

##删除元素
itm = lt.pop()          #弹出末尾的元素，返回的元素可以继续使用
itm = lt.pop(-2)        #弹出指定位置的元素，并返回该元素
itm = lt.remove('b')    #删除指定值的元素，即按值删除
# itm = lt.remove('k')    #如果值不在列表中，会抛出ValueError异常
itm = lt.remove('e')    #如果存在相同值的多个元素，则只删除第一个元素

del(lt[0])              #删除指定位置的单个元素
del(lt[0:2])            #删除多个元素，指定切片
lt = ['a', 'b', 'c','d','e']
lt[1:3] = []            #利用切片来删除,变成['a', 'd', 'e']

lt.clear()              #清空整个列表

##列表操作
lt = list('abcde')
if 'a' in lt:
    print('项在列表中。')
else:
    pass

#列表合并
lt1 = list('abcd')
lt2 = list('efg')
lt = lt1 + lt2          #运算符合并

lt1.extend(lt2)         #函数合并：将lt2合并到lt1列表中

#列表排序
cars = ['BMW', 'Audi', 'Toyota', 'Subaru']
cars.sort()                 #列表升序
cars.sort(reverse = True)   #列表降序

#列表反转顺序
cars.reverse()              #列表反转顺序

#临时排序，不改变原来列表
cars = ['BMW', 'Audi', 'Toyota', 'Subaru']
tmp = sorted(cars)
print('原始列表：', cars)
print('排序后列表：', tmp)

#列表复制 
newCars = cars.copy()       #函数复制
newCars = cars[:2]           #切片复制

#列表赋值
lt = list('abc')
newlt = lt                  #列表赋值，两个列表指向的是同一个对象，而不是复制
lt[0] = 'd'
print(newlt)                #列表是可变序列，改变lt, newlt也会改变


######################################################################
##======元组类型tuple=======================================
######################################################################
## 元组是不可改变的列表
## 除了不允许修改元素外，其余操作与列表基本类似

##元组定义
# 1.元组是用()来表示，用逗号分隔开元素
# 2.元组中的元素类似可以不相同，也可嵌套复杂数据类型
# 3.元组与字符串类似，其实，字符串可看作一种特殊的元组
t = 12345, 54321, 'hello!'          #1.赋值语句
tp = ('ab', 12, [1,2,3])            #1.直接定义
tp = ()                             #2.空元组

tp = (20,)                          #3.一个元素的元组，注意：必须添加逗号
print(type(tp))     #<class 'tuple'>
tp = 'hello',                       #注意后面的逗号，也是一个元素的元组

tp = (20)           #这样定义的话，返回的就是int型
print(type(tp))     #<class 'int'>

tp = tuple('abcd')                  #4.字符串转换为元组
tp = tuple(i for i in range(10))    #5.序列转换为元组
tp = tuple([1,2,'OK'])              #6.列表转换为元组
tp2 = tuple({'b':4, 'c':'OK'})      #7.字典转换为元组（字典的键转换为元组）

tp = ('Hi',)*4                      #8.有4个元素的元组，所有元素初始化为'Hi'，即重复4次的元素
#('Hi','Hi','Hi','Hi')

##元素合并
tp1 = ('ab', 12)
tp2 = (34, 'cd')
tp = tp1 + tp2          #合并为(‘ab’,12,34,’cd’)


##元组访问
# 元组访问和列表一样，可使用索引位置，也可使用遍历
# 元组也可以使用切片

tp = ('ab', 12, 'cd')

#索引访问,用下标找值
val = tp[0]     #'ab'
val = tp[-1]    #'cd'

#用值来找下标
key = tp.index(12)

#遍历元组
for itm in tp:
    print(itm)

#遍历索引和元素值
for index, val in enumerate(tp):        #enumerate函数返回两个值：索引下标和元素值
    print('索引=', index, ' 值=', val)

#切片访问
subtp = tp[0:2]     #参考列表切片示例

#元组修改
#元组不可以修改，修改会抛出TypeError异常
#元组不可修改，但元组中的元素如果是可变的对象，比如list列表，则可以修改此元素列表中的值
lt = [1,2,3]
tp = ('ab', 12, lt)     #('ab', 12, [4, 2, 3])

#tp[0] = 'cd'       #修改元组，抛出TypeError异常
tp[2][0] = 4        #修改元组中可变元素lt的值
print(tp)           #('ab', 12, [4, 2, 3])


#元组的常用函数和方法，请参考官方文档

######################################################################
##======字典类型dict=======================================
######################################################################
# 字典和列表类似，两者区别在于：
# 1.列表是有序的对象集合，而字典是无序的对象集合。
# 2.列表的元素是通过索引位置访问，而字典中元素是通过键来访问。
# 3.列表的索引必须是数字，而字典的索引（即键）可以是字符串，更易读。
# 4.列表的索引是隐式，而字典显式地保留了键值对（key-Value）。
# 5.列表支持切片访问，但字典不支持切片访问（切片的本质是位置）

##字典定义
# 1.字典用{}标识，用逗号分隔元素，用:分隔键值（键:值）。
# 2.键(key)必须是不可变类型，如果字符串、数字或元组等。
# 3.键必须是唯一的，不能重复；重复的关键字指的是同一个元素。
dct = {}                                #1.空字典
dct = {'color':'green', 'point':5}      #2.键值对定义

dct = dict(color = 'green', point = 5)  #3.形参格式定义

lt = [('color', 'green'), ('point', 5)]
dct = dict(lt)                          #4.单列表构造，列表中元素为键值元组
##dct = dict([('color', 'green'), ('point', 5)])

# ltkey = ['color', 'point']              #5.双列表构造
# ltval = ['green', 5]                    #第一个列表为健列表，第二个列表为值列表
# dct = dict.fromkeys(ltkey,  ltval)      

dct = {x : x**2 for x in (2,4,6)}       #6.键值对构造

##字典访问
# 字典访问和列表类似，有几种访问方式：
# 1.基于键来得到值
# 2.遍历字典的键列表 dct.keys()
# 3.遍历字典的值列表 dct.values()
# 4.遍历字典的元素列表 dct.items()

#字典的访问:基于键来得到值
dct = {'color':'green', 'point':5} 
val = dct['color']                    #1.按键访问值
                                        #如果键不存在，则抛出KeyError异常
val = dct.get('color')                #2.函数访问
                                        #如果键不存在，默认返回None，无异常

#遍历字典：遍历键列表
#访问键列表
for key in dct.keys():
    print('key=',key)

#访问值列表
for val in dct.values():
    print('value=', val)

#访问键-值列表
print("遍历字典中的键-值对")
itms = dct.items()
print(itms)
for key, val in dct.items():
    print('\nKey=', key)
    print('value=', val)

##字典修改
dct = {'color':'green', 'point':5}
dct['loc'] = (23, 45)           #添加元素
dct['color'] = 'red'            #修改值
dct['point'] += 1               #修改值
dct.update(loc = 1, blue = 2)   #修改/增加元素
##{'color': 'red', 'point': 6, 'loc': 1, 'blue': 2}

#按键删除元素，使用del函数
del dct['loc']                  #按键删除，如果键不存在，则抛出KeyError异常
#del(dct['loc'])                #同上

#按键弹出元素，使用pop函数
val = dct.pop('blue')           #按键删除元素，返回元素值
                                #如果键不存在，则抛出KeyError异常

#弹出末尾元素
itm = dct.popitem()             #删除末尾的元素,注意：返回是元组(键，值)哟。

#清空整个字典
dct.clear()                     #dct成了空列表

##字典的其它操作，请参考官方文档
# if key in dct.keys():
# if val in dct.values():
# if (key, val) in dct.items():
dct2 = dct.copy()               #字典复制
dct3 = dct                      #指针赋值

######################################################################
##======集合类型set=======================================
######################################################################
# 集合是一个无序的不重复的无索引的序列

##集合定义
# 1.使用{}定义集合，元素间用逗号分隔
# 2.集合中元素不重复（重复的元素当成一个）
# 3.集合中元素没有顺序，不支持索引访问
# 4.集合中的元素必须是不可哈希的，可以是数字、字符串、元组，但不能是列表、字典

st = {1,2,2, 3,4}               #1.直接定义集合，会自动去重
st = {x for x in 'abcd'}        #2.序列转化为集合
st = {x for x in 'abcd' if x not in 'abef'} #序列转化为集合

st = set()                      #3.空集合。注间：不能用{}来定义空集合，{}表示空字典
st = set('abcd')                #4.字符串转化为集合
st = set([1,2,3,4])             #5.列表转化为集合
st = set((1,2,'OK'))            #6.元组转化为集合

##集合访问
#集合不支持索引，只能遍历
st = set([1,3,5])
for val in st:
    print(val)

##集合修改
#添加元素，元素必须是可哈希的
st.add(6)           #添加元素,元素为数字
st.add('OK')        #添加元素，元素为字符串
st.add((1,2,3))     #添加元素，此元素为元组
#st.add({2, 'Hello'})       #TypeError异常，不能添加字典元素
#st.add([4,5,6])            #TypeError异常，不能添加列表元素

#添加多个元素，从其它迭代类中添加新的集合元素
#注意：add函数与update函数的区别
st.update('abc')        #将单个字符增加到集合中
st.update([4, 'OK'])    #将列表中元素增加到集合中
                        #即将列表中的单个元素加入集合，并不是把整个列表当成一个元素加入集合
st.update((1,6))        #将元组中元素增加到集合中
st.update({'a':5, 'b':9})   #将字典中的所有键增加到集合中，注意：字典中的值没有用

#添加混合元素
st = set([1,3,5])
st.update((4,5),{'a':5, 'b':9}, 'bc')   
#{1, 3, 4, 5, 'c', 'b', 'a'}

#集合删除
st.remove(3)     #删除指定元素，移除不存在的值时,会抛出KeyError异常
st.discard(3)    #丢弃指定元素，移除不存在的值时不会报错

val = st.pop()   #弹出某个元素，并返回此元素。集合为空时会抛出KeyError异常

st.clear()       #清空集合, st为空集合 

##集合运算
st1 = set('abcd')
st2 = set('cdef')

#并集A∪B
st = st1 | st2      #{'a', 'b', 'c', 'd', 'e', 'f'}
#交集A∩B
st = st1 & st2      #{'c', 'd'}
#差集/补集B - A = { x| x∈B且x∉A}
st = st1 - st2      #{'a', 'b'}
#（对称差集？反集？）：不包含两个集合的公共元素
st = st1 ^ st2      #{'a', 'b', 'e', 'f'},相当于并集减去交集(st1|st2) - (st1&st2)

#集合的其它操作函数，请参考官方文档
stNew = st.copy()
if 'a' in st:
    print('元素在集合中。')

######################################################################
##======类型转换=======================================
######################################################################

# 各种数据类型的强制转换函数
# int(x, abse)    #-->整数
# float(x)    #-->浮点数
# ord(x)      #字符-->整数
# hex(x)      #整数-->十六进制
# oct(x)      #整数-->八进制
# complex(real[,image])   #-->复数

# str(x)      #-->字符串
# rept(x)     #-->表达式字符串
# chr(x)      #整数-->字符

# list(s)
# tuple(s)
# set(s)
# frozenset(s)
# dict(s)

# eval(str)   #用来执行表达式，并返回表达式的值

######################################################################
##======数据运算=======================================
######################################################################

# 赋值运算符
# 算术运算符
# 布尔运算符
# 比较运算符
# 位运算符
# 成员运算符
# 身份运算符
# 还要弄明白各种运算符的优先级

######################################################################
##======时间类型========================================
######################################################################

#日期时间类型有4个
from datetime import datetime,date,time,timedelta

#日期时间datetime
#datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
dttm1 = datetime(2017, 3,8)
dttm2 = datetime.strptime('2016-10-01', '%Y-%m-%d')
dttm3 = datetime.strptime('01/12/16 16:30', '%d/%m/%y %H:%M')
dttm4 = datetime.today()   #获取当前日期时间
dttm5 = datetime.now()     #效果和today是一样的
dttm6 = datetime.fromisoformat("2019-02-18*01:04:05.123000")  #格式形如YYYY-MM-DD[*HH[:MM[:SS[.fff[fff]]]][+HH:MM[:SS[.ffffff]]]]
print(dttm1,dttm2,dttm3,dttm4,dttm5,dttm6)
#print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)
#print(dt.weekday())    #Monday=0
#print(dt.isoweekday()) #Monday=1
#print(dt.isoformat())  #返回形如YYYY-MM-DDTHH:MM:SS.ffffff的时间格式

# #日期格式实参含义----------------------------
# %Y 年份，四位数字表示，如2015
# %y 年份，两位数字表示，如15
# %B 月份名，如January
# %b 月份名，简写，如Jan,
# %m 月份的数字表示，用数字表示的月份（01-12）
# %d 日(月)，用2位数字表示的一天（01-31）
# %j 日(年)，用3位数字表示的一天，(001-366)
# %H 时，24小时制的小时数（00-23）
# %I 时，12小时制的小时数（01-12）
# %M 分（00-59）
# %S 秒（00-60）
# %f 微秒数，6位数字表示，000000，000001，...，999999
# %Z 时区名,(empty),UTC,EST,CST
# %z 时区偏置，形如±HHMM[SS[.ffffff]](empty),+0000,-0400,+063415,-030712.345216

# %p am或pm
# %A 星期的名称，如Monday,Monday,...,Staturday
# %a 星期的名称简写，如Sun,Mon,...,Sat
# %w 星期的数字表示，0是周日，6表示星期六。
# %W 周数(Sun作为一周的第一天)，（00-53）
# %U 周数(Mon作为一周的第一天)，（00-53）

# %c 本地日期时间表示，比如Tue Aug 16 21:30:00 1989
# %x 本地日期表示，比如08/16/1989
# %X 本地时间表示，如21:30:00

#日期date
#datetime.date(year, month, day)
dt1 = date(2017,4,2)
dt2 = date.today()  #
dt3 = date.fromisoformat("2018-07-06") #格式必须为形如YYYY-MM-DD
str = dt1.strftime("%A %d/%m/%y")   #输出指定的日期格式
print(dt1, dt2, dt3, str)
#print(dt1.year, dt1.month, dt1.day)
#print(dt1.weekday())   #Monday is 0
#print(dt1.isoformat()) #返回字符串，形如YYYY-MM-DD

#时间time
#datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
tm = time(12, 34, 56, 123456)
print(tm)
#print(tm.hour, tm.minute, tm.second, tm.microsecond, tm.tzinfo, tm.fold)

#时间差 timedelta
#datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
dlt1 = timedelta(days=10, hours=5)  #相差10天5小时
print(dlt1)

print(dlt1.days, dlt1.seconds, dlt1.microseconds)
#时间差只用（天、秒、微秒）共同来表示，其余的参数都会转化为这几个参数

dt1 = datetime(2019,1,1)
dt2 = datetime(2019,1,2, 1,2,3,4)
dlt2 = dt2-dt1                  #应该是相差1天1个小时2分钟3秒4微秒,即除去整天数，还相差3600+120+3=3723秒
print(dlt2)                     #输出结果是datetime.timedelta(days=1, seconds=3723, microseconds=4)
print(dlt2.total_seconds())     #总秒数，1天=86400秒，共86400+3723=90123.000004秒
