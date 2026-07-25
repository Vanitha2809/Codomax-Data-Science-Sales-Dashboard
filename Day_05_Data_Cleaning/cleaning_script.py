import pandas as pd
df = pd.read_csv('../Day_04_Pandas_Basics/dataset.csv')
df['Price'].fillna(df['Price'].median(), inplace=True)
df.drop_duplicates(inplace=True)
print('Data cleaned successfully!')
