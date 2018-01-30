#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types
class Restaurant(object):
#__代指私有变量
    def __init__(self, name, position, account):
        self.name = name
        self.position = position
        self.__account = account

    def print_info(self):
        print '%s : %s , %s' %(self.name, self.position, self.__account)

class CoffeeRes(Restaurant):
    pass


if __name__ =='__main__':
    xiaoxiong = CoffeeRes('xiaoxiong', 'jiaodadonglu', '20000000')
    xiaoxiong.name = 'littlebear'
    xiaoxiong.print_info()
    print isinstance(xiaoxiong, Restaurant)
    print type('string') == types.StringType