#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

######################################################################

#Python模块化、面向对象

######################################################################

######################################################################
##======函数=======================================
######################################################################

# 函数是可重复使用实现单一功能的代码段。
# 函数能够提高代码的可重用性，也方便代码结构的组织

##函数定义===============
# 
# 1.函数以def关键字开头，接不接函数名和（参数列表）
# 2.函数可以有形参，也可以不带形参
# 3.形参可以有默认值，也可以不带默认值
# 4.函数可以没有返回值，也可以有返回值，或者有多个返回值

##函数值返回===============
# 指的是函数要向外（调用者）传递处理后的数据
# 1.返回值数量：
#   1）无返回
#   2）返回单个值
#   3）返回多个值（相当于返回一个元组）
# 2.返回值方式：
#   1）使用return语句返回
#   2）通过可变参数返回，传入的实参在函数体内可修改，在函数体外可以被使用

##函数参数===============
# 
# 指的是传入函数进行处理的数据变量
# 1.参数个数：
#   1）固定个数：函数的参数，可以无参数，也可以有参数（有限的固定的个数）。
#   2）任意个数：参数的个数也可以是任意数量个（加*var号表示以元组的形式传入）。
#   3）关键字参数：任意个数，但有约定的名称（加**var号表示以字典的形式传入）。
# 2.参数默认值：
#   1）参数可以无默认值
#   2）也可以有默认值
#   3）如果参数有默认值，其顺序要靠后（比无默认值的参数）。

#1、无返回（相当于返回None）
def hello():     
    print("Hello World!")
    #return

hello()                 #直接调用

#2、有返回(返回布尔值)
import os
def isLogExists():  #判断日志是否存在
    logFile = "/log/log.txt"
    if os.path.exists(logFile):
        return True
    else:
        return False

# 有返回调用，可用赋值语句取得返回值
rt = isLogExists()
if rt:
    print('日志文件存在。')
else:
    print('日志文件缺失！')

#3、返回单值，固定数量形参
def getArea(width, height): #计算长方形面积
    area = width * height
    return area

#4、返回多个值，形参带默认值
# 有默认值的形参位置要靠后
def getAreaAndCircle(width, height, msg="OK"):
    area = width * height
    circle = 2 * width * height
    print(msg)
    return area, circle         #相当于返回一个元组（area, circle)

area, circle = getAreaAndCircle(3, 5)   #返回多个值，形参使用默认值
print('面积=', area, ' 周长=', circle)
area = getAreaAndCircle(3, 5, "计算面积")  #如果只有一个变量，则此变量是一个元组
print(area)

#5、通过可变实参返回值
# 传入的实参在函数体内可修改，在函数体外可以被使用
def getNewList(mylist):
    mylist.append([1,2,3])  #增加一个元素，元素为列表
    # mylist.extend([1,2,3]) #增加三个元素
    return

lt = list('abc')
print('调用前列表：', lt)       #['a', 'b', 'c']
ret = getNewList(lt)     #调用函数处理
print('调用后列表：', lt)       #['a', 'b', 'c', [1, 2, 3]]


#6、任意数量的参数(*var空元组)
# 参数个数不确定，是任意数量个；而且参数列表只有顺序，没有名字
# 典型的print函数的参数可以传入任意个
# 带星号的形参*var表示一个空元组
def fun2(*var):
    if len(var)==0:
        print('没有传入任何参数!')
    else:
        print('传入的第1个参数为:', var[0])
        print('传入的参数列表：')
        for itm in var:
            print(itm, end = ' ')
    print()             #打印一个换行符而已

#调用时可以调用任意数量个
fun2()              #可以没有参数
fun2(10,'OK')       #也可以传入多个参数

#7、任意数量的关键字参数(**var空字典)
# 参数个数不确定，但参数的名称是有约定的。这样方便在函数体内使用
# 比如，大多数的配置文件，里面的配置项的名称是确定了的
# 带两个星号的形参**var表示一个空字典
def printColorText(**var):
    #约定传入的参数中：
    # 1.text参数用来指定打印的文本
    # 2.color参数来指定字体颜色，当前只处理red和blue两种颜色
    sColor = '30'     #默认为黑色
    if var['color'] == 'red':
        sColor = '31'
    elif var['color'] == 'blue':
        sColor = '34'
    else:
        pass
    
    txt = var['text']
    #构造字体颜色字符串
    msg = '\033[{}m{}\033[0m'.format(sColor, txt)   #请参考输出字体颜色小节
    print(msg)

#调用时，需要指定参数名称，以键=值对的形式传入
#打印红色字体的“我爱中国”
printColorText(text='Python编程！', color='red')

