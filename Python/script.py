import pandas as pd 
import matplotlib.pyplot as plt

ds1 = pd.read_csv("dataset1.csv")
ds2 = pd.read_csv("dataset2.csv")


ds2_bat_landing_number = ds2["bat_landing_number"]

sample = ds2_bat_landing_number.values


plt.hist(sample, edgecolor="black", bins=20)
plt.title("Histogram of Bat Landing Numbers")
plt.xlabel("Bat Landing Number")
plt.ylabel("Frequency")     
plt.show()