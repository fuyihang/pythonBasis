# -*- coding: utf-8 -*-

# Python学习 函数、类、模块
# 任务一、定义一个函数，在“我的文档”目录下，查找是否有某个文件或子目录，找到后返回True,其余返回False

# os.environ['HOME'] 可以获取我的文档
# os.environ['USERPROFILE'] windows下用户工作目录

import os

def searchFile(rootPath, sFileName):
    # 判断路径是否存在
    if not os.path.exists(rootPath):
        print('错误：指定路径不存在！')
        return False
    # 判断路径是否是目录
    if not os.path.isdir(rootPath):
        print('错误：指定路径不是目录！')
        return False

    # 只匹配文件
    names = os.listdir(rootPath)
    searchingFileName = sFileName.lower()
    for name in names:
        file = os.path.join(rootPath, name)
        tmpName = file.lower()
        if tmpName.find(searchingFileName) != -1:
            return True     #找到一个即中止搜索

    return False

# if __name__ == '__main__':

# 构造测试案例
localDir = os.getcwd()

lt_tests = [
    (localDir, '基本格式', True),
    (os.path.join(localDir, '2'), '基本格式', False),
    # (os.path.join(localDir, '基本格式.py'), '', False),
    ('..', 'dataset', True),
    ('..', 'DataSet', True) 
]

# 执行测试案例并验证
for path, file, retVal in lt_tests:
    print('执行案例:',path, file)
    ret = searchFile(path, file)
    assert(ret==retVal)

# 字符串数据类型
name = 'Python'

print(name[3])
print(name[-1])

# 切片
print(name[0:3])
print(name[:])

lt = [2, 'OK', 'hello', 5, 7]

print(lt[1])
for val in lt:
    print(val)

# 切片
print(lt[2:])
