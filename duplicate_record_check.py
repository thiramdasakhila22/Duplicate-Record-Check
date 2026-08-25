import pandas as pd

df = pd.read_csv("superstore_cleaned.csv")

# Full-row duplicate check
full_duplicates = df[df.duplicated(keep=False)]
print("Exact duplicate rows:", df.duplicated().sum())
print("Rows in duplicate groups:", len(full_duplicates))

# Key-column screening
key_columns = [
    "City", "State", "Postal Code", "Category", "Sub-Category",
    "Sales", "Quantity", "Discount", "Profit"
]

key_counts = df.groupby(key_columns, dropna=False).size().reset_index(name="Occurrences")
potential_duplicates = key_counts[key_counts["Occurrences"] > 1]

print("Potential key-column duplicate groups:", len(potential_duplicates))

# Clean only confirmed exact duplicates
cleaned_df = df.drop_duplicates()
cleaned_df.to_csv("superstore_cleaned_task13.csv", index=False)
