# -*- coding: utf-8 -*-
# 双下划线开头和结尾的是特殊变量

#try list
list = ['call', 'what', 'you', 'want']
list.append(2017)
list.insert(1, 'it')
print len(list)

#try tuple可查不可变
boyfriend = ('icodeu', 1992, 'zz')
for msg in boyfriend:
    print msg

#try input
salary = int(raw_input('salary:'))
if(salary <= 20000):
    print '中等偏渣的程序员'
else:
    print '匿名区的程序员'

#dict对应Java中的map
#set去重
