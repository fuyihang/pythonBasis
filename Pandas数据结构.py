# Pandas 数据结构

import pandas as pd
import numpy as np

######################Series整列数据的操作#############################

#~ ##########检验数值是否缺失############
#~ sr2 = sr.isnull()
#~ print(sr2)         #sr2中值为True的表示该索引对应的值是缺失的

#~ #也可直接使用PD的函数
#~ #print(pd.isnull(sr))
#~ #print(pd.notnull(sr))

#~ ##########筛选、过滤条目，指定一个值的过滤条件############
#~ print('\n只保留>=2的行：')
#~ sr2 = sr[sr>=2]
#~ print(sr2)

#~ ###############Series的运算#################
#~ #序列的纯量乘法
#~ print('\n序列值都乘以2：')
#~ sr2 = sr*2
#~ print(sr2)

#~ #序列的加法，按照索引将不同列的值相加
#~ #因为sr2没有索引a的值，所以相加后索引a的值为空值(NaN)
#~ print('\n序列值相加：')
#~ sr2 = sr[sr>=2]
#~ print(sr+sr2)

#~ #序列的数学函数
#~ print('\n序列值都求指数：')
#~ sr2 = np.exp(sr)
#~ print(sr2)

#~ ###############序列的统计函数#################

#~ sr = pd.Series([1,2,3,2,2,3], index=['a','b','c','d','e','f'])
#~ print('\n', sr)

#~ #统计值出现的次数
#~ sr2 = sr.value_counts() #统计序列：索引为值，值为次数
#~ sr2.index.name = "值"
#~ sr2.name = "次数"
#~ print("\n统计值出现的次数：\n", sr2.sort_values())

#~ #函数max,min,count,sum
#~ print('\nMAX=', sr.max())

#~ #去重后的值list
#~ print(sr.unique())

#~ sr2 = sr.describe() #描述性统计count,mean,std,min,max,25%, 50%,75%
#~ print(sr2)
#~ print(sr2.loc['25%'])

#~ #计算四分位数IQR
#~ sr2['IQR'] = sr2.loc['75%'] - sr2.loc['25%']
#~ print(sr2)

###################DataFrame数据表对象#####################

#DataFrame是Series的容器

################DF的创建###########
#~ #1.利用Series创建表格. 1列DF
#~ sr = pd.Series([1,2,3], index=['a','b','c'])
#~ df = pd.DataFrame(sr)    
#~ print('\n',df)

#~ #注：这是2行DF，而不是2列。
#~ df = pd.DataFrame([sr, sr*2]) 
#~ print('\n',df)

#~ #2.利用映射创建
#~ data = {'one':3,
        #~ 'two':range(1,6),
        #~ 'letter':['a','a','b','b','c']}
#~ df = pd.DataFrame(data)
#~ print('\n',df)

#~ #3.利用多个列表创建。构建2行DF，不指定index,columns时表示默认索引为0~N-1
#~ df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],
                    #~ index = ['a','b','c'],           #index表示行索引
                    #~ columns=['数量','价格','金额']    #columns表示列标题
                    #~ )  
#~ print('\n',df)

################DF的索引、值访问###########
#~ print(df.columns)  #标题list，相当于Series的名称，唯一标识
#~ print(df.index)    #索引list，相当于Series的index
#~ print(df.values[0:2]) #指定序号列的值list

#~ #访问列：单列/多列
#~ print('\n列：金额\n', df['金额'])     #按列标题访问列
#~ print('\n列：数量，价格\n', df[['数量', '价格']]) #按列标题访问多列
#~ #注：不能按序号访问DF，因为它不知道序号是行还是列的索引了。

#~ #访问行：单行/多行
#~ print('\n第1行：\n', df.iloc[0])      #按索引序号访问单行
#~ print('\n行：0:2\n', df.iloc[0:2])    #按索引序号访问多行
#~ #注：经验证，使用df[0:2]也当成行访问，但不建议

#~ print('\n行：a\n',df.loc['a'])     #按索引名称访问单行
#~ print('\n行：a:b\n',df.loc['a':'b'])     #按索引名称访问多行（连续）
#~ print('\n行：a,c\n',df.loc[['a','c']])     #按索引名称访问多行（不连续）

#~ #访问指定的行列块.df.ix[rows, columns]
#~ print('\n0：3~"数量"\n', df.ix[0:3, '数量'])
#~ print('\n0：3~"数量","价格"\n', df.ix[0:3, ['数量','价格']])

#~ #访问指定行列的值
#~ print(df['金额']['a'])
#~ print(df['金额'][0])