#打印蓝色字体的“Python编程”
printColorText(color='blue', text='Python编程！', other = '其它无用信息')

##函数调用===============
# 
# 函数调用时，形参和实参要匹配。匹配的方式有两种：位置匹配，关键字名称匹配
# 1.位置匹配：不需要指定参数名称，但要注意位置顺序
#     1）一般形参的个数和实参的个数要一样多（除非有形参有默认值）
#     2）形参的位置顺序和实参的位置顺序要一一对应
# 2.关键字名称匹配：按名称匹配，顺序无关
#     1）指定参数名称，顺序无关
#     2）实参的顺序无关
# 3.如果形参有默认值，则在调用时，对应的实参可以传入新的值，也可以使用默念值

#1. 按位置匹配形参，实参的位置顺序必须正确
def printUser(name, age):
    print('用户名={},年龄={}.'.format(name, age))
    return

printUser('zhangsan', 25)   #输出正确结果
printUser(25, 'zhangsan')   #输出错误结果

#2. 关键字参数，按名称匹配形参，实参的顺序无关
printUser(name= 'zhangsan', age = 25)
printUser(age = 25, name= 'zhangsan')

#3.对于任意数量的参数，要注意顺序，但不能使用关键字参数
fun2('zhangsan', 25)
# fun2(name= 'zhangsan', age = 25)  #这样是不允许的

#4.对于关键字参数，必须指定参数名称，但顺序无关。
printColorText(text='Python编程！', color='blue', other = '其它无用信息')


##匿名函数===============
# 
# 普通函数需要用def关键字定义，匿名函数使用关键字lambda定义
# 1.其格式形如 [fun = ]lambda [arg1 [,arg2,.....argn]]:expression
# 2.lambda语句返回一个函数，可以有名字，也可以不指定名字
# 3.冒号前是参数,冒号后是表达式。
# 4.匿名函数只能有一个表达式，函数返回值就是表达式的结果

#给匿名函数一个名字，可单纯调用函数
f = lambda x: x*x               #一个参数
n = f(5)        #返回25

f = lambda x, y: (x**2 + y)     #多个参数
n = f(2, 3)     #返回7

#将函数作为参数传递
f = lambda a,b: a+b
def average(num1, num2, opt):
    ret = opt(num1, num2)
    return ret/2

a,b = 10, 20
result = average(a, b, f)
#这样直接调用使用也是可以的，没有函数名
result = average(a, b, lambda a,b: a+b)

#按字典中各种key方式来排序
my_list = [{"name": "小明", "age": 23}, \
           {"name": "小红", "age": 22}, \
           {"name": "小刚", "age": 33}]
# 按age排序
my_list.sort(key=lambda dict: dict["age"])
print(my_list)

pairs = [(1, 'one'), (2, 'two'), (4, 'four'), (3, 'three')]
pairs.sort(key=lambda pair: pair[0])	#按第一个值排序
print(pairs)
# [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])	#按第二个值排序
print(pairs)
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

######################################################################
##变量作用域===============
######################################################################

# 变量的作用域决定了哪些代码块可以使用这个变量名称。
# Python变量一共有4种层次的作用域：
# 1）L(local)局部作用域。
#   只在本代码块内有用，或者只在本函数体内有效，其余代码块中无法访问。
# 2）E(Enclosing)闭包作用域。
#           这是一种特殊的作用域，往往存在于函数内再嵌套一个函数的场景。
#           在外层函数内的一个局部变量，相对于内层函数来说，就是一个闭包变量。
# 3）G(Global)全局作用域。
#   一般在函数体外该模块内的变量。
#   该模块内或者导入该模块的程序都可以访问。
# 4）B(Built-in)内置作用域，
#   即Python核心程序中定义的。任何程序皆可直接访问（不用明确导入）。
#   典型的系统属性如__name__, __spec__等

# 不同作用域的变量位置
count = 0		        #G全局作用域，当前整个模块内可使用
def outer():
    print(count)
    ecount = 1		    #E闭包作用域，outer和inner都可使用
    def inner():
        print(count)
        print(ecount)
        lcount = 10	    #L局部作用域，仅限inner()函数内可使用
        print(lcount)
    inner()

outer()
print(count)

import builtins		#内置作用域是通过名为builtin的标准模块实现
dir(builtins)		#可以显示有哪些内置变量，
			#比如True, None这些对象就是B内置作用域

