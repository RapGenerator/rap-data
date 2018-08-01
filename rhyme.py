# -*- coding: utf-8 -*-
# @Time    : 18-7-31下午8:12
# @Author  : 石头人m
# @File    : rhyme.py

import pandas as pd
from pypinyin import pinyin, lazy_pinyin, Style

df_all = pd.read_csv('df_all.csv', names=['lyric', 'label'])
print(df_all.head())

for i in range(len(df_all)):
    if i % 1000 == 0:
        df_all.to_csv('df_all_pinyin.csv', index=False)
        print(i)
    pinyin_loci = lazy_pinyin(df_all.loc[i, 'lyric'], errors='ignore')
    len_pinyin_loci = len(pinyin_loci)
    df_all.loc[i, 'pinyin_neg1'] = pinyin_loci[-1]
    if len_pinyin_loci > 1:
        df_all.loc[i, 'pinyin_neg2'] = pinyin_loci[-2]
    if len_pinyin_loci > 2:
        df_all.loc[i, 'pinyin_neg3'] = pinyin_loci[-3]
    if len_pinyin_loci > 3:
        df_all.loc[i, 'pinyin_neg4'] = pinyin_loci[-4]
    if len_pinyin_loci > 5:
        df_all.loc[i, 'pinyin_neg5'] = pinyin_loci[-5]

print(df_all.head())

df_all.to_csv('df_all_pinyin.csv', index=False)