#~ #更新指定的值
#~ df['金额']['a'] = 20   #先列标题，再用索引
#~ print('\n',df)

#~ #删除行
#~ df2 = df.drop('a')  #原DF不会改变
#~ #df2 = df.drop(['a','b'])  #原DF不会改变，删除多行
#~ print(df2)

#~ df2 = del df[0:2]

#~ print(df2)

#~ del df.loc['b']
#~ print(df)

#~ #删除列
#~ del df['数量']    #原DF会改变
#~ print(df)

#~ #查看前N行
#~ print('\n前2行：\n', df.head(2))  #default=5
#~ #查看后N行
#~ print('\n后N行：\n', df.tail())  #default = 5

######更新####

#~ #######列操作############
#~ #排序
#~ #按指定列的值排序，临时排序
#~ df2 = df.sort_values(['数量'], ascending=False) #默认是ascending=True升序
#~ print('\n按数量值降序:\n', df2)

#~ df3 = df2.sort_index()  #默认是ascending=True升序
#~ print('\n按索引排序：\n', df3)

#~ #筛选列
#~ df2 = df[df['数量']>2]  #只保留满足条件的行
#~ print(df2)

#~ #增加列
#~ df['达标'] = None         #增加空列
#~ df['达标'] = 5            #增加固定值的列
#~ df['达标'] =list([4,3,3])   #增加指定值的列
#~ #df['达标'] = df['数量'] +1 #基于原有列增加列
#~ df['flag'] = df['数量']>=df['达标'] #基于原有列增加列
#~ print('\n', df)

#~ #插入列
#~ print('\n在第2行处插入bar列：\n')
#~ df.insert(1,'bar', df['数量']*2)  #在第2列插入名为'bar'，其值为'数量'列的2位
#~ print(df)

#~ #删除列
#~ df['foo'] = 10  #先增加行，再删除
#~ df['foo2'] = range(2,5)
#~ print(df)

#~ del df['foo']
#~ print("\n删除’foo‘列：\n",df)
#~ sm = df.pop('foo2')
#~ print("\n删除’foo2‘列：\n",sm)

#~ #行列转置
#~ dft = df.T
#~ print(dft)

#######################DF的统计操作函数############################
#读取文件中的DF表格
filename = "..\DataSet\数据分析.xlsx"
with pd.ExcelFile(filename) as xls:
    users = pd.read_excel(xls, sheetname='用户明细')  
#~ #print('\n',users)

#~ #表格信息：N个列，N个行，多少非空行，等等
#~ #print(users.info()) #返回各列的非空行行数
#~ #print(users.dtypes) #返回各列的数据类型
#~ #print(users.shape)  #返回行数和列数
#~ #len(users)          #返回行数

#~ #对于单列的统计，和Series一样使用函数max,min,count,...
#~ #print("\n年龄MAX=", users['年龄'].max())

#~ #分类计数:单列
#~ usr = users[['用户ID','省份']]  #一般指定操作列，避免海量计算
#~ df2 = usr.groupby('省份')  #指定分类列-索引.
#~ df3 = df2.count()          #对所有列进行汇总
#~ print('\n各省份人数\n', df3.sort_values(['用户ID']))  #按值排序，默认ascending=True升序
#~ print('\n广东=\n',df3.loc['广东'])  #指定省份的人数

#~ #分类计数：两列
#~ usr = users[['用户ID','省份','性别']]
#~ df2 = usr.groupby(['省份','性别']).count()
#~ df3 = df2.sort_values(['用户ID'], ascending=False)
#~ print('\n各省份+性别的人数：\n', df3)
#~ print('\n广东：\n',df3.loc['广东'])  #返回表(性别-用户ID)
#~ print('\n广东男=',df3.loc['广东','男']['用户ID'])  #返回值
#~ print('\n广东男女和=', df3.loc['广东']['用户ID'].sum())  #返回指定省份的总用户数

#交叉表：分类计数
#~ df2 = pd.crosstab(users['省份'], users['性别'])
#~ print(df2)
#~ print('\n广东:',df2.loc['广东'])  #返回行
#~ print('\n列：女\n', df2['女']) #返回列
#~ #返回值
#~ print('\n广东-女=',df2['女']['广东'])  #参数顺序：先列再行
#~ print('\n广东-女=',df2.loc['广东']['女'])  #如果先行再列，则需要使用loc关键字

#~ #离散化计数
#~ userAge = pd.cut(users['年龄'], 10)  #将数据按照年龄划分成10个组
#~ #users['年龄段']= userAge   #将年龄段直接增加到原DF中
#~ df2 =userAge.value_counts()  #进行分段统计
#~ print(df2)

