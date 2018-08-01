import pandas as pd


# Create csv file list
df_list = []
for i in range(1, 11):
    df = pd.read_csv('data/{}.csv'.format(str(i)), header=None)
    df_list.append(df)

# Read in
df = pd.concat(df_list)


## change columns
df.columns = ['lyrics', 'isBad']
df['lyrics'].value_counts()
# set the threshold to be 4 and remove all rows that occur greater or equal to 4 times.
df = df.groupby('lyrics').filter(lambda x: x.lyrics.value_counts().max() < 4)

## remove bad words
df = df.loc[df['isBad'] == 0]

## write to csv
df.to_csv('cleaned dataset.csv')