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

df = ds2[['food_availability', 'bat_landing_number', 'rat_arrival_number']]


foodMean = df['food_availability'].mean()
foodSTD = df['food_availability'].std()
batMean = df['bat_landing_number'].mean()
batSTD = df['bat_landing_number'].std()
ratMean = df['rat_arrival_number'].mean()
ratSTD = df['rat_arrival_number'].std()

df = df[
    # do not filter food, reduces data points too much. Food is controlled by experimenter, so we assume it is accurate. 
    (df['bat_landing_number'].between(batMean - 2*batSTD, batMean + 2*batSTD)) &
    (df['rat_arrival_number'].between(ratMean - 2*ratSTD, ratMean + 2*ratSTD))
]

x = df['food_availability']
y1 = df['bat_landing_number']
y2 = df['rat_arrival_number']

y3 = df['bat_landing_number']
x3 = df['rat_arrival_number']

# print(x, y1, y2, y3, x3)

plt.scatter(x, y1, alpha = 0.5, color = 'red' , label='Bat Landing Number')
m1, b1 = np.polyfit(x, y1, 1)
plt.plot(x, m1*x + b1, color='red', label='Best Fit Line')


plt.legend()
plt.xlabel('Food Availability')
plt.show()

plt.scatter(x, y2, alpha = 0.5, color = 'blue', label='Rat Arrival Number')
m2, b2 = np.polyfit(x, y2, 1)
plt.plot(x, m2*x + b2, color='red', label='Best Fit Line')

plt.legend()
plt.xlabel('Food Availability')
plt.show()
print(m2)

plt.scatter(x3, y3, alpha = 0.5, color = 'green', label='Rat Arrival Number vs Bat Landing Number')
m3, b3 = np.polyfit(x3, y3, 1)
plt.plot(x3, m3*x3 + b3, color='red', label='Best Fit Line')


plt.legend()
plt.xlabel('Rat Arrival Number')
plt.ylabel('Bat Landing Number')
plt.show()

plt.hist(df['food_availability'])
plt.show()


print("Gradient for Bat Landing Number:", m1)
print("Gradient for Rat Arrival Number:", m2)
print("Gradient for Bat Landing Number vs Rat Arrival Number:", m3)