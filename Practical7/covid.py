# The code for importing the .csv file works

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/MINGW64/Jonas/IBI1_2022-23/Practical7")

covid_data = pd.read_csv("full_data.csv")

# Showing the second column from every 100th row from the first 1000 rows
covid_data.iloc[0:1100:100, 2]

# Using a Boolean to show “total cases” for all rows corresponding to Afghanistan

# Computing the mean number of new cases and new deaths on 31 March 2020

new_data = covid_data[covid_data['date'] == '2020-03-31'][['location', 'new_cases', 'new_deaths']]

import numpy as np

mean_new_cases = np.mean(new_data['new_cases'])
mean_new_deaths = np.mean(new_data['new_deaths'])

print("Mean new cases:", mean_new_cases)
print("Mean new deaths:", mean_new_deaths)

# Creating boxplot of new cases and new deaths on 31 March 2020

import matplotlib.pyplot as plt

plt.boxplot([new_data['new_cases'], new_data['new_deaths']])
plt.xticks([1, 2], ['New Cases', 'New Deaths'])
plt.ylabel('Number')
plt.title('New Cases and New Deaths on 31 March 2020')
plt.show()

# Plotting both new cases and new deaths worldwide over time

world_new_cases = covid_data[covid_data['location'] == 'World']['new_cases']
world_new_deaths = covid_data[covid_data['location'] == 'World']['new_deaths']
world_dates = covid_data[covid_data['location'] == 'World']['date']

plt.plot(world_dates, world_new_cases, 'b+', label='New Cases')
plt.plot(world_dates, world_new_deaths, 'r+', label='New Deaths')
plt.xticks(world_dates.iloc[0:len(world_dates):4], rotation=-90)
plt.xlabel('Date')
plt.ylabel('Number')
plt.title('New Cases and New Deaths Across the World')
plt.legend()
plt.show()

# Code to answer the question
