import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np


# when food value is same/similar, do bats hesitate more when rats are present? 

ds2 = pd.read_csv("dataset2.csv")

#food = ds2.loc[(ds2['food_availability'] >= 0) & (ds2['food_availability'] <= 1.4), ['rat_arrival_number', 'bat_landing_number']]
food = ds2[['food_availability', 'rat_arrival_number', 'bat_landing_number']]

meanBat = food['bat_landing_number'].mean()
stdBat = food['bat_landing_number'].std()
fFood = food[food['bat_landing_number'].between(meanBat - 2*stdBat, meanBat + 2*stdBat)]

meanRat = food['rat_arrival_number'].mean()
stdRat = food['rat_arrival_number'].std()
fFood = fFood[fFood['rat_arrival_number'].between(meanRat - 2*stdRat, meanRat + 2*stdRat)]


x = food['rat_arrival_number']
y = food['bat_landing_number']

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red', label='Best Fit Line')

plt.scatter(x, y)
plt.legend()
plt.xlabel('Rat Arrival Number')
plt.ylabel('Bat Landing Number')
plt.show()
