import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway, kruskal

# Sample DataFrame
data = {
    'nli_evidence': [0.92, 0.75, 0.60, 0.30, 0.85, 0.40, 0.95, 0.70, 0.55, 0.20],
    'Truthfulness?': ['Fully True', 'Partially True', 'Not True', 'NaN',
                     'Fully True', 'Not True', 'Fully True', 'Partially True', 'Not True', 'NaN']
}

df = pd.DataFrame(data)

# Drop NaN rows for statistical analysis (or you can treat them separately)
df = df[df['Truthfulness?'] != 'NaN']

# Convert Truthfulness? to Ordered Numerical Values
Truthfulness?_mapping = {'Fully True': 3, 'Partially True': 2, 'Not True': 1}
df['Truthfulness?_Numeric'] = df['Truthfulness?'].map(Truthfulness?_mapping)

# ANOVA Test (Check if means differ)
fully_true = df[df['Truthfulness?'] == 'Fully True']['nli_evidence']
partially_true = df[df['Truthfulness?'] == 'Partially True']['nli_evidence']
not_true = df[df['Truthfulness?'] == 'Not True']['nli_evidence']

anova_result = f_oneway(fully_true, partially_true, not_true)
print(f'ANOVA Test: F-statistic={anova_result.statistic}, P-value={anova_result.pvalue}')

# Kruskal-Wallis Test (If ANOVA assumptions are violated)
kruskal_result = kruskal(fully_true, partially_true, not_true)
print(f'Kruskal-Wallis Test: H-statistic={kruskal_result.statistic}, P-value={kruskal_result.pvalue}')

# Box Plot to visualize the relationship
plt.figure(figsize=(7, 5))
sns.boxplot(x='Truthfulness?', y='nli_evidence', data=df)
plt.title("Distribution of NLI Evidence by Truthfulness?")
plt.show()

# Violin Plot for better density visualization
plt.figure(figsize=(7, 5))
sns.violinplot(x='Truthfulness?', y='nli_evidence', data=df)
plt.title("Violin Plot: NLI Evidence vs Truthfulness?")
plt.show()

# Scatter Plot to observe any trends
plt.figure(figsize=(7, 5))
sns.stripplot(x='Truthfulness?', y='nli_evidence', data=df, jitter=True)
plt.title("Scatter Plot: NLI Evidence vs Truthfulness?")
plt.show()

import numpy as np

plt.figure(figsize=(7, 5))
jitter = np.random.normal(0, 0.02, len(df))  # Add slight noise for better visibility
plt.scatter(df['Float_Column'], df['Category_numeric'] + jitter, alpha=0.5)
plt.xlabel("Float Value")
plt.ylabel("Category (0 = No, 1 = Yes)")
plt.title("Scatter Plot: Float Value vs Category")
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from statsmodels.formula.api import ols
import pingouin as pg

# Configuration
plt.style.use('seaborn')
pd.options.display.float_format = '{:.4f}'.format

# Load data
df = pd.read_csv('your_data.csv')  # Replace with your actual data path

# Data cleaning
# Handle missing values in critical columns
print("Missing values before handling:")
print(df[['nli_evidence', 'Truthfulness?', 'Indicate the presence of hallucination in the model summar']].isna().sum())

# Convert Truthfulness? to ordered category
Truthfulness?_order = ['not true', 'partially true', 'fully true']
df['Truthfulness?'] = pd.Categorical(
    df['Truthfulness?'],
    categories=Truthfulness?_order,
    ordered=True
)

# Convert hallucination to boolean for analysis
df['hallucination_bool'] = df['Indicate the presence of hallucination in the model summar'].map({'yes': 1, 'no': 0})

# 1. Descriptive statistics
print("\nDescriptive Statistics:")
print(df[['nli_evidence', 'Truthfulness?', 'Indicate the presence of hallucination in the model summar']].describe(include='all'))

# 2. Distribution analysis
fig, ax = plt.subplots(2, 2, figsize=(15, 12))

# NLI Evidence distribution
sns.histplot(df['nli_evidence'], bins=20, kde=True, ax=ax[0,0])
ax[0,0].set_title('NLI Evidence Score Distribution')

# Truthfulness? distribution
sns.countplot(x='Truthfulness?', data=df, ax=ax[0,1], order=Truthfulness?_order)
ax[0,1].set_title('Truthfulness? Distribution')

# Hallucination distribution
sns.countplot(x='Indicate the presence of hallucination in the model summar', data=df, ax=ax[1,0])
ax[1,0].set_title('Hallucination Distribution')

# NLI vs Truthfulness? boxplot
sns.boxplot(x='Truthfulness?', y='nli_evidence', data=df, ax=ax[1,1], order=Truthfulness?_order)
ax[1,1].set_title('NLI Evidence by Truthfulness? Category')

plt.tight_layout()
plt.show()

# 3. Correlation analysis
# Calculate Spearman correlation (for ordinal vs continuous)
corr, pval = stats.spearmanr(
    df['nli_evidence'].rank(method='average'),
    df['Truthfulness?'].cat.codes.replace({-1: np.nan}).rank(method='average'),
    nan_policy='omit'
)
print(f"\nSpearman Correlation between NLI and Truthfulness?: {corr:.4f} (p={pval:.4f})")

# 4. Hypothesis testing
# Compare NLI scores between hallucination groups
print("\nHallucination Group Comparison:")
print(pg.mwu(df[df['Indicate the presence of hallucination in the model summar'] == 'yes']['nli_evidence'],
             df[df['Indicate the presence of hallucination in the model summar'] == 'no']['nli_evidence']))

# 5. Advanced visualization
plt.figure(figsize=(12, 6))
sns.violinplot(x='Truthfulness?', y='nli_evidence', hue='Indicate the presence of hallucination in the model summar',
               data=df, split=True, order=Truthfulness?_order)
plt.title('NLI Evidence Distribution by Truthfulness? and Hallucination Status')
plt.show()

# 6. Contingency analysis
cross_tab = pd.crosstab(
    df['Truthfulness?'],
    df['Indicate the presence of hallucination in the model summar'],
    normalize='index'
)
print("\nHallucination Proportion by Truthfulness? Category:")
print(cross_tab)

# 7. Regression analysis
# Ordinal logistic regression would be ideal, but for simplicity:
model = ols('nli_evidence ~ C(Truthfulness?) + C(Indicate the presence of hallucination in the model summar)', data=df).fit()
print("\nRegression Analysis Summary:")
print(model.summary())

# 8. Binning analysis for NLI thresholds
df['NLI_bin'] = pd.qcut(df['nli_evidence'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
bin_analysis = df.groupby('NLI_bin').agg(
    mean_Truthfulness?=('Truthfulness?', lambda x: x.cat.codes.mean()),
    hallucination_rate=('hallucination_bool', 'mean')
).reset_index()

print("\nBinned Analysis:")
print(bin_analysis)
