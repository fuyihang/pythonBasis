# -*- coding: utf-8 -*-

# 单行注释，用#
# Python学习 课堂演示
# 任务：
# 1、任务一、了解本机操作系统、CPU、内存、磁盘等信息
# 2、任务二、了解工作路径、目录、文件等信息
# 3、任务三、遍历指定目录下的子目录、文件和快捷方式

###########################################################
########  Python五大基本语句
# 1、赋值语句(var = object)
# 2、输入输出语句(input, print)
# 3、条件语句(if-elif-else)
# 4、循环语句(for, while)
# 5、异常语句try-exception-finally
# 6、其它特殊语句：
    # import, break, continue, 

###########################################################

# 1、导入语句
import this     #打印Python之禅

import os       #导入一个标准module

# 2、输出语句
print("下面学习print语句\n")

# 任务一：了解本机操作系统信息
# 操作系统信息
print(os.name)
print(os.sys.platform)
print(os.sys.version)
print(os.sys.version_info)

import psutil
# CPU信息
print('CPU逻辑个数：', psutil.cpu_count())
print('CPU物理个数：', psutil.cpu_count(False))
print('CPU频率：', psutil.cpu_freq())
print('CPU使用百分率(%):', psutil.cpu_percent())

# 内存信息
print('虚拟内存信息：',psutil.virtual_memory())
print('\n交换内存信息：',psutil.swap_memory())

# 硬盘信息
print('磁盘分区:\n', psutil.disk_partitions())
print('磁盘使用率:\n', psutil.disk_usage('/'))

# 3、输入语句

filename = input('请输入你的名字：')
print('你输入的名字是：', filename)


# 4、赋值语句
currDir = os.getcwd()   #默认是在代码所在的目录
print(currDir)      #禁止使用dir作变量，因为dir是内置标识符

# 5、条件语句

newpath = '/Users/fusx/OneDrive/Python/dataset/'
# newpath = 'D:\\python\dataset'
if os.path.exists(newpath):
    print("路径存在")


age = input('请输入你的年龄:')
if age.isdigit():
    print('你的年龄是:', age, '岁。')
else:
    print('你输入的数据不正确!')

################################
# 练习任务二：了解工作路径、目录、文件等信息
# 1）路径表示
# 2）当前工作路径查看、修改
# 3）判断路径(目录或文件)是否存在
#################################

# 绝对路径
filename = "/Users/fusx/OneDrive/Python/dataset/用户明细.csv"

# 相对路径
filename = '用户明细.csv'       # 表示当前工作目录下的文件

filename = '../dataset/用户明细.csv'    # 表示上一级目录下的dataset子目录下的一个文件

ret = os.path.exists(filename)  # 检查路径(文件或目录)是否存在

#windows下路径表示，三种都可以通过
path = r'C:\Users\fusx\OneDrive\Python\数据分析'       #注意前面有r字符
path = 'C:\\Users\\fusx\\OneDrive\\Python\\数据分析'    #或者用双反斜杠
path = 'C:/Users/fusx/OneDrive/Python/数据分析'        #或者用斜杠即可

# 更改工作路径
# newpath = '/Users/fusx/OneDrive/Python/dataset/'
path = 'C:/Users/fusx/OneDrive/Python/dataset'
os.chdir(newpath)

# 改变工作路径后，使用相对路径更简洁
filename = '用户明细.csv'
ret = os.path.exists(filename)

print('文件名:', filename)

filesize = os.path.getsize(filename)/1024**2
print('文件大小(M):', filesize)
# print('文件大小(M):{:.2f}'.format(filesize))

ctime = os.path.getctime(filename)
atime = os.path.getatime(filename)
mtime = os.path.getmtime(filename)

import datetime as dt
time = dt.datetime.fromtimestamp(ctime)
print("创建时间：",time)

time = dt.datetime.fromtimestamp(mtime)
print("最后修改时间：",time)

time = dt.datetime.fromtimestamp(atime)
print("最后访问时间：",time)

# 5、遍历循环语句for
# 用于访问所有的序列对象

# 最常用整数序列函数range(start, stop, step)
for i in range(2,10,3):
    print(i)

dirPath = '/Users/fusx/OneDrive/Python'

# for
if os.path.exists(dirPath):
    names = os.listdir(dirPath)    #返回列表

    for name in names:
        print(name)

# for-else
for name in names:
    print(name)
else:
    print('\n遍历结束!')    #当序列被遍历完后，才执行else部分的语句

# for-else + continue
for name in names:
    if name.isupper():  #不打印大写字符串
        continue
    print(name)
else:
    print('\n遍历结束!')

# for-else + break
# 遍历查找目录下是否存在某文件名，
for name in names:
    if name == 'ML':
        print('找到文件名字！')
        break
    print(name)
else:
    print('\n遍历结束，也没有找到该文件名！')

# 6、条件循环语句while
num = 0
while num < len(names):
    print('第{}个文件名:{}'.format(num, names[num]))
    num += 1
else:
    print('\n完成遍历！')

# else,break, continue语句,在while中和在for中，用法相同


################################
# 练习任务三：了解目录、文件等信息
# 1）遍历目录下的子目录、文件等信息
# 2）区分路径是目录，还是文件，或者是快捷方式
#################################

# 7、如何区分是文件，还是目录？
dirPath = '/test'
if os.path.exists(dirPath):
    names = os.listdir(dirPath)
    if names:   # names非空
        files = []
        dirs = []
        links = []
        for name in names:
            path = os.path.join(dirPath, name)

            if os.path.isfile(path):
                files.append(name)
            elif os.path.isdir(path):
                dirs.append(name)
            elif os.path.islink(path):
                links.append(name)
            else:
                pass

        print('文件列表：', files)
        print('目录列表：', dirs)
        print('链接文件：', links)
