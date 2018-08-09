# -*- coding: utf-8 -*-
# @Time    : 18-8-8上午10:44
# @Author  : 石头人m
# @File    : rhymeStatistics.py

import pdb
import pandas as pd
import numpy as np
from pypinyin import lazy_pinyin, Style
from collections import Counter

# 是否Strict
IS_STRICT = True
# for循环几押
FOR_NUM = 1

'''
# 读取数据
df_all = pd.read_csv('df_all_01.csv', names=['lyric'])
len_df = len(df_all)
print('数据总条数:', len_df)

# 得到每行没字的韵母
df_all['rhyme'] = df_all.loc[:, 'lyric'].apply(lambda x: lazy_pinyin(x, style=Style.FINALS, strict=IS_STRICT))
df_all['Finals_neg5'] = df_all['rhyme'].apply(lambda x: x[-5:-4][0] if len(x) > 4 else None)
df_all['Finals_neg4'] = df_all['rhyme'].apply(lambda x: x[-4:-3][0] if len(x) > 3 else None)
df_all['Finals_neg3'] = df_all['rhyme'].apply(lambda x: x[-3:-2][0] if len(x) > 2 else None)
df_all['Finals_neg2'] = df_all['rhyme'].apply(lambda x: x[-2:-1][0] if len(x) > 1 else None)
df_all['Finals_neg1'] = df_all['rhyme'].apply(lambda x: x[-1])

if IS_STRICT:
    del df_all['rhyme']
    df_all.to_csv('df_all_rhyme_Finals_strict.csv', index=False)
else:
    del df_all['rhyme']
    df_all.to_csv('df_all_rhyme_Finals_no_strict.csv', index=False)
'''

# 读取处理了韵母的文件
if IS_STRICT:
    df_all = pd.read_csv('df_all_rhyme_Finals_strict.csv')
else:
    df_all = pd.read_csv('df_all_rhyme_Finals_no_strict.csv')

len_df = len(df_all)
print('数据总条数:', len_df)

# 押韵规则
yun_strict = {
    'i': 'i',
    'u': 'u',
    'v': 'v',
    'a': 'a', 'ia': 'a', 'ua': 'a',
    'o': 'o', 'uo': 'o',
    'e': 'e', 'ie': 'e', 'ue': 'e', 've': 'e', 'er': 'e',
    'ai': 'ai', 'uai': 'ai',
    'ei': 'ei', 'uei': 'ei',
    'ao': 'ao', 'iao': 'ao',
    'ou': 'ou', 'iou': 'ou',
    'an': 'an', 'ian': 'an', 'uan': 'an', 'van': 'an',
    'en': 'en', 'uen': 'en', 'eng': 'eng',
    'in': 'in', 'ing': 'ing',
    'vn': 'vn',
    'ang': 'ang', 'iang': 'ang', 'uang': 'ang',
    'ong': 'ong', 'iong': 'ong'
}
yun_not_strict = {
    'i': 'i',
    'u': 'u',
    'a': 'a', 'ia': 'a', 'ua': 'a',
    'o': 'o', 'uo': 'o',
    'e': 'e', 'ie': 'e', 'ue': 'e', 'er': 'e',
    'ai': 'ai', 'uai': 'ai',
    'ei': 'ei', 'ui': 'ei',
    'ao': 'ao', 'iao': 'ao',
    'ou': 'ou', 'iu': 'ou',
    'an': 'an', 'ian': 'an', 'uan': 'an',
    'en': 'en', 'un': 'en', 'eng': 'en',
    'in': 'in', 'ing': 'in',
    'ang': 'ang', 'iang': 'ang', 'uang': 'ang',
    'ong': 'ong', 'iong': 'ong'
}


# 判断连个韵母是否押韵
def is_rhymeis_rhym(a: str, b: str, strict_or_not=IS_STRICT):
    if strict_or_not:
        return yun_strict[a] == yun_strict[b]
    else:
        return yun_not_strict[a] == yun_not_strict[b]


# 判断两个list里每个韵母是否押韵
def is_rhymes_list(list_a, list_b, strict_or_not=IS_STRICT):
    if strict_or_not:
        for ab in zip(list_a, list_b):
            if yun_strict.get(ab[0], '-') != yun_strict.get(ab[1], '--'):
                return False
    else:
        for ab in zip(list_a, list_b):
            if yun_not_strict.get(ab[0], '-') != yun_not_strict.get(ab[1], '--'):
                return False
    return True


# 1 排韵
def dict_count_paiyun(list_last):
    len_list_last = len(list_last)
    res_count = {}  # 存放计数字典
    df_all.loc[:, 'isPaiYun'] = 0
    head, tail = 0, 0
    while head < len_list_last:
        # print(list(list_last.iloc[tail]), list(list_last.iloc[head]))
        while tail < len_list_last and is_rhymes_list(list(list_last.iloc[tail]), list(list_last.iloc[head])) \
                and df_all.loc[head, 'lyric'] != df_all.loc[tail, 'lyric']:
            if len(df_all.loc[tail]) > 30:
                print(df_all.loc[head, 'lyric'], df_all.loc[tail, 'lyric'])
                pass
            tail += 1
        if tail - head > 1:
            dict_key = 'ya_0' + str(tail - head) if (tail - head) < 10 else 'ya_' + str(tail - head)
            res_count[dict_key] = res_count.get(dict_key, 0) + 1
            # 标记是否押韵
            df_all.loc[head:tail - 1, 'isPaiYun'] = 1

        head = tail
        tail += 1
    res_count = sorted(res_count.items(), key=lambda item: item[0])
    return res_count


