import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np


df = pd.read_csv("dataset1.csv")

mean = df['bat_landing_to_food'].mean()
std = df['bat_landing_to_food'].std()
df = df[df['bat_landing_to_food'].between(mean - 2*std, mean + 2*std)]

mean_hesitancy = df.groupby('habit')['bat_landing_to_food'].mean()

sorted_habits = mean_hesitancy.sort_values()

plt.bar(range(len(sorted_habits)), sorted_habits.values)
plt.xlabel('Habit (index)')
plt.ylabel('Mean Bat Landing to Food Time (seconds)')
plt.show()