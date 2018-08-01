# -*- coding: utf-8 -*-
# @Time    : 18-8-1上午10:41
# @Author  : 石头人m
# @File    : lyric_txt.py

import pandas as pd

df_all_pinyin_clear = pd.read_csv('df_all_pinyin_clear.csv')

df_txt = df_all_pinyin_clear['lyrics']

df_txt.to_csv('df_all_lyrics.txt', index=False)
