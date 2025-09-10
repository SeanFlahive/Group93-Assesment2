import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np


# ds1 is single bat landing onto food platform with context and behavior
# ds2 is recording values of food, bats, rats over a fixed, 30minute period 
# for ds1, look at seconds_after_rat_arrival, (can think of this as hesitation time to landing)
# and bat_landing_to_food, (hesitancy to get food after landing)


ds1 = pd.read_csv("dataset1.csv")

flightHesitancy = ds1['seconds_after_rat_arrival']
foodHesitancy = ds1['bat_landing_to_food']

flightMean = flightHesitancy.mean()
flightSTD = flightHesitancy.std()

foodMean = foodHesitancy.mean()
foodSTD = foodHesitancy.std()


filtered_df = ds1
# [
#     ds1['seconds_after_rat_arrival'].between(flightMean - 2*flightSTD, flightMean + 2*flightSTD) &
#     ds1['bat_landing_to_food'].between(foodMean - 2*foodSTD, foodMean + 2*foodSTD)
# ]


x = filtered_df['seconds_after_rat_arrival']
y = filtered_df['bat_landing_to_food']

print(filtered_df['bat_landing_to_food'].mean())

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b, color='red', label='Best Fit Line')


plt.scatter(x, y)
plt.xlabel('Flight Hesitancy (Seconds After Rat Arrival)')
plt.ylabel('Food Hesitancy (Bat Landing to Food)')



plt.show()
plt.hist(y)
plt.show()