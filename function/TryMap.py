# -*- coding: utf-8 -*-

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
test = [1, 2, 3, 4, 5, 6]
def is_odd(x):
    if(x % 2 == 1):
        return x
map_result = map(is_odd, test)
print map_result


def append(x, y):
    return x * 10 + y

print reduce(append, test)

print filter(is_odd, test)