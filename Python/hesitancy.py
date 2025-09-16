import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st
import numpy as np

# combine dataset 1 and dataset 2 based on time to see if bat landing to food time (hesitancy)
# correlates with rat arrival number and bat landing number at that time

df = pd.read_csv("dataset1.csv")
df2 = pd.read_csv("dataset2.csv")

# from dataset2, get bat_landing_number and rat_arrival_number for each start_time
ratMean = df2['rat_arrival_number'].mean()
ratSTD = df2['rat_arrival_number'].std()
batMean = df2['bat_landing_number'].mean()
batSTD = df2['bat_landing_number'].std()
df2 = df2[
    (df2['bat_landing_number'].between(batMean - 2*batSTD, batMean + 2*batSTD)) &
    (df2['rat_arrival_number'].between(ratMean - 2*ratSTD, ratMean + 2*ratSTD))
]

df2['time_only'] = pd.to_datetime(df2['time'], format='%d/%m/%Y %H:%M', dayfirst=True).dt.strftime('%H:%M')
df2['time_after_0'] = pd.to_datetime(df2['time_only'], format='%H:%M').dt.hour * 60 + pd.to_datetime(df2['time_only'], format='%H:%M').dt.minute
# -----------------------------------------------------------------------------------




#from dataset 1, get bat_landing_to_food and start_time
batMean = df['bat_landing_to_food'].mean()
batSTD = df['bat_landing_to_food'].std()

df = df[
    (df['bat_landing_to_food'].between(batMean - 2*batSTD, batMean + 2*batSTD))
]

df['time'] = pd.to_datetime(df['start_time'], format='%d/%m/%Y %H:%M', dayfirst=True).dt.strftime('%H:%M')
df['time_after_0'] = pd.to_datetime(df['time'], format='%H:%M').dt.hour * 60 + pd.to_datetime(df['time'], format='%H:%M').dt.minute
#print(df['time_after_0'])
#-----------------------------------------------------------------------------------








# merged df based on time
merged_df = pd.merge(df, df2, on='time_after_0', how='inner')
#print(list(merged_df.columns))


print(merged_df)

corr, p_value = st.spearmanr(merged_df['rat_arrival_number'], merged_df['bat_landing_to_food'])
print(f"Spearman correlation: {corr:.3f}, p-value: {p_value:.3g}")



merged_df = merged_df.sort_values(by='time_after_0')

merged_df.to_csv("merged_hesitancy.csv", index=False)

plt.scatter(merged_df['time_after_0'], merged_df['bat_landing_to_food'])
plt.xlabel('Time after midnight (minutes)')
plt.ylabel('Bat landing to food time (seconds)')
plt.show()

plt.scatter(merged_df['time_after_0'], merged_df['rat_arrival_number'])
plt.xlabel('Time after midnight (minutes)')
plt.ylabel('Rat arrival number')
plt.ylim(-1, 10)
plt.show()


