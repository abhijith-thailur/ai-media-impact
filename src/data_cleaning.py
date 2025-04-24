import pandas as pd
import numpy as np
from tabulate import tabulate

# Load the dataset
file_path = '/Users/ABHIJN/Downloads/Global_AI_Content_Impact_Dataset.csv'
df = pd.read_csv(file_path)

#Step 1: Display information for first 50 rows in a table format
print(tabulate(df.head(50), headers='keys', tablefmt='psql'))

#Step 2: Check for duplicates
duplicates = df.duplicated()
num_duplicates = duplicates.sum()
print('Number of duplicate rows: ', num_duplicates)

# Step 3: Check for missing values
missing_data = df.isnull().sum()
# Show only columns where missing values > 0
missing_data = missing_data[missing_data > 0]

# Check for empty strings
empty_strings = (df == '').sum()

# Check for common placeholders
placeholders = ['N/A', 'Unknown', 'None', '-', 'missing', '']

# Step 4: Check each placeholder
for placeholder in placeholders:
    print(f"\nPlaceholder '{placeholder}':")
    counts = (df == placeholder).sum()
    # Convert the Series to a DataFrame for nice tabular output
    table_data = counts.reset_index()
    table_data.columns = ['Column', 'Count']
    print(tabulate(table_data, headers='keys', tablefmt='psql', showindex=False))

if missing_data.empty:
    print('✅ No missing values found!')
else:
    print(f'Missing values: {missing_data}')

# Step 5: Check Data Types
dtypes_df = pd.DataFrame(df.dtypes, columns=['Data Type'])
dtypes_df.reset_index(inplace=True)
dtypes_df.rename(columns={'index': 'Column'}, inplace=True)

print('Data Types Summary:\n')
print(tabulate(dtypes_df, headers='keys', tablefmt='psql'))

# Step 6: Detect Outliers using IQR method
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns


outlier_summary = {}

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outlier_summary[col] = outliers.shape[0]

outlier_df = pd.DataFrame(list(outlier_summary.items()), columns=['Headers', 'Number of Outliers'])
print('Outlier summary:\n')
print(tabulate(outlier_df, headers='keys', tablefmt='psql'))

# Step 7: Feature Engineering Example
# Create AI Adoption Category
def categorize_adoption(rate):
    if rate > 70:
        return 'High'
    elif rate >= 30:
        return 'Medium'
    else:
        return 'Low'

df['AI Adoption Category'] = df['AI Adoption Rate (%)'].apply(categorize_adoption)

print(tabulate(df[['AI Adoption Rate (%)', 'AI Adoption Category']].head(), headers='keys', tablefmt='psql'))