#===================变量作用域覆盖的问题========================
# 1）如果定义了不同作用域的变量，则在使用变量时，变量的查找顺序是：L->E->G->B
# 2）如果找不到相应的变量，最后会抛出异常NameError
# 3)本层作用域内可读取和修改本层的变量
# 4)下层作用域可读取上层变量，但不能修改（赋值）上层变量。

count = 1	#变量在本层作用域内可修改，在下层作用域不能修改
def outer1():
    print(count)    #可直接使用外层的变量，允许
    pass

def outer2():
    count = 2	    #试图修改上层变量，实际上是定义了一个新的局部变量
    print(count)

outer1()
outer2()
print(count)

#===================跨域修改变量值========================
# 如果下层想要明确使用/修改上层的变量值，需要用到特殊的声明关键字（global和nonlocal）来声明；
#跨域修改全局变量
num = 1			#全局num
def fun3():
    global num		#显式指定，使用全局变量
    print(num)		#打印1
    num += 2		#将全局变量修改为3
    print(num)		#打印3

fun3()
print(num)		#打印3，用的是全局变量

#跨域修改闭包变量
num = 1				#全局变量
def outer3():
    num = 10			#闭包变量
    def inner():
        nonlocal num		#显式指定为本函数外，上层函数内的闭包变量
        print(num)		#打印10
        num = 100		#修改闭包变量
        print(num)		#打印100
    inner()
    print(num)			#打印100,闭包变量

outer3()
print(num)			#打印1，全局变量

#===============示例======================
spam = '全局变量'
def scope_test():
    def do_local():
        spam = "local spam"		#2.修改局部变量，不改变闭包变量

    def do_nonlocal():
        nonlocal spam			#3.说明下面改变的是闭包变量
        spam = "nonlocal spam"

    def do_global():
        global spam			#4.使用全局变量，也不改变闭包变量
        spam = "global spam"

    spam = "test spam"			#1.闭包变量
    
    do_local()
    print("After local assignment:", spam)
    
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)		#5.打印全局变量

#结果是
#After local assignment: test spam
#Befor nonlocal assignment: test spam
#After nonlocal assignment: nonlocal spam
#After global assignment: nonlocal spam
#In global scope: global spam

######################################################################
##======对象类=======================================
######################################################################

# Python本身是面向对象的，所以支持类的定义

##类定义===============
# 
# 1.类以class关键字开头，后接类名及冒号(:)
# 2.每个类的成员，有两种：
#   1）类属性，即类中实例化的变量
#   2）类方法，即类中定义的函数
# 3.类成员的性质（只是约定）：
#    a)public: 默认的属性和方法都公共的，在类外部可以直接访问
#    b)pretected:以下划线(_)开头的属性和方法，约定是受保护的，
#                在类外部不要直接访问，但在子类中可直接访问，也可被重载或者覆盖。
#    c)name mangling(名称重整):以双下划线(__)开头，也算是私有的，
#                在类外不要直接访问，在子类中也不要直接访问，也无法被重载或者覆盖。
#          其实，这个名称会被系统重新加一个类名前缀(形如_classname__attribute)，
#          所以，即使子类中取一个同样的名字，也是有区别的。
#   （特别说明：实际情况下，不管是私有还是公有名称，其实在类外都是可以访问的，只是方式不同，参考示例代码）
# 4.类成员的引用格式
#   a)在类中，格式：self.member
#   b)在类外，即对象引用，格式：obj.member
#   c)如果是名称重整的成员，引用格式要加上类名前缀（如下所示）

class Dog:
    def __init__(self):
        self.kind = 'dog'
        self._name = 0
        self.__age = 0

    def out(self):
        pStr = 'kind={},name={},age={}'.format(
            self.kind, self._name, self.__age)
        print(pStr)

d1 = Dog()
d1.kind = '哈士奇'
d1._name = '帅帅'
d1._Dog__age = 2
d1.out()

# 5.类属性，进一步可以分为两种：
#    a)类变量：在类中直接赋值的变量（变量前面不带任何前缀）
#           类变量，约定是所有类对象共有的。
#           一个实例对象改变类变量（且类变量是可变类型），则会影响另一个实例对象。
#    b)实例变量：在类方法（一般是在__init__）中赋值，且变量前必须加上self.前缀，
#           实例变量，约定为单个对象特有的。
#           一个实例对象改变实例变量，不会影响另一个实例对象。
# 6.类变量和实例变量的差异
#    a)一般情况下，在使用上没有差异。
#    b)实例变量的修改，只会影响单个类对象
#    c)类变量的修改，其影响有两种情况：
#       1）如果类变量是不可变的数据类型，则只会涉及到单个类对象
#       2）如果类变量是可变的数据类型，则会涉及到所有的类对象

