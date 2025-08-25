import pandas as pd 
import matplotlib.pyplot as plt
import scipy.stats as st

ds1 = pd.read_csv("dataset1.csv")
ds2 = pd.read_csv("dataset2.csv")

# Create series for each group of rat_arrival_number (1, 2, 3, 4+)

rat1 = ds2.loc[ds2['rat_arrival_number'] == 1, 'bat_landing_number']
rat2 = ds2.loc[ds2['rat_arrival_number'] == 2, 'bat_landing_number']
rat3 = ds2.loc[ds2['rat_arrival_number'] == 3, 'bat_landing_number']
rat4plus = ds2.loc[ds2['rat_arrival_number'] >= 4, 'bat_landing_number']


# Series of average number of bat landings for each rat number group: 1, 2, 3, 4+

rat_mean = pd.Series({
    'rat1': rat1.mean(),
    'rat2': rat2.mean(),
    'rat3': rat3.mean(),
    'rat4plus': rat4plus.mean() 
})
# print(rat_mean)



# Rat 1 tests
x_bar_r1 = rat1.mean()
s_r1 = st.tstd(rat1)
n_r1 = len(rat1)

# Rat 2 tests
x_bar_r2 = rat2.mean()
s_r2 = st.tstd(rat2)
n_r2 = len(rat2)

# Rat 3 tests
x_bar_r3 = rat3.mean()
s_r3 = st.tstd(rat3)
n_r3 = len(rat3)

# Rat 4+ tests
x_bar_r4 = rat4plus.mean()
s_r4 = st.tstd(rat4plus)
n_r4 = len(rat4plus)



p_val = st.ttest_ind_from_stats(x_bar_r1, s_r1, n_r1, x_bar_r2, s_r2, n_r2)
print("P-value for rat 1 vs rat 2:", p_val.pvalue)



# plt.bar(rat_mean.index, rat_mean.values, edgecolor='black')
# plt.title("Average Bat Landing Number by Rat Arrival Number")
# plt.xlabel("Rat Arrival Number")
# plt.ylabel("Average Bat Landing Number")
# plt.show()
