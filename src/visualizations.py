import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
file_path = '/Users/ABHIJN/Downloads/Global_AI_Content_Impact_Dataset.csv'
df = pd.read_csv(file_path)

# 1. Bar chart for Top 5 Countries by AI Adoption Rate
# top5 = df.groupby('Country')['AI Adoption Rate (%)'].mean().sort_values(ascending=False).head(5)
#
# # Plot
# plt.figure(figsize=(10,6))
# sns.barplot(x=top5.index, y=top5.values, color='skyblue')  # <-- change here
# plt.title('Top 5 Countries by Average AI Adoption Rate (%)')
# plt.ylabel('AI Adoption Rate (%)')
# plt.xlabel('Country')
# plt.xticks(rotation=45)
# plt.tight_layout()
#
# # Save chart as an image
# plt.savefig('top5_countries_ai_adoption.png')
# plt.show()

# Group data: Average Revenue Increase per Year
# revenue_by_year = df.groupby('Year')['Revenue Increase Due to AI (%)'].mean().reset_index()
#
# # Plot
# plt.figure(figsize=(10,6))
# sns.lineplot(x='Year', y='Revenue Increase Due to AI (%)', data=revenue_by_year, marker='o', color='green')
# plt.title('Average Revenue Increase Due to AI Over Years')
# plt.xlabel('Year')
# plt.ylabel('Average Revenue Increase (%)')
# plt.grid(True)
# plt.tight_layout()
#
# # Save the figure
# plt.savefig('revenue_increase_trend.png')
# plt.show()

# Show all column names
# print(df.columns.tolist())

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