import pandas as pd

df = pd.read_csv('diamonds.csv')



new= []
for row in df['fancy_color_dominant_color']:
    if row not in new:
        new.append(row)
new.sort()
for item in new:
    print(item)
for i in range(0, 13):
    count = 0
    for row in df['fancy_color_dominant_color']:
        if row == new[i]:
            count += 1
    print( count, '/219703')
print(df['total_sales_price'].mode())
print(df['total_sales_price'].median())
print(df['total_sales_price'].mean())
print(df['total_sales_price'].std())
print(df['total_sales_price'].max())
print(df['total_sales_price'].min())


quartiles = df['total_sales_price'].quantile([0.25, 0.75])
iqr = quartiles[0.75] - quartiles[0.25]
print(iqr)

print(df.corr(method='pearson', numeric_only=True))