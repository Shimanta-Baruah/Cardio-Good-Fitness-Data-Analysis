# Boxplot: Income distribution by Product type
sns.boxplot(data=df, x='Product', y='Income')
plt.show()

# Pairplot: Numerical relationships
sns.pairplot(df, hue='Product')
plt.show()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()
