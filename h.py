import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway, kruskal

# Sample DataFrame
data = {
    'NLI_Evidence': [0.92, 0.75, 0.60, 0.30, 0.85, 0.40, 0.95, 0.70, 0.55, 0.20],
    'Truthfulness': ['Fully True', 'Partially True', 'Not True', 'NaN',
                     'Fully True', 'Not True', 'Fully True', 'Partially True', 'Not True', 'NaN']
}

df = pd.DataFrame(data)

# Drop NaN rows for statistical analysis (or you can treat them separately)
df = df[df['Truthfulness'] != 'NaN']

# Convert Truthfulness to Ordered Numerical Values
truthfulness_mapping = {'Fully True': 3, 'Partially True': 2, 'Not True': 1}
df['Truthfulness_Numeric'] = df['Truthfulness'].map(truthfulness_mapping)

# ANOVA Test (Check if means differ)
fully_true = df[df['Truthfulness'] == 'Fully True']['NLI_Evidence']
partially_true = df[df['Truthfulness'] == 'Partially True']['NLI_Evidence']
not_true = df[df['Truthfulness'] == 'Not True']['NLI_Evidence']

anova_result = f_oneway(fully_true, partially_true, not_true)
print(f'ANOVA Test: F-statistic={anova_result.statistic}, P-value={anova_result.pvalue}')

# Kruskal-Wallis Test (If ANOVA assumptions are violated)
kruskal_result = kruskal(fully_true, partially_true, not_true)
print(f'Kruskal-Wallis Test: H-statistic={kruskal_result.statistic}, P-value={kruskal_result.pvalue}')

# Box Plot to visualize the relationship
plt.figure(figsize=(7, 5))
sns.boxplot(x='Truthfulness', y='NLI_Evidence', data=df)
plt.title("Distribution of NLI Evidence by Truthfulness")
plt.show()

# Violin Plot for better density visualization
plt.figure(figsize=(7, 5))
sns.violinplot(x='Truthfulness', y='NLI_Evidence', data=df)
plt.title("Violin Plot: NLI Evidence vs Truthfulness")
plt.show()

# Scatter Plot to observe any trends
plt.figure(figsize=(7, 5))
sns.stripplot(x='Truthfulness', y='NLI_Evidence', data=df, jitter=True)
plt.title("Scatter Plot: NLI Evidence vs Truthfulness")
plt.show()

import numpy as np

plt.figure(figsize=(7, 5))
jitter = np.random.normal(0, 0.02, len(df))  # Add slight noise for better visibility
plt.scatter(df['Float_Column'], df['Category_numeric'] + jitter, alpha=0.5)
plt.xlabel("Float Value")
plt.ylabel("Category (0 = No, 1 = Yes)")
plt.title("Scatter Plot: Float Value vs Category")
plt.show()
