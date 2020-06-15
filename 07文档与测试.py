#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

######################################################################
#  Python文档化
######################################################################

import survey   #导入被测试类、函数等

##======显示模块描述内容=========
##
##显示模块描述(主要有7个)
print('='*60)
print('1模块name：', survey.__name__)          #模块的名称
print('2模块doc：', survey.__doc__)            #模块的描述信息
print('3模块loader:', survey.__loader__)       #本模块的调用者，系统自动生成的
print('4模块file:', survey.__file__)           #模块所在全路径
print('5模块package:', survey.__package__)     #模块所在包
print('6模块cached', survey.__cached__)        #模块生成机器码文件.pyc的全路径
print('7模块spec', survey.__spec__)            #模块规范说明，包括name,loader,origin(即file)
# print('8模块dict', survey.__dict__)

#其实，第8个属性：__dict__属性中以字典的方式包含了：
# 1）前面7个属性的内容
# 2）内置模块属性__builtins__，所有属性是相同的，
# 3）以及模块特有的函数、类等标识符。
print('='*60)
for k,v in survey.__dict__.items():
    if k != '__builtins__': 
        print(k,':', v)
print('='*60)
print(dir(survey))  #dir（）显示的是__dict__属性的关键字名称


#下面打印本模块的相关信息
print('='*60)
print('\n模块name：', __name__)     #名称不是模块名，而是__main__
print('模块doc：', __doc__)
print('模块loader:', __loader__)
print('模块file:', __file__) 
print('模块package:', __package__) 
print('模块debug', survey.__cached__)
print('模块debug', survey.__spec__)
print('='*60)

##======显示函数功能描述内容=========
##
print('='*60)
print(survey.openLogFile.__doc__)


##======显示函数参数描述内容=========
##
print('='*60)
print(survey.getFormatedName.__doc__)           #如果没有，则返回None
print(survey.getFormatedName.__annotations__)   #如果没有，则返回{}


##======类对象的描述内容=========
##
print(survey.AnonymousSurvey.__doc__)                    #类功能描述
print(survey.AnonymousSurvey.storeResponse.__doc__)         #类方法功能描述
print(survey.AnonymousSurvey.storeResponse.__annotations__) #类方法参数描述


######################################################################
#  Python单元测试自动化
######################################################################

#单元测试类，用于测试survey模块
import unittest #导入单元测试库

#unittest提供代码测试工具
#操作过程：
# 1.文件开头，导入库：import unittest
# 2.创建一个继承于unittest.TestCase的测试类
# 3.测试类中定义测试函数，一个用例一个测试函数，测试函数名必须以test_开头（后面最好是被测试的类或函数名，以便理解）
# 4.测试函数中，使用断言来判断执行结果
# assertEqual, asserNotEqual
# assertTrue, assertFalse
# assertIn, assertNotIn ...
# 5.文件最后，执行unittest.main()


##======函数的单元测试=========
##
class MyFunTest(unittest.TestCase):
    #用例1
    def test_getFormatedName1(self):
        fullName = survey.getFormatedName('janis','joplin')
        self.assertEqual(fullName,'Janis Joplin')

    #用例2
    def test_geFormatedName2(self):
        fullName = survey.getFormatedName('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(fullName,'Wolfgang Amadeus Mozart')

    #用例3，检查空串。这个用例应该是失败，因为函数没有处理前后缀空格
    def test_getFormatedName3(self):
        fullName = survey.getFormatedName('jack', 'wang', ' ')
        self.assertEqual(fullName,'Jack Wang')

##======类的单元测试=========
##
class MyClassTest(unittest.TestCase):

    #用例1
    def test_Response(self):
        #构建临时对象测试
        question = "你学的第一种语言是什么?"
        mySurvey = survey.AnonymousSurvey(question)
        mySurvey.storeResponse('中文')
        self.assertIn('中文', mySurvey.responses)

    #此函数只在开始时调用一次，所以对象构建可以放在这里
    def setUp(self):
        question = "你还学了哪些语言?"
        self.mySurvey = survey.AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']
    
    #用例2
    def test_singleResponse(self):
        self.mySurvey.storeResponse(self.responses[0])
        self.assertIn(self.responses[0], self.mySurvey.responses)

    #用例3
    def test_MultiResponse(self):
        for res in self.responses:
            self.mySurvey.storeResponse(res)

        for res in self.responses:
            self.assertIn(res, self.mySurvey.responses)

try:
    result = unittest.main()
except :
    pass

