import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
corona_dataset = pd.read_csv('./Datasets/covid19_Confirmed_dataset.csv')
corona_dataset.shape

corona_dataset.drop(['Lat', 'Long', 'Province/State'], axis=1, inplace=True)
corona_dataset_aggregated = corona_dataset.groupby('Country/Region').sum()
corona_dataset_aggregated.head()
print(corona_dataset_aggregated.loc['China'].head())
print(corona_dataset_aggregated.dtypes)

corona_dataset_aggregated.loc['China'].plot()
plt.title("Covid-19 cases in China")
plt.xlabel("Days")
plt.ylabel("Confirmed cases")
plt.show()
corona_dataset_aggregated.loc['China'].diff().plot()
plt.title("Daily new Covid-19 cases in China")
plt.xlabel("Days")
plt.ylabel("New cases")
plt.show()
corona_dataset_aggregated.loc['China'].diff().max()

countries = list(corona_dataset_aggregated.index)
max_infection_rates = []

for country in countries:
    max_infection_rates.append(
        corona_dataset_aggregated.loc[country].diff().max()
    )

corona_data = pd.DataFrame(max_infection_rates, index=countries, columns=['Max_infection_rate'])

print(corona_data.head())

happiness_report = pd.read_csv('./Datasets/worldwide_happiness_report.csv')
happiness_report.drop([
    'Overall rank',
    'Score',
    'Generosity',
    'Perceptions of corruption'
], axis=1, inplace=True)

happiness_report.set_index('Country or region', inplace=True)
data = corona_data.join(happiness_report, how='inner')

data.corr()

sns.scatterplot(
    data=data,
    x='GDP per capita',
    y='Max_infection_rate'
)
plt.title("GDP per capita vs Maximum Infection Rate")
plt.xlabel("GDP per capita")
plt.ylabel("Maximum infection rate")
plt.show()


sns.scatterplot(
    data=data,
    x='Social support',
    y='Max_infection_rate'
)
plt.title("Healthy Life Expectancy vs Maximum Infection Rate")
plt.xlabel("Healthy life expectancy")
plt.ylabel("Maximum infection rate")
plt.show()

sns.scatterplot(
    data=data,
    x='Healthy life expectancy',
    y='Max_infection_rate'
)
plt.show()

sns.scatterplot(
    data=data,
    x='Freedom to make life choices',
    y='Max_infection_rate'
)
plt.show()
