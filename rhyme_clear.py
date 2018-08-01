import pandas as pd

# Read in
df = pd.read_csv('df_all_pinyin.csv')

# set the threshold to be 4 and remove all rows that occur greater or equal to 4 times.
df = df.groupby('lyrics').filter(lambda x: x.lyrics.value_counts().max() < 4)

## remove bad words
df = df.loc[(df['isBad'] == '0') | (df['isBad'] == '0.0')]
print(df.head())
print(len(df))

## write to csv
df.to_csv('df_all_pinyin_clear.csv', index=False)
