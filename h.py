import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, pointbiserialr, f_oneway

# Load data
file_path = "data.xlsx"  # Update file path
df = pd.read_excel(file_path)

# Define encoding for categorical columns
encoding_dict = {
    "Evaluate the Transcript Quality": {"Low": -1, "Medium": 0, "High": 1},
    "Evaluate the Model-Generated Summary": {"Worse": -1, "Similar": 0, "Better": 1},
    "Model-Generated Summary Coherence": {"Bad": -1, "Neutral": 0, "Good": 1},
    "Did the Summary Contain Foul/Offensive Text?": {"Yes": 1, "No": 0},
    "Do You Think the Resolution Was Captured in the Summary?": {"Yes": 1, "No": 0},
    "Truthfulness": {"Not True": -1, "Partially True": 0, "Fully True": 1},
    "Indicate the Presence of Hallucinations in the Model Summary": {"Yes": 1, "No": 0}
}

# Encode categorical columns
for column, mapping in encoding_dict.items():
    if column in df.columns:
        df[column] = df[column].map(mapping)

# Handle missing values
df.fillna(0, inplace=True)

# Identify numerical and categorical columns
numerical_columns = ["Transcript Quality", "Summary Quality", "Summary Coherence", "Resolution", "Capture", 
                     "Informative", "Content", "Truthfulness", "Absence of Hallucination", 
                     "Presence of Toxic Language"]
encoded_categorical_columns = list(encoding_dict.keys())

# Initialize correlation results
correlations = {}

# Compute Spearman Correlation for ordinal relationships
for cat_col in encoded_categorical_columns:
    for num_col in numerical_columns:
        corr, _ = spearmanr(df[cat_col], df[num_col])
        correlations[(cat_col, num_col)] = corr

# Convert correlation results into a DataFrame
corr_df = pd.DataFrame.from_dict(correlations, orient="index", columns=["Correlation"])
corr_df = corr_df.reset_index()
corr_df.columns = ["Categorical Column", "Numerical Column", "Correlation"]

# Pivot for heatmap
heatmap_data = corr_df.pivot("Categorical Column", "Numerical Column", "Correlation")

# Plot the correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Spearman Correlation Between Categorical and Numerical Columns")
plt.show()

# Boxplots for distribution visualization
for cat_col in encoded_categorical_columns:
    for num_col in numerical_columns:
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=df, x=cat_col, y=num_col, palette="viridis")
        plt.title(f"{num_col} vs {cat_col}")
        plt.xticks(rotation=45)
        plt.show()