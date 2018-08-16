# -*- coding: utf-8 -*-
# @Time    : 18-8-16上午10:12
# @Author  : 石头人m
# @File    : topic2seq.py

import pandas as pd
import jieba

dict_topic = {0.0: '',
              1.0: '亲情', 1.1: '痛苦',
              2.0: '爱情', 2.1: '青春', 2.2: '失恋',
              3.0: '友情', 3.1: '兄弟', 3.2: '背叛',
              4.0: '成功', 4.1: '坚持', 4.2: '告诫',
              5.0: '失败', 5.1: '迷茫', 5.2: '艰难不易',
              6.0: '过去', 6.1: '回忆', 6.2: '成长',
              7.0: '将来',
              8.0: '金钱', 8.1: '物欲',
              9.0: '努力',
              10.0: 'diss', 10.1: '讨厌', 10.2: '憎恶', 10.3: '虚伪',
              11.0: '积极',
              12.0: '生活',
              13.0: '中国风',
              14.0: '耍帅'}
data_topic = pd.read_csv('data_topic.csv', names=['lyric', 'topic'])

# 删除0.0
data_topic = data_topic[data_topic['topic'] != 0.0]
data_topic['topic'] = data_topic['topic'].map(dict_topic)
# 替换空格
# data_topic['lyric'] = data_topic['lyric'].apply(lambda x: x.replace(' ', '_'))

# print(data_topic.groupby('topic').count())

# 主题放歌词前面,不分词
data_topic['topic_lyric'] = data_topic['topic'] + data_topic['lyric']
data_topic['topic_lyric'].to_csv('df_topic_add_lyric.txt', index=False, header=False)

# 主题放分词后的歌词前面
data_topic['lyric'] = data_topic['lyric'].apply(lambda x: "/".join(jieba.cut(x)))
data_topic['topic_lyric'] = data_topic['topic'] + '/' + data_topic['lyric']
data_topic['topic_lyric'].to_csv('df_topic_add_lyric_cut.txt', index=False, header=False)

print(data_topic.head())

# 各类歌词句数统计
'''
diss    5739
中国风     1771
亲情       881
兄弟       484
努力      1822
友情       479
回忆      1152
坚持      1290
失恋      3807
失败      1088
将来        82
憎恶       406
成功       358
成长      1328
无      10128
爱情      7235
物欲      2843
生活      1996
痛苦       378
积极      3115
耍帅      1740
背叛        90
艰难不易    1962
虚伪       535
讨厌      1185
过去      2195
迷茫      2452
金钱       939
青春       828
'''
