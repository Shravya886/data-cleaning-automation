import pandas as pd

# -----------------------------
# STEP 1: Load raw data
# -----------------------------
df = pd.read_csv("data/raw_data.csv")

print("Original Data:")
print(df)

# -----------------------------
# STEP 2: Handle missing values
# -----------------------------

# Fill Age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill Salary with mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Fill City with "Unknown"
df["City"] = df["City"].fillna("Unknown")

# -----------------------------
# STEP 3: Remove duplicates
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# STEP 4: Standardize text
# -----------------------------

df["Name"] = df["Name"].str.title()
df["City"] = df["City"].str.title()
df["Department"] = df["Department"].str.upper()

# -----------------------------
# STEP 5: Save cleaned data
# -----------------------------
df.to_csv("output/cleaned_data.csv", index=False)

print("\n Cleaning completed successfully!")
print("Cleaned file saved in output folder.")