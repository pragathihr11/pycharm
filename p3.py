import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('p3.csv')

sns.set_style("whitegrid")

data['Month-Year'] = data['Month'] + '-' + data['Year'].astype(str)

fig, axes = plt.subplots(1, 2, figsize=(18, 8))

sns.lineplot(
    x='Month-Year', y='Admissions',
    marker='*' ,color='blue',
    label='Admissions', ax=axes[0], data=data
)
axes[0].set_title('MONTHLY PATIENT ADMISSIONS')
axes[0].set_xlabel('MONTH')
axes[0].set_ylabel('NUMBER OF PATIENTS')
axes[0].tick_params(axis='x', rotation=90)
axes[0].legend()

sns.barplot(
    x='Month-Year', y='Emergency',
    color='#A7C7E7', ax=axes[1], data=data
)
axes[1].set_title('MONTHLY EMERGENCY CASES')
axes[1].set_xlabel('MONTH')
axes[1].set_ylabel('EMERGENCY CASES')
axes[1].tick_params(axis='x', rotation=90)

fig.suptitle('HOSPITAL PATIENT ANALYSIS',fontsize=20)
plt.tight_layout()
plt.savefig('hospital_analysis.png')
plt.show()