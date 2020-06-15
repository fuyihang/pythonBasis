
# -*- coding:utf-8 -*-

"""
# 本文件实现了一个日志功能模块，提供一个分级记录日志的接口

"""
import os
from datetime import datetime
from enum import Enum

class MyLogLevel(Enum):
    NONE = 0            #无级别
    TIP = 1             #提示，黑色
    WARNING = 2         #警告，蓝色
    ERROR = 3           #错误，红色

class log():
    logFileName = ''
    Lev = 2
    f = None
    def __init__(self):
        pass

    def __del__(self):
        if self.f != None:
            self.f.close()

    #产生日志文件的全路径
    def _generateFileName(self):
        logDir = 'Log'                  #固定日志目录 
        currentDir = os.getcwd()
        if not os.path.exists(logDir):
            os.mkdir(logDir)
        currentDir = os.path.join(currentDir, logDir)

        dt = datetime.now()
        fileName = dt.strftime("log%Y%m%d%H.txt") ##日志名称形如 log年月日时.txt

        self.logFileName = os.path.join(currentDir, fileName)

        return self.logFileName

    def setLevel(self, nLevel):           #设置日志记录级别，只有超过这个级别的日志，才会显示出来。
        self.Lev = nLevel

    def writeLog(self, strlog, nLevel=MyLogLevel.TIP):
        """
        本函数实现日志功能，会在日志前自动增加时间
        会根据日志级别自动在屏幕上显示不同的颜色
        """
        if self.f == None :
            try:
                self._generateFileName()
                self.f = open(self.logFileName, 'a+')
            except Exception as e:
                print("日志文件打开失败！err=[{}]".format(e))
                return

        if self.f != None:
            dt = datetime.now()
            prefix = dt.strftime('%Y%m%d%H%M%S')
            if nLevel == MyLogLevel.TIP:
                prefix += '[Tip]'
            elif nLevel == MyLogLevel.WARNING:
                prefix += '[Warn]'
            elif nLevel == MyLogLevel.ERROR:
                prefix += '[Error]'
            else:
                prefix += '[None]'
            self.f.write(prefix)                        #日志自动加上时间，级别
            self.f.write(strlog)
            self.f.write('\n')                          #自动加上换行符
        
        #在界面上输出，可根据级别输出不同的颜色
        nColor = 30         #默认，黑色
        if nLevel == MyLogLevel.TIP:
            nColor = 30
        elif nLevel == MyLogLevel.WARNING:
            nColor = 34
        elif nLevel == MyLogLevel.ERROR:
            nColor = 31
        else:
            nColor = 30     #默认，黑色
        
        #只级别高的才显示
        if isinstance(nLevel, MyLogLevel):
            nLevel = nLevel.value
        if nLevel > self.Lev: 
            print('\033[{}m{}\033[0m'.format(nColor, strlog))

if __name__ == '__main__':
    lg =log()
    lg.writeLog('提示：程序正常记录！',MyLogLevel.TIP)
    lg.writeLog('警告：程序出现异常！', MyLogLevel.WARNING)
    lg.writeLog('错误：程序运行错误！', MyLogLevel.ERROR)
