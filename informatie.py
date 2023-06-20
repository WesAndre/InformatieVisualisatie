import pandas as pd

df = pd.read_csv('dataset_Facebook.csv', delimiter=";", decimal=',')

new = []

for i in range(1,13):
    count = 0
    for index,  row in df.iterrows():
        if row['Post Month'] == i:
            count += 1
    print(count)
    new.append(count)

total = 0
for i in new:
    total += i

print(total)


for col in df.columns:
    if df[col].dtype != type(object):
        print(col ,':', df[col].mode())

quartiles = df['Page total likes'].quantile([0.25, 0.75])
iqr = quartiles[0.75] - quartiles[0.25]
print(iqr)

print(df['Page total likes'].std())