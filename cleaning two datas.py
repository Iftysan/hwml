
import pandas as pd
import numpy as np

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print(matches.head())
print(deliveries.head())

matches.info()
deliveries.info()

print(matches.isnull().sum())
print(deliveries.isnull().sum())

matches = matches.dropna(axis=1, how="all")
deliveries = deliveries.dropna(axis=1, how="all")

for column in matches.columns:
    if matches[column].isnull().sum() > 0:
        if pd.api.types.is_numeric_dtype(matches[column]):
            matches[column] = matches[column].fillna(matches[column].median())
        else:
            matches[column] = matches[column].fillna("Unknown")

for column in deliveries.columns:
    if deliveries[column].isnull().sum() > 0:
        if pd.api.types.is_numeric_dtype(deliveries[column]):
            deliveries[column] = deliveries[column].fillna(deliveries[column].median())
        else:
            deliveries[column] = deliveries[column].fillna("Unknown")

print(matches.isnull().sum())
print(deliveries.isnull().sum())

matches.to_csv("cleaned_matches.csv", index=False)
deliveries.to_csv("cleaned_deliveries.csv", index=False)

print("Data preprocessing completed!")

