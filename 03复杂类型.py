#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

######################################################################

########    特殊类型使用

######################################################################
# 下面介绍Python中的几种特殊的类型/函数的使用
# range类：特殊的序列类
# 迭代类：可以返回迭代器，支持遍历操作
# 生成器：生成器函数返回迭代器，支持遍历操作


######################################################################
##======range类、序列类sequence=======================================
######################################################################

# 序列类是list/tuple/dict/set等类型的基类
# 最典型的序列类就是range语句返回类
# range([star,]stop[,step])格式：从star开始，按步长step增加，始终小于stop。
# 即序列中的元素x满足如下条件：
# 1. start <= x < stop
# 2. x = star + n*stip，其中n为非负整数，即n为从0开始的整数

for i in range(5):
    print(i)        #注：打印0,1,2,3,4，但不打印5

for num in range(1,5):
    print(num)       #注：打印1,2,3,4，但不打印5。

for num in range(1, 10, 2):
    print(num)       #注：打印1,3,5,7,9


######################################################################
##======迭代类、迭代器iterator=======================================
######################################################################

##迭代类===============
# 
# 迭代类可以返回迭代器，支持遍历操作
# 迭代类必须实现__next__(), __iter__()两个函数
class MyData:
    def __init__(self):
        self.tuplist = [(1,2),(3,4),(5,6)]  #假定是固定的列表
        self.loc = 0

    def __iter__(self):     #返回迭代对象
        return self

    def __next__(self):     #返回下一个元素
        if self.loc == len(self.tuplist):
            self.loc = 0     #这句很重要，否则下次就不能够再继续访问迭代类的元素了
            raise StopIteration
        else:
            tup = self.tuplist[self.loc]
            self.loc += 1
            return tup

# 使用迭代类
mydata = MyData()

#1）可以直接遍历
for x in mydata:
    print(x)

#2）也可以使用迭代类
it = iter(mydata)   #返回迭代类
for x in it:
    print(x)

#3）也可以使用next读取
it = iter(mydata)
while True:
    try:
        itm = next(it)
    except StopIteration as e:
        break
    else:
        print(itm)


######################################################################
##======生成函数generator=======================================
######################################################################
# 
# 生成函数也可以返回迭代器，支持遍历操作
# 自定义生成函数时，请使用yield关键字，系统会自动保留当前的对象状态
def Fibonacci(n):
    a, b ,counter = 0,1,0
    while counter <= n:
        yield a                 #yield关键字，相当于返回迭代器
        a, b = b, a+b
        counter += 1

# 使用生成函数
#1）直接遍历
it = Fibonacci(10)
for x in it:
    print(x, end = ' ')
print('==end==')

#2）使用next函数遍历
it = Fibonacci(10)      #注意：这里要重新赋值，因为前面代码it已经到末尾了
while True:
    try:
        print(next(it), end=' ')
    except StopIteration:
        break
print('==end==')


######################################################################
##======上下文管理器contextmanager=======================================
######################################################################
# 1、使用with语句，管理文件
with open("text.txt",'r') as f:
    for line in f.readlines():
        print(line)
#此时，程序会自动调用f.close()语句

#使用with语句，管理锁
import  threading
lock = threading.lock()
with lock:
    #执行一些操作
    pass
#此处，程序会自动释放锁 


# 2、自定义上下文管理类
class DBConnection(object):
     def __init__(self):
         pass

     def cursor(self):
         #返回一个游标并且启动一个事务
         pass

     def commit(self):
         #提交当前事务
         pass

     def rollback(self):
         #回滚当前事务
         pass

     def __enter__(self):
         #返回一个cursor
         cursor = self.cursor()
         return cursor

def __exit__(self, type, value, tb):
    if tb is None:
             #没有异常则提交事务
             self.commit() 
         else:
             #有异常则回滚数据库
self.rollback()


sql = ‘select  * from User’
con = DBConnection()
with con as cursor:
	curson.execute(sql)
	#。。。

# 3.装饰器实现
from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()

with my_open(‘mytext.txt’,’r’) as f:
	#文件操作

#此处自动调用f.close()函数

@contextmanager
def transaction(db):
    db.begin()
    try：
        yield 
    except:
        db.rollback()
        raise
    else:
        db.commit()

