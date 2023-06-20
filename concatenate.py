import pandas as pd


df1 = pd.read_csv('owid-covid-data.csv')
df1['date'] = pd.to_datetime(df1['date'])
df1 = df1[df1['date'].dt.strftime('%Y') == '2021']
df1 = df1.groupby('location', as_index=False).max(numeric_only=True)

df1 = df1.drop(['new_cases', 'new_cases_smoothed', 'new_deaths', 'new_deaths_smoothed', 'new_cases_per_million', 'new_cases_smoothed_per_million', 'new_deaths_per_million', 'new_deaths_smoothed_per_million', 'new_tests', 'new_tests_per_thousand', 'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'new_vaccinations', 'new_vaccinations_smoothed',  'new_vaccinations_smoothed_per_million', 'new_people_vaccinated_smoothed', 'new_people_vaccinated_smoothed_per_hundred'   ], axis= 1)

# Read the second dataset
df2 = pd.read_csv('Life expectancy.csv')
df2 = df2.rename(columns={'Country': 'location'})
df2 = df2.groupby('location', as_index=False).max(numeric_only=True)




# Concatenate the two datasets
concat = merged_df = df1.merge(df2, on='location', how='inner')


for col in concat.columns:
    print(col)

print((concat.corr(method='pearson', numeric_only=True)))

df1.to_csv('Covid.csv', index=False)
df2.to_csv('Vaccination.csv', index=False)
concat.to_csv('Concat.csv', index=False)