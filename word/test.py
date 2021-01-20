# -*- coding: utf-8 -*-
"""
**********************************
   File Name：     test
   Description :
   Author :       shine
   date：          2021/1/13
**********************************
"""

f1 = open('src.txt', encoding='utf-8')
f2 = open('now.txt', 'w')

infos = f1.readlines()

infos = infos[0].split(' ')

w_info = []

for x in infos:
    if x is not '':
        w_info.append(x)

for y in w_info:
    f2.write(y)
    try:
        res = y.index(',')
        f2.write('\n')
    except:
        print(y)




