import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("air_quality_cleaned.csv")

# Display first 5 records
print("First 5 Records:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Average pollution values
print("\nAverage Pollution Levels:")
print(df[['pollutant_min', 'pollutant_max', 'pollutant_avg']].mean())
# Pollution distribution
plt.figure(figsize=(8, 5))

df['pollutant_avg'].hist(bins=20)

plt.title("Distribution of Average Pollution")
plt.xlabel("Pollution Level")
plt.ylabel("Frequency")

plt.savefig("pollution_distribution.png")
plt.show()
# Average pollution by city
city_pollution = df.groupby('city')['pollutant_avg'].mean().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
city_pollution.head(10).plot(kind='bar')

plt.title("Top 10 Cities by Average Pollution")
plt.xlabel("City")
plt.ylabel("Average Pollution")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("top_10_cities.png")
plt.show()
print("All graphs generated successfully")