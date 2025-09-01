import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st



# Compare the following:
# -food_availability 
# -bat_landing_number
# -rat_arrival_number


# Notes: These 3 data points are in dataset2.csv so we can focus purely on that
# first, should clean data and remove any outliers if necessary. This is so we can index all the values and plot them easily for comparison.




ds2 = pd.read_csv("dataset2.csv")




collatedDF = ds2[['food_availability', 'bat_landing_number', 'rat_arrival_number']]

means = collatedDF.mean()
stds = collatedDF.std()




filteredDF = collatedDF[
    (collatedDF['food_availability'].between(means['food_availability'] - 2*stds['food_availability'], means['food_availability'] + 2*stds['food_availability'])) &
    (collatedDF['bat_landing_number'].between(means['bat_landing_number'] - 2*stds['bat_landing_number'], means['bat_landing_number'] + 2*stds['bat_landing_number'])) &
    (collatedDF['rat_arrival_number'].between(means['rat_arrival_number'] - 2*stds['rat_arrival_number'], means['rat_arrival_number'] + 2*stds['rat_arrival_number']))
]

plt.hist(filteredDF['food_availability'].dropna(), label='Food Availability')
plt.xlabel('Food Availability')
plt.ylabel('Frequency') 
plt.show()

plt.hist(filteredDF['bat_landing_number'].dropna(), label='Bat Landing Number')
plt.xlabel('bat_landing_number')
plt.ylabel('Frequency') 
plt.show()

plt.hist(filteredDF['rat_arrival_number'].dropna(), label='Rat Arrival Number')
plt.xlabel('rat_arrival_number')
plt.ylabel('Frequency') 
plt.show()