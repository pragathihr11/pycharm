import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv("p6b.csv")

data["Date"] = pd.to_datetime(data["Date"])

sns.lineplot(
    x="Date",
    y="Close",
    hue="Symbol",
    linestyle="--",
    style="Symbol",
    marker="*",
    ms=10,
    data=data
)

plt.title("Monthly Electricity Consumption Trend Analysis")
plt.xlabel("Timeline")
plt.ylabel("Electricity Consumption (kWh)")

plt.xticks(
    rotation=45,
    ha="center",
    fontsize=8,
    fontfamily="Times New Roman",
    fontweight="bold"
)
plt.tight_layout()
plt.savefig("electricity_plot.png")
plt.show()