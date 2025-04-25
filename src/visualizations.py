import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
file_path = '/Users/ABHIJN/Downloads/Global_AI_Content_Impact_Dataset.csv'
df = pd.read_csv(file_path)

# 1. Bar chart for Top 5 Countries by AI Adoption Rate
top5 = df.groupby('Country')['AI Adoption Rate (%)'].mean().sort_values(ascending=False).head(5)

# Plot
plt.figure(figsize=(10,6))
sns.barplot(x=top5.index, y=top5.values, color='skyblue')  # <-- change here
plt.title('Top 5 Countries by Average AI Adoption Rate (%)')
plt.ylabel('AI Adoption Rate (%)')
plt.xlabel('Country')
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart as an image
plt.savefig('top5_countries_ai_adoption.png')
plt.show()

#Group data: Average Revenue Increase per Year
revenue_by_year = df.groupby('Year')['Revenue Increase Due to AI (%)'].mean().reset_index()

# Plot
plt.figure(figsize=(10,6))
sns.lineplot(x='Year', y='Revenue Increase Due to AI (%)', data=revenue_by_year, marker='o', color='green')
plt.title('Average Revenue Increase Due to AI Over Years')
plt.xlabel('Year')
plt.ylabel('Average Revenue Increase (%)')
plt.grid(True)
plt.tight_layout()

# Save the figure
plt.savefig('revenue_increase_trend.png')
plt.show()

#Show all column names
print(df.columns.tolist())

# SAFELY fix column names (optional but useful)
df.columns = df.columns.str.strip()  # Remove any accidental spaces or newlines

# Group data: Count of each AI Adoption Category
category_counts = df['Industry'].value_counts()

# Plot
plt.figure(figsize=(8,8))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribution of AI Adoption Categories')
plt.tight_layout()

# Save the figure
plt.savefig('ai_adoption_category_piechart.png')
plt.show()

#1. YoY Trend Analysis by Industry (Line Plot)
sns.set_style("whitegrid")

# Aggregate data by Year and Industry
yoy_industry = df.groupby(['Year', 'Industry'])['AI Adoption Rate (%)'].mean().unstack()

# Plot
ax = yoy_industry.plot(kind='line', marker='o', linewidth=2.5, figsize=(14, 7))
plt.title('YoY AI Adoption Rate by Industry (2020-2025)', fontsize=16, pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('AI Adoption Rate (%)', fontsize=12)
plt.legend(title='Industry', bbox_to_anchor=(1.05, 1))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('YoY_linechart.png')
plt.show()

# 2. YoY Growth Rate Heatmap (All Metrics)
metrics = ['AI Adoption Rate (%)', 'AI-Generated Content Volume (TBs per year)',
           'Job Loss Due to AI (%)', 'Revenue Increase Due to AI (%)']

# Calculate YoY growth rates
growth_rates = df.groupby('Year')[metrics].mean().pct_change() * 100

# Plot
plt.figure(figsize=(12, 6))
sns.heatmap(growth_rates.iloc[1:].T, annot=True, fmt=".1f", cmap='RdYlGn',
            center=0, linewidths=0.5)
plt.title('YoY Growth Rates of Key Metrics (%)', fontsize=14)
plt.tight_layout()
plt.savefig('YoY_heatmap.png')
plt.show()

# 3. Country-Specific YoY Trends (Interactive Plot)
top_countries = df['Country'].value_counts().nlargest(5).index.tolist()

plt.figure(figsize=(14, 7))
for country in top_countries:
    country_data = df[df['Country'] == country].groupby('Year')['AI Adoption Rate (%)'].mean()
    plt.plot(country_data.index, country_data.values, label=country, linewidth=2.5)

plt.title('YoY AI Adoption in Top 5 Countries', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('AI Adoption Rate (%)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('YoY_interactive.png')
plt.show()

# 4. Advanced: Small Multiples by Industry
g = sns.FacetGrid(df, col='Industry', col_wrap=3, height=4, sharey=False)
g.map(sns.lineplot, 'Year', 'AI Adoption Rate (%)', errorbar=None, marker='o')
g.set_titles("{col_name}")
g.fig.suptitle('YoY AI Adoption Across Industries', y=1.05, fontsize=16)
plt.tight_layout()
#plt.savefig('YoY_Trends_by_Industry.png')
plt.show()

# Pivot and plot
plt.figure(figsize=(16, 10))
sns.heatmap(df.pivot_table(values='AI Adoption Rate (%)',
                         index='Country',
                         columns='Year'),
           annot=True,
           fmt=".1f",
           cmap='YlGnBu',  # Built-in colormap
           linewidths=0.5)
plt.title('Country-Wise AI Adoption Trends', fontsize=16)
plt.tight_layout()
plt.savefig('CountryWise_heatmap.png')
plt.show()