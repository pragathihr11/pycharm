import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('pgm1.csv')
sns.set_theme(style='darkgrid')

fig, axes = plt.subplots(1, 2, figsize=(16,7))

sns.boxplot(data=data, x='Product Category', y='Price',
            ax=axes[0], hue='Product Category',
            palette=['#CDB4DB', '#A2D2FF', '#95D5B2',
                     '#FFE08A', '#BDE0FE', '#D8C3F5'])

axes[0].set_title('Product Price Box Plot')
axes[0].set_xlabel('Product Category')
axes[0].set_ylabel('Price')

axes[0].legend()
sns.violinplot(x='Product Category', y='Price', data=data,
               ax=axes[1], hue='Product Category',
               palette=['#CDB4DB', '#A2D2FF', '#95D5B2',
                        '#FFE08A', '#BDE0FE', '#D8C3F5'])
axes[1].set_title('Product Price Violin Plot')
axes[1].set_xlabel('Product Category')
axes[1].set_ylabel('Price')

axes[1].legend()

fig.suptitle('Product Price Analysis Across Categories', fontsize=20)
plt.tight_layout()
plt.savefig('product_analysis.png')
plt.show()