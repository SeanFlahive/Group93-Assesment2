import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st

# Determine whether bats hesitate when rats are present. 
# seconds_after_rat_arrival : Time taken for a bat to land after a rat has arrived.

# risk : 0 - means no risk taken, i.e, bats did not attack rats. 1 - means risk taken, i.e, bats did attack rats.
# reward : directly influenced by risk. Did the behavior presented in risk result in a reward? 0 - no reward, 1 - reward.

# bat_landing_to_food : time taken from when bat lands to when it approaches food. Higher values indicate more hesitation, therefore if values tend to increase when rats are present-
# this would indicate that bats hesitate more when rats are present.

ds1 = pd.read_csv("dataset1.csv")


df = ds1[['bat_landing_to_food', 'habit']]
rat = df[df['habit'] == 'rat']['bat_landing_to_food']
fast = df[df['habit'] == 'fast']['bat_landing_to_food']
bat_landing_to_food = ds1['bat_landing_to_food']


bat_mean = bat_landing_to_food.mean()
bat_std = bat_landing_to_food.std()
bat_landing_to_food = bat_landing_to_food[bat_landing_to_food.between(bat_mean - 2*bat_std, bat_mean + 2*bat_std)]

rat_mean = rat.mean()
rat_std = rat.std()
rat = rat[rat.between(rat_mean - 2*rat_std, rat_mean + 2*rat_std)]

fast_mean = fast.mean()
fast_std = fast.std()
fast = fast[fast.between(fast_mean - 2  *fast_std, fast_mean + 2*fast_std)]


risk = ds1['risk']
risk = risk - 0.05 # to make it more visible on the histogram
reward = ds1['reward']
reward = reward + 0.05 # to make it more visible on the histogram

count = reward.count()
count_1 = reward[reward == 1].count()
count_0 = reward[reward == 0].count()

percent = (count_1 / count) * 100
print (count, count_1, count_0, percent)


plt.hist(risk, alpha=1, label='Risk', color = 'blue')
plt.hist(reward, alpha=1, label='Reward', color = 'red')
plt.xlabel('Risk/Reward (red = reward, blue = risk)')
plt.ylabel('Frequency')
plt.legend()










# plt.hist(rat, alpha=0.5, label='Rat', color = 'red')
# plt.hist(fast, alpha=0.5, label='Fast', color = 'blue')
# plt.xlabel('Bat Landing to Food Time (seconds)')
# plt.ylabel('Frequency')
# plt.title('Histogram Title')
plt.show()