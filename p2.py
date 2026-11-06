
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="whitegrid")

dataset = pd.read_csv("vehicle.csv", sep="\t")
dataset.info()

sns.relplot(x="Engine Capacity (cc)",y="Fuel Efficiency (km/l)",data=dataset,hue="Vehicle Type",s=100,marker="*")

plt.xlabel("Engine Capacity (cc)")
plt.ylabel("Fuel Efficiency (km/l)")
plt.show()