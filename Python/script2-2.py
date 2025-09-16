import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

# Compare the following:
# -food_availability 
# -bat_landing_number
# -rat_arrival_number

# Notes: These 3 data points are in dataset2.csv so we can focus purely on that
# first, should clean data and remove any outliers if necessary. This is so we can index all the values and plot them easily for comparison.

ds2 = pd.read_csv("dataset2.csv")

collatedDF = ds2[['food_availability', 'bat_landing_number', 'rat_arrival_number']]


# The following filters the data points to remove outliers that don't fit within 2 standard deviations of the mean.

means = collatedDF.mean()
stds = collatedDF.std()

filteredDF = collatedDF[
    (collatedDF['food_availability'].between(means['food_availability'] - 2*stds['food_availability'], means['food_availability'] + 2*stds['food_availability'])) &
    (collatedDF['bat_landing_number'].between(means['bat_landing_number'] - 2*stds['bat_landing_number'], means['bat_landing_number'] + 2*stds['bat_landing_number'])) &
    (collatedDF['rat_arrival_number'].between(means['rat_arrival_number'] - 2*stds['rat_arrival_number'], means['rat_arrival_number'] + 2*stds['rat_arrival_number']))
]



indexedDF = filteredDF.copy()
# indexedDF['food_availability'] = filteredDF['food_availability'] / filteredDF['food_availability'].max()
# indexedDF['bat_landing_number'] = filteredDF['bat_landing_number'] / filteredDF['bat_landing_number'].max()
# indexedDF['rat_arrival_number'] = filteredDF['rat_arrival_number'] / filteredDF['rat_arrival_number'].max()
indexedDF = indexedDF.sort_values(by='food_availability').reset_index(drop=True)

print(indexedDF)
x = indexedDF['food_availability']
y = indexedDF['bat_landing_number']

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red', label='Best Fit Line')

# = indexedDF['rat_arrival_number']
#plt.scatter(x, y1, alpha = 0.5, color = 'red' , label='Bat Landing Number')
plt.scatter(x, y, alpha = 0.5, color = 'blue', label='Rat Arrival Number')

























# plt.hist(indexedDF['food_availability'].dropna(), color = 'red', alpha = 0.5, label='Food Availability')
# plt.hist(indexedDF['bat_landing_number'].dropna(), color = 'green', alpha = 0.5, label='Bat Landing Number')
# plt.hist(indexedDF['rat_arrival_number'].dropna(), color = 'blue', alpha = 0.5, label='Rat Arrival Number')



# Used to visualize data distrubution. 
 
# plt.hist(filteredDF['food_availability'].dropna(), label='Food Availability')
# plt.xlabel('Food Availability')
# plt.ylabel('Frequency') 

# plt.hist(filteredDF['bat_landing_number'].dropna(), label='Bat Landing Number')
# plt.xlabel('bat_landing_number')
# plt.ylabel('Frequency') 

# plt.hist(filteredDF['rat_arrival_number'].dropna(), label='Rat Arrival Number')
# plt.xlabel('rat_arrival_number')
# plt.ylabel('Frequency') 



plt.show()