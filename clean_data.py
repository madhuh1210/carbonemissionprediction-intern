import pandas as pd
import numpy as np

# Define the file name and sheet
orig_data_file = "climate_change_download_0.xls"
data_sheet = "Data"

# Read Excel file
data_orig = pd.read_excel(io=orig_data_file, sheet_name=data_sheet)

print("Shape of the original dataset:")
print(data_orig.shape)

print("Available columns:")
print(data_orig.columns)

print("Column data types:")
print(data_orig.dtypes)

print("Overview of the first 5 rows:")
print(data_orig.head())

print("Descriptive statistics of the columns:")
print(data_orig.describe())

# Look at unique values
print("Unique Series names:", data_orig['Series name'].unique())
print("Unique Series codes:", data_orig['Series code'].unique())
print("Unique SCALE values:", data_orig['SCALE'].unique())
print("Unique Decimals values:", data_orig['Decimals'].unique())

# Inspect rows with text values
print(data_orig[data_orig['SCALE'] == 'Text'])
print(data_orig[data_orig['Decimals'] == 'Text'])

# Start cleaning
data_clean = data_orig.copy()
print("Original number of rows:", data_clean.shape[0])

# Remove rows with 'Text' in SCALE and Decimals
data_clean = data_clean[data_clean['SCALE'] != 'Text']
data_clean = data_clean[data_clean['Decimals'] != 'Text']

print("Rows after removing 'Text' SCALE/Decimals:", data_clean.shape[0])

# Drop unneeded columns
columns_to_drop = ['Country name', 'Series code', 'SCALE', 'Decimals']
data_clean = data_clean.drop(columns=columns_to_drop, errors='ignore')

# Replace ".." and "" with NaN
data_clean.replace(["..", ""], np.nan, inplace=True)

# Drop rows with any missing values
data_clean.dropna(axis=0, how='any', inplace=True)

print("Final cleaned shape:", data_clean.shape)

# Export to CSV
data_clean.to_csv("data_cleaned.csv", index=False)
print("✅ Data cleaned and saved to data_cleaned.csv")
