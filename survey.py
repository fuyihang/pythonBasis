#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

################模块说明信息__doc__########################
# 模块说明信息放在文件的所有代码的前面
# 使用多行注释号括起来
# 在系统中使用__doc__可查看

"""\
本模块定义了函数和类，用于测试和呈现文档描述之用。
"""


################函数功能说明信息__doc__########################
# 
# 函数功能说明，放在def这一行后面
# 使用多行注释号括起来
# 在系统中使用__doc__可查看
def openLogFile():
    '''\
本函数openLogFile负责打开日志文件，以便记录系统运行的信息
请注意在使用请关闭日志文件。
'''
    pass

################函数参数说明信息__doc__########################
# 函数参数说明，内置在函数定义中
# 使用:描述形参的数据类型
# 使用->描述返回值的数据类型
# 在系统中使用__annotations__可查看
def getFormatedName(first:str, last:str,middle:str='')->str:
    """\
        本函数完成姓和名的拼接，实现全名的功能！
    """
    if middle:
        fullName = first + ' ' + middle +' ' + last
    else:
        fullName = first + ' ' + last
    
    return fullName.title()


################类对象说明信息########################
# 同前面函数的描述
# 类对象的说明放在__doc__属性中
# 类方法的功能说明放在__doc__属性中
# 类方法的参数说明放在__annotations__中
class AnonymousSurvey():
    """\
        本类AnonymousSurvey为自定义类，实现匿名调查功能。
    """
    def __init__(self, question):
        self.question = question
        self.responses = []

    def showQuestion(self):
        '''\
            本方法showQuestion用于显示问题。
        '''
        print(self.question)

    def storeResponse(self, newResponse:list)->None:
        """\
            本方法storeResponse将新的答案和响应添加到原来的响应列表中。
        """
        self.responses.append(newResponse)

    def showResults(self):
        print('Survey Result:')
        for res in self.responses:
            print('-'+res)
