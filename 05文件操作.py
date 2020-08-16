#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

######################################################################

#第*部分  Python文件操作

######################################################################


######################################################################
##======通用文件基本操作=======================================
######################################################################


##文件打开===============
# 
#open(file, mode='r', buffering=-1, encoding=None, errors=None, 
    # newline=None, closefd=True, opener=None)
    # file      指的是文件路径及文件名
    # mode      文件打开的模式
    # buffering 缓存大小字节数。特别的，0表示关闭缓存(二进制模式有效),1表示行缓存(文本模式有效)
    # encoding  (文本模式有效)默认编码是UTF-8
    # errors    (文本模式有效)编码错误时处理(默认是ValueError)
    # newline   (文本模式有效)换行符，可以是None,'', '\n', '\r'和'\r\n'或者其它任何字符串
    #           默认为None，表示\r,\n,\r\n都支持，并且会统一转换为\n再返回给调用者；
    #           如果为''，则不会统一转换换行符。
    # closefd   True时，表示file是一个文件名，False时表示file是文件描述符fd。
    # opener
# 返回文件对象,有可能是
    # TextIOWrapper, 
    # BufferedReader, BufferedWriter, BufferedRandom
    # 或RawIOBase,FileIO等。

#mode参数有：
    #t text mode (default)文本模式（默认），文件读取返回的都是str对象
    #b binary mode二进制模式，文件读取返回的都是bytes对象

    #r 只读，指针在文件开头，默认；如果文件不存在，则会报错！
    #w 写文件，清空文件原有内容；如果文件不存在，则会创建文件
    #+ 打开一个磁盘文件进行更新（可读写）
    #x 创建文件，如果文件存在则会报错；
    #a 追加文件，指针在文件末尾

    #rt读文本文件；w+b读写二进制文件，并清空原内容；r+b读写二进制文件，但不清空原内容

#1.打开文本文件读Text I/O。参考TextIOBase
filename = "mytxt.txt"
f1 = open(filename, 'r', encoding='utf-8')

#2.打开二进制文件读Binary I/O或bufferd I/O
filename = "myfile.jpg"
f2 = open(filename, 'rb')    #文件不存在会抛出异常


##文件写入===============
# 
#写入文件,如果文件存在，会清空原文件内容
filename = 'mytxt.txt'
f = open(filename, 'w')
if f.writable():
    f.write('this is first line!\n')    #手工增加换行符
    f.writelines(['I love you.\n', 'the seconde line.\n'])

# 写入时注意事项：
# 1）任何写入函数都不会自动添加换行符，需要手工加入。
# 2）write()返回的写入的字符数。

#追加文件内容
with open(filename, 'a') as f:
    f.write('the third line.\n')


##文件读取===============
# 
#读取文件行：1.遍历
with open(filename, 'r') as f:
    lines = f.readlines()       #读取所有行，返回行列表
    for line in lines:  
        print(line.rstrip())    #每行都带有\n换行符，所以需要使用rstrip()函数去掉它

#读取文件行：2.读取
with open(filename, 'r') as f:
    # bChars = f.read(3)        #读取指定字符数
    while True:
        line = f.readline()   #调用一次读一行
        if line:
            print(line.rstrip())  #调用rstrip函数去掉最后的换行符，否则 打印出来有空行。
        else:
            break


##关于换行符===============
# 
# wintxt.txt是在Windows下的纯文本文件,以\r\n为换行符，以\FEFF为开头表示文件编码
# mactxt.txt是在Macos下的纯文件文件，以\n为换行符

# 默认newline=None时，表示Python会智能转换换行符，将其转换为Python中的\n
# 当newline = ''时，表示Python不会处理换行符，直接返回给用户处理
# filename = 'mactxt.txt'
filename = 'wintxt.txt'
with open(filename, 'r') as f:
    # line = f.readline()         #返回一行，行末带\n
    cnts = f.read()             #返回的换行符被转换为\n
    print(cnts.strip())

with open(filename, 'r', newline='') as f:
    # line = f.readline()
    cnts = f.read()             #返回的换行符是\r\n,没有被转换
    print(cnts)


#使用with，python会自动在文件不需要时，关闭文件，因此不需要显示调用close语句来关闭文件
# f.close()

