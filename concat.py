import pandas as pd


# Create csv file list
df_list = []
for i in range(1, 11):
    df = pd.read_csv('data/{}.csv'.format(str(i)), header=None)
    df_list.append(df)

# Read in
df = pd.concat(df_list)

