import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("air_quality_cleaned.csv")

# Remove rows missing important information
df = df.dropna(subset=["city", "station", "pollutant_avg"])

# Count monitoring stations and calculate average pollution per city
city_stats = df.groupby("city").agg(
    station_count=("station", "nunique"),
    average_pollution=("pollutant_avg", "mean"),
    records=("pollutant_avg", "count")
).reset_index()

# Sort cities by number of monitoring stations
city_stats = city_stats.sort_values(
    "station_count", ascending=False
)

print("\nCITY-WISE ANALYSIS")
print(city_stats.head(15).to_string(index=False))

# Test our hypothesis
correlation = city_stats["station_count"].corr(
    city_stats["average_pollution"]
)

print("\nCorrelation:", round(correlation, 3))

# Chart 1: Monitoring stations vs average pollution
plt.figure(figsize=(9, 5))
plt.scatter(
    city_stats["station_count"],
    city_stats["average_pollution"]
)
plt.xlabel("Number of Monitoring Stations")
plt.ylabel("Average Pollutant Value")
plt.title("Monitoring Stations vs Average Pollution by City")
plt.grid(True)
plt.savefig("stations_vs_pollution.png")
plt.show()

# Chart 2: Top 10 cities by monitoring stations
top_cities = city_stats.head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_cities["city"], top_cities["station_count"])
plt.xlabel("City")
plt.ylabel("Number of Monitoring Stations")
plt.title("Top 10 Cities by Monitoring Station Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_10_monitoring_stations.png")
plt.show()
# Compare cities with fewer and more monitoring stations
median_stations = city_stats["station_count"].median()

city_stats["station_group"] = city_stats["station_count"].apply(
    lambda x: "More stations" if x > median_stations
    else "Fewer stations"
)

print("\nAverage pollution by station group:")
print(city_stats.groupby("station_group")["average_pollution"].agg(
    ["count", "mean", "median"]
))

print("\nSpearman correlation:")
print("Spearman correlation:")
print(city_stats["station_count"].rank().corr(
    city_stats["average_pollution"].rank()
))