######################################################################
##二进制文件操作===============
######################################################################
filename = 'mybinary.dat'
bts1 = bytearray(range(10))
bts2 = bytearray(b'I love you!')
with open(filename, 'wb') as f:
    f.write(bts1)
    f.write(bts2)

with open(filename, 'rb') as f:
    byCnt1 = f.read(10)
    byCnt2 = f.read()
    pass

##文件读取指针的管理===============
# 
# seek(offset[, whence])函数可以根据需要调整读取的位置
# 改变读取指针的位置
# offset表示指定位置的偏移量，可以是任何整数（正或负）
# whence指针的位置，有三个取值：
#   SEEK_SET or 0 – 默认是首部，offset必须为0或正整数
#   SEEK_CUR or 1 – 当前位置，offset可正可负
#   SEEK_END or 2 – 文件末尾，offset必须为0或负整数

import io

filename = 'mybinary.dat'
with open(filename, 'rb') as f:
    if f.seekable():                #判断是否支持随机访问
        bts = f.read(5)             #读取指定的5个字符
        offset = f.tell()           #返回当前的位置，字节数
        f.seek(0)                   #默认返回文件首部
        bts = f.read(4)
        f.seek(2, io.SEEK_SET)      #返回文件首部后的2个字节。
        line = f.read(6)           #读取指定的6个字符
        f.seek(-4, io.SEEK_CUR)     #回退4个节节。
        contexts = f.read()        #读取余下的所有字符串，此时指针在末尾
        f.seek(-6,io.SEEK_END)     #指针跑到文件末尾倒数第6个字节。
        chars = f.read()
        pass
    else:
        print('文件不支持随机访问！')
pass


######################################################################
##对象序列化/反序列化===============
######################################################################
# 文件文件只能保存字符串，而二进制文件是把所有文件当成字符数组处理。
# 而在真实的场景中，数据都是某种对象，读取出来的也应该是对象。

import pickle as pk

dt1 = 35
dt2 = {'a':[1,2], 'b':'this is a string', 'c':None}
dt3 = [1,2,'OK']

##对象序列化到文件
filename = 'data.pkl'
with open(filename, 'wb') as f:
    pk.dump(dt1, f)
    pk.dump(dt2, f)
    pk.dump(dt3, f)

##将文件反序列化到对象
with open(filename, 'rb') as f:
    dt1 = pk.load(f); print(dt1)
    dt2 = pk.load(f); print(dt2)
    dt3 = pk.load(f); print(dt3)
    pass

######################################################################
##配置文件读写===============
######################################################################
# 最常用的配置文件，就是INI文件。
import configparser
config = configparser.ConfigParser()

config['DEFAULT'] = {'ServerAliveInterval': '45',
                        'Compression': 'yes',
                        'CompressionLevel': '9'}
config['DEFAULT']['ForwardX11'] = 'yes'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'
topsecret['ForwardX11'] = 'no'

with open('example.ini', 'w') as configfile:
    config.write(configfile)

# 生成的example.ini配置文件如下：
# [DEFAULT]
# ServerAliveInterval = 45
# Compression = yes
# CompressionLevel = 9
# ForwardX11 = yes

# [topsecret.server.com]
# Port = 50022
# ForwardX11 = no

# 读取配置文件
config = configparser.ConfigParser()
config.read('example.ini')

scts = config.sections()
topsecret = config['topsecret.server.com']
sFrd = topsecret['ForwardX11']
port = topsecret['Port']

for key,val in config['DEFAULT'].items():  
    print(key,'=',val)


######################################################################
##JSON文件操行===============
######################################################################
# JSON是一种轻量级的数据交换格式，采用键值对表示数据
# JSON模块也是典型的对象序列化的一种

import json
nums = [1,2,5,0]
BOOKS = {
    '0132269937':{'title':'Core Python',
                    'edition':2,
                    'year':2007,},
    '0132356139':{'title':'Python Web',
                    'authors':['Jeff', 'Paul'],
                    'year':2009,},
    '0137143419':{'title':'Python Fundamentals',
                    'year':2009,},
}

filename = 'numbers.json'
#以JSON格式保存对象数据
with open(filename, 'w') as f:
    json.dump(BOOKS, f)
    # json.dump(nums, f)

#读取JSON格式的对象数据
with open(filename) as f:
    bks = json.load(f)
    print(bks)
    # nums = json.load(f)
    # print(nums)
