# -*- coding: utf-8 -*-
# @Time    : 18-8-9下午5:47
# @Author  : 石头人m
# @File    : stone-test.py

f = open('df_all.csv', 'r', encoding='utf-8')
dataf = f.readlines()
print(len(dataf))

with open('df_all_01.csv', 'w') as f:
    for i in range(len(dataf)):
        line = dataf[i].replace('.0', '')
        print(line)
        line = line[:-3].replace(',', ' ')
        f.write(line + '\n')
