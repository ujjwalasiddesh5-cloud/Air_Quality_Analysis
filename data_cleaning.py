import pandas as pd

# Load the air quality dataset
df = pd.read_csv(
    r"C:\Users\DELL\Downloads\3b01bcb8-0b14-4abf-b6f2-c1bfd384ba69.csv"
)

# Display first five records
print("First 5 Records:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())
print("\nTotal Rows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())
print("\nMissing Value Percentage:")
print((df.isnull().mean() * 100).round(2))

print("\nData Types:")
print(df.dtypes)
print("\nExact Missing Values:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())
print("\nRows with all pollutant values missing:")
print(
    df[['pollutant_min', 'pollutant_max', 'pollutant_avg']]
    .isnull().all(axis=1).sum()
)

print("\nRows with partially missing values:")
print(
    df[['pollutant_min', 'pollutant_max', 'pollutant_avg']]
    .isnull().any(axis=1).sum()
)
# Create a cleaned copy
df_clean = df.dropna(
    subset=['pollutant_min', 'pollutant_max', 'pollutant_avg'],
    how='all'
)

print("\nBefore Cleaning:", df.shape)
print("After Cleaning:", df_clean.shape)

print("\nRemaining Missing Values:")
print(df_clean.isnull().sum())
# Save cleaned dataset
df_clean.to_csv(
    r"C:\Users\DELL\Downloads\air_quality_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")
print("Final dataset shape:", df_clean.shape)