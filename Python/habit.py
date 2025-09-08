import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np


ds1 = pd.read_csv("dataset1.csv")



# fight 
# both no fight
# just bats 

# risk 

habit_map = {
    'bat_fight': 1,
    'attack_rat': 1,
    'rat_fight': 1,
    'fast': 2,
    'gaze': 2,
    'other_bats': 2
}

ds1['habit_value'] = ds1['habit'].map(habit_map)


# habitConflict = ds1[ds1['habit'].isin(['bat_fight', 'attack_rat', 'rat_fight'])]['bat_landing_to_food']
# habitPeace = ds1[ds1['habit'].isin(['fast', 'gaze', 'other_bats'])]['bat_landing_to_food']

# habitConflictAvg = habitConflict.mean()
# habitPeaceAvg = habitPeace.mean()

# print(habitConflictAvg, habitPeaceAvg)

# plt.bar(['Conflict Habits', 'Peaceful Habits'], [habitConflictAvg, habitPeaceAvg], color=['red', 'green'])
# plt.ylabel('Average Bats')
# plt.xlabel('Habit Type')

x = ds1['habit_value']
y = ds1['bat_landing_to_food']

ymean = y.mean()
xmean = x.mean()

# m, b = np.polyfit(x, y, 1)
# plt.plot(x, m*x + b, color='red', label='Best Fit Line')

print('Y-Mean',ymean, 'X-Mean', xmean)

plt.scatter(x, y)
plt.xlabel('Habit Value (1 = Conflict, 2 = Peaceful)')
plt.ylabel('Bat Landing to Food')

plt.show()