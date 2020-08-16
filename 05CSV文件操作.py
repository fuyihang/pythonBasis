#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

######################################################################
##CSV文件操行===============
######################################################################
# CSV（Comma-Separated Value）格式的文件是一种特殊的文本文件，每一行数据用逗号隔开
# CSV格式的文件通常用于电子表格软件和纯文本之间交互数据
# 理论上，CSV文件可以和纯文本文本一样处理， 但是如果文本中本来就包含有逗号，就比较麻烦。
# 而CSV模块可以较好地处理字段值中本身就带有逗号的情况

import csv

#采用csv标准库
#https://docs.python.org/3/library/csv.html

#1.用reader/writer对象，操作的是列表或元组
#csv.reader(csvfile, dialect='excel', **fmtparams)
#csv.writer(csvfile, dialect='excel', **fmtparams)


#2.用DictReader对象，操作的是字典
#csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
#csv.DictWriter(f, fieldnames, restval='', extrasaction='raise', dialect='excel', *args, **kwds)


###########################csv.reader/writer操作###########################################

##列表方式写入
# 
# 应该使用newline=''

filename ='mycsv.csv'
with open(filename, 'w', newline='') as f:
    #delimiter分隔符指定为CSV（逗号），或者TSV（\t）等等。
    #lineterminator行分隔符默认为\r\n，所以会导致写入的行与行之间存在空行，所以需要指定为\n即可
    writer = csv.writer(f, delimiter=',',lineterminator='\n')
    writer.writerow(['ID', 'firstname', 'lastname'])
    writer.writerow([1, 'John', 'Alex'])
    writer.writerow([2, 'Mike', 'Michal'])

##列表方式读取
with open(filename, 'r', newline='') as f:
    reader = csv.reader(f)

    #1.可以用next函数结合while一行一行地读取
    #注意：next会抛StopIteration异常
    header_row = next(reader)   #返回行头list，
    #打印出标题
    for hd in header_row:
        print(hd, end=' ')
    print('')

    #2.遍历reader，遍历数据项
    for row in reader:
        print(row)
        # print(row[0], row[1])
    print('行数=',reader.line_num)    #返回实际读取的行数


##元组方式写入
# 
DATA = (
    (9, 'Web Clients', 'base64,urllib'),
    (10, 'Web Programming:CGI&WSGI', 'cgi,time,wsgiref'),
    (13, 'Web Services', 'urllib, twython')
)

filename = 'mycsv2.csv'
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    for record in DATA:
        writer.writerow(record)

with open(filename, 'r', newline='') as f:
    reader = csv.reader(f)
    for id, tl, des in reader:
        print(id, tl, des)


###########################csv.DictReader/DictWriter操作###########################################
#相比csv.reader/writer，DictReader/DictWriter只是：
# 1）多一个属性fieldnames
# 2）多一个方法writeheader()

filename = 'mydictcsv.csv'
fieldName = ['名字', '姓']
with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldName)

    writer.writeheader()    #写标题
    writer.writerow({'名字':'小明', '姓':'黄'})
    writer.writerow({'名字':'大刚', '姓':'李'})
    writer.writerow({'名字':'国安', '姓':'张'})

##字典方式读取
# 
# 如果CSV文件第一行是标题
with open(filename, 'r', newline='') as f:
    reader = csv.DictReader(f)
    fieldName = reader.fieldnames
    print(fieldName)
    for row in reader:
        print(row['名字'], row['姓'])           #注意，键必须与第一行标题相同，否则异常

        # for fld in fieldName:                #如果不知道标题名，也可以这样访问
        #     print(row[fld], end=' ')
        # print('')
    print('读取行数:{}'.format(reader.line_num))


##字典方式读取
# 
# 如果CSV文件第一行不是标题
fields = ['firstName', 'lastName']
with open(filename, 'r', newline='') as f:
    reader = csv.DictReader(f, fieldnames = fields)
    for row in reader:
        print(row['firstName'], row['lastName'])
