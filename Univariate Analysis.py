import matplotlib.pyplot as plt
import seaborn as sns

# Example: Histogram for numerical columns
df.hist(bins=15, figsize=(15, 10))
plt.tight_layout()
plt.show()

# Count plots for categorical features
sns.countplot(data=df, x='Product')
plt.show()

sns.countplot(data=df, x='Gender')
plt.show()
