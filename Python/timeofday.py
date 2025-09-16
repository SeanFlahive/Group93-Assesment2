import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

# time
# rat_arrival_number

df = pd.read_csv("dataset2.csv")


ratMean = df['rat_arrival_number'].mean()
ratSTD = df['rat_arrival_number'].std()
batMean = df['bat_landing_number'].mean()
batSTD = df['bat_landing_number'].std()
df = df[
    (df['bat_landing_number'].between(batMean - 2*batSTD, batMean + 2*batSTD)) &
    (df['rat_arrival_number'].between(ratMean - 2*ratSTD, ratMean + 2*ratSTD))
]

df['time_only'] = pd.to_datetime(df['time']).dt.strftime('%H:%M')
df['time_after_0'] = pd.to_datetime(df['time_only'], format='%H:%M').dt.hour * 60 + pd.to_datetime(df['time_only'], format='%H:%M').dt.minute
#print(df['time_after_0'])

plt.scatter(df['time_after_0'], df['rat_arrival_number'])
plt.xlabel('Minutes Past Midnight')
plt.ylabel('Rat Arrival Number')
plt.ylim(-2, 10)
plt.show()

plt.scatter(df['time_after_0'], df['bat_landing_number'])
plt.xlabel('Minutes Past Midnight')
plt.ylabel('Bat Landing Number')
plt.show()