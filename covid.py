import pandas as pd


df = pd.read_csv('owid-covid-data.csv')




print(df['total_deaths'].max())
df['date'] = pd.to_datetime(df['date'])

df  = df[df['date'].dt.strftime('%Y') == '2021']

df = df.groupby('location').max(numeric_only=True)

print(df)

print(df['total_deaths'].max())