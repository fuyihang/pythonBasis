#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

######################################################################

#第*部分  Python异常处理

######################################################################

##======异常语句=======================================
##
# Python程序发生异常时，异常信息保存在系统中，可通过sys.exc_info()获取
# 不过一般直接使用异常对象就可以了。

# try-except-else-finally （其中except可重复，else, finally可选）
# 1.异常语句是对try子句代码异常的检测，代码执行的顺序有两种：
#   无异常时：try子句-->else子句-->finally子句
#   有异常时：try子句-->except子句-->finally子句
# 2.异常发生时，try子句余下的代码不会被执行
# 3.如果异常的类型与excep之后的名称匹配，则对应的excep子句被执行
# 4.如果没有匹配的异常类型，则异常将会传递到上层的try中，如果没有上层的try，程序将崩溃并中止。
# 5.还可以使用raise手工抛出异常。

import sys

filename = 'test.txt'
try:
    f = open(filename, 'r')
    line = f.readline()
    # num = int(line.strip())
except FileNotFoundError as err:                        #对单个异常处理
    print("文件不存在！错误代码={}, 错误描述={},文件名={}".format( \
            err.errno, err.strerror, err.filename))
except (ValueError,TypeError) as err:                   #匹配多个异常
    print("类型或值转换错误！except={}".format(err))
else:                                                 #匹配所有错误
    print("未知错误！", sys.exc_info())
    #raise                                              #也可以继续抛出异常
    #raise Exception('手工抛出的异常！')                   #或手工抛出特定异常
finally:
    f.close()

##异常的顺序===============
# 
# 如果异常类之间存在派生关系，建议子类在前，父类在后。
# 如下：OSError是FileNotFoundError的父类，下面的代码将不会处理FileNotFoundError异常
filename = 'myfile.txt'
try:
    f = open(filename, 'r')
    line = f.readline()
except OSError as err:                                  
    print("文件操作失败！error={}".format(err))
except FileNotFoundError as err:
    print("文件不存在！错误代码={}, 错误描述={},文件名={}".format( \
            err.errno, err.strerror, err.filename))


##======自定义异常=======================================
##
# 1.异常一般从Exception派生
# 2.大多数异常类名都以Error结尾

class MyError(Exception):
    def __init__(self, code, msg=""):
        self.code = code
        self.msg = msg
    def __str__(self):
        return repr('errCode={},errMsg={}'.format(
                    self.code, self.msg))

##
import os
try:
    logFile = 'Log.txt'
    if not os.path.exists(logFile):
        raise MyError(2, '文件不存在')
except MyError as err:
    print(err)
    pass