class people:
    kind = 'Human'           #类变量(不可变变量)
    clslt = []               #类变量（可变变量）
    def __init__(self, name):
        self.name = name    #实例变量（不可变）
        self.instlist = []  #实例变量（可变）
    
    def __str__(self):      #重载系统函数
        pStr = 'kind={},name={},clslt={},instlist={}'.format(
            self.kind, self.name,self.clslt, self.instlist)
        return pStr

# 实例化两个不同的类对象
p1 = people('John')
print(p1)

p2 = people('Mike')
print(p2)

####======修改实例变量，两个对象不会相互影响==================
p1.name = 'Pone'  #修改类变量（不可变类型）
print(p1)
print(p2)

p1.instlist.append(20) #修改类变量（可变类型）
print(p1)
print(p2) 

####======修改类变量，如果是可变类型，则所有对象改变==================
p1.kind = 'People'  #修改类变量（不可变类型）
print(p1)
print(p2)

p1.clslt.append(10) #修改类变量（可变类型）
print(p1)
print(p2)           #居然p2也变化了！

# 
# 7.类方法
#   a)类方法的定义和函数定义方式基本一样
#   b)唯一的区别是类方法的第一个参数约定为self（这代表类的实例对象）
#   c)类方法的调用格式有两种:
#       1)obj.fun()
#       2)className.fun(obj)。这种方式较少使用。

# 8.类中的特殊的方法（即系统方法）
#    __init__()  #初始化方法，实例化时系统自动调用，当然也可以手工调用
#    __del__()   #析构方法，对象在销废时系统自动调用
#   等其它

class Human:
    #重载系统函数
    def __init__(self, name):
        self.name = name        #1.定义公共属性
        self.age = 10           #2.定义公共属性
        self._height = 170      #3.定义受保护属性，子类可直接使用
        self.__weight = 60      #4.定义私有属性，子类不可覆盖

    def speak(self):            #5.定义公共函数
        print('Human speak:name={}, age={}, height={}, weight={}'.format(
                self.name, self.age, self._height, self.__weight))

    def _hu(self):              #6.定义受保护方法，子类可重载，可覆盖
        print('Human hu:私有函数')

    def __fo(self):             #7.定义私有重整方法，子类不可覆盖，系统会自动命名（添加前缀）
        print('Human fo:私有重整函数')

#使用类对象
p = Human('John')          #实例化类对象

#访问类属性
print(p.name, p.age)        #1.直接访问公共属性
print(p._height)            #2.直接访问私有属性
#print(p.__weight)           #不能访问重整属性,会抛出AttributeError异常
print(p._Human__weight)     #3.可以这样访问重整私有属性

#调用方法
p.speak()                   #1.直接调用公共方法
p._hu()                     #2.直接调用受保护方法
#p.__fo()                   #不能直接调用重整私有方法，会抛出AttributeError异常
p._Human__fo()             #3.可以这样调用重整私有方法

##派生类===============
# 
# 1.类还可以从其它基类（父类）进行派生，派生类也叫子类。
# 2.父类可以有多个，但要注意父类的顺序。特别是当两个父类都有相同的方法时，
#      在通过子类调用该方法时，其搜索的顺序如下：
#      子类-->第一个基类-->第二个基类-->...直到找到可用的方法为止
# 3.子类的初始化方法，强烈建议一定要调用父类的初始化方法，否则无法访问父类的实例变量（会抛出AttributeError异常）
# 4.在子类中，要访问父类的方法，可以有几种格式
#     a)使用super().fun()格式（建议），明确表示访问的是父类的方法
#     b)直接使用parentclassname.fun(self) 格式 （不常用）
#     c)使用self.fun()格式，像使用子类本身函数一样（前提是子类没有重载父类的这个函数）
# 5.子类可以改写/重写/重载父类的方法
#   a)此时父类的方法被覆盖。
#   b)子类要访问父类的被重载的方法，可以使用super().fun()。
#   c)子类对象要访问父类被重载的方法，？？?

#定义派生类/定义子类
class student(Human):
    def __init__(self, name, no, grade):
        self.no = no
        self.grade = grade
        self._height = 180          #这个直接对父类变量赋值
        self.__weight = 90          #注：这个不是使用父类的属性，而是新定义了一个子类的实例属性
        super().__init__(name)      #调用父类的初始化方法 （强调建议）

    def talk(self):                 #编写子类的方法
        print('student talk: No={}, Grade={}.'.format(self.no, self.grade))
        super()._hu()               #子类也可以直接调用父类的方法
        # self._hu()                  #子类可以直接调用父类的方法
        # people._hu(self)            #还可以这样调用，但一定要带上self参数，否则会抛出TypeError异常

    def speak(self):                #重载父类的方法
        print('student speak:no={}, age={}'.format(\
            self.no, self.age))

    def __fo(self):
        print('student fo:重整函数')