def get_yun_pai():
    print('排韵...')
    for i in range(FOR_NUM):
        list_last = df_all.iloc[:, -(i + 1):]
        res_last = dict_count_paiyun(list_last)
        print('排韵-%d押:' % (i + 1))
        print(res_last)
        # 保存截取出来押韵,只保存单押情况
        if i == 0:
            df_yun_pai = df_all[df_all['isPaiYun'] == 1]['lyric']
            if IS_STRICT:
                df_yun_pai.to_csv('df_yun_pai_strict.txt', index=False)
            else:
                df_yun_pai.to_csv('df_yun_pai_no_strict.txt', index=False)
            print('排韵-单押保存成功...\n\n')


# 2 隔行韵
def dict_count_gehangyun(list_last):
    len_list_last = len(list_last)
    res_count = {}  # 存放计数字典
    df_all.loc[:, 'isGeHangYun'] = 0
    head, tail = 0, 0
    while head < len_list_last:
        while head == tail or (tail < len_list_last and \
                               is_rhymes_list(list(list_last.iloc[tail]), list(list_last.iloc[head]))):
            tail += 2
        # print(head, tail)
        if tail - head > 2:
            t_h = (tail - head) / 2
            dict_key = 'ya_0' + str(t_h) if t_h < 10 else 'ya_' + str(t_h)
            res_count[dict_key] = res_count.get(dict_key, 0) + 1
            # 标记是否押韵
            df_all.loc[head:tail - 2, 'isGeHangYun'] = 1

        head = tail - 1
        tail = head
    res_count = sorted(res_count.items(), key=lambda item: item[0])
    return res_count


def get_yun_gehang():
    print('隔行韵...')
    for i in range(FOR_NUM):
        list_last = df_all.iloc[:, -(i + 1):]
        res_last = dict_count_gehangyun(list_last)
        print('隔行韵-%d押:' % (i + 1))
        print(res_last)
        # 保存截取出来押韵,只保存单押情况
        if i == 0:
            df_yun_gehang = df_all[df_all['isGeHangYun'] == 1]['lyric']
            if IS_STRICT:
                df_yun_gehang.to_csv('df_yun_gehang_strict.txt', index=False)
            else:
                df_yun_gehang.to_csv('df_yun_gehang_no_strict.txt', index=False)
            print('隔行韵-单押保存成功...\n\n')


# 3 交韵
def dict_count_jiaoyun(list_last):
    len_list_last = len(list_last)
    res_count = {}  # 存放计数字典
    df_all.loc[:, 'isJiaoYun'] = 0
    head, tail = 0, 0
    while head < len_list_last:
        # print(head, list_last.loc[head], tail, list_last.loc[tail])
        # pdb.set_trace()
        while tail + 1 < len_list_last and is_rhymes_list(list(list_last.iloc[head]), list(list_last.iloc[tail])) \
                and is_rhymes_list(list(list_last.iloc[head + 1]), list(list_last.iloc[tail + 1])):
            tail += 2
            # print('tail+2')
        if tail - head > 2:
            dict_key = 'ya_0' + str(tail - head) if (tail - head) < 10 else 'ya_' + str(tail - head)
            res_count[dict_key] = res_count.get(dict_key, 0) + 1
            # 标记是否押韵
            df_all.loc[head:tail - 1, 'isJiaoYun'] = 1
            # print(df_all.loc[head:tail-1])
        head = tail - 1
        tail += 1
    res_count = sorted(res_count.items(), key=lambda item: item[0])
    return res_count


def get_yun_jiao():
    print('交韵...')
    for i in range(FOR_NUM):
        list_last = df_all.iloc[:, -(i + 1):]
        res_last = dict_count_jiaoyun(list_last)
        print('交韵-%d押:' % (i + 1))
        print(res_last)
        if i == 0:
            df_yun_jiao = df_all[df_all['isJiaoYun'] == 1]['lyric']
            if IS_STRICT:
                df_yun_jiao.to_csv('df_yun_jiao_strict.txt', index=False)
            else:
                df_yun_jiao.to_csv('df_yun_jiao_no_strict.txt', index=False)
            print('交韵-单押保存成功...\n\n')


# 4 抱韵
def dict_count_baoyun(list_last):
    len_list_last = len(list_last)
    res_count = {}  # 存放计数字典
    df_all.loc[:, 'isBaoYun'] = 0
    head = 0
    dict_key = 'ya_count'
    while head + 3 < len_list_last:
        if is_rhymes_list(list(list_last.iloc[head]), list(list_last.iloc[head + 3])) \
                and is_rhymes_list(list(list_last.iloc[head + 1]), list(list_last.iloc[head + 2])):
            # 标记是否押韵
            df_all.loc[head:head + 3, 'isBaoYun'] = 1
            head += 3
            res_count['ya_count'] = res_count.get(dict_key, 0) + 1
        head += 1
    res_count = sorted(res_count.items(), key=lambda item: item[0])
    return res_count


def get_yun_bao():
    print('抱韵...')
    for i in range(FOR_NUM):
        list_last = df_all.iloc[:, -(i + 1):]
        res_last = dict_count_baoyun(list_last)
        print('抱韵-%d押:' % (i + 1))
        print(res_last)
        if i == 0:
            df_yun_bao = df_all[df_all['isBaoYun'] == 1]['lyric']
            if IS_STRICT:
                df_yun_bao.to_csv('df_yun_bao_strict.txt', index=False)
            else:
                df_yun_bao.to_csv('df_yun_bao_no_strict.txt', index=False)
            print('交韵-单押保存成功...\n\n')


if __name__ == '__main__':
    # get_yun_pai()
    # get_yun_gehang()
    # get_yun_jiao()
    get_yun_bao()
