import pandas as pd


df = pd.read_csv('country_vaccinations.csv')


df['date'] = pd.to_datetime(df['date'])

df  = df[df['date'].dt.strftime('%Y') == '2021']

df = df.groupby('country').max(numeric_only=True)


