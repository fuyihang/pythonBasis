#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

######################################################################

########  Python基本格式

######################################################################

##======官方参考文档=========
##

#一）官方参考文档（英文）：
# https://docs.python.org/3/index.html
#二）官方参考文档（中文）：
# https://docs.python.org/zh-cn/3.7/index.html

#其它中文参考文档：
#三）Python中文开发者社区（中文）
# https://www.pythontab.com
#四）Python基础课程（中文）：
# http://www.runoob.com/python3/python3-file-methods.html

##======关于脚本执行能力=========
##
# 如果允许Python脚本文件可以直接执行，则要在.py文件的第一行加上如下"shebang行"
#!/usr/local/bin/python3

##======关于编码=========
##
#Python脚本文件的编码默认使用utf-8编码，可以在.py文件的 第一或第二行加上如下行
# -*- coding: UTF-8 -*-

##======关于注释=========
##
#1.单行注释用#
#2.多行注释用三个单引号或三个双引号,将要注释的内容包围起来

# print('Hello World')

'''
print('Hello World')
print('OK')
'''

"""
print('Hello World')
print('OK')
"""


##======关于缩进=========
##
# 缩进（空格和制表符）
# 1）一个Tab键，默认是4个空格
# 2）其它开发语言中，缩进是为了美观；同一段代码块需要用{}来括起来
# 3）但在Python中，缩进比较严格：
#   缩进不是为了美观，而是用来决定代码行的层次（语句组）
#   同一段代码块必须包含相同的缩进空格数。

age = 20
if age < 18:
    print("不允许你进入会场！") 
else:
    print("允许进入会场！")

##======标识符命名规范=========
##
##标识符，指的是变量名、函数名、类名等。
# 1）由字母、数字和下划线组成，第一个字符不能是数字
# 2）不能包含空格，不能用关键字作标识符（见后面关键字）
# 3）标识符对大小写敏感，即要区分大小写
# 4）标识符应该与其它Python内置标识符尽量避免命名冲突，以免引起意想不到的后果。
# 5）一般情况下，标识符的命名的写法遵循两种模式：
#   驼峰命名法：即包含多个单词时首字母大写，其余字母小写，
#             比如userName，或UserName。
#   下划线分隔法：即包含多个单词时用下划线隔开，
#             比如user_name, sum_list。
# 类的命名，第一个字母一般大写
# 函数的命名，第一个字母一般小写

#查看保留的关键字
import keyword
print(keyword.kwlist)

# 查看内置标识符
import builtins
dir(builtins)

# 内置标识符包括：
# 1）内置特殊对象，如Ellipsis,NotImplemented
# 2）内置数据类型，如bool, int, str, list, tuple, dict, set, frozenset等
# 3）内置布尔运算符，如and, or, not
# 4）内置函数，如abs, sum, dir, help, id
# 5）内置异常,如EOFError, NameError
# 6）系统特殊属性，如__debug, __name__
# 7）其它系统内置类

##======Python语句书写格式=========
##
# 语句书写格式有三种情况：
# 1）一行一句（建议）
# 2）一行多句（不建议）
# 3）一句多行（为了易读性，可以使用）

#1.一行一句
# 一条python语句在一行内写完
print("Hello, World")

#2.一行多句
# 但是，也可以一行有多条语句,必须要使用分号隔开
msg = "Hello"; print(msg)

#3.一句多行，显性的换行
# 也可以一条语句在多行（物理行）
#如果语句很长，可用反斜杠(\)来实现多行语句
msg = "在这个个列表中，" + \
    "最大的值是" + \
    "75."
print(msg)

# 类似如下语句在多行，其可读性大大增强
# if (1900 < year < 2100) and (1 <= month <= 12) \
#    and (1 <= day <= 31) and (0 <= hour < 24) \
#    and (0 <= minute < 60) and (0 <= second < 60):
#         return 1

# 4.隐性的换行
month_names = ['Januari', 'Februari', 'Maart',      # These are the
               'April',   'Mei',      'Juni',       # Dutch names
               'Juli',    'Augustus', 'September',  # for the months
               'Oktober', 'November', 'December']   # of the year

# 5.隐性的合并（不建议，装B用法）
msg = 'Hello ' 'World'
print(msg)

msg = "Hello "
"World"
print(msg)
