# -*- coding: utf-8 -*-
def func_abs(x):
    if x < 0:
        return x, -x
    else:
        return x


if __name__ == '__main__':
    a = -234
    x, y = func_abs(a)
    print x

def caculate_salary(*salary):
    sum_salary = 0
    for sal in salary:
        sum_salary = sum_salary +sal
    return sum_salary

salary_list =[10000, 20000, 15000, 16000]
sum_all = caculate_salary(*salary_list)
print sum_all
