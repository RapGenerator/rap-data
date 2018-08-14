# -*- coding: utf-8 -*-
# @Time    : 18-8-14下午8:23
# @Author  : 石头人m
# @File    : topic_statistics.py

import pandas as pd

df_topic = pd.read_csv('data_topic.csv', names=['lyric', 'topic'])
df_topic = df_topic.dropna(axis=0)
print(df_topic.groupby('topic').count())

list_topic = set(df_topic['topic'])
print(list_topic, len(list_topic))

for topic in list_topic:
    topic_class = df_topic[df_topic['topic'] == topic]
    len_topic_class = len(topic_class)
    topic_class_sources = df_topic[:len_topic_class - 1]
    topic_class_targets = df_topic[1:len_topic_class]
    topic_class_sources['lyric'].to_csv('data_topic/' + str(topic) + '_sources.txt', index=False, header=False)
    topic_class_targets['lyric'].to_csv('data_topic/' + str(topic) + '_targets.txt', index=False, header=False)