stu = student('Jonh', 123, '二年级')

#访问类属性
print(stu.name, stu.age, stu._height, stu._Human__weight)   #访问父类属性
print(stu.no, stu.grade, stu._student__weight)              #访问子类属性

stu.talk()                      #调用子类公共方法
stu.speak()                     #调用子类重载方法

stu._hu()                       #调用父类方法
stu._Human__fo()                #调用父类重整方法
stu._student__fo()              #调用子类重整方法

rst = isinstance(stu, student)
rst = isinstance(stu, Human)

rst = issubclass(student, Human)
rst = issubclass(student, people)

#从多个父类继承时，写法如下：（其它略）
#class ElectricCar(Car,Bike):
#       pass
# 但基类顺序要注意，假定ElectricCar, Car, Bike都有一个方法叫run
# 现在使用ElectricCar的一个对象obj.run(),那么用的是如个类的方法呢？
# 系统寻找run方法的顺序是：先是子类本身，再从左到右（然后是Car，再然后是Bike）

##======模块=======================================
##
# 模块的本质，其实就是一个.py文件，文件的名称就是模块名。
# 模块中可以定义函数，可以定义类，以实现特定的公共的功能。
# 在使用别的模块时，必须要导入模块。模块只会被导入一次
# Python之所以功能强大，盖因为有着大量的标准模块供调用

##导入模块===============
# 
# 1.使用import导入整个模块，模块只会被导入一次
# 2.还可以使用as给导入的模块一个简单的别名
# 3.Python在寻找模块时，会按照sys.path路径来搜索可用的模块（其中，第一个空格就是当前目录）
# 4.调用模块中方法时，形如modulesname.function()，函数必须带前缀，前缀为模块名

import os
import numpy as np  #导入时指定别名,后续可以直接使用别名

path = os.getcwd()              #返回当前工作目录
dirs = os.listdir(path)         #返回上当下的所有子目录和文件列表
print(dirs)

# # 修改当前工作路径
# path = '/'
# os.chdir(path)

##导入模块中指定的名称（方法、类、常量）===============
# 
# 1.可以同时导入多个名称，用逗号分隔开
# 2.也可以使用as取别名
# 3.调用模块中的方法时，形如function()，不需要前缀，直接调用函数即可（但要小说模块名冲突）

#其中导入的getcwd(), listdir()是函数，而path是类
from os import getcwd, listdir, path
pathName = getcwd()                 #不需要模块前缀
dirs = listdir(pathName)
print(dirs)

if path.exists(pathName):
    print('路径存在！')

##导入模块中所有名称（方法、类、常量等）===============
# 
# 1.此种较少用，慎用，容易引发名称冲突。
# 2.from os import *
# 3.此时调用方法同2，不需要带模块名
# dirs = listdir(path)

##特殊的模块属性
#
# __name__  模块名，不同的情况下有不同的值

print(__name__)     #本模块的名称，因为是直接执行，所以输出的应该是'__main__'
print(os.__name__)  #由于os模块是被导入的，所以输出的应该是模块名'os'

if __name__ == '__main__':
    print('本模块自身在运行')       #使用$python mymodule.py命令执行
else:
    print('表示本模块被导入')       #使用import mymodule命令执行


##特殊的dir()函数===============
# 
# 1.dir()函数可以列出模块中所有的可用的名称
# 2.dir(modulename)可以列出指定模块中所有的可用的名称 

dir()       #列出当前程序中定义的名称
dir(os)    #列出os模块定义的名称

##======包=======================================
##
# 如果说模块是一个文件，那么包就是一个目录
# 1.包相当于一个目录，目录下可以有多个不同的模块
# 2.包目录中必须包含一个__init__.py的文件，此文件可以是空的，也可以包含一些初始化代码，
#       或者定义变量__all__（该变量指定可以导入的名称）
# 3.包可以嵌套，即包还可以包含子包（子目录）
# 4.包的导入和模块的导入基本类似（此略）

#比如下面是一个叫做sound的包的目录结构，包还有formats, effects,filters三个子包
#package  sound 处理声音文件和数据
# sound/                          顶层包
#       __init__.py               初始化 sound 包
#       formats/                  文件格式转换子包
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  声音效果子包
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  filters 子包
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py
#               ...
