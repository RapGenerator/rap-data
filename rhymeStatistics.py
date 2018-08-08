# -*- coding: utf-8 -*-
# @Time    : 18-8-8上午10:44
# @Author  : 石头人m
# @File    : rhymeStatistics.py

import pandas as pd
import numpy as np
from pypinyin import lazy_pinyin, Style
from collections import Counter

df_all = pd.read_csv('df_all.csv', names=['lyric', 'isBad'])
len_df = len(df_all)
print('数据总条数:', len_df)
# 得到每行没字的韵母
df_all['rhyme'] = df_all.loc[:, 'lyric'].apply(lambda x: lazy_pinyin(x, style=Style.FINALS, strict=False))

df_all['Finals_neg5'] = df_all['rhyme'].apply(lambda x: x[-5:-4][0] if len(x) > 4 else None)
df_all['Finals_neg4'] = df_all['rhyme'].apply(lambda x: x[-4:-3][0] if len(x) > 3 else None)
df_all['Finals_neg3'] = df_all['rhyme'].apply(lambda x: x[-3:-2][0] if len(x) > 2 else None)
df_all['Finals_neg2'] = df_all['rhyme'].apply(lambda x: x[-2:-1][0] if len(x) > 1 else None)
df_all['Finals_neg1'] = df_all['rhyme'].apply(lambda x: x[-1])
df_all.to_csv('df_all_rhyme_Finals.csv', index=False)

# 将韵母列转list
# list_rhyme = df_all.loc[:, 'rhyme'].tolist()


# 1 排韵
'''
def dict_count_paiyun(list_last):
    len_list_last = len(list_last)
    res_count = {}  # 存放计数字典
    head, tail = 0, 0
    while head < len_list_last:
        # print(list(list_last.iloc[tail]), list(list_last.iloc[head]))
        while tail < len_list_last and list(list_last.iloc[tail]) == list(list_last.iloc[head]) \
                and df_all.loc[head, 'lyric'] != df_all.loc[tail, 'lyric']:
            if len(df_all.loc[tail]) > 30:
                print(df_all.loc[head, 'lyric'], df_all.loc[tail, 'lyric'])
                pass
            tail += 1
        if tail - head > 1:
            dict_key = 'ya_0' + str(tail - head) if (tail - head) < 10 else 'ya_' + str(tail - head)
            res_count[dict_key] = res_count.get(dict_key, 0) + 1
        head = tail
        tail += 1
    res_count = sorted(res_count.items(), key=lambda item: item[0])
    return res_count


print('排韵...')
for i in range(5):
    # list_last = [line[-(i + 1):] for line in list_rhyme if len(line) > i]
    list_last = df_all.iloc[:, -(i + 1):]
    res_last = dict_count_paiyun(list_last)
    print('排韵-%d押:' % (i + 1))
    print(res_last, '\n\n')



# 2 隔行韵


# 3 交韵
def dict_count_jiaoyun(list_last):
    len_list_last = len(list_last)
    res_count = {}  # 存放计数字典
    head, tail = 0, 0
    while head < len_list_last:
        # print(head, tail)
        while tail + 1 < len_list_last and list(list_last.iloc[head]) == list(list_last.iloc[tail]) \
                and list(list_last.iloc[head + 1]) == list(list_last.iloc[tail + 1]):
            tail += 2
        if tail - head > 2:
            dict_key = 'ya_0' + str(tail - head) if (tail - head) < 10 else 'ya_' + str(tail - head)
            res_count[dict_key] = res_count.get(dict_key, 0) + 1
        head = tail
    res_count = sorted(res_count.items(), key=lambda item: item[0])
    return res_count


print('交韵...')
for i in range(5):
    list_last = df_all.iloc[:, -(i + 1):]
    res_last = dict_count_jiaoyun(list_last)
    print('交韵-%d押:' % (i + 1))
    print(res_last, '\n\n')

'''


# 4 抱韵
def dict_count_baoyun(list_last):
    len_list_last = len(list_last)
    res_count = {}  # 存放计数字典
    head = 0
    dict_key = 'ya_count'
    while head + 3 < len_list_last:
        if list(list_last.iloc[head]) == list(list_last.iloc[head + 3]) \
                and list(list_last.iloc[head + 1]) == list(list_last.iloc[head + 2]):
            print(head, df_all.loc[head, 'lyric'], df_all.loc[head + 1, 'lyric'], df_all.loc[head + 2, 'lyric'],
                  df_all.loc[head + 3, 'lyric'])
            head += 3
            res_count['ya_count'] = res_count.get(dict_key, 0) + 1
        head += 1
    res_count = sorted(res_count.items(), key=lambda item: item[0])
    return res_count


print('抱韵...')
for i in range(5):
    list_last = df_all.iloc[:, -(i + 1):]
    res_last = dict_count_baoyun(list_last)
    print('抱韵-%d押:' % (i + 1))
    print(res_last, '\n\n')
