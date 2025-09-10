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
    'rat_attack': 1,
    'fight_rat' :1,
    
    'rat': 2,
    'fast': 2,
    'gaze': 2,
    'other_bats': 2
}

ds1['habit_value'] = ds1['habit'].map(habit_map)


conflict = ds1[ds1['habit_value']==1]
no_conflict = ds1[ds1['habit_value']==2]

conflictHesitancy = conflict['bat_landing_to_food']
noConflictHesitancy = no_conflict['bat_landing_to_food']

print(conflictHesitancy.mean(), conflictHesitancy.std())
print(noConflictHesitancy.mean(), noConflictHesitancy.std())    

plt.bar(['Conflict Behavior', 'No Conflict Behavior'], [conflictHesitancy.mean(), noConflictHesitancy.mean()])
plt.ylabel('Hesitancy (seconds)')
plt.title('Bat Hesitancy After Landing Based on Conflict Behavior')
plt.show()